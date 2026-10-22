---
title: Natural Numbers and Mathematical Induction
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Natural Numbers and Mathematical Induction

> [!abstract] In one paragraph
> $\mathbb N=\{1,2,3,\dots\}$ is pinned down by the Peano axioms: $1$ is not a successor, the successor map is injective, and induction holds. Induction comes in three equivalent forms — weak induction, strong induction, and well-ordering (every non-empty subset of $\mathbb N$ has a least element).

## Definitions

- **Peano axioms.** (i) $n+1\ne1$; (ii) $m\ne n\Rightarrow m+1\ne n+1$; (iii) if $P(1)$ and $\forall n\,(P(n)\Rightarrow P(n+1))$ then $\forall n\,P(n)$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Definition — Peano axioms|lecture]]
- **Weak induction (WPI)** is axiom (iii).
- **Strong induction (SPI).** If $P(1)$ and $\forall n\ \big(P(m)\ \forall m\le n\big)\Rightarrow P(n+1)$, then $\forall n\,P(n)$.
- **Well-ordering (WOP).** If $P(n)$ holds for some $n$, there is a least such $n$.
- **Order.** $a<b$ iff $a+c=b$ for some $c\in\mathbb N$.

## Key results

- **WPI $\iff$ SPI.** *Idea:* for WPI $\Rightarrow$ SPI apply WPI to $Q(n)=$ "$P(m)$ for all $m\le n$". → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Definition — Strong induction and well-ordering|lecture]]
- **Theorem 1 — SPI $\Rightarrow$ WOP.** *Idea:* if there is no least $n$ with $P(n)$, strong induction proves $\neg P(n)$ for every $n$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 1 — Strong induction implies well-ordering|proof]]

## Writing an induction proof

1. Prove the base case $P(1)$.
2. Fix an arbitrary $n$, assume $P(n)$ (or $P(1),\dots,P(n)$ for strong induction), prove $P(n+1)$.
3. Conclude $\forall n\in\mathbb N,\ P(n)$.

**Least counterexample.** If $\forall n\,P(n)$ were false, WOP gives a least counterexample; derive a contradiction from it.

## Examples

- Existence of prime factorizations uses strong induction. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 2 — Existence of prime factorization|Proposition 2]]
- Proof 2 of Bézout picks the least positive linear combination by WOP. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 7 — Bezout's identity|Theorem 7]]

## Related

[[Divisibility and Prime Numbers]] · [[Proof by Contradiction and Contraposition]]
