---
title: Real Inner Products and Cauchy-Schwarz
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices]
---

# Real Inner Products and Cauchy–Schwarz

> [!abstract] In one paragraph
> The dot product $\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta$ measures lengths, angles and projections. Abstracting its properties gives an inner product. Cauchy–Schwarz, $|\mathbf x\cdot\mathbf y|\le|\mathbf x||\mathbf y|$, is what makes "$\cos\theta$" lie in $[-1,1]$ and gives the triangle inequality. On complex spaces the inner product conjugates its first argument, and the same inequalities hold.

## Definitions

- **Dot product** $\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta$; in an orthonormal basis $=a_1b_1+a_2b_2+a_3b_3$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Dot product|lecture]]
- **Orthogonal**: $\mathbf a\cdot\mathbf b=0$. **Projection** of $\mathbf b$ onto $\mathbf a$: $(\hat{\mathbf a}\cdot\mathbf b)\hat{\mathbf a}=\frac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\mathbf a$; the remainder is orthogonal to $\mathbf a$.
- **Inner product** on a real vector space: symmetric, linear in the second argument, positive definite; norm $\|\mathbf x\|=\sqrt{\langle\mathbf x,\mathbf x\rangle}$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Inner product|lecture]]
- **Complex inner product** on $\mathbb C^n$: $\langle\mathbf z,\mathbf w\rangle=\sum\bar z_jw_j$. Axioms: Hermitian symmetry, linear in the second argument (so antilinear in the first), positive definite. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Inner product over a complex vector space|lecture]]

## Key results

- **Cosine rule.** $|\overrightarrow{BC}|^2=|\overrightarrow{AB}|^2+|\overrightarrow{AC}|^2-2|\overrightarrow{AB}||\overrightarrow{AC}|\cos\theta$. → [[Vectors and Matrices - Chapter 2 Vectors#Cosine rule|proof]]
- **Cauchy–Schwarz.** $|\mathbf x\cdot\mathbf y|\le|\mathbf x||\mathbf y|$ (any inner product: $|\langle\mathbf x,\mathbf y\rangle|\le\|\mathbf x\|\|\mathbf y\|$), equality iff one is a multiple of the other. *Idea:* $|\mathbf x-\lambda\mathbf y|^2\ge0$ is a quadratic in $\lambda$ with discriminant $\le0$. → [[Vectors and Matrices - Chapter 2 Vectors#Theorem — Cauchy-Schwarz inequality|proof]]
- **Triangle inequality.** $|\mathbf x+\mathbf y|\le|\mathbf x|+|\mathbf y|$. *Idea:* expand $|\mathbf x+\mathbf y|^2$ and apply Cauchy–Schwarz. → [[Vectors and Matrices - Chapter 2 Vectors#Theorem — Triangle inequality|proof]]
- **Over any inner product (real or complex).** $|\langle\mathbf v,\mathbf w\rangle|\le\|\mathbf v\|\|\mathbf w\|$ and $\|\mathbf v+\mathbf w\|\le\|\mathbf v\|+\|\mathbf w\|$. *Idea:* take $\lambda=\langle\mathbf w,\mathbf v\rangle/\|\mathbf w\|^2$ in $\|\mathbf v-\lambda\mathbf w\|^2\ge0$. → [[Vectors and Matrices - Chapter 2 Vectors#Theorem — Cauchy-Schwarz and triangle inequalities for inner products|proof]]

## Pitfalls

- Over $\mathbb C$ use $\sum\bar z_jw_j$, not $\sum z_jw_j$: the latter is not positive (for $z=i$ it gives $-1$).

## Related

[[Orthonormal Bases and Vector Coordinates]] · [[Triangle Inequality for Complex Numbers]] · [[Vectors and Linear Span]]
