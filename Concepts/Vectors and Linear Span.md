---
title: Vectors and Linear Span
material_type: concept note
course: Part IA Vectors and Matrices
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: [1, 2, 3, 4]
---

# Vectors and Linear Span

For a non-zero vector $\mathbf v$, its unit vector is $\widehat{\mathbf v}=\mathbf v/|\mathbf v|$.

Geometric vector addition follows the parallelogram rule. It is commutative and associative, has identity $\mathbf0$, and has inverse $-\mathbf a$ for $\mathbf a$. Vectors under addition form an abelian [[Groups|group]].

For real scalars,
$$|\lambda\mathbf a|=|\lambda|\,|\mathbf a|,$$
$$\lambda(\mathbf a+\mathbf b)=\lambda\mathbf a+\lambda\mathbf b,\qquad
(\lambda+\mu)\mathbf a=\lambda\mathbf a+\mu\mathbf a,$$
$$\lambda(\mu\mathbf a)=(\lambda\mu)\mathbf a,\qquad1\mathbf a=\mathbf a.$$

A **linear combination** of $\mathbf a,\mathbf b$ is $\alpha\mathbf a+\beta\mathbf b$. Their **span** is
$$\operatorname{span}\{\mathbf a,\mathbf b\}
=\{\alpha\mathbf a+\beta\mathbf b:\alpha,\beta\in\mathbb R\}.$$
The definition extends to any number of vectors.

Vectors are parallel if one is a real scalar multiple of the other. A non-zero vector spans a line through the origin; two non-zero, non-parallel geometric vectors span the plane through their endpoints and the origin.

$\mathbb R^n$ with componentwise operations is a vector space. A line such as $x+y=1$ that misses the origin is not a vector space under those operations.

See [[Vectors and Matrices - Chapter 2 Vectors]], pages 1–4. [[Real Inner Products and Cauchy-Schwarz]] introduces orthogonality, length and projection.

[[Orthonormal Bases and Vector Coordinates]] gives coordinate descriptions in $\mathbb R^3$. [[Cross Products and Scalar Triple Products]] treats oriented area, rotation and volume there.

[[Lines, Planes and Vector Equations]] applies these directions and spans to affine lines, planes, intersections and distances.

## From span to a basis

For finitely many vectors $\mathbf v_1,\ldots,\mathbf v_m$ in a real vector space, their span contains all sums $\sum_{i=1}^m a_i\mathbf v_i$ with $a_i\in\mathbb R$. For an infinite set, span still uses only **finite** sums. It contains zero and is closed under addition and real scalar multiplication, so it is a vector subspace.

The vectors are **linearly independent** if
$$\sum_{i=1}^m a_i\mathbf v_i=\mathbf0\quad\Longrightarrow\quad a_1=\cdots=a_m=0.$$
A **basis** is a linearly independent spanning set. Spanning gives existence of coordinates; independence gives uniqueness by subtracting two proposed expansions. This is the missing step between a span and the coordinate formulas in [[Orthonormal Bases and Vector Coordinates]]. An additive subgroup need not be a real vector subspace: $\mathbb Z\le(\mathbb R,+)$, but $\tfrac12\cdot1\notin\mathbb Z$.
