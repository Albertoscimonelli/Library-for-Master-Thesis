"""Controllo numerico preliminare per la Fase 3 (NON sono risultati per la tesi).
Esempio giocattolo: un giorno rappresentativo ripetuto, 1 produttore e 6 consumatori, profili inventati
per illustrare la struttura del gioco. Servono solo a verificare affermazioni qualitative [INFERENZA].
Eseguire con:  python3 -I toy_game.py   (richiede numpy e scipy)
Single representative day (24 h), 1 producer (pure injection), 6 consumers.
Shared energy per hour = min(injection, total withdrawal) (Italian definition, simplified).
"""
import itertools, math
import numpy as np
from scipy.optimize import linprog

H=np.arange(24)
def pv_profile(kwp):
    # bell between 7 and 17 h
    p=np.zeros(24)
    for h in range(24):
        if 7<=h<=17:
            p[h]=math.sin(math.pi*(h-7+0.5)/11.0)
    return kwp*p
def load_house(ann):  # evening-peaking
    base=np.array([0.3,0.25,0.2,0.2,0.2,0.3,0.5,0.7,0.5,0.4,0.4,0.5,0.6,0.5,0.4,0.4,0.5,0.8,1.2,1.4,1.3,1.0,0.7,0.4])
    return base/base.sum()*ann
def load_day(ann):    # daytime flat 8-18
    b=np.zeros(24); b[8:18]=1.0; b[[6,7,18,19]]=0.3
    return b/b.sum()*ann

def make(pv_kwp=10.0, scale=1.0):
    pv=pv_profile(pv_kwp)
    loads=[load_house(6*scale),load_house(6*scale),load_house(6*scale),
           load_day(14*scale),load_day(8*scale),load_day(30*scale)]
    return pv,np.array(loads)

def shared(pv,L,S):
    """value of coalition S: S is a set of player ids; 0 = producer, 1..n = consumers"""
    if 0 not in S: return 0.0
    cons=[i-1 for i in S if i>0]
    if not cons: return 0.0
    return float(np.minimum(pv, L[cons].sum(0)).sum())

def shapley(pv,L):
    n=L.shape[0]+1
    phi=np.zeros(n)
    vals={}
    for r in range(n+1):
        for S in itertools.combinations(range(n),r):
            vals[S]=shared(pv,L,set(S))
    for i in range(n):
        for r in range(n):
            for S in itertools.combinations([j for j in range(n) if j!=i],r):
                w=math.factorial(r)*math.factorial(n-r-1)/math.factorial(n)
                Si=tuple(sorted(S+(i,)))
                phi[i]+=w*(vals[Si]-vals[S])
    return phi,vals

def core_lp(pv,L):
    """Check core non-emptiness / min epsilon for least core (value of eps*) via LP."""
    n=L.shape[0]+1
    vals={}
    for r in range(1,n+1):
        for S in itertools.combinations(range(n),r):
            vals[S]=shared(pv,L,set(S))
    A=[];b=[]
    for S,v in vals.items():
        if len(S)==n: continue
        row=np.zeros(n+1)
        for i in S: row[i]=-1.0   # -x(S) - e <= -v(S)
        row[n]=-1.0
        A.append(row); b.append(-v)
    Aeq=[np.r_[np.ones(n),0.0]]; beq=[vals[tuple(range(n))]]
    c=np.r_[np.zeros(n),1.0]
    res=linprog(c,A_ub=np.array(A),b_ub=np.array(b),A_eq=np.array(Aeq),b_eq=beq,bounds=[(None,None)]*n+[(None,None)],method='highs')
    return res.x[:n],res.x[n],vals[tuple(range(n))]

if __name__=='__main__':
    print('== Experiment 1: producer share under Shapley and core as a function of PV size ==')
    for kwp in [2,5,10,20,40,80]:
        pv,L=make(kwp)
        phi,vals=shapley(pv,L)
        B=vals[tuple(range(7))]
        x,eps,_=core_lp(pv,L)
        print(f'PV={kwp:3d} kWp  B={B:7.2f} kWh  PV/load={pv.sum()/L.sum():5.2f}  Shapley producer share={phi[0]/B:5.3f}  least-core eps*={eps:8.4f}')
    print('(eps* <= 0: core non vuoto; eps* = 0: nessuna allocazione strettamente interna al core. Il punto di least core restituito dall LP non e unico e non viene riportato.)')
