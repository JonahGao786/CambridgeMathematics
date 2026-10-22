---
title: Orthonormal Bases and Vector Coordinates
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices]
---

# Orthonormal Bases and Vector Coordinates

> [!abstract] In one paragraph
> Three mutually perpendicular unit vectors $\mathbf e_1,\mathbf e_2,\mathbf e_3$ act as Cartesian axes. Every vector has unique coordinates $a_i=\mathbf e_i\cdot\mathbf a$, and dot products become $a_1b_1+a_2b_2+a_3b_3$.

## Definition

$\{\mathbf e_1,\mathbf e_2,\mathbf e_3\}$ is **orthonormal** if $\mathbf e_i\cdot\mathbf e_j=\delta_{ij}$. It is a **basis** of $\mathbb R^3$. **Right-handed** additionally means $\mathbf e_1\times\mathbf e_2=\mathbf e_3$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Orthonormal basis|lecture]]

## Key facts

- $\mathbf a=a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3$ with $a_i=\mathbf e_i\cdot\mathbf a$ (dot both sides with $\mathbf e_i$).
- $\mathbf a\cdot\mathbf b=a_1b_1+a_2b_2+a_3b_3$ (the six mixed terms vanish); $|\mathbf a|^2=a_1^2+a_2^2+a_3^2$.
- Standard basis $(1,0,0),(0,1,0),(0,0,1)$, also written $\hat\imath,\hat\jmath,\hat k$.
- In components the cross product is a formal determinant. → [[Cross Products and Scalar Triple Products]]

## Related

[[Real Inner Products and Cauchy-Schwarz]] · [[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]]
