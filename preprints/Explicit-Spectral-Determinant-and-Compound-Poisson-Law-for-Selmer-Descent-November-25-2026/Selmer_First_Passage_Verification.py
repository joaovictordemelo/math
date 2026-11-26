"""Reproduce numerical and exact path checks for the Selmer descent paper.
Requirements: Python 3.10+, mpmath, numpy, scipy.
No elliptic curve or modular-symbol computations are performed here.
"""
from fractions import Fraction as F
from math import prod
import mpmath as mp
import numpy as np
from scipy.linalg import eigh_tridiagonal


def path_probability(p, d, k):
    q = F(1, p)
    steps = d + 2*k
    v = {d: F(1)}
    for _ in range(steps):
        w = {}
        for j, a in v.items():
            if j == 0:  # Remove paths that already hit zero.
                continue
            for i, b in ((j-1, 1-q**j), (j+1, q**j)):
                w[i] = w.get(i, F(0)) + a*b
        v = w
    return v.get(0, F(0))


def determinant_probability(p, d, k):
    q = F(1,p)
    N = d+k
    one = [F(1)]+[F(0)]*k
    D = {N+1: one[:], N: one[:]}
    for j in range(N-1, 0, -1):
        a2 = q**j*(1-q**(j+1))
        D[j] = [D[j+1][i] - (a2*D[j+2][i-1] if i else 0)
                for i in range(k+1)]
    # Formal power series division (D[1][0] = 1).
    h = []
    for i in range(k+1):
        h.append(D[d+1][i] - sum(D[1][j]*h[i-j] for j in range(1,i+1)))
    return prod(1-q**j for j in range(1,d+1))*h[k]


def explicit_det(z, q, N=50):
    # D_1(z) = sum_n (-z)^n q^(n^2) sum_{j=0}^n q^j/(q^2;q^2)_j.
    den = mp.mpf(1)
    s = mp.mpf(1)
    out = mp.mpf(1)
    for n in range(1,N+1):
        den *= 1-q**(2*n)
        s += q**n/den
        out += (-z)**n*q**(n*n)*s
    return out


def spectrum(p, start=1, N=80):
    q = 1/p
    j = np.arange(start,start+N-1,dtype=float)
    a = np.sqrt(q**j*(1-q**(j+1)))
    return eigh_tridiagonal(np.zeros(N),a,eigvals_only=True)


def main():
    checks=0
    for p in [3,5,7,11,17]:
        for d in [2,4,8]:
            for k in range(11):
                assert path_probability(p,d,k)==determinant_probability(p,d,k),(p,d,k)
                checks+=1
    print(f'Exact rational path/determinant checks: {checks}/{checks}')
    mp.mp.dps=70
    print('p,alpha_q_series,alpha_matrix,mean_tau2,lambda_infty,poisson_bound')
    for p in [3,5,7,11,17,31]:
        q=mp.mpf(1)/p
        # Unique first root in (1,q^-2).
        lo,hi=mp.mpf(1),q**-2
        for _ in range(230):
            mid=(lo+hi)/2
            if explicit_det(mid,q)>0: lo=mid
            else: hi=mid
        alpha=1/((lo+hi)/2)
        eig=spectrum(p)
        alpha_mat=eig[-1]**2
        assert abs(float(alpha)-alpha_mat)<2e-14
        tail=spectrum(p,start=3)
        T2=2+sum(eig**2/(1-eig**2))-sum(tail**2/(1-tail**2))
        lam=-sum(mp.log1p(-q**j) for j in range(1,151))
        trace=q/(1-q)-q**3/(1-q*q)
        bound=1-mp.exp(-(lam-trace))
        print(f'{p},{float(alpha):.12f},{alpha_mat:.12f},{T2:.9f},{float(lam):.9f},{float(bound):.9f}')

if __name__=='__main__': main()
