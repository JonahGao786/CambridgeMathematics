---
title: Möbius Transformations
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Möbius Transformations

> [!abstract] In one paragraph
> A Möbius transformation is $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc\ne0$, acting on the Riemann sphere $\hat{\mathbb C}=\mathbb C\cup\{\infty\}$. Composing two of them multiplies their coefficient matrices, so they form a group, the Möbius group $\mathcal M\le\operatorname{Sym}(\hat{\mathbb C})$.

## Definitions

- **Riemann sphere** $\hat{\mathbb C}=\mathbb C\cup\{\infty\}$; stereographic projection from the north pole matches $S^2\setminus\{N\}$ with $\mathbb C$ and $N$ with $\infty$. → [[Groups - Chapter 4 The Möbius Group#Definition 4.1 — Riemann sphere|lecture]]
- **Möbius transformation** $\mu(z)=\frac{az+b}{cz+d}$, $ad-bc\ne0$, with $\mu(-\frac dc)=\infty$ and $\mu(\infty)=\frac ac$ when $c\ne0$, and $\mu(\infty)=\infty$ when $c=0$. → [[Groups - Chapter 4 The Möbius Group#Definition 4.2 — Möbius transformation|lecture]]

## Key results

- **Composition = matrix product.** The coefficients of $\mu_1\circ\mu_2$ are the entries of $\begin{pmatrix}a_1&b_1\\c_1&d_1\end{pmatrix}\begin{pmatrix}a_2&b_2\\c_2&d_2\end{pmatrix}$. → [[Groups - Chapter 4 The Möbius Group#Composition of Möbius transformations|lecture]]
- **Theorem 4.3.** Möbius transformations form a subgroup of $\operatorname{Sym}(\hat{\mathbb C})$. *Idea:* the inverse of $\frac{az+b}{cz+d}$ is $\frac{dz-b}{-cz+a}$; closure because $\det$ is multiplicative. → [[Groups - Chapter 4 The Möbius Group#Theorem 4.3 — The Möbius group|proof]]

## Related

[[Groups]] · [[Subgroups and Generated Subgroups]] · [[Bijections and Permutations]] · [[Complex Numbers]] · [[Linear Maps and Matrices]]
