"""Pilot: esegue la pipeline completa (regole -> indicatori -> ranking -> concordanza -> cluster -> regret) su poche
composizioni sintetiche. NON sono risultati della tesi: servono a verificare che la pipeline funzioni e a stimare i tempi."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.stats import kendalltau, rankdata
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
import pilot_engine as pe

RULES = ['EQ', 'PA', 'PS', 'PH', 'PG', 'CT', 'EP', 'PF', 'SW', 'MC', 'SV', 'SVa', 'NUC']
IND = ['E1_1-Gini', 'E2_Jain', 'E3_MinMax', 'E4_1-GiniRate', 'P1_PhysC', 'P2_PhysP', 'P3_-D_MC', 'P4_-D_SV',
       'S1_-MaxExcess', 'S2_1-Blocking', 'S3_MinShare', 'Q1_NPratio', 'Q2_VULNratio']
CIRCULAR = ['P3_-D_MC', 'P4_-D_SV']      # dipendono da un riferimento game-theoretic (circolari per MC e SV)

def run(pv_to_load, sigma, seed, pi=0.4, mix='balanced'):
    com = pe.make_community(seed, pv_to_load, sigma, mix=mix)
    v = pe.all_values(com['inj'], com['wd'])
    out, aux = pe.rules_all(com, v, pi=pi, rng=np.random.default_rng(1000 + seed))
    ind = {r: pe.indicators(out[r], com, aux, v) for r in RULES}
    X = np.array([[ind[r][k] for k in IND] for r in RULES])
    return X, {r: ind[r]['pi_eff'] for r in RULES}, aux

def ranks(X):  # rango 1 = migliore (valore piu alto); NaN = peggiore
    return np.column_stack([rankdata(-np.nan_to_num(X[:, j], nan=-1e9), method='average') for j in range(X.shape[1])])

def tau_matrix(Rk):
    K = Rk.shape[1]; M = np.eye(K)
    for a in range(K):
        for b in range(a + 1, K):
            t = kendalltau(Rk[:, a], Rk[:, b]).statistic
            M[a, b] = M[b, a] = 0.0 if np.isnan(t) else t
    return M

def analyze(Rks, names, label, cut=0.25):
    """Concordanza fra indicatori, cluster (distanza (1-tau)/2) e rango per cluster con rimpianto minimax."""
    sel = [IND.index(k) for k in names]
    Ts = np.array([tau_matrix(Rk[:, sel]) for Rk in Rks]); Tm = Ts.mean(0)
    iu = np.triu_indices(len(sel), 1)
    print(f'\n##### {label}: {len(sel)} indicatori')
    print('tau medio fra coppie = %.2f; coppie con tau medio<0: %.0f%%; coppie con tau medio>0.8: %.0f%%' %
          (Ts[:, iu[0], iu[1]].mean(), 100 * (Tm[iu] < 0).mean(), 100 * (Tm[iu] > 0.8).mean()))
    D = (1 - Tm) / 2; np.fill_diagonal(D, 0); D = (D + D.T) / 2
    cl = fcluster(linkage(squareform(D, checks=False), 'average'), t=cut, criterion='distance')
    clusters = {}
    for k, c in zip(names, cl): clusters.setdefault(c, []).append(k)
    for c, ks in clusters.items(): print(f'  cluster {c}: {ks}')
    # rango per cluster (media dei rangui degli indicatori del cluster) e rimpianto minimax
    cr = np.array([[Rk[:, [IND.index(k) for k in ks]].mean(1) for ks in clusters.values()] for Rk in Rks])  # run x cluster x rule
    cr = cr.mean(0)                      # cluster x rule
    regret = cr - 1.0
    mm = regret.max(0); avg = cr.mean(0)
    order = np.argsort(mm)
    print('  Regole per rimpianto minimax (rango medio per cluster - 1; max sui cluster) | rango medio sui cluster:')
    print('   ' + ', '.join(f'{RULES[i]} {mm[i]:.1f}|{avg[i]:.1f}' for i in order))
    # sottoinsieme minimo: un rappresentante per cluster; tau fra Borda a pesi di cluster uguali e Borda dei soli rappresentanti
    reps = []
    for ks in clusters.values():
        idx = [names.index(k) for k in ks]
        reps.append(ks[int(np.argmax(Tm[np.ix_(idx, idx)].mean(1)))])
    vals = []
    for Rk in Rks:
        full = np.mean([Rk[:, [IND.index(k) for k in ks]].mean(1) for ks in clusters.values()], axis=0)
        sub = np.mean([Rk[:, IND.index(k)] for k in reps], axis=0)
        vals.append(kendalltau(full, sub).statistic)
    print(f'  Rappresentanti (1 per cluster): {reps}; tau fra Borda a cluster e Borda dei rappresentanti = {np.mean(vals):.2f}')
    return Tm, clusters

if __name__ == '__main__':
    t00 = time.time(); np.set_printoptions(linewidth=200, precision=2, suppress=True)
    grid = [(pv, sg, sd) for pv in (0.5, 1.0, 1.5) for sg in (0.3, 1.0) for sd in (1, 2, 3, 4)]
    Rks, Xs, pies = [], [], []
    for pv, sg, sd in grid:
        t0 = time.time(); X, pie, aux = run(pv, sg, sd)
        Xs.append(X); Rks.append(ranks(X)); pies.append(pie)
        print(f'run PV/carico={pv} sigma={sg} seme={sd}: {time.time()-t0:.1f}s  energia condivisa/immessa={aux["B"]/aux["G"].sum():.2f}', flush=True)
    Rks = np.array(Rks)
    print('\n=== Rango medio per indicatore (1 = migliore; media su %d run) ===' % len(grid))
    mr = Rks.mean(0)
    print('regola ' + ' '.join(f'{k[:10]:>10s}' for k in IND))
    for i, r in enumerate(RULES): print(f'{r:6s} ' + ' '.join(f'{mr[i, j]:10.1f}' for j in range(len(IND))))
    Tm, _ = analyze(Rks, IND, 'Tutti gli indicatori')
    print('\nMatrice tau di Kendall (media sui run):')
    print(' ' * 15 + ' '.join(f'{k[:6]:>6s}' for k in IND))
    for a, k in enumerate(IND): print(f'{k:14s} ' + ' '.join(f'{Tm[a, b]:6.2f}' for b in range(len(IND))))
    analyze(Rks, [k for k in IND if k not in CIRCULAR], 'Senza indicatori circolari (P3, P4)')
    print('\n=== Quota effettiva ai produttori (pi_eff), media; pi fisso = 0.40 per le regole semplici ===')
    print({r: round(float(np.mean([p[r] for p in pies])), 3) for r in RULES})
    print('\nTempo totale: %.0f s' % (time.time() - t00))
