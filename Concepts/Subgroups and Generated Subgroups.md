---
title: Subgroups and Generated Subgroups
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Subgroups and Generated Subgroups

> [!abstract] In one paragraph
> A subgroup is a subset that is a group with the same operation: it contains $e$ and is closed under products and inverses. Intersections of subgroups are subgroups, so every subset $X$ lies in a smallest subgroup $\langle X\rangle$, made of words in $X^{\pm1}$.

## Definitions

- $H\le G$ if $e_G\in H$, $ab\in H$ and $a^{-1}\in H$ for all $a,b\in H$. **Trivial subgroup** $I_G=\{e_G\}$. → [[Groups - Chapter 1 Examples and Definitions#Definition 1.15 — Subgroup|lecture]]
- $\langle X\rangle=\bigcap_{X\subseteq H\le G}H$; $X$ **generates** $G$ if $\langle X\rangle=G$. → [[Groups - Chapter 1 Examples and Definitions#Definition 1.17 — Generated subgroup|lecture]]

## Key results

- **Proposition 1.16.** The subgroups of $(\mathbb Z,+)$ are exactly $n\mathbb Z$, $n\ge0$. *Idea:* take the least positive element $n$ (well-ordering) and divide with remainder. → [[Groups - Chapter 1 Examples and Definitions#Proposition 1.16 — Subgroups of the integers|proof]]
- **Intersections.** Any intersection of subgroups is a subgroup.
- **Lemma 1.18.** If $X$ generates $G$, each $g\in G$ is $x_1^{\pm1}\cdots x_m^{\pm1}$ with $x_i\in X$. (Example Sheet 1, Q9.)
- **Cyclic subgroup** $\langle g\rangle=\{g^k:k\in\mathbb Z\}$. → [[Cyclic Groups and Element Orders]]

## Examples

- $\mathbb Z\le\mathbb Q\le\mathbb R\le\mathbb C$ under $+$; $C_n\le C_m$ if $n\mid m$; the three rotations in the triangle symmetries.
- $\langle\{2\}\rangle=2\mathbb Z$ in $(\mathbb Z,+)$; $\langle\varnothing\rangle=\{e\}$.

## Pitfalls

- In this course "proper subgroup" excludes both $G$ and $\{e\}$; many texts exclude only $G$.

## Related

[[Groups]] · [[Divisibility and Prime Numbers]] · [[Groups - Example Sheet 1 2025]]
