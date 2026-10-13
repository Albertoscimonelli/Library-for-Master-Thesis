"""Test di correttezza dell'implementazione di riferimento (pilot). Esegui: python3 -B -I test_engine.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pilot_engine as pe

def check(name, cond, extra=''):
    print(('OK   ' if cond else 'FAIL ') + name + (' ' + extra if extra else '')); 
    assert cond, name

# T1: gioco "guanto" 1 produttore + 2 consumatori, offerta scarsa (un solo passo orario)
inj = np.array([[1.0, 0, 0]]); wd = np.array([[0, 1.0, 1.0]])
v = pe.all_values(inj, wd); phi = pe.shapley_from_v(v, 3); nuc = pe.nucleolus_from_v(v, 3)
check('T1 Shapley glove 1+2 = (2/3, 1/6, 1/6)', np.allclose(phi, [2/3, 1/6, 1/6]), str(np.round(phi, 4)))
check('T1 nucleolo glove 1+2 = (1, 0, 0) (core = singolo punto)', np.allclose(nuc, [1, 0, 0], atol=1e-6), str(np.round(nuc, 6)))
# T2: offerta abbondante: v(S)=|S cap C| se P in S  -> Shapley (n/2, 1/2, 1/2) con n=2 consumatori unitari
inj = np.array([[5.0, 0, 0]]); wd = np.array([[0, 1.0, 1.0]])
v = pe.all_values(inj, wd); phi = pe.shapley_from_v(v, 3)
check('T2 Shapley offerta abbondante = (1, 1/2, 1/2)', np.allclose(phi, [1, .5, .5]), str(np.round(phi, 4)))
# T3: efficienza, simmetria, non negativita su una comunita sintetica N=8
rng = np.random.default_rng(3)
T = 240
G = np.abs(rng.normal(3, 1, size=(T, 2))) * (np.arange(T)[:, None] % 24 > 7) * (np.arange(T)[:, None] % 24 < 17)
W = np.abs(rng.normal(1, 0.5, size=(T, 6)))
W[:, 1] = W[:, 0]                                            # giocatori 1 e 2 (consumatori 0 e 1) identici
inj = np.hstack([G, np.zeros((T, 6))]); wd = np.hstack([np.zeros((T, 2)), W]); n = 8
v = pe.all_values(inj, wd); phi = pe.shapley_from_v(v, n)
check('T3 efficienza Shapley', abs(phi.sum() - v[-1]) < 1e-8 * v[-1])
check('T3 simmetria Shapley (giocatori identici)', abs(phi[2] - phi[3]) < 1e-9 * v[-1])
check('T3 non negativita Shapley (gioco monotono)', phi.min() > -1e-9)
mc = pe.marginal_from_v(v, n); check('T3 contributi marginali >= 0', mc.min() >= -1e-9)
nuc = pe.nucleolus_from_v(v, n); ex, blk = pe.max_excess(nuc, v, n)
check('T3 nucleolo efficiente e nel core (max eccesso <= 1e-6 v(N))', abs(nuc.sum() - v[-1]) < 1e-6 * v[-1] and ex <= 1e-6 * v[-1], f'max eccesso/v(N)={ex/v[-1]:.2e}')
check('T3 nucleolo simmetrico', abs(nuc[2] - nuc[3]) < 1e-5 * v[-1])
eps = pe.least_core_eps(v, n); check('T3 least core eps* <= 0 (core non vuoto, gioco bilanciato)', eps <= 1e-8 * v[-1], f'eps*={eps:.3g}')
# T4: campionamento Shapley converge e somma a v(N)
ps = pe.shapley_sampled(v, n, 4000, np.random.default_rng(1))
check('T4 Shapley campionato efficiente', abs(ps.sum() - v[-1]) < 1e-8 * v[-1])
check('T4 Shapley campionato vicino all esatto (errore L1 relativo < 3%)', np.abs(ps - phi).sum() / v[-1] < 0.03, f'{np.abs(ps-phi).sum()/v[-1]:.3f}')
# T5: water-filling
c = np.array([1.0, 2.0, 5.0]); a = pe.waterfill(c, 4.0)
check('T5 water-filling (1,2,5) con 4 -> (1,1.5,1.5)', np.allclose(a, [1, 1.5, 1.5]), str(a))
check('T5 water-filling somma e limiti', abs(a.sum() - 4) < 1e-9 and np.all(a <= c + 1e-12))
# T6: regole su una comunita sintetica: efficienza e confronto con calcolo indipendente di PH
com = pe.make_community(7, 1.0, 0.3)
v = pe.all_values(com['inj'], com['wd']); out, aux = pe.rules_all(com, v, pi=0.4, rng=np.random.default_rng(0))
B = aux['B']
for k, r in out.items(): check(f'T6 efficienza regola {k}', abs(r.sum() - B) < 1e-7 * B, f'sum/B={r.sum()/B:.9f}')
P, C = aux['P'], aux['C']; inj, wd = com['inj'], com['wd']; ph = np.zeros(com['n'])
for t in range(com['T']):
    G_t, W_t = inj[t].sum(), wd[t].sum(); e_t = min(G_t, W_t)
    if e_t > 0:
        for i in P: ph[i] += 0.4 * e_t * inj[t, i] / G_t
        for i in C: ph[i] += 0.6 * e_t * wd[t, i] / W_t
check('T6 PH = pro-rata orario calcolato con cicli indipendenti', np.allclose(out['PH'], ph, rtol=1e-9, atol=1e-9))
check('T6 EQ: parti uguali dentro ciascun lato', np.allclose(out['EQ'][C], out['EQ'][C][0]) and np.allclose(out['EQ'][P], out['EQ'][P][0]))
check('T6 PA: tasso di premio uguale fra consumatori', np.allclose(out['PA'][C] / wd[:, C].sum(0), (out['PA'][C] / wd[:, C].sum(0))[0]))
# T7: equivalenza Eq. 34-35 della tesi Cecini (peso produttore = somma_y [E_inj,i,y / sum_i E_inj,i,y] * SE_y, normalizzato) con PH lato produttori
w = np.array([sum((inj[t, i] / inj[t, P].sum()) * aux['e'][t] for t in range(com['T']) if inj[t, P].sum() > 0) for i in P])
check('T7 lato produttori di PH proporzionale ai pesi di Cecini (Eq. 34-35)', np.allclose(out['PH'][P] / out['PH'][P].sum(), w / w.sum(), rtol=1e-9))

# T8: categoria vuota in CT: la percentuale dei cluster assenti e ridistribuita e la quota ai produttori resta pi
com2 = dict(com); ct2 = com['ctype'].copy(); ct2[ct2 == 'OE'] = 'SME'; com2['ctype'] = ct2
v2 = pe.all_values(com2['inj'], com2['wd']); out2, aux2 = pe.rules_all(com2, v2, pi=0.4, rng=np.random.default_rng(0), with_nuc=False)
check('T8 CT con categoria vuota: efficienza', abs(out2['CT'].sum() - aux2['B']) < 1e-7 * aux2['B'])
check('T8 CT con categoria vuota: quota ai produttori = pi', abs(out2['CT'][aux2['P']].sum() / aux2['B'] - 0.4) < 1e-9)

# T9: la regola EP (il lato scarso prende l'ora) e l'allocazione con i prezzi duali orari di un gioco di produzione lineare: sta nel core
for pv_ in (0.5, 1.0, 1.5):
    com3 = pe.make_community(11, pv_, 0.5); v3 = pe.all_values(com3['inj'], com3['wd'])
    out3, aux3 = pe.rules_all(com3, v3, pi=0.4, rng=np.random.default_rng(0), with_nuc=False)
    ex3, _ = pe.max_excess(out3['EP'], v3, com3['n'])
    check(f'T9 EP nel core (PV/carico={pv_})', ex3 <= 1e-9 * aux3['B'], f'max eccesso/B={ex3/aux3["B"]:.2e}')

# T10: indicatori su casi calcolabili a mano e valori attesi per regole campione
check('T10 Gini([1,1,1,1]) = 0', abs(pe.gini([1, 1, 1, 1])) < 1e-12)
check('T10 Gini([0,0,0,1]) = 0.75', abs(pe.gini([0, 0, 0, 1]) - 0.75) < 1e-12)
check('T10 Gini([1,2,3]) = 2/9', abs(pe.gini([1, 2, 3]) - 2 / 9) < 1e-12)
com4 = pe.make_community(5, 1.0, 0.3); v4 = pe.all_values(com4['inj'], com4['wd'])
out4, aux4 = pe.rules_all(com4, v4, pi=0.4, rng=np.random.default_rng(0), with_nuc=False)
ind_eq = pe.indicators(out4['EQ'], com4, aux4, v4); ind_ph = pe.indicators(out4['PH'], com4, aux4, v4); ind_pa = pe.indicators(out4['PA'], com4, aux4, v4)
check('T10 EQ: E1=E2=E3=1 (consumatori con premi uguali)', all(abs(ind_eq[k] - 1) < 1e-9 for k in ('E1_1-Gini', 'E2_Jain', 'E3_MinMax')))
check('T10 PH: P1c = P2p = 1 (proporzionalita fisica per definizione)', abs(ind_ph['P1_PhysC'] - 1) < 1e-9 and abs(ind_ph['P2_PhysP'] - 1) < 1e-9)
check('T10 PA: E4 = 1 (stesso premio per kWh fra consumatori)', abs(ind_pa['E4_1-GiniRate'] - 1) < 1e-9)
check('T10 pi_eff = pi per le regole semplici', abs(ind_ph['pi_eff'] - 0.4) < 1e-9 and abs(ind_eq['pi_eff'] - 0.4) < 1e-9)

# T11: coerenza con la colonna P7 (partecipazione di gruppo = core) della Tab. 1 di gonzalezasenjo2025: Shapley e Average Price fuori dal core, Extreme Price nel core
com5 = pe.make_community(7, 1.0, 0.3); v5 = pe.all_values(com5['inj'], com5['wd'])
out5, aux5 = pe.rules_all(com5, v5, pi=0.5, rng=np.random.default_rng(0), with_nuc=False)
ex_sv, _ = pe.max_excess(out5['SV'], v5, com5['n']); ex_ap, _ = pe.max_excess(out5['PH'], v5, com5['n']); ex_ep, _ = pe.max_excess(out5['EP'], v5, com5['n'])
check('T11 Shapley fuori dal core (P7 = N in Tab. 1)', ex_sv > 1e-3 * aux5['B'], f'max eccesso/B={ex_sv/aux5["B"]:+.4f}')
check('T11 Average Price (= PH a pi=0,5) fuori dal core (P7 = N in Tab. 1)', ex_ap > 1e-3 * aux5['B'], f'max eccesso/B={ex_ap/aux5["B"]:+.4f}')
check('T11 Extreme Price (= EP) nel core (P7 = Y in Tab. 1)', ex_ep <= 1e-9 * aux5['B'], f'max eccesso/B={ex_ep/aux5["B"]:+.2e}')
print('\nTutti i test superati.')
