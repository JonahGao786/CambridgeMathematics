---
title: Cross Products and Scalar Triple Products
material_type: concept note
course: Part IA Vectors and Matrices
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: [10, 11, 12, 13, 14, 20, 21, 22, 23]
---

# Cross Products and Scalar Triple Products

For non-zero, non-parallel $\mathbf a,\mathbf b\in\mathbb R^3$,
$$\mathbf a\times\mathbf b=|\mathbf a|\,|\mathbf b|\sin\theta\,\widehat{\mathbf n},$$
where $\widehat{\mathbf n}$ is the unit normal selected by the right-hand rule. The cross product is also written $\mathbf a\wedge\mathbf b$. It is zero for parallel vectors or when either vector is zero.

Taking the opposite angle replaces $\theta$ by $2\pi-\theta$ and $\widehat{\mathbf n}$ by $-\widehat{\mathbf n}$; the two signs cancel.

## Properties

For real $\lambda$ and vectors in $\mathbb R^3$,
$$\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a,\qquad
\mathbf a\times\mathbf a=\mathbf0,$$
$$\mathbf a\times\mathbf b=\mathbf0
\quad\Longleftrightarrow\quad
\mathbf a=\lambda\mathbf b\text{ for some }\lambda\in\mathbb R
\text{ or }\mathbf b=\mathbf0,$$
$$ (\lambda\mathbf a)\times\mathbf b
=\lambda(\mathbf a\times\mathbf b)=\mathbf a\times(\lambda\mathbf b),$$
$$\mathbf a\times(\mathbf b+\mathbf c)
=\mathbf a\times\mathbf b+\mathbf a\times\mathbf c,$$
$$\mathbf a\cdot(\mathbf a\times\mathbf b)
=\mathbf b\cdot(\mathbf a\times\mathbf b)=0.$$

## Area and rotation

The cross product is the **vector area** of the parallelogram spanned by $\mathbf a,\mathbf b$:
$$\text{scalar area}=|\mathbf a\times\mathbf b|.$$
For $0\le\theta\le\pi$, this is base times height, $|\mathbf a|(|\mathbf b|\sin\theta)$. Exchanging the vectors reverses orientation and preserves the scalar area. The triangle area is half the magnitude of the cross product of its two edge vectors.

Fix $\mathbf a\ne\mathbf0$. On the plane perpendicular to $\mathbf a$, the map $\mathbf x\mapsto\mathbf a\times\mathbf x$ stays in the plane and satisfies
$$|\mathbf a\times\mathbf x|=|\mathbf a|\,|\mathbf x|,
\qquad\mathbf x\cdot(\mathbf a\times\mathbf x)=0.$$
It scales lengths by $|\mathbf a|$ and rotates non-zero vectors through a right-hand quarter-turn about $\mathbf a$. For unit $\mathbf a$, there is no length change.

## Coordinate formula

For the standard right-handed [[Orthonormal Bases and Vector Coordinates|orthonormal basis]],
$$\mathbf e_1\times\mathbf e_2=\mathbf e_3,\qquad
\mathbf e_2\times\mathbf e_3=\mathbf e_1,\qquad
\mathbf e_3\times\mathbf e_1=\mathbf e_2.$$
Reversing the order reverses the sign. Expanding by bilinearity gives
$$\mathbf a\times\mathbf b=
(a_2b_3-a_3b_2)\mathbf e_1
+(a_3b_1-a_1b_3)\mathbf e_2
+(a_1b_2-a_2b_1)\mathbf e_3.$$
The determinant mnemonic is
$$\mathbf a\times\mathbf b=
\begin{vmatrix}
\mathbf e_1&\mathbf e_2&\mathbf e_3\\
a_1&a_2&a_3\\
b_1&b_2&b_3
\end{vmatrix}.$$

## Scalar triple product and volume

Define
$$[\mathbf a,\mathbf b,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c).$$
Cyclic permutations preserve it:
$$\mathbf a\cdot(\mathbf b\times\mathbf c)
=\mathbf b\cdot(\mathbf c\times\mathbf a)
=\mathbf c\cdot(\mathbf a\times\mathbf b).$$
Exchanging two vectors reverses its sign. It is zero if two vectors are equal. In a right-handed orthonormal basis,
$$[\mathbf a,\mathbf b,\mathbf c]=
\begin{vmatrix}
a_1&a_2&a_3\\
b_1&b_2&b_3\\
c_1&c_2&c_3
\end{vmatrix}.$$

For non-parallel $\mathbf a,\mathbf b$, the normal to their parallelogram is $\widehat{\mathbf n}=(\mathbf a\times\mathbf b)/|\mathbf a\times\mathbf b|$. With third edge $\mathbf c$, the perpendicular height is $h=|\widehat{\mathbf n}\cdot\mathbf c|$. Therefore the parallelepiped volume is
$$V=|\mathbf a\times\mathbf b|h
=|\mathbf c\cdot(\mathbf a\times\mathbf b)|.$$

The scalar triple product is a signed volume: its sign records the component of $\mathbf c$ along $\mathbf a\times\mathbf b$. It is zero exactly when the three vectors are coplanar, equivalently one is a linear combination of the other two.

## Vector triple product

For vectors in $\mathbb R^3$,
$$\mathbf a\times(\mathbf b\times\mathbf c)
=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf c,$$
whereas
$$(\mathbf a\times\mathbf b)\times\mathbf c
=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf b\cdot\mathbf c)\mathbf a.$$
Thus the cross product is not associative. These identities are stated on page 14 and applied to [[Lines, Planes and Vector Equations|line–plane intersections]] on page 16. A component proof using epsilon contraction appears on page 22.

## Levi-Civita notation and contraction

For the right-handed orthonormal basis, $\varepsilon_{123}=\varepsilon_{231}=\varepsilon_{312}=1$, the reversed permutations have value $-1$, and repeated index values give zero. Repeated index letters are summed over $1,2,3$:
$$\mathbf e_i\times\mathbf e_j=\varepsilon_{ijk}\mathbf e_k,$$
$$(\mathbf a\times\mathbf b)_i=\varepsilon_{ijk}a_jb_k,$$
$$\mathbf a\cdot(\mathbf b\times\mathbf c)
=\varepsilon_{ijk}a_ib_jc_k.$$
The contraction identity
$$\varepsilon_{ijk}\varepsilon_{pqk}
=\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp}$$
gives the page-22 vector triple-product proof after cyclically rewriting $\varepsilon_{kpq}$ as $\varepsilon_{pqk}$.

## Lagrange's identity

Page 23 proves, using the same contraction,
$$(\mathbf a\times\mathbf b)\cdot(\mathbf b\times\mathbf c)
=(\mathbf a\cdot\mathbf b)(\mathbf b\cdot\mathbf c)
-(\mathbf a\cdot\mathbf c)|\mathbf b|^2.$$
For the full calculation, see [[Vectors and Matrices - Chapter 2 Vectors]]. [[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]] expands the notation, signs, contractions and a numerical check.

See [[Vectors and Matrices - Chapter 2 Vectors]], pages 10–14 and 20–23. Related: [[Real Inner Products and Cauchy-Schwarz]].

## Zero volume and operation order

The volume formula also holds when $\mathbf a,\mathbf b$ are parallel: both the cross product and the volume are zero, although dividing by $|\mathbf a\times\mathbf b|$ to define a normal is then invalid. More generally, $[\mathbf a,\mathbf b,\mathbf c]=0$ exactly when the three vectors are linearly dependent, equivalently their span has dimension at most two.

The scalar triple product is a real number. It must not be confused with a vector triple product such as $\mathbf a\times(\mathbf b\times\mathbf c)$. Cross products are not associative, so parentheses in the latter are essential; see question 2(v) of [[Groups 0 - Handwritten Attempts]].
