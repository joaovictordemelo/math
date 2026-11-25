# Recovering Selmer Invariants from Cyclic Mazur–Tate Leading Terms

**Author:** João Víctor de Mello  
**Date:** November 25, 2026

## Abstract

This paper develops an integral framework for recovering Selmer invariants of elliptic curves from the leading augmentation terms of cyclic Mazur–Tate elements.

By combining integral Fitting ideals, Kurihara derivatives, Euler systems and a factorial-free polarization identity, we establish, under the hypotheses specified in the manuscript,

```math
\min_K v_p(\mathrm{LT}_r(\Theta_K)) = v_p(|\mathrm{Sha}(E)[p^\infty]|).
```

The minimum is interpreted as infinity when the primary Tate–Shafarevich group is infinite.

This provides an exact arithmetic characterization of primary Tate–Shafarevich finiteness without assuming the Birch–Swinnerton-Dyer conjecture.

## Main Contributions

- Exact minimum-valuation formula for cyclic Mazur–Tate leading terms.
- Integral polarization without factorial denominators.
- Removal of the restriction on rank relative to p.
- Recovery of higher Selmer Fitting ideals.
- Finite arithmetic criteria for primary Tate–Shafarevich finiteness.
- Computational certificates at 19 primes omitted from the Stein–Wuthrich computation.

## Principal Arithmetic Consequence

Under the stated hypotheses and sufficient integral precision,

```math
|\mathrm{Sha}(E)[p^\infty]| \leq p^{2\lfloor v_p(C_r)/2\rfloor}.
```

In particular,

```math
v_p(C_r)\leq 1 \implies \mathrm{Sha}(E)[p^\infty]=0.
```

This allows certain residually vanishing modular-symbol coefficients to certify primary Tate–Shafarevich vanishing through higher integral precision.

## Computational Application

The theoretical framework is applied to the rank-two elliptic curve of conductor 389:

```math
E: y^2+y=x^3+x^2-2x.
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

1. Mazur and Tate (1987).
   [Refined conjectures of the Birch and Swinnerton-Dyer type](https://doi.org/10.1215/S0012-7094-87-05431-7).

2. [Kurihara — The structure of Selmer groups of elliptic curves and modular symbols](https://arxiv.org/abs/1407.2465).

3. [Kim — The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves](https://arxiv.org/abs/2203.12159).

4. [Bullach and Honnor — On the refined Birch–Swinnerton-Dyer type conjectures of Mazur and Tate](https://arxiv.org/abs/2511.07203).

5. [Castella and Sano — On refined nonvanishing conjectures by Kurihara and Kolyvagin](https://arxiv.org/abs/2601.14504).

## Research Status

The principal results are derived under the hypotheses specified in the manuscript, using existing Euler-system and Fitting-ideal theorems together with integral augmentation and polarization techniques.

Historical originality and mathematical correctness remain subject to independent verification and peer review.

The manuscript does not claim a complete proof of the Birch–Swinnerton-Dyer conjecture.

## Keywords

Birch–Swinnerton-Dyer conjecture · Elliptic curves · Mazur–Tate elements · Selmer groups · Tate–Shafarevich groups · Fitting ideals · Euler systems · Iwasawa theory.
