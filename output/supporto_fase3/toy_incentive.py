"""Toy check (NOT thesis results): incentive strength of allocation rules in a shared-energy game.
1 producer (PV) + 6 consumers; one representative day; hourly shared energy = min(PV, total load)."""
import sys, os, itertools, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from toy_game import pv_profile, load_house, load_day, shared, shapley

PI=0.5  # fixed producer share for the simple rules (parameter, arbitrary)

def hourly_shared(pv,L): return np.minimum(pv,L.sum(0))

def waterfill(c, s):
    """give s units among consumers with demands c (vector), progressive/water-filling"""
    c=np.asarray(c,float)
    if s<=0: return np.zeros_like(c)
    if s>=c.sum(): return c.copy()
    lo,hi=0.0,c.max()
    for _ in range(80):
        lam=(lo+hi)/2
        if np.minimum(c,lam).sum()>s: hi=lam
        else: lo=lam
    return np.minimum(c,lo)

def rewards(rule,pv,L,pi=PI):
    n=L.shape[0]
    s=hourly_shared(pv,L)           # per hour shared energy (value = kWh, price normalised to 1)
    B=s.sum()
    cons=(1-pi)*B
    if rule=='equal':
        r=np.full(n,cons/n); prod=pi*B
    elif rule=='prop_annual':
        r=cons*L.sum(1)/L.sum(); prod=pi*B
    elif rule=='prop_hourly':
        r=np.zeros(n)
        for h in range(24):
            if L[:,h].sum()>0: r+= (1-pi)*s[h]*L[:,h]/L[:,h].sum()
        prod=pi*B
    elif rule=='progressive':
        r=np.zeros(n)
        for h in range(24):
            r+= (1-pi)*waterfill(L[:,h],s[h])
        prod=pi*B
    elif rule=='marginal':
        m=np.array([B-hourly_shared(pv,np.delete(L,i,0)).sum() for i in range(n)])
        r=cons*m/m.sum(); prod=pi*B
    elif rule=='shapley':
        phi,vals=shapley(pv,L); r=phi[1:]; prod=phi[0]
    else: raise ValueError(rule)
    return r,prod,B

RULES=['equal','prop_annual','prop_hourly','progressive','marginal','shapley']

def shifted(L,i,h_from,h_to,q):
    L2=L.copy(); L2[i,h_from]-=q; L2[i,h_to]+=q; return L2

if __name__=='__main__':
    # community with three consumers of identical annual energy and different synchronism
    pv=pv_profile(10.0)
    ann=6.0
    def flat(a): return np.full(24,a/24.0)
    L=np.array([load_house(ann),           # 0 evening-peaking (asynchronous)
                flat(ann),                 # 1 flat
                load_day(ann),             # 2 daytime (synchronous), same annual energy
                load_house(10.0),load_day(14.0),load_day(30.0)])
    print('annual energy of members 0-2:',L[:3].sum(1))
    print('\n== reward dispersion at equal annual energy (members 0,1,2 differ only in synchronism) ==')
    print(f'{"rule":12s} R0(async)  R1(flat)  R2(sync)   R2/R0')
    for rule in RULES:
        r,prod,B=rewards(rule,pv,L)
        print(f'{rule:12s} {r[0]:8.3f} {r[1]:9.3f} {r[2]:9.3f} {r[2]/r[0]:8.2f}   (pie B={B:.2f}, producer={prod:.2f}, sum={r.sum()+prod:.2f})')
    print('\n== internalisation ratio: member 0 moves q kWh from hour 19 to hour 12 ==')
    q=0.4
    print(f'(load of member 0 at h19 = {L[0,19]:.3f} kWh; q={q})')
    print(f'{"rule":12s}   dB     dR0    dR0/dB   (1/N={1/6:.3f})')
    for rule in RULES:
        r0,p0,B0=rewards(rule,pv,L)
        L2=shifted(L,0,19,12,q)
        r1,p1,B1=rewards(rule,pv,L2)
        print(f'{rule:12s} {B1-B0:6.3f} {r1[0]-r0[0]:7.3f} {(r1[0]-r0[0])/(B1-B0) if B1!=B0 else float("nan"):8.3f}')
    print('\n== same, but member 5 (largest daytime consumer, 30 kWh/day) moves q kWh from hour 18 to hour 12 ==')
    for rule in RULES:
        r0,p0,B0=rewards(rule,pv,L)
        L2=shifted(L,5,18,12,q)
        r1,p1,B1=rewards(rule,pv,L2)
        print(f'{rule:12s} {B1-B0:6.3f} {r1[5]-r0[5]:7.3f} {(r1[5]-r0[5])/(B1-B0) if B1!=B0 else float("nan"):8.3f}')

    print('\n== PV-scarce regime (3 kWp): member 2 INCREASES load by q at hour 12 (no shift; hour is generation-constrained) ==')
    pv3=pv_profile(3.0)
    print(f'at h12: PV={pv3[12]:.3f} kWh vs total load={L[:,12].sum():.3f} kWh  -> generation-constrained hour: {pv3[12]<L[:,12].sum()}')
    for rule in RULES:
        r0,p0,B0=rewards(rule,pv3,L)
        L2=L.copy(); L2[2,12]+=q
        r1,p1,B1=rewards(rule,pv3,L2)
        print(f'{rule:12s} dB={B1-B0:6.3f}  dR2={r1[2]-r0[2]:7.3f}   (extra kWh consumed by member 2: {q})')
