"""Pilot 2: effetto della composizione (PV/carico, mix serale/diurno, eterogeneita) e della quota produttori pi sul ranking."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.stats import kendalltau, rankdata
import pilot_engine as pe
from pilot_run import RULES, IND, ranks, tau_matrix

def run(pv, sg, sd, mix, pi):
    com = pe.make_community(sd, pv, sg, mix=mix)
    v = pe.all_values(com['inj'], com['wd'])
    out, aux = pe.rules_all(com, v, pi=pi, rng=np.random.default_rng(1000 + sd))
    X = np.array([[pe.indicators(out[r], com, aux, v)[k] for k in IND] for r in RULES])
    corr_lp = np.corrcoef(aux['W'], aux['G'])[0, 1]
    return X, aux['B'] / aux['G'].sum(), corr_lp

if __name__ == '__main__':
    t00 = time.time(); np.set_printoptions(linewidth=220, precision=2, suppress=True)
    cells = {}
    for pv in (0.5, 1.0, 1.5):
        for mix in ('evening', 'daytime'):
            for sg in (0.3, 1.0):
                Rk = []; fr = []; cc = []
                for sd in (1, 2, 3):
                    X, f, c = run(pv, sg, sd, mix, 0.4); Rk.append(ranks(X)); fr.append(f); cc.append(c)
                cells[(pv, mix, sg)] = (np.array(Rk), np.mean(fr), np.mean(cc))
                print(f'cell PV/load={pv} mix={mix} sigma={sg}: shared/PV={np.mean(fr):.2f} corr(load,PV)={np.mean(cc):.2f}', flush=True)
    iu = np.triu_indices(len(IND), 1)
    print('\n=== tau medio fra indicatori, per cella ===')
    for k, (Rk, f, c) in cells.items():
        print(k, 'tau medio coppie = %.2f' % np.mean([tau_matrix(r)[iu].mean() for r in Rk]))
    # stabilita del ranking fra celle, per indicatore (tau fra vettori di rango medio)
    keys = list(cells); MR = {k: cells[k][0].mean(0) for k in keys}
    print('\n=== Stabilita del ranking fra composizioni (tau medio fra celle, per indicatore) ===')
    for j, ind in enumerate(IND):
        ts = [kendalltau(MR[a][:, j], MR[b][:, j]).statistic for ia, a in enumerate(keys) for b in keys[ia + 1:]]
        ts = np.nan_to_num(ts, nan=0.0)
        print(f'{ind:15s} tau medio = {np.mean(ts):5.2f}   min = {np.min(ts):5.2f}')
    # confronto: tra indicatori (nella stessa cella) vs tra celle (stesso indicatore)
    inter_ind = np.mean([tau_matrix(cells[k][0].mean(0))[iu].mean() for k in keys])
    print('\ntau medio fra indicatori (stessa cella) = %.2f' % inter_ind)
    # effetto della quota produttori pi sul ranking (cella base, 3 semi)
    print('\n=== Effetto di pi (cella PV/load=1.0, balanced, sigma=0.3): rango medio per indicatore chiave ===')
    key_ind = ['E1_1-Gini', 'P1_PhysC', 'S1_-MaxExcess', 'S3_MinShare']
    res = {}
    for pi in (0.2, 0.4, 0.6):
        Rk = []
        for sd in (1, 2, 3):
            X, f, c = run(1.0, 0.3, sd, 'balanced', pi); Rk.append(ranks(X))
        res[pi] = np.array(Rk).mean(0)
    for ind in key_ind:
        j = IND.index(ind)
        print(f'-- {ind}')
        print('rule  ' + ' '.join(f'pi={p:.1f}' for p in res))
        for i, r in enumerate(RULES): print(f'{r:5s} ' + ' '.join(f'{res[p][i, j]:6.1f}' for p in res))
    print('\nTempo totale: %.0f s' % (time.time() - t00))
