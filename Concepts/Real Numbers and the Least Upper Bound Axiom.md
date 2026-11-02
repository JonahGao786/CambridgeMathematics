---
title: Real Numbers and the Least Upper Bound Axiom
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Real Numbers and the Least Upper Bound Axiom

> [!abstract] In one paragraph
> $\mathbb Q$ has "gaps": $\sqrt2\notin\mathbb Q$, and $\{x:x^2<2\}$ has upper bounds $2,1.5,1.42,\dots$ but no least one. $\mathbb R$ is the ordered field in which every non-empty set bounded above has a least upper bound.

## Definitions

- **Real numbers:** a set with $0\ne1$, operations $+,\cdot$ and an order $<$ satisfying the field axioms, the order axioms and the least upper bound axiom. → [[Numbers and Sets - Chapter 2 The Reals#Definition — The real numbers|lecture]]
- **Upper bound, least upper bound** $\sup S$: $x\ge y$ for all $y\in S$; the least such $x$. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Upper bound and least upper bound|lecture]]
- **Lower bound, greatest lower bound** $\inf S=-\sup(-S)$. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Lower bound and greatest lower bound|lecture]]
- **Irrational:** a real that is not rational. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Irrational numbers|lecture]]

## Key results

- **Proposition 1.** No rational $x$ has $x^2=2$. *Ideas:* parity of the exponent of $2$ in $a^2=2b^2$ (FTA); or $(x-1)^n$ would be an integer combination $cx+d$ yet tend to $0$ below $1/b$. → [[Numbers and Sets - Chapter 2 The Reals#Proposition 1 — No rational square root of 2|proof]]
- $\mathbb Q$ fails the least upper bound axiom; "non-empty" and "bounded above" are both needed.
- Examples: $\sup[0,1]=1$ and $\sup(0,1)=1$ (for $c<1$, $\frac{c+1}2\in(0,1)$ exceeds $c$); $\sup\{1-\frac1n\}=1$ is not attained.
- **Proposition 2 — Archimedes.** $\mathbb N$ is not bounded above. *Idea:* if $c=\sup\mathbb N$, some $n>c-1$, so $n+1>c$. → [[Numbers and Sets - Chapter 2 The Reals#Proposition 2 — Axiom of Archimedes|proof]]
- **Corollary 3.** For $t>0$ there is $n$ with $\frac1n<t$; so $\inf\{\frac1n\}=0$. → [[Numbers and Sets - Chapter 2 The Reals#Corollary 3 — Arbitrarily small 1 over n|proof]]
- **Theorem 4.** $\sqrt2$ exists in $\mathbb R$: take $c=\sup\{x:x^2<2\}$; $c^2<2$ puts some $c+t$ in the set, $c^2>2$ makes $c-t$ a smaller upper bound. Same for $\sqrt[n]x$. → [[Numbers and Sets - Chapter 2 The Reals#Theorem 4 — Existence of square root of 2|proof]]
- **Density.** Between any $a<b$ lie a rational (step along multiples of $\frac1n<b-a$) and an irrational ($\frac c{\sqrt2}$ with $c$ rational). → [[Numbers and Sets - Chapter 2 The Reals#Density of the rationals|proof]] · [[Numbers and Sets - Chapter 2 The Reals#Density of the irrationals|proof]]

## Related

[[Divisibility and Prime Numbers]] · [[Natural Numbers and Mathematical Induction]]
