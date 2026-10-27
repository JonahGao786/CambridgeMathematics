---
title: Cosets and Lagrange's Theorem
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Cosets and Lagrange's Theorem

> [!abstract] In one paragraph
> The left cosets $gH$ of a subgroup $H\le G$ cut $G$ into disjoint pieces, each the same size as $H$. Counting pieces gives $|G|=|G:H|\cdot|H|$, so the order of a subgroup — and of every element — divides $|G|$ when $G$ is finite.

## Definitions

- **Left coset** $gH=\{gh:h\in H\}$; $G/H$ = the set of left cosets. Right coset $Hg$; $H\backslash G$. → [[Groups - Chapter 2 Lagrange's Theorem#Definition 2.2 — Left coset|lecture]]
- **Index** $|G:H|=|G/H|$. → [[Groups - Chapter 2 Lagrange's Theorem#Definition 2.5 — Index|lecture]]

## Key results

- **Lemma 2.3.** Left cosets partition $G$. *Idea:* $g\in gH$; if $g_1h_1=g_2h_2$ then $g_1=g_2h_2h_1^{-1}$, so $g_1H\subseteq g_2H$. → [[Groups - Chapter 2 Lagrange's Theorem#Lemma 2.3 — Cosets partition the group|proof]]
- **Lemma 2.4.** $h\mapsto gh$ is a bijection $H\to gH$. → [[Groups - Chapter 2 Lagrange's Theorem#Lemma 2.4 — Cosets have the size of H|proof]]
- **Theorem 2.6 (Lagrange).** $|G|=|G:H|\cdot|H|$ for finite $G$; in particular $|H|$ divides $|G|$. → [[Groups - Chapter 2 Lagrange's Theorem#Theorem 2.6 — Lagrange (version 2)|proof]]
- **Corollary 2.7.** $\operatorname{ord}(g)\mid|G|$, since $\operatorname{ord}(g)=|\langle g\rangle|$.
- **Corollary 2.8.** $g^{|G|}=e$ (write $|G|=\operatorname{ord}(g)k$). → [[Groups - Chapter 2 Lagrange's Theorem#Corollary 2.8 — g to the order of G is e|proof]]
- **Corollary 2.9.** If $|G|$ is prime, $G$ is cyclic and every $g\ne e$ generates it. *Idea:* $\operatorname{ord}(g)\mid|G|$ forces $\operatorname{ord}(g)=|G|$. → [[Groups - Chapter 2 Lagrange's Theorem#Corollary 2.9 — Groups of prime order|proof]]
- **Theorem 2.11 (Fermat–Euler).** $\mathbb Z_n^\times=\{x:\gcd(x,n)=1\}$ is a group under multiplication of order $\varphi(n)$, so $x^{\varphi(n)}\equiv1\pmod n$ by Corollary 2.8. → [[Groups - Chapter 2 Lagrange's Theorem#Theorem 2.11 — Fermat–Euler|proof]]

## Pitfalls

- $gH$ is a **subset** of $G$, not an element; $g_1H=g_2H$ can hold with $g_1\ne g_2$.
- Lagrange needs $|G|<\infty$ (the index may be $\infty$ otherwise).

## Related

[[Subgroups and Generated Subgroups]] · [[Cyclic Groups and Element Orders]] · [[Groups]]
