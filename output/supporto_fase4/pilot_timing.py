"""Tempi di calcolo del pilot (Python/numpy/scipy) per N crescente. Indicativi: Matlab sara diverso."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pilot_engine as pe

def community(n, seed=0, T=8760):
    rng = np.random.default_rng(seed)
    n_p = max(2, n // 4); n_c = n - n_p
    kinds = ['hh_evening', 'hh_day', 'office', 'shop', 'school', 'industry']
    W = np.column_stack([pe.load_profile(kinds[k % 6], float(rng.lognormal(np.log(8000), 0.8)), rng, T) for k in range(n_c)])
    kwp = W.sum() / 1250.0
    G = np.column_stack([pe.pv_per_kwp(rng, T) * kwp / n_p for _ in range(n_p)])
    return np.hstack([G, np.zeros_like(W)]), np.hstack([np.zeros_like(G), W])

def sampled_shapley_cumsum(inj, wd, n_perm, rng):
    """Shapley campionato SENZA enumerare coalizioni: per ogni permutazione somme cumulate lungo l'ordine."""
    T, n = inj.shape; phi = np.zeros(n)
    for _ in range(n_perm):
        perm = rng.permutation(n)
        cg = np.cumsum(inj[:, perm], axis=1); cw = np.cumsum(wd[:, perm], axis=1)
        vals = np.minimum(cg, cw).sum(0)              # v dei prefissi
        marg = np.diff(np.r_[0.0, vals])
        phi[perm] += marg
    return phi / n_perm

if __name__ == '__main__':
    print('N   | valori v(S) | Shapley | least core LP | nucleolo (LP iterativi)')
    for n in (8, 10, 12, 14, 16, 18):
        inj, wd = community(n)
        t0 = time.time(); v = pe.all_values(inj, wd); tv = time.time() - t0
        t0 = time.time(); phi = pe.shapley_from_v(v, n); ts = time.time() - t0
        t0 = time.time(); eps = pe.least_core_eps(v, n); tl = time.time() - t0
        tn = float('nan')
        if n <= 16:
            t0 = time.time(); x = pe.nucleolus_from_v(v, n); tn = time.time() - t0
        print(f'{n:3d} | {tv:8.1f} s  | {ts:6.2f} s | {tl:8.1f} s    | {tn:8.1f} s   (eps*={eps:.3g})', flush=True)
    print('\nShapley campionato con somme cumulate (M=500 permutazioni):')
    for n in (50, 100, 200):
        inj, wd = community(n, T=8760)
        t0 = time.time(); phi = sampled_shapley_cumsum(inj, wd, 500, np.random.default_rng(1)); dt = time.time() - t0
        print(f'N={n:4d}: {dt:6.1f} s  (somma phi/v(N) = {phi.sum()/np.minimum(inj.sum(1),wd.sum(1)).sum():.6f})', flush=True)
