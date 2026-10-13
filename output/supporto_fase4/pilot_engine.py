"""Pilot engine (Python) per la Fase 4: implementazione di riferimento SEMPLIFICATA del modello previsto in Matlab.
NON e il modello della tesi e NON produce risultati della tesi: serve a (i) stimare i tempi di calcolo, (ii) verificare che
la pipeline di analisi funzioni end-to-end, (iii) fornire un'implementazione indipendente per il confronto con Matlab.
Profili sintetici (inventati), un'ora = un passo, 8760 passi, un solo anno."""
import math, time
import numpy as np
from scipy.optimize import linprog
from scipy.stats import kendalltau

# ------------------------------------------------------------------ profili sintetici
def calendar(T=8760):
    t = np.arange(T); hour = t % 24; day = t // 24; dow = day % 7
    return hour, day, dow

def pv_per_kwp(rng, T=8760, yield_kwh_per_kwp=1250.0, lat=45.0):
    hour, day, dow = calendar(T)
    decl = np.radians(23.45 * np.sin(2 * np.pi * (284 + day + 1) / 365))
    ha = np.radians(15.0 * (hour + 0.5 - 12.0))
    cosz = np.sin(np.radians(lat)) * np.sin(decl) + np.cos(np.radians(lat)) * np.cos(decl) * np.cos(ha)
    clear = np.clip(cosz, 0, None) ** 1.15
    dd = np.arange(T // 24)
    seas = 0.55 + 0.25 * np.sin(2 * np.pi * (dd - 80) / 365)             # chiarezza media stagionale (per giorno)
    cloud = np.clip(rng.beta(4.0, 2.0, size=T // 24) * (seas / 0.667), 0.05, 1.0).repeat(24)
    x = clear * cloud * rng.lognormal(0, 0.05, size=T)
    return x / x.sum() * yield_kwh_per_kwp

def load_profile(kind, annual_kwh, rng, T=8760):
    hour, day, dow = calendar(T); we = (dow >= 5)
    season = 1 + 0.15 * np.cos(2 * np.pi * (day - 15) / 365)
    g = lambda mu, s: np.exp(-0.5 * ((hour - mu) / s) ** 2)
    if kind == 'hh_evening':
        base = 0.35 + 0.25 * g(7.5, 1.2) + 0.9 * g(20, 1.8) + 0.3 * g(13, 2.5) * we
    elif kind == 'hh_day':
        base = 0.4 + 0.5 * g(12, 3.5) + 0.3 * g(20, 2.0)
    elif kind == 'office':
        base = np.where((hour >= 8) & (hour < 18) & (~we), 1.0, 0.12)
    elif kind == 'shop':
        base = np.where((hour >= 9) & (hour < 20), np.where(dow == 6, 0.4, 1.0), 0.1)
    elif kind == 'school':
        base = np.where((hour >= 8) & (hour < 16) & (~we), 1.0, 0.08) * (1 - 0.6 * ((day > 165) & (day < 250)))
    elif kind == 'industry':
        base = 0.6 + 0.4 * (np.where((hour >= 6) & (hour < 22), 1, 0) * (~we))
    else:
        raise ValueError(kind)
    x = base * season * rng.lognormal(0, 0.25, size=T) * rng.lognormal(0, 0.15, size=T // 24).repeat(24)
    return x / x.sum() * annual_kwh

def make_community(seed, pv_to_load=1.0, sigma=0.3, T=8760, mix='balanced'):
    """3 produttori + 9 consumatori (5 persone fisiche, 4 enti). Ritorna dict con matrici T x n e metadati."""
    rng = np.random.default_rng(seed)
    cons_spec = [('hh_evening', 3500, 'NP', 0), ('hh_evening', 2800, 'NP', 1), ('hh_evening', 4200, 'NP', 0),
                 ('hh_day', 3200, 'NP', 1), ('hh_evening', 3000, 'NP', 0),
                 ('office', 25000, 'SME', 0), ('shop', 40000, 'SME', 0),
                 ('school', 18000, 'OE', 0), ('industry', 60000, 'SME', 0)]
    sizes = np.array([c[1] for c in cons_spec], float)
    kinds = [c[0] for c in cons_spec]
    if mix == 'evening':      # carico piu serale: famiglie x3, uffici/scuola/industria x0.6
        sizes = sizes * np.array([3.0 if k.startswith('hh') else (1.0 if k == 'shop' else 0.6) for k in kinds])
    elif mix == 'daytime':    # carico piu diurno: famiglie x0.5, uffici/scuola/industria x1.5, negozio x0.7
        sizes = sizes * np.array([0.5 if k.startswith('hh') else (0.7 if k == 'shop' else 1.5) for k in kinds])
    z = rng.normal(size=len(sizes)); scale = np.exp(sigma * z); scale *= sizes.sum() / (sizes * scale).sum()
    sizes = sizes * scale
    W = np.column_stack([load_profile(c[0], s, rng, T) for c, s in zip(cons_spec, sizes)])
    pv_unit = [pv_per_kwp(rng, T) for _ in range(3)]
    share_kwp = np.array([0.45, 0.35, 0.20])
    kwp_tot = pv_to_load * sizes.sum() / 1250.0
    G = np.column_stack([pv_unit[k] * kwp_tot * share_kwp[k] for k in range(3)])
    inj = np.hstack([G, np.zeros_like(W)]); wd = np.hstack([np.zeros_like(G), W])
    role = np.array(['P'] * 3 + ['C'] * len(cons_spec))
    ctype = np.array(['PR'] * 3 + [c[2] for c in cons_spec])
    vuln = np.array([0] * 3 + [c[3] for c in cons_spec])
    return dict(inj=inj, wd=wd, role=role, ctype=ctype, vuln=vuln, n=len(role), T=T)

# ------------------------------------------------------------------ gioco dell'energia condivisa
def all_values(inj, wd, price=None, chunk=1024):
    """v[mask] = sum_t price_t * min(sum_{i in S} inj_it, sum_{i in S} wd_it) per tutte le coalizioni (bitmask)."""
    T, n = inj.shape; M = 1 << n
    price = np.ones(T) if price is None else price
    bits = ((np.arange(M)[:, None] >> np.arange(n)) & 1).astype(np.float64)
    v = np.zeros(M)
    for s in range(0, M, chunk):
        b = bits[s:s + chunk]
        v[s:s + chunk] = (np.minimum(b @ inj.T, b @ wd.T) * price).sum(1)
    return v

def shapley_from_v(v, n):
    M = 1 << n; idx = np.arange(M)
    pc = np.array([bin(m).count('1') for m in range(M)])
    w = np.array([math.factorial(k) * math.factorial(n - k - 1) / math.factorial(n) for k in range(n)])
    phi = np.zeros(n)
    for i in range(n):
        no = idx[((idx >> i) & 1) == 0]
        phi[i] = np.sum(w[pc[no]] * (v[no | (1 << i)] - v[no]))
    return phi

def marginal_from_v(v, n):
    full = (1 << n) - 1
    return np.array([v[full] - v[full & ~(1 << i)] for i in range(n)])

def shapley_sampled(v, n, n_perm, rng, perms=None):
    """Shapley campionato; se 'perms' (lista di permutazioni) e dato viene usato al posto del generatore casuale."""
    phi = np.zeros(n)
    if perms is not None: n_perm = len(perms)
    for k in range(n_perm):
        perm = perms[k] if perms is not None else rng.permutation(n); mask = 0; prev = v[0]
        for i in perm:
            mask |= (1 << i); cur = v[mask]; phi[i] += cur - prev; prev = cur
    return phi / n_perm

def nucleolus_from_v(v, n, tol=1e-7, max_iter=60):
    """Pre-nucleolo per LP iterativi (dual-based). Con core non vuoto coincide con il nucleolo."""
    M = 1 << n; full = M - 1
    bits = ((np.arange(M)[:, None] >> np.arange(n)) & 1).astype(np.float64)
    S = np.arange(1, full); A_all = bits[S]; v_all = v[S]
    active = np.ones(len(S), bool)
    eq_rows = [np.ones(n)]; eq_rhs = [v[full]]
    x = None
    for _ in range(max_iter):
        A_ub = np.hstack([-A_all[active], -np.ones((active.sum(), 1))]); b_ub = -v_all[active]
        A_eq = np.vstack([np.r_[r, 0.0] for r in eq_rows]); b_eq = np.array(eq_rhs)
        res = linprog(np.r_[np.zeros(n), 1.0], A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                      bounds=[(None, None)] * (n + 1), method='highs')
        if res.status != 0: raise RuntimeError('LP nucleolo: ' + res.message)
        x = res.x[:n]; eps = res.x[n]
        duals = np.abs(res.ineqlin.marginals)
        pick = np.where(active)[0][duals > tol]
        if len(pick) == 0: break
        for k in pick:
            eq_rows.append(A_all[k]); eq_rhs.append(v_all[k] - eps)
        active[pick] = False
        if np.linalg.matrix_rank(np.array(eq_rows), tol=1e-9) >= n or not active.any(): break
    return x

def least_core_eps(v, n):
    M = 1 << n; full = M - 1
    bits = ((np.arange(M)[:, None] >> np.arange(n)) & 1).astype(np.float64)
    S = np.arange(1, full)
    A_ub = np.hstack([-bits[S], -np.ones((len(S), 1))]); b_ub = -v[S]
    res = linprog(np.r_[np.zeros(n), 1.0], A_ub=A_ub, b_ub=b_ub, A_eq=np.r_[np.ones(n), 0.0][None, :],
                  b_eq=[v[full]], bounds=[(None, None)] * (n + 1), method='highs')
    return res.x[n]

def max_excess(R, v, n):
    """max_S [v(S) - R(S)] su coalizioni proprie non vuote, e quota di coalizioni bloccanti."""
    M = 1 << n; full = M - 1
    bits = ((np.arange(M)[:, None] >> np.arange(n)) & 1).astype(np.float64)
    ex = v - bits @ R
    ex = ex[1:full]
    return ex.max(), np.mean(ex > 1e-9 * max(1.0, abs(v[full])))

# ------------------------------------------------------------------ regole di ripartizione
def waterfill(c, s):
    c = np.asarray(c, float)
    if s <= 0: return np.zeros_like(c)
    if s >= c.sum(): return c.copy()
    lo, hi = 0.0, c.max()
    for _ in range(60):
        lam = (lo + hi) / 2
        if np.minimum(c, lam).sum() > s: hi = lam
        else: lo = lam
    return np.minimum(c, lo)

def rules_all(com, v, pi=0.4, pct_cluster=(0.2, 0.5, 0.3), n_perm=200, rng=None, with_nuc=True, vuln_quota=(0.02, 0.5), perms=None):
    inj, wd, role, ctype, vuln, n = com['inj'], com['wd'], com['role'], com['ctype'], com['vuln'], com['n']
    P = np.where(role == 'P')[0]; C = np.where(role == 'C')[0]
    G = inj.sum(1); W = wd.sum(1); e = np.minimum(G, W); B = e.sum()
    shw = np.where(e > 0, e / np.where(W > 0, W, 1), 0.0)       # e_t / W_t
    shg = np.where(e > 0, e / np.where(G > 0, G, 1), 0.0)       # e_t / G_t
    out = {}
    def side_P_hourly(pi_t):   # produttori: pro-rata orario dell'immissione, con quota oraria pi_t
        r = np.zeros(n); r[P] = (inj[:, P] * (shg * pi_t)[:, None]).sum(0); return r
    pot_P, pot_C = pi * B, (1 - pi) * B
    # EQ
    r = np.zeros(n); r[P] = pot_P / len(P); r[C] = pot_C / len(C); out['EQ'] = r
    # PA (annuale)
    r = np.zeros(n); r[P] = pot_P * inj[:, P].sum(0) / inj[:, P].sum(); r[C] = pot_C * wd[:, C].sum(0) / wd[:, C].sum(); out['PA'] = r
    # PS (consumo nelle ore con energia condivisa)
    sh = e > 0
    r = np.zeros(n); r[P] = pot_P * inj[sh][:, P].sum(0) / inj[sh][:, P].sum(); r[C] = pot_C * wd[sh][:, C].sum(0) / wd[sh][:, C].sum(); out['PS'] = r
    # PH (pro-rata orario)
    r = np.zeros(n); r[P] = pi * (inj[:, P] * shg[:, None]).sum(0); r[C] = (1 - pi) * (wd[:, C] * shw[:, None]).sum(0); out['PH'] = r
    # PG (progressiva / water-filling orario sul lato consumo)
    r = np.zeros(n); r[P] = pi * (inj[:, P] * shg[:, None]).sum(0)
    for t in np.where(sh)[0]: r[C] += (1 - pi) * waterfill(wd[t, C], e[t])
    out['PG'] = r
    # CT (albero di categorie: cluster persone fisiche / PMI / altri enti sul lato consumo; dentro il cluster PS)
    r = np.zeros(n); r[P] = pot_P * inj[sh][:, P].sum(0) / inj[sh][:, P].sum()
    wps = wd[sh][:, C].sum(0)
    present = [(ct, pc) for ct, pc in zip(('NP', 'SME', 'OE'), pct_cluster) if (ctype[C] == ct).any()]
    tot = sum(pc for _, pc in present)          # una categoria vuota cede la sua percentuale alle altre (pro rata)
    for ct, pc in present:
        m = (ctype[C] == ct); den = wps[m].sum()
        r[C[m]] = pot_C * (pc / tot) * (wps[m] / den if den > 0 else 1.0 / m.sum())
    out['CT'] = r
    # EP (scarcity pricing): il lato scarso prende tutta l'ora
    r = np.zeros(n)
    prod_scarce = (G < W); cons_scarce = (G > W); tie = (G == W)
    pit = np.where(prod_scarce, 1.0, np.where(tie, 0.5, 0.0))
    r[P] = (inj[:, P] * (shg * pit)[:, None]).sum(0); r[C] = (wd[:, C] * (shw * (1 - pit))[:, None]).sum(0); out['EP'] = r
    # PF (chiave giornaliera basata su correlazione di Pearson, rimappata in [0,1]) sul lato consumo
    r = np.zeros(n); r[P] = pi * (inj[:, P] * shg[:, None]).sum(0)
    days = com['T'] // 24
    for d in range(days):
        sl = slice(24 * d, 24 * d + 24); Bd = e[sl].sum()
        if Bd <= 0: continue
        g = G[sl]; rho = np.zeros(len(C))
        for k, i in enumerate(C):
            w = wd[sl, i]
            rho[k] = np.corrcoef(w, g)[0, 1] if w.std() > 0 and g.std() > 0 else 0.0
        rt = (1 + rho) / 2; r[C] += (1 - pi) * Bd * rt / rt.sum()
    out['PF'] = r
    # SW (quota riservata ai vulnerabili, resto PH)
    nq, qcap = vuln_quota
    Vm = (vuln[C] == 1); share_v = min(qcap, nq * Vm.sum()) if Vm.any() else 0.0
    r = np.zeros(n); r[P] = pi * (inj[:, P] * shg[:, None]).sum(0)
    ph_c = (wd[:, C] * shw[:, None]).sum(0)
    r[C] = (1 - pi) * (1 - share_v) * ph_c
    if Vm.any():
        wv = wd[:, C][:, Vm].sum(0); r[C[Vm]] += pot_C * share_v * wv / wv.sum()
    out['SW'] = r
    # MC normalizzato
    mc = marginal_from_v(v, n); out['MC'] = B * mc / mc.sum()
    # Shapley esatto e campionato
    phi = shapley_from_v(v, n); out['SV'] = phi
    rng = np.random.default_rng(0) if rng is None else rng
    out['SVa'] = shapley_sampled(v, n, n_perm, rng, perms=perms)
    if with_nuc: out['NUC'] = nucleolus_from_v(v, n)
    return out, dict(B=B, phi=phi, mc=mc, G=G, W=W, e=e, shw=shw, shg=shg, P=P, C=C)

# ------------------------------------------------------------------ indicatori (orientati: piu alto = meglio)
def gini(x):
    x = np.sort(np.asarray(x, float)); n = len(x)
    if x.sum() == 0: return 0.0
    return (2 * np.sum((np.arange(1, n + 1)) * x) / (n * x.sum())) - (n + 1) / n

def indicators(R, com, aux, v):
    n = com['n']; P, C = aux['P'], aux['C']; B = aux['B']
    wd, inj = com['wd'], com['inj']; e, shw, shg = aux['e'], aux['shw'], aux['shg']
    out = {}
    Rc = R[C]
    out['E1_1-Gini'] = 1 - gini(Rc)
    out['E2_Jain'] = (Rc.sum() ** 2) / (len(Rc) * (Rc ** 2).sum()) if (Rc ** 2).sum() > 0 else 1.0
    out['E3_MinMax'] = Rc.min() / Rc.max() if Rc.max() > 0 else 1.0
    rate = Rc / wd[:, C].sum(0)
    out['E4_1-GiniRate'] = 1 - gini(rate)
    qC = (wd[:, C] * shw[:, None]).sum(0) / e.sum()
    out['P1_PhysC'] = 1 - 0.5 * np.abs(Rc / Rc.sum() - qC).sum() if Rc.sum() > 0 else 0.0
    qP = (inj[:, P] * shg[:, None]).sum(0) / e.sum()
    out['P2_PhysP'] = 1 - 0.5 * np.abs(R[P] / R[P].sum() - qP).sum() if R[P].sum() > 0 else 0.0
    mc = aux['mc']; out['P3_-D_MC'] = -0.5 * np.abs(R / B - mc / mc.sum()).sum()
    out['P4_-D_SV'] = -0.5 * np.abs(R / B - aux['phi'] / B).sum()
    ex, blk = max_excess(R, v, n)
    out['S1_-MaxExcess'] = -ex / B
    out['S2_1-Blocking'] = 1 - blk
    out['S3_MinShare'] = R.min() / B
    npm = (com['ctype'][C] == 'NP')
    out['Q1_NPratio'] = (Rc[npm].sum() / Rc.sum()) / (npm.sum() / len(Rc)) if Rc.sum() > 0 else 0.0
    vm = (com['vuln'][C] == 1)
    out['Q2_VULNratio'] = (Rc[vm].sum() / Rc.sum()) / (vm.sum() / len(Rc)) if (vm.any() and Rc.sum() > 0) else np.nan
    out['pi_eff'] = R[P].sum() / B
    return out
