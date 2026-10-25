---
title: Vectors and Linear Span
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices]
---

# Vectors and Linear Span

> [!abstract] In one paragraph
> Vectors can be added (parallelogram rule) and scaled. The span of some vectors is everything you can build from them by linear combinations; it is always a subspace. Vectors are linearly independent when no non-trivial combination gives $\mathbf 0$. A basis is an independent spanning set; the number of vectors in it is the dimension.

## Definitions

- **Vector space** over $\mathbb F=\mathbb R$ or $\mathbb C$: a set with addition and scalar multiplication satisfying the usual axioms; e.g. $\mathbb R^n$, $\mathbb C^n$, smooth functions on $[0,1]$ vanishing at $0$ and $1$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Vector space over a field|lecture]]
- **Span** $\operatorname{span}\{\mathbf v_1,\dots,\mathbf v_r\}=\{\sum\lambda_i\mathbf v_i:\lambda_i\in\mathbb F\}$.
- **Subspace**: non-empty $U\subseteq V$ with $\lambda\mathbf u+\mu\mathbf w\in U$ for all $\mathbf u,\mathbf w\in U$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Subspace|lecture]]
- **Parallel**: $\mathbf a=\lambda\mathbf b$ or $\mathbf b=\lambda\mathbf a$.
- **Linearly independent**: $\sum\lambda_i\mathbf v_i=\mathbf 0\Rightarrow$ all $\lambda_i=0$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Linear independence|lecture]]

## Key facts

- Vectors under addition form an abelian group. → [[Vectors and Matrices - Chapter 2 Vectors#Vector addition|lecture]]
- For $\mathbf a\ne\mathbf 0$, $\operatorname{span}\{\mathbf a\}$ is the line through $O$ along $\mathbf a$; for non-parallel non-zero $\mathbf a,\mathbf b$, $\operatorname{span}\{\mathbf a,\mathbf b\}$ is the plane through $O$ containing them.
- Every span is a subspace; a line or plane missing the origin is not.
- Dependent $\iff$ some $\mathbf v_j$ is a combination of the others. Any set containing $\mathbf 0$ is dependent.
- **Independence and the triple product.** In $\mathbb R^3$, $\mathbf a\cdot(\mathbf b\times\mathbf c)\ne0$ iff $\mathbf a,\mathbf b,\mathbf c$ are independent. *Idea:* dot a vanishing combination with $\mathbf b\times\mathbf c$, $\mathbf c\times\mathbf a$, $\mathbf a\times\mathbf b$. → [[Vectors and Matrices - Chapter 2 Vectors#Proposition — Independence and the scalar triple product|proof]]
- **Basis and coordinates.** A basis spans and is independent, so each vector has unique coordinates; e.g. $\{\mathbf e_i\}$ or $\{(1,1),(1,-1)\}$ in $\mathbb R^2$. → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Basis|lecture]]
- **Dimension.** All bases of $V$ have the same size $\dim V$; $\dim_{\mathbb R}\mathbb R^n=\dim_{\mathbb C}\mathbb C^n=n$, but $\dim_{\mathbb R}\mathbb C^n=2n$. A spanning set has at least $\dim V$ vectors, an independent set at most $\dim V$, and either can be cut down or extended to a basis; so $\dim U\le\dim V$ for a subspace $U$. *Intuition:* the number of coordinates you can choose freely (a plane $2x+y+z=0$ in $\mathbb R^3$ has $3$ components but only $2$ free, so dimension $2$). → [[Vectors and Matrices - Chapter 2 Vectors#Definition — Dimension|lecture]] · [[Vectors and Matrices - Chapter 2 Vectors#Proposition — Spanning and independent sets in dimension n|proposition]]

## Pitfalls

- Dependence means *some* vector is a combination of the others, not *every* one: $\{(1,0),(0,1),(0,2)\}$ is dependent but $(1,0)$ is not a combination of the other two.

## Related

[[Real Inner Products and Cauchy-Schwarz]] · [[Orthonormal Bases and Vector Coordinates]] · [[Lines, Planes and Vector Equations]]
