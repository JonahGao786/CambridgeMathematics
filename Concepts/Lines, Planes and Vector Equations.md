---
title: Lines, Planes and Vector Equations
material_type: source-backed equations, geometric interpretations and proofs
course: Part IA Vectors and Matrices
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: [14, 15, 16, 17, 18, 19]
---

# Lines, Planes and Vector Equations

All vectors here lie in $\mathbb R^3$. For a point with position vector $\mathbf a$ and non-zero direction $\mathbf u$, a line is
$$\mathbf r=\mathbf a+\lambda\mathbf u,\qquad\lambda\in\mathbb R,$$
equivalently $\mathbf u\times(\mathbf r-\mathbf a)=\mathbf0$.

A plane with non-parallel directions $\mathbf u,\mathbf v$ has equations
$$\mathbf r=\mathbf a+\lambda\mathbf u+\mu\mathbf v,
\qquad\lambda,\mu\in\mathbb R,$$
$$(\mathbf r-\mathbf a)\cdot\mathbf n=0,
\qquad\mathbf n=\mathbf u\times\mathbf v\ne\mathbf0.$$
Writing $\mathbf n\cdot\mathbf r=k$, with $k=\mathbf n\cdot\mathbf a$, its distance from the origin is $|k|/|\mathbf n|$.

For three non-collinear points with position vectors $\mathbf a,\mathbf b,\mathbf c$, the plane through them is
$$(\mathbf r-\mathbf a)\cdot[(\mathbf b-\mathbf a)\times(\mathbf c-\mathbf a)]=0.$$

## Line–plane intersection

For a line through $\mathbf a$ with direction $\mathbf u$, and plane $\mathbf n\cdot\mathbf r=\mathbf n\cdot\mathbf b$:

- If $\mathbf u\cdot\mathbf n\ne0$, the unique intersection is
  $$\mathbf r=\frac{(\mathbf n\cdot\mathbf b)\mathbf u-(\mathbf a\times\mathbf u)\times\mathbf n}{\mathbf u\cdot\mathbf n}.$$
- If $\mathbf u\cdot\mathbf n=0$ and $\mathbf n\cdot\mathbf a=\mathbf n\cdot\mathbf b$, the line is contained in the plane.
- Otherwise there is no intersection.

The source derives the first formula using the [[Cross Products and Scalar Triple Products|vector triple-product identity]].

## Distance between non-parallel lines

For $\mathbf r=\mathbf a_1+\lambda\mathbf u_1$ and $\mathbf r=\mathbf a_2+\mu\mathbf u_2$, with $\mathbf u_1\times\mathbf u_2\ne\mathbf0$,
$$s=\left|(\mathbf a_1-\mathbf a_2)\cdot
\frac{\mathbf u_1\times\mathbf u_2}{|\mathbf u_1\times\mathbf u_2|}\right|.$$
The projection of every connecting vector onto the common unit normal is fixed, so Cauchy–Schwarz bounds its length below by $s$. Writing $\mathbf a_1-\mathbf a_2$ as a combination of $\mathbf u_1,\mathbf u_2$ and the normal lets one cancel the two directional components, attaining the bound. The source does not cover parallel lines.

## A vector equation with three solution cases

For
$$\mathbf r+\mathbf a\times(\mathbf b\times\mathbf r)=\mathbf c,$$
expand the triple product and take the dot product with $\mathbf a$. This gives $\mathbf a\cdot\mathbf r=\mathbf a\cdot\mathbf c$ and hence
$$(1-\mathbf a\cdot\mathbf b)\mathbf r
=\mathbf c-(\mathbf a\cdot\mathbf c)\mathbf b.$$

- If $\mathbf a\cdot\mathbf b\ne1$, the unique solution is
  $$\mathbf r=\frac{\mathbf c-(\mathbf a\cdot\mathbf c)\mathbf b}{1-\mathbf a\cdot\mathbf b}.$$
- If $\mathbf a\cdot\mathbf b=1$ and the right side is non-zero, there is no solution.
- If $\mathbf a\cdot\mathbf b=1$ and the right side is zero, the solutions form the plane $\mathbf a\cdot\mathbf r=\mathbf a\cdot\mathbf c$.

Source: [[Vectors and Matrices - Chapter 2 Vectors]], pages 14–19, which retains the full derivations and all geometric sketches as TikZ. The current source supplies the complete vector-equation solution on pages 18–19.

Related: [[Vectors and Linear Span]], [[Orthonormal Bases and Vector Coordinates]], [[Real Inner Products and Cauchy-Schwarz]].
