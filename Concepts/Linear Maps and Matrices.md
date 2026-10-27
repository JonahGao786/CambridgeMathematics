---
title: Linear Maps and Matrices
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices]
---

# Linear Maps and Matrices

> [!abstract] In one paragraph
> A linear map $T:V\to W$ respects linear combinations. Its kernel and image are subspaces, and rank plus nullity equals $\dim V$. Once bases are chosen, $T$ is the same thing as a matrix: column $j$ lists the coordinates of $T(\mathbf e_j)$.

## Definitions

- **Linear map:** $T(\lambda\mathbf x+\mu\mathbf y)=\lambda T\mathbf x+\mu T\mathbf y$. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Linear map|lecture]]
- **Image, kernel, rank, nullity:** $\operatorname{Im}T$, $\ker T$, $\operatorname{rank}T=\dim\operatorname{Im}T$, $\operatorname{null}T=\dim\ker T$. Injective $\iff\ker T=\{\mathbf 0\}$; surjective $\iff\operatorname{Im}T=W$. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Image, kernel, rank and nullity|lecture]]
- **Matrix of $T$** in bases $B$, $C$: $T(\mathbf e_j)=\sum_iM_{ij}\mathbf f_i$. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Matrix of a linear map|lecture]]

## Key results

- **Rank–nullity.** $\operatorname{rank}T+\operatorname{null}T=\dim V$. *Idea:* extend a basis of $\ker T$ to a basis of $V$; the images of the new vectors form a basis of $\operatorname{Im}T$. → [[Vectors and Matrices - Chapter 3 Matrices#Theorem — Rank-nullity theorem|proof]]
- **Matrix action.** $[T\mathbf x]_C=M[\mathbf x]_B$. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Matrix of a linear map|proof]]
- Sums and compositions of linear maps are linear; $\dim\mathcal L(V,W)=\dim V\dim W$. → [[Vectors and Matrices - Chapter 3 Matrices#Linear combinations and composition|lecture]]

## Related

[[Vectors and Linear Span]] · [[Real Inner Products and Cauchy-Schwarz]] · [[Orthonormal Bases and Vector Coordinates]]
