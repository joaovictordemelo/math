# Recovering Selmer Invariants from Cyclic Mazur–Tate Leading Terms

**Author:** João Víctor de Mello  
**Date:** November 25, 2026

## Abstract

This paper develops an integral framework for recovering Selmer invariants of elliptic curves from the leading augmentation terms of cyclic Mazur–Tate elements.

By combining integral Fitting ideals, Kurihara derivatives, Euler systems and a factorial-free polarization identity, we establish, under the hypotheses specified in the manuscript,

```math
\min_K v_p(\operatorname{LT}_r(\Theta_K))
= v_p\left(\#\mathrm{Sha}(E)[p^\infty]\right).
```

The minimum is interpreted as infinity when the primary Tate–Shafarevich group is infinite.

This establishes an exact arithmetic characterization of primary Tate–Shafarevich finiteness through cyclic Mazur–Tate leading terms, without assuming the Birch–Swinnerton-Dyer conjecture.

## Main Contributions

- Exact minimum-valuation formula for cyclic Mazur–Tate leading terms.
- Integral polarization without factorial denominators.
- Removal of the restriction $r<p$.
- Recovery of higher Selmer Fitting ideals.
- A finite arithmetic criterion for primary Tate–Shafarevich finiteness.
- Explicit computational certificates at 19 primes omitted from the Stein–Wuthrich computation.

## Principal Arithmetic Consequence

Under the stated hypotheses and sufficient integral precision, the leading augmentation coefficient provides the bound

```math
\#\mathrm{Sha}(E)[p^\infty]
\leq p^{2\lfloor v_p(C_r)/2\rfloor}.
```

In particular,

```math
v_p(C_r)\leq 1
\implies
\mathrm{Sha}(E)[p^\infty]=0.
```

This allows certain residually vanishing modular-symbol coefficients to certify primary Tate–Shafarevich vanishing through higher integral precision.

## Computational Application

The manuscript applies the theoretical framework to the rank-two elliptic curve of conductor 389:

```math
E:\quad y^2+y=x^3+x^2-2x.
```

The computational results include certificates at the exceptional prime 16231 and other primes omitted from earlier computations.

## Reproducibility

This repository contains:

- Research manuscript (PDF).
- Editable LaTeX source.
- Python verification programs.
- Exact computational results.
- Reproduction instructions.

## References

1. Mazur, B. and Tate, J. (1987).
   [Refined conjectures of the Birch and Swinnerton-Dyer type](https://doi.org/10.1215/S0012-7094-87-05431-7).

2. Kurihara, M.
   [The structure of Selmer groups of elliptic curves and modular symbols](https://arxiv.org/abs/1407.2465).

3. Kim, C. H.
   [The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves](https://arxiv.org/abs/2203.12159).

4. Bullach, D. and Honnor, A. (2025).
   [On the refined Birch–Swinnerton-Dyer type conjectures of Mazur and Tate](https://arxiv.org/abs/2511.07203).

5. Castella, F. and Sano, T. (2026).
   [On refined nonvanishing conjectures by Kurihara and Kolyvagin](https://arxiv.org/abs/2601.14504).

## Research Status

The principal results are established under the hypotheses specified in the manuscript, using existing Euler-system and Fitting-ideal theorems together with integral augmentation and polarization techniques.

Historical originality and the mathematical arguments remain subject to independent verification and peer review.

The manuscript does not claim a complete proof of the Birch–Swinnerton-Dyer conjecture.

## Keywords

Birch–Swinnerton-Dyer conjecture · Elliptic curves · Mazur–Tate elements · Selmer groups · Tate–Shafarevich groups · Fitting ideals · Euler systems · Galois cohomology · Iwasawa theory · Integral arithmetic.
