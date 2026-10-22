---
title: Divisibility and Prime Numbers
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Divisibility and Prime Numbers

> [!abstract] In one paragraph
> Every $n\ge2$ factors into primes (strong induction), there are infinitely many primes, and the factorization is unique. Uniqueness needs Euclid's lemma, which in turn rests on Bézout's identity.
> Logical chain: division algorithm → Euclid's algorithm → Bézout → Euclid's lemma → unique factorization.

## Definitions

- $a\mid b$ iff $b=ac$ for some $c\in\mathbb Z$. Factors other than $\pm1,\pm b$ are **proper** (non-trivial).
- $n\ge2$ is **prime** if its only factors are $\pm1,\pm n$; otherwise **composite**.

## Key results

- **Proposition 2 — Existence.** Every $n\ge2$ is a product of primes. *Idea:* strong induction; if $n=ab$ with $1<a,b<n$, factor $a$ and $b$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 2 — Existence of prime factorization|proof]]
- **Theorem 3 — Infinitely many primes.** *Idea:* no $p_i$ divides $p_1\cdots p_k+1$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 3 — Infinitely many primes|proof]] (Erdős's counting proof: [[Numbers and Sets - Chapter 1 Elementary Number Theory#Applications of Theorem 9|application (4)]])
- **Proposition 4 — Euclid's lemma.** $p$ prime, $p\mid ab\Rightarrow p\mid a$ or $p\mid b$; similarly for $p\mid a_1\cdots a_n$. *Idea:* if $p\nmid a$, write $xp+ya=1$ and multiply by $b$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 4 — Euclid's lemma|proof]]
- **Theorem 9 — Fundamental theorem of arithmetic.** Factorization into primes is unique up to order. *Idea:* $p_1$ divides some $q_i$, so $p_1=q_i$; cancel and induct. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 9 — Fundamental theorem of arithmetic|proof]]

## Consequences of unique factorization

For $n=p_1^{a_1}\cdots p_k^{a_k}$ the factors are exactly $p_1^{b_1}\cdots p_k^{b_k}$ with $0\le b_i\le a_i$. gcd and lcm take the minimum and maximum exponents: see [[Greatest Common Divisors and Euclid's Algorithm]].

## Pitfalls

- Euclid's lemma needs $p$ prime: $6\mid2\cdot3$ but $6\nmid2$, $6\nmid3$.
- Unique factorization can fail in other number systems: $4=2\cdot2=(1+\sqrt{-3})(1-\sqrt{-3})$ in $\mathbb Z[\sqrt{-3}]$.
- In this course "proper factor" excludes both $\pm1$ and $\pm n$.

## Related

[[Natural Numbers and Mathematical Induction]] · [[Bezout's Identity and Linear Diophantine Equations]] · [[Modular Arithmetic]]
