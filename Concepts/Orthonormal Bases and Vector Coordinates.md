---
title: Orthonormal Bases and Vector Coordinates
material_type: source-backed definitions and coordinate calculations
course: Part IA Vectors and Matrices
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: [9, 10, 19, 21]
---

# Orthonormal Bases and Vector Coordinates

In $\mathbb R^3$, an orthonormal basis $\mathbf e_1,\mathbf e_2,\mathbf e_3$ satisfies
$$\mathbf e_i\cdot\mathbf e_j=\delta_{ij}
=\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}$$
Each vector has length $1$, and distinct basis vectors are perpendicular. Choosing these directions corresponds to choosing Cartesian axes.

Every vector has a unique expansion
$$\mathbf a=a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3,
\qquad a_i=\mathbf e_i\cdot\mathbf a.$$
Its coordinates may be written as $(a_1,a_2,a_3)$ or as a column $\begin{pmatrix}a_1&a_2&a_3\end{pmatrix}^{\mathsf T}$.

For $\mathbf b=b_1\mathbf e_1+b_2\mathbf e_2+b_3\mathbf e_3$, bilinearity and orthonormality give
$$\begin{aligned}
\mathbf a\cdot\mathbf b
&=\sum_{i=1}^3\sum_{j=1}^3a_ib_j(\mathbf e_i\cdot\mathbf e_j)\\
&=a_1b_1+a_2b_2+a_3b_3.
\end{aligned}$$
The six mixed terms vanish. In particular,
$$|\mathbf a|^2=a_1^2+a_2^2+a_3^2.$$

The standard basis is
$$\mathbf e_1=(1,0,0),\qquad\mathbf e_2=(0,1,0),\qquad\mathbf e_3=(0,0,1),$$
also denoted $\widehat{\mathbf i},\widehat{\mathbf j},\widehat{\mathbf k}$.

## Index notation

In the lecture's Cartesian summation convention, an index appearing twice in a term is summed over $1,2,3$. Thus
$$\mathbf a=a_i\mathbf e_i,\qquad
\mathbf a\cdot\mathbf b=\delta_{ij}a_ib_j=a_ib_i.$$
The delta selects a matching component:
$$\delta_{ij}a_j=a_i.$$
Here $i$ is free and $j$ is summed. A single entry $\delta_{11}=1$ differs from the summed trace $\delta_{ii}=3$.

[[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]] gives explicit sums, numerical examples, free/dummy-index rules and the connection to cross products.

Source: [[Vectors and Matrices - Chapter 2 Vectors]], pages 9–10, 19 and 21. Related: [[Vectors and Linear Span]], [[Real Inner Products and Cauchy-Schwarz]] and [[Cross Products and Scalar Triple Products]].
