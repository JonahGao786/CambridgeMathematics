---
title: Real Inner Products and Cauchy-Schwarz
material_type: source-backed definitions, theorems and proofs
course: Part IA Vectors and Matrices
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: [4, 5, 6, 7, 8]
---

# Real Inner Products and Cauchy-Schwarz

An inner product on a real vector space $V$ is a map $\langle\cdot,\cdot\rangle:V\times V\to\mathbb R$ that is symmetric, linear in its second argument, and positive definite:
$$\langle\mathbf x,\mathbf y\rangle=\langle\mathbf y,\mathbf x\rangle,$$
$$\langle\mathbf x,\alpha\mathbf y+\beta\mathbf z\rangle
=\alpha\langle\mathbf x,\mathbf y\rangle+\beta\langle\mathbf x,\mathbf z\rangle,$$
$$\langle\mathbf x,\mathbf x\rangle\ge0,\qquad
\langle\mathbf x,\mathbf x\rangle=0\Longleftrightarrow\mathbf x=\mathbf0.$$
These hold for all vectors in $V$ and all real $\alpha,\beta$. Symmetry gives linearity in the first argument as well. The induced norm is
$$\|\mathbf x\|=\sqrt{\langle\mathbf x,\mathbf x\rangle}.$$

For non-zero Euclidean vectors, $\mathbf a\cdot\mathbf b=|\mathbf a|\,|\mathbf b|\cos\theta$. Orthogonality means $\mathbf a\cdot\mathbf b=0$, including when either vector is zero.

For $\mathbf a\ne\mathbf0$, the orthogonal projection onto its line is
$$\operatorname{proj}_{\mathbf a}\mathbf b
=\frac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\mathbf a
=(\widehat{\mathbf a}\cdot\mathbf b)\widehat{\mathbf a}.$$
The difference between $\mathbf b$ and this projection is orthogonal to $\mathbf a$.

**Cauchy–Schwarz:**
$$|\langle\mathbf x,\mathbf y\rangle|\le\|\mathbf x\|\,\|\mathbf y\|.$$
The source proves the Euclidean version using the non-negativity of
$$|\mathbf x-\lambda\mathbf y|^2
=|\mathbf y|^2\lambda^2-2(\mathbf x\cdot\mathbf y)\lambda+|\mathbf x|^2$$
for every real $\lambda$. With $\mathbf y\ne0$, its discriminant is non-positive, giving the squared inequality; the zero case is immediate. The source also states the extension to every real inner product.

Equality holds iff one vector is a real scalar multiple of the other, including the zero cases; no separate proof of this characterization is supplied.

The Euclidean **triangle inequality** follows by expanding the squared norm and applying Cauchy–Schwarz:
$$\begin{aligned}
|\mathbf x+\mathbf y|^2
&=|\mathbf x|^2+|\mathbf y|^2+2\mathbf x\cdot\mathbf y\\
&\le(|\mathbf x|+|\mathbf y|)^2.
\end{aligned}$$
Taking non-negative square roots gives $|\mathbf x+\mathbf y|\le|\mathbf x|+|\mathbf y|$.

Source: [[Vectors and Matrices - Chapter 2 Vectors]], pages 4–8, which also retains the dot-product projection and cosine-rule diagrams. Related: [[Vectors and Linear Span]] and [[Triangle Inequality for Complex Numbers]].
