---
title: Modular Arithmetic
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Modular Arithmetic

> [!abstract] In one paragraph
> Working modulo $n$ treats integers differing by a multiple of $n$ as equal. Addition and multiplication are well defined, so ordinary algebra works — except that you may only divide by **units**, the residues coprime to $n$.

## Definitions

- For $n\ge2$: $x\equiv y\pmod n\iff n\mid x-y\iff x=y+kn$ for some $k\in\mathbb Z$. The set of residues is $\mathbb Z_n=\mathbb Z/n\mathbb Z$.
- $b$ is an **inverse** of $a$ mod $n$ if $ab\equiv1\pmod n$; then $a$ is a **unit** (invertible) mod $n$, with unique inverse $a^{-1}$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Definition — Units modulo n|lecture]]

## Key results

- **Well-definedness.** $a\equiv a'$, $b\equiv b'$ $\Rightarrow$ $a+b\equiv a'+b'$, $ab\equiv a'b'$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Definition — Integers modulo n|proof]]
- **Proposition 10.** If $p$ is prime, every $a\not\equiv0\pmod p$ is a unit. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 10 — Units modulo a prime|proof]]
- **Proposition 10′.** $a$ is a unit mod $n$ iff $\operatorname{hcf}(a,n)=1$. *Idea:* Bézout. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 10' — Units modulo n|proof]]
- **Corollary 11.** If $\operatorname{hcf}(a,n)=1$, $ax\equiv b\pmod n$ has a unique solution mod $n$. If $\operatorname{hcf}(a,n)=\alpha>1$: no solution unless $\alpha\mid b$, and then the solutions are those of $\frac a\alpha x\equiv\frac b\alpha\pmod{\frac n\alpha}$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Corollary 11 — Solving linear congruences|lecture]]
- **Theorem 12 — Chinese Remainder Theorem.** For coprime $m,n$, $x\equiv a\ (m)$ and $x\equiv b\ (n)$ have a unique common solution mod $mn$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 12 — Chinese Remainder Theorem|lecture]]

## Examples

- $2a^2+3b^2=1$ has no integer solution: mod $3$, $2a^2\in\{0,2\}$.
- $7x\equiv4\ (30)$: $13\cdot7\equiv1$, so $x\equiv52\equiv22\ (30)$.
- $10x\equiv12\ (34)\iff5x\equiv6\ (17)\iff x\equiv8\ (17)$.

## Pitfalls

- Cancel only units: $4\cdot3\equiv4\cdot8\pmod{10}$ but $3\not\equiv8$.

## Related

[[Bezout's Identity and Linear Diophantine Equations]] · [[Divisibility and Prime Numbers]] · [[Groups]]
