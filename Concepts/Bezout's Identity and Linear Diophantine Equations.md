---
title: Bezout's Identity and Linear Diophantine Equations
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Bézout's Identity and Linear Diophantine Equations

> [!abstract] In one paragraph
> The gcd of $a,b$ is an integer combination $xa+yb$. Consequently $ax+by=c$ has integer solutions exactly when $\gcd(a,b)\mid c$. This is the engine behind Euclid's lemma and inverses modulo $n$.

## Key results

- **Theorem 7 — Bézout's identity.** $\forall a,b\in\mathbb N\ \exists x,y\in\mathbb Z:\ xa+yb=\gcd(a,b)$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 7 — Bezout's identity|proofs]]
  - *Proof 1:* reverse Euclid's algorithm — also **computes** $x,y$.
  - *Proof 2:* the least positive combination $h=xa+yb$ divides $a$ and $b$ — existence only.
- **Corollary 8 — Bézout's theorem.** $ax+by=c$ has an integer solution iff $\gcd(a,b)\mid c$. *Idea:* multiply $h=ax+by$ by $c/h$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Corollary 8 — Bezout's theorem|proof]]

## Examples

- Reversing Euclid for $\gcd(87,52)=1$: $1=35-2\cdot17=-2\cdot52+3\cdot35=-5\cdot52+3\cdot87$.
- $87x+52y=33$: take $x=33\cdot3$, $y=33\cdot(-5)$.
- $160x+72y=33$: no solution (left side even, right side odd).

## Uses

- Euclid's lemma. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 4 — Euclid's lemma|Proposition 4]]
- $a$ is a unit mod $n$ iff $\gcd(a,n)=1$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 10' — Units modulo n|Proposition 10′]]

## Related

[[Greatest Common Divisors and Euclid's Algorithm]] · [[Modular Arithmetic]]
