"""Genera l'istanza 'golden' (N=6, T=168) e i risultati attesi dell'implementazione di riferimento, per verificare il futuro
modello Matlab sugli stessi dati. Eseguire: python3 -B -I make_golden.py"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pilot_engine as pe

RULES = ['EQ', 'PA', 'PS', 'PH', 'PG', 'CT', 'EP', 'PF', 'SW', 'MC', 'SV', 'SVa', 'NUC']
IND = ['E1_1-Gini', 'E2_Jain', 'E3_MinMax', 'E4_1-GiniRate', 'P1_PhysC', 'P2_PhysP', 'P3_-D_MC', 'P4_-D_SV',
       'S1_-MaxExcess', 'S2_1-Blocking', 'S3_MinShare', 'Q1_NPratio', 'Q2_VULNratio', 'pi_eff']
here = os.path.dirname(os.path.abspath(__file__)); outdir = os.path.join(here, 'golden'); os.makedirs(outdir, exist_ok=True)
rng = np.random.default_rng(2026); T = 168; n = 6
pvu = pe.pv_per_kwp(rng, T=T, yield_kwh_per_kwp=24.0)
G = np.column_stack([pvu * 6.0, pvu * 4.0])
W = np.column_stack([pe.load_profile('hh_evening', 45.0, rng, T), pe.load_profile('hh_day', 40.0, rng, T),
                     pe.load_profile('office', 80.0, rng, T), pe.load_profile('school', 50.0, rng, T)])
inj = np.hstack([G, np.zeros_like(W)]); wd = np.hstack([np.zeros_like(G), W])
meta = dict(n=n, T=T, role=['P', 'P', 'C', 'C', 'C', 'C'], ctype=['PR', 'PR', 'NP', 'NP', 'SME', 'OE'], vuln=[0, 0, 0, 1, 0, 0],
            pi=0.4, pct_cluster_NP_SME_OE=[0.2, 0.5, 0.3], vuln_quota_n_cap=[0.02, 0.5], price_per_kWh=1.0,
            note='Profili sintetici (seed 2026). 0-based; ordine membri: produttori P1,P2, poi consumatori C1..C4. Un passo = 1 ora, 7 giorni da 24 ore.')
prng = np.random.default_rng(99); perms = np.array([prng.permutation(n) for _ in range(24)])
com = dict(inj=inj, wd=wd, role=np.array(meta['role']), ctype=np.array(meta['ctype']), vuln=np.array(meta['vuln']), n=n, T=T)
v = pe.all_values(inj, wd)
out, aux = pe.rules_all(com, v, pi=0.4, perms=perms)
R = np.array([out[r] for r in RULES])
ind = [pe.indicators(out[r], com, aux, v) for r in RULES]
Ind = np.array([[d[k] for k in IND] for d in ind])
np.savetxt(os.path.join(outdir, 'golden_inj.csv'), inj, delimiter=',', fmt='%.12e')
np.savetxt(os.path.join(outdir, 'golden_wd.csv'), wd, delimiter=',', fmt='%.12e')
np.savetxt(os.path.join(outdir, 'golden_perms_0based.csv'), perms, delimiter=',', fmt='%d')
np.savetxt(os.path.join(outdir, 'golden_values_v_by_mask.csv'), v, delimiter=',', fmt='%.12e')
np.savetxt(os.path.join(outdir, 'golden_rewards.csv'), R, delimiter=',', fmt='%.12e', header='righe: ' + ','.join(RULES) + ' | colonne: membri 1..6')
np.savetxt(os.path.join(outdir, 'golden_indicators.csv'), Ind, delimiter=',', fmt='%.12e', header='righe: ' + ','.join(RULES) + ' | colonne: ' + ','.join(IND))
json.dump(meta, open(os.path.join(outdir, 'golden_meta.json'), 'w'), indent=1, ensure_ascii=False)
np.set_printoptions(linewidth=200, precision=4, suppress=True)
print('B =', aux['B'], ' v(N) =', v[-1])
print('Premi (righe = regole', RULES, ')'); print(R)
print('somme righe / B:', np.round(R.sum(1) / aux['B'], 9))
print('Indicatori:', IND); print(Ind)
