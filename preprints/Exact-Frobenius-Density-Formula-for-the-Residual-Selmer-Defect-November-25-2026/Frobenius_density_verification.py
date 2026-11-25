from itertools import product
from collections import Counter
import numpy as np
from sympy import primerange

def add(A,B,q):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and (y+v+1)%q==0:return None
    if x==u:m=(3*x*x+2*x-2)*pow((2*y+1)%q,-1,q)%q
    else:m=(v-y)*pow((u-x)%q,-1,q)%q
    z=(m*m-1-x-u)%q
    return z,(-y-1-m*(z-x))%q

def mul(A,n,q):
    B=None
    while n:
        if n&1:B=add(B,A,q)
        A=add(A,A,q);n//=2
    return B

for p in [3,5,7,11]:
    ct=Counter()
    for a,b,c,d in product(range(p),repeat=4):
        if (a*d-b*c)%p==0:continue
        k=2 if (a,b,c,d)==(1,0,0,1) else int(((a-1)*(d-1)-b*c)%p==0)
        ct[k]+=1
    assert ct[1]==(p+1)*(p*p-p-1) and ct[2]==1
    print('GL2',p,sorted(ct.items()))

# Count regular-unipotent type with v_p(#E)=1 (automatic type when q=1 mod p).
for p in [5,7,11]:
    cnt=0;silent=0;witness=[]
    for q in primerange(3,50001):
        q=int(q)
        if q==389 or q%p!=1:continue
        x=np.arange(q,dtype=np.int64)
        chi=np.full(q,-1,dtype=np.int8);chi[x*x%q]=1;chi[0]=0
        f=(4*x*x*x+4*x*x-8*x+1)%q
        N=int(q+1+chi[f].sum())
        if N%p or N%(p*p)==0:continue
        cnt+=1
        if mul((0,0),N//p,q) is None and mul((1,0),N//p,q) is None:
            silent+=1;witness.append(q)
    print('E',p,cnt,silent,witness,flush=True)
