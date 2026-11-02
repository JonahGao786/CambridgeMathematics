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

## Matrix algebra

- **Product** $(MN)_{ij}=\sum_kM_{ik}N_{kj}$ (row $i$ of $M$ dotted with column $j$ of $N$); $T\circ S$ has matrix $MN$. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Matrix product|lecture]]
- **Inverses.** $NM=I$ (left), $ML=I$ (right); for square $M$ they agree: $N=N(ML)=(NM)L=L$. $(MN)^{-1}=N^{-1}M^{-1}$. Invertible matrices represent isomorphisms. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Left, right and two-sided inverses|lecture]]
- **Transpose and adjoint.** $(M^{\mathsf T})_{ij}=M_{ji}$, $M^\dagger=\overline M^{\mathsf T}$; both reverse products. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Transpose|lecture]] · [[Vectors and Matrices - Chapter 3 Matrices#Definition — Complex conjugate and adjoint|lecture]]
- **Decompositions.** Real: symmetric + antisymmetric, $\frac12(M\pm M^{\mathsf T})$. Complex: Hermitian + anti-Hermitian, $\frac12(M\pm M^\dagger)$. → [[Vectors and Matrices - Chapter 3 Matrices#Definition — Symmetric and antisymmetric matrices|lecture]] · [[Vectors and Matrices - Chapter 3 Matrices#Definition — Hermitian and anti-Hermitian matrices|lecture]]

## Geometric examples

- Rotation in the plane $R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$, with $R(\theta_1)R(\theta_2)=R(\theta_1+\theta_2)$. → [[Vectors and Matrices - Chapter 3 Matrices#Rotations in the plane|lecture]]
- Reflection in the line at angle $\theta$: $H(\theta)=\begin{pmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{pmatrix}$; $H(\theta_1)H(\theta_2)=R(2(\theta_1-\theta_2))$. → [[Vectors and Matrices - Chapter 3 Matrices#Reflections in the plane|lecture]]
- Rodrigues' formula: $R(\theta,\mathbf n)\mathbf x=\cos\theta\,\mathbf x+(1-\cos\theta)(\mathbf n\cdot\mathbf x)\mathbf n+\sin\theta\,\mathbf n\times\mathbf x$ (split $\mathbf x$ into parts along and perpendicular to $\mathbf n$). → [[Vectors and Matrices - Chapter 3 Matrices#Rotations in space and Rodrigues' formula|derivation]]
- Reflection in a plane with unit normal $\mathbf n$: $I-2\mathbf n\mathbf n^{\mathsf T}$; dilations and shears. Inverses: $R(\theta)^{-1}=R(-\theta)$, $S(\lambda)^{-1}=S(-\lambda)$, $H^{-1}=H$. → [[Vectors and Matrices - Chapter 3 Matrices#Reflections, dilations and shears in space|lecture]]

## Related

[[Vectors and Linear Span]] · [[Real Inner Products and Cauchy-Schwarz]] · [[Orthonormal Bases and Vector Coordinates]]
