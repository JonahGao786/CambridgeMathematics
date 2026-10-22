---
title: Cross Products and Scalar Triple Products
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices]
---

# Cross Products and Scalar Triple Products

> [!abstract] In one paragraph
> $\mathbf a\times\mathbf b$ is perpendicular to $\mathbf a$ and $\mathbf b$ (right-hand rule) with length equal to the area of their parallelogram. $[\mathbf a,\mathbf b,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c)$ is the signed volume of their parallelepiped, zero exactly when they are coplanar.

## Definitions

- $\mathbf a\times\mathbf b=|\mathbf a||\mathbf b|\sin\theta\,\hat{\mathbf n}$; components $(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1)$, i.e. $(\mathbf a\times\mathbf b)_i=\varepsilon_{ijk}a_jb_k$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Cross product|lecture]]
- $[\mathbf a,\mathbf b,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c)=\det\begin{pmatrix}\mathbf a\\\mathbf b\\\mathbf c\end{pmatrix}$ (rows). → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Scalar triple product|lecture]]

## Key results

- **Properties.** Antisymmetric, $\mathbf a\times\mathbf a=\mathbf 0$, bilinear, $\mathbf a\cdot(\mathbf a\times\mathbf b)=0$; $\mathbf a\times\mathbf b=\mathbf 0\iff$ parallel or zero. → [[Vectors and Matrices - Chapter 2 Vectors#Proposition — Properties of the cross product|lecture]]
- **Area.** $|\mathbf a\times\mathbf b|$ = area of parallelogram; triangle $OAB$ has area $\frac12|\mathbf a\times\mathbf b|$.
- **Rotation.** For $\mathbf x\perp\mathbf a$, $\mathbf x\mapsto\mathbf a\times\mathbf x$ scales by $|\mathbf a|$ and turns through $\pi/2$ about $\mathbf a$.
- **Triple product.** Invariant under cyclic permutation, changes sign under a swap; $|[\mathbf a,\mathbf b,\mathbf c]|$ = volume; $=0\iff$ coplanar.
- **Vector triple product.** $\mathbf a\times(\mathbf b\times\mathbf c)=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf c$ ("BAC − CAB"). → [[Vectors and Matrices - Chapter 2 Vectors#Proof of the vector triple product identity|proof]]
- **Lagrange's identity.** $(\mathbf a\times\mathbf b)\cdot(\mathbf b\times\mathbf c)=(\mathbf a\cdot\mathbf b)(\mathbf b\cdot\mathbf c)-(\mathbf a\cdot\mathbf c)|\mathbf b|^2$. → [[Vectors and Matrices - Chapter 2 Vectors#Lagrange's identity|proof]]
- **2D signed area.** $[\mathbf a,\mathbf b]=a_1b_2-a_2b_1$, positive iff $\mathbf b$ is counterclockwise from $\mathbf a$.

## Pitfalls

- The cross product is not associative: $(\mathbf a\times\mathbf b)\times\mathbf c=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf b\cdot\mathbf c)\mathbf a$.
- Component formulas assume a **right-handed** orthonormal basis.

## Related

[[Lines, Planes and Vector Equations]] · [[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]] · [[Orthonormal Bases and Vector Coordinates]]
