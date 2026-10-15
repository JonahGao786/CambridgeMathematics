---
title: Vectors and Linear Span
material_type: source-backed definitions and operation properties
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

Source: [[Vectors and Matrices - Chapter 2 Vectors]], pages 1–4, including the actual geometric sketches in TikZ. [[Real Inner Products and Cauchy-Schwarz]] introduces orthogonality, length and projection.

[[Orthonormal Bases and Vector Coordinates]] gives coordinate descriptions in $\mathbb R^3$. [[Cross Products and Scalar Triple Products]] treats oriented area, rotation and volume there.
