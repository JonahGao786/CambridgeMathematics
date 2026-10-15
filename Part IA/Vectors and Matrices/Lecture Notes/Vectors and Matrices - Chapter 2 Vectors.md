---
title: Vectors and Matrices - Chapter 2 Vectors
material_type: handwritten lecture notes
course: Part IA Vectors and Matrices
date: null
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: 13
---

# Vectors and Matrices — Chapter 2: Vectors

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view). No date is supplied. The ten drawings below preserve the labelled geometry and meaningful colours; their layout coordinates are schematic. Drawings of three-dimensional geometry are shown in projection.

## 2.1 Vectors (page 1)

A non-zero geometric vector has a positive magnitude and a direction in space. Represent it by
$$\mathbf v=\overrightarrow{AB},$$
with length $|\mathbf v|$ and direction and sense from $A$ to $B$. The zero vector is included in the vector operations below.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (A) at (0,0);
  \coordinate (B) at (2,1.6);
  \draw[blue,thick,->] (A)--(B);
  \fill[red] (A) circle (1.5pt);
  \node[red,below left] at (A) {$A$};
  \node[red,above right] at (B) {$B$};
\end{tikzpicture}
\end{document}
```

If $O$ is the origin, the position vector of $A$ is $\mathbf a=\overrightarrow{OA}$.

A **unit vector** has length $1$. For $\mathbf v\ne\mathbf0$, write
$$\widehat{\mathbf v}=\frac{\mathbf v}{|\mathbf v|}.$$

A **vector space** over $\mathbb R$ or $\mathbb C$ is described here as a collection $V$ of vectors with vector addition and multiplication by scalars from the corresponding field. The operations and their properties follow below; see [[Vectors and Linear Span]].

### 2.1.1 Vector addition (pages 1–2)

For non-parallel $\mathbf a=\overrightarrow{OA}$ and $\mathbf b=\overrightarrow{OB}$, draw a line through $A$ parallel to $\mathbf b$ and a line through $B$ parallel to $\mathbf a$. Their intersection $C$ gives the parallelogram $OACB$, with
$$\mathbf c=\overrightarrow{OC}=\mathbf a+\mathbf b.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \coordinate (A) at (1,1.8);
  \coordinate (B) at (2.3,0);
  \coordinate (C) at (3.3,1.8);
  \draw[thick,->] (O)--(A) node[midway,left] {$\mathbf a$};
  \draw[thick,->] (O)--(B) node[midway,below] {$\mathbf b$};
  \draw[red,thick,->] (A)--(3.85,1.8);
  \draw[red,thick,->] (B)--(3.6,2.34);
  \draw[blue,thick,->] (O)--(C) node[midway,below right,black] {$\mathbf c$};
  \node[below left] at (O) {$O$};
  \node[above left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[red,below right] at (C) {$C$};
  \node[blue,right] at (4.2,1.2) {$\mathbf c=\mathbf a+\mathbf b$};
\end{tikzpicture}
\end{document}
```

The properties on page 2 are:

1. **Commutativity:** $\mathbf a+\mathbf b=\mathbf b+\mathbf a$.
2. **Associativity:** $(\mathbf a+\mathbf b)+\mathbf c=\mathbf a+(\mathbf b+\mathbf c)$.
3. **Identity:** $\mathbf a+\mathbf0=\mathbf a$.
4. **Inverse:** $\mathbf a+(-\mathbf a)=\mathbf0$.

Vectors under addition form an abelian [[Groups|group]]. The associativity sketch uses black arrows for $\mathbf a,\mathbf b,\mathbf c$, blue for the pairwise sums, and red for their total:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \draw[thick,->] (O)--(2.3,-0.5) node[midway,below] {$\mathbf a$};
  \draw[thick,->] (O)--(1.25,0.5) node[midway,above] {$\mathbf b$};
  \draw[thick,->] (O)--(0.4,1.85) node[midway,left] {$\mathbf c$};
  \draw[blue,thick,->] (O)--(3.55,0) node[near end,above] {$\mathbf a+\mathbf b$};
  \draw[blue,thick,->] (O)--(1.65,2.35) node[above left] {$\mathbf b+\mathbf c$};
  \draw[red,thick,->] (O)--(3.95,1.85) node[near end,above] {$\mathbf a+\mathbf b+\mathbf c$};
  \node[below left] at (O) {$O$};
\end{tikzpicture}
\end{document}
```

### 2.1.2 Scalar multiplication (pages 2–3)

For $\lambda\in\mathbb R$,
$$|\lambda\mathbf a|=|\lambda|\,|\mathbf a|.$$
For $\lambda>0$, the direction agrees with $\mathbf a$; for $\lambda<0$, it is opposite. For $\lambda=0$, the result is the zero vector.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \draw[red,thick,->] (O)--(2.3,2.3) node[midway,above left] {$\lambda\mathbf a$};
  \node[red,right] at (2.3,2.3) {$\lambda>0$};
  \draw[thick,->] (O)--(1.1,1.1) node[midway,below right] {$\mathbf a$};
  \draw[blue,thick,->] (O)--(-1.6,-1.6) node[midway,below right] {$\lambda\mathbf a$};
  \node[blue,below] at (-1.6,-1.6) {$\lambda<0$};
  \node[below right] at (O) {$O$};
\end{tikzpicture}
\end{document}
```

For $\mathbf a\ne\mathbf0$, the set $\{\lambda\mathbf a:\lambda\in\mathbb R\}$ is the line through $O$ in the direction of $\mathbf a$.

For real scalars $\lambda,\mu$:
$$\begin{aligned}
\lambda(\mathbf a+\mathbf b)&=\lambda\mathbf a+\lambda\mathbf b,\\
(\lambda+\mu)\mathbf a&=\lambda\mathbf a+\mu\mathbf a,\\
\lambda(\mu\mathbf a)&=(\lambda\mu)\mathbf a,\\
1\mathbf a&=\mathbf a.
\end{aligned}$$

### 2.1.3 Linear combinations and span (pages 3–4)

For vectors $\mathbf a,\mathbf b$ and scalars $\alpha,\beta$, the vector $\alpha\mathbf a+\beta\mathbf b$ is a **linear combination**, and
$$\operatorname{span}\{\mathbf a,\mathbf b\}
=\{\alpha\mathbf a+\beta\mathbf b:\alpha,\beta\in\mathbb R\}.$$
This extends to any number of vectors.

Vectors $\mathbf a,\mathbf b$ are **parallel**, written $\mathbf a\parallel\mathbf b$, if $\mathbf a=\lambda\mathbf b$ or $\mathbf b=\lambda\mathbf a$ for some $\lambda\in\mathbb R$.

For non-zero, non-parallel vectors, written $\mathbf a\nparallel\mathbf b$, their span is the plane through their endpoints and the origin.

The space $\mathbb R^n$, with componentwise addition and scalar multiplication, is a vector space. A line that does not contain the origin, for example $x+y=1$, is not a vector space under these operations.

## 2.2 Scalar or dot product (pages 4–5)

The scalar or dot product returns a scalar. For non-zero $\mathbf a,\mathbf b\in\mathbb R^n$ with angle $\theta$ between them,
$$\mathbf a\cdot\mathbf b=|\mathbf a|\,|\mathbf b|\cos\theta.$$
The dot product with a zero vector is zero.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(3,0) node[right] {$\mathbf a$};
  \draw[thick,->] (0,0)--(1,2) node[midway,left] {$\mathbf b$};
  \draw (0.55,0) arc (0:63.435:0.55) node[midway,right] {$\theta$};
  \draw[red,dashed] (1,2)--(1,0);
  \draw[red] (0,-0.15)--(1,-0.15);
  \draw[red] (0,-0.1)--(0,-0.2);
  \draw[red] (1,-0.1)--(1,-0.2);
  \node[red,below] at (0.5,-0.2) {$|\mathbf b|\cos\theta$};
\end{tikzpicture}
\end{document}
```

The properties are
$$\begin{aligned}
\mathbf a\cdot\mathbf b&=\mathbf b\cdot\mathbf a,\\
\mathbf a\cdot\mathbf a&=|\mathbf a|^2\ge0,
\quad\text{with equality iff }\mathbf a=\mathbf0,\\
(\lambda\mathbf a)\cdot\mathbf b&=\lambda(\mathbf a\cdot\mathbf b)
=\mathbf a\cdot(\lambda\mathbf b),\\
\mathbf a\cdot(\mathbf b+\mathbf c)&=\mathbf a\cdot\mathbf b+\mathbf a\cdot\mathbf c.
\end{aligned}$$

### Orthogonality and projection (page 5)

Vectors are **orthogonal**, written $\mathbf a\perp\mathbf b$, if $\mathbf a\cdot\mathbf b=0$. The zero vector is orthogonal to every vector.

For $\mathbf a\ne\mathbf0$, let $\widehat{\mathbf a}=\mathbf a/|\mathbf a|$. The orthogonal projection of $\mathbf b$ onto the line in the direction of $\mathbf a$ is
$$\operatorname{proj}_{\mathbf a}\mathbf b
=(\widehat{\mathbf a}\cdot\mathbf b)\widehat{\mathbf a}
=\frac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\mathbf a.$$
For $\mathbf b\ne\mathbf0$, the signed component is $|\mathbf b|\cos\theta$, so the projection is $|\mathbf b|\cos\theta\,\widehat{\mathbf a}$.

The remaining part
$$\mathbf b-(\widehat{\mathbf a}\cdot\mathbf b)\widehat{\mathbf a}$$
is orthogonal to $\mathbf a$.

### Cosine rule (page 5)

Let $\theta=\angle BAC$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (A) at (0,0);
  \coordinate (B) at (3.2,0);
  \coordinate (C) at (1.25,1.7);
  \draw[thick,->] (A)--(B) node[midway,below,blue] {$|\overrightarrow{AB}|$};
  \draw[thick,->] (A)--(C) node[midway,above left,blue] {$|\overrightarrow{AC}|$};
  \draw[thick,->] (C)--(B) node[midway,above right,blue] {$|\overrightarrow{BC}|$};
  \draw (0.45,0) arc (0:53.673:0.45) node[midway,right] {$\theta$};
  \node[below left] at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above] at (C) {$C$};
\end{tikzpicture}
\end{document}
```

Since $\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$,
$$\begin{aligned}
|\overrightarrow{BC}|^2
&=(\overrightarrow{AC}-\overrightarrow{AB})\cdot
(\overrightarrow{AC}-\overrightarrow{AB})\\
&=|\overrightarrow{AC}|^2+|\overrightarrow{AB}|^2
-2\overrightarrow{AB}\cdot\overrightarrow{AC}\\
&=|\overrightarrow{AC}|^2+|\overrightarrow{AB}|^2
-2|\overrightarrow{AB}|\,|\overrightarrow{AC}|\cos\theta.
\end{aligned}$$
If $\theta=\pi/2$, the last term vanishes and Pythagoras' theorem is recovered.

## Inner products on a real vector space (page 6)

For a real vector space $V$, an **inner product** is a map $V\times V\to\mathbb R$, written $\langle\mathbf x,\mathbf y\rangle$, satisfying, for all $\mathbf x,\mathbf y,\mathbf z\in V$ and $\alpha,\beta\in\mathbb R$:

1. **Symmetry:** $\langle\mathbf x,\mathbf y\rangle=\langle\mathbf y,\mathbf x\rangle$.
2. **Linearity in the second argument:**
   $$\langle\mathbf x,\alpha\mathbf y+\beta\mathbf z\rangle
   =\alpha\langle\mathbf x,\mathbf y\rangle+\beta\langle\mathbf x,\mathbf z\rangle.$$
3. **Positive definiteness:** $\langle\mathbf x,\mathbf x\rangle\ge0$, with equality iff $\mathbf x=\mathbf0$.

These are bilinear: symmetry also gives linearity in the first argument. The induced norm is
$$\|\mathbf a\|=\sqrt{\langle\mathbf a,\mathbf a\rangle}.$$
For the Euclidean dot product, $\|\mathbf a\|=\sqrt{\mathbf a\cdot\mathbf a}=|\mathbf a|$.

## Cauchy–Schwarz inequality (pages 7–8)

**Theorem.** For all $\mathbf x,\mathbf y\in\mathbb R^n$,
$$|\mathbf x\cdot\mathbf y|\le|\mathbf x|\,|\mathbf y|.$$

**Proof.** If $\mathbf y=\mathbf0$, both sides are zero. Otherwise, for every $\lambda\in\mathbb R$,
$$\begin{aligned}
0\le|\mathbf x-\lambda\mathbf y|^2
&=(\mathbf x-\lambda\mathbf y)\cdot(\mathbf x-\lambda\mathbf y)\\
&=\mathbf x\cdot\mathbf x-2\lambda\mathbf x\cdot\mathbf y
+\lambda^2\mathbf y\cdot\mathbf y\\
&=|\mathbf y|^2\lambda^2-2(\mathbf x\cdot\mathbf y)\lambda+|\mathbf x|^2.
\end{aligned}$$
This quadratic is non-negative for every real $\lambda$, so its discriminant is non-positive:
$$[-2(\mathbf x\cdot\mathbf y)]^2-4|\mathbf y|^2|\mathbf x|^2\le0.$$
Equivalently, $(\mathbf x\cdot\mathbf y)^2\le|\mathbf y|^2|\mathbf x|^2$. Taking non-negative square roots gives the result.

The inequality holds for any inner product on a real vector space:
$$|\langle\mathbf x,\mathbf y\rangle|\le\|\mathbf x\|\,\|\mathbf y\|.$$
The source states that equality holds iff $\mathbf x=\lambda\mathbf y$ or $\mathbf y=\lambda\mathbf x$ for some real $\lambda$; it supplies no separate equality-case proof.

## Triangle inequality (page 8)

$$|\mathbf x+\mathbf y|\le|\mathbf x|+|\mathbf y|.$$

**Proof.** Using Cauchy–Schwarz,
$$\begin{aligned}
|\mathbf x+\mathbf y|^2
&=(\mathbf x+\mathbf y)\cdot(\mathbf x+\mathbf y)\\
&=|\mathbf x|^2+|\mathbf y|^2+2\mathbf x\cdot\mathbf y\\
&\le|\mathbf x|^2+|\mathbf y|^2+2|\mathbf x|\,|\mathbf y|\\
&=(|\mathbf x|+|\mathbf y|)^2.
\end{aligned}$$
Taking non-negative square roots gives the stated inequality.

See [[Real Inner Products and Cauchy-Schwarz]] and the related [[Triangle Inequality for Complex Numbers]].

## 2.3 Orthonormal bases (pages 9–10)

In $\mathbb R^3$, let $\mathbf e_1,\mathbf e_2,\mathbf e_3$ be **orthonormal**: each has length $1$, and distinct vectors are perpendicular. Equivalently,
$$\mathbf e_i\cdot\mathbf e_j=\delta_{ij}
=\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}$$
This corresponds to choosing Cartesian axes in these directions. The set $\{\mathbf e_1,\mathbf e_2,\mathbf e_3\}$ is a basis of $\mathbb R^3$.

Every $\mathbf a\in\mathbb R^3$ has a unique expansion
$$\mathbf a=a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3,
\qquad a_i=\mathbf e_i\cdot\mathbf a.$$
Write either a row or column of coordinates:
$$\mathbf a=(a_1,a_2,a_3),\qquad
\mathbf a=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}.$$
Similarly,
$$\mathbf b=b_1\mathbf e_1+b_2\mathbf e_2+b_3\mathbf e_3,
\qquad b_i=\mathbf e_i\cdot\mathbf b.$$

Expanding the dot product gives
$$\begin{aligned}
\mathbf a\cdot\mathbf b
&=(a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3)
\cdot(b_1\mathbf e_1+b_2\mathbf e_2+b_3\mathbf e_3)\\
&=a_1b_1+a_2b_2+a_3b_3.
\end{aligned}$$
The six mixed terms vanish because $\mathbf e_i\cdot\mathbf e_j=0$ when $i\ne j$. Taking $\mathbf b=\mathbf a$,
$$|\mathbf a|^2=\mathbf a\cdot\mathbf a=a_1^2+a_2^2+a_3^2.$$

The standard basis is
$$\mathbf e_1=(1,0,0),\qquad\mathbf e_2=(0,1,0),\qquad\mathbf e_3=(0,0,1),$$
also written $\widehat{\mathbf i},\widehat{\mathbf j},\widehat{\mathbf k}$. See [[Orthonormal Bases and Vector Coordinates]].

## 2.4 Vector or cross product (pages 10–12)

For vectors $\mathbf a,\mathbf b\in\mathbb R^3$, write the **vector product** as $\mathbf a\times\mathbf b$ or $\mathbf a\wedge\mathbf b$.

For non-zero, non-parallel vectors, it is
$$\mathbf a\times\mathbf b=|\mathbf a|\,|\mathbf b|\sin\theta\,\widehat{\mathbf n},$$
where $\theta$ is the angle between them and $\widehat{\mathbf n}$ is the unit normal perpendicular to both, chosen by the right-hand rule. The cross product is zero if the vectors are parallel or either is zero.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \draw[thick,->] (O)--(2.8,1) node[above right] {$\mathbf a$};
  \draw[thick,->] (O)--(2.5,-0.95) node[below right] {$\mathbf b$};
  \draw[red,thick,->] (O)--(0,2) node[above] {$\mathbf a\times\mathbf b$};
  \draw (19.654:0.8) arc (19.654:-20.807:0.8);
  \node at (1.05,-0.03) {$\theta$};
  \node[below left] at (O) {$O$};
\end{tikzpicture}
\end{document}
```

For non-parallel vectors, taking the opposite route from $\mathbf a$ to $\mathbf b$ gives the oriented angle $2\pi-\theta$ and the opposite normal. Since
$$\sin(2\pi-\theta)=-\sin\theta,$$
the two sign changes leave the cross product unchanged.

### Properties (page 11)

For $\mathbf a,\mathbf b,\mathbf c\in\mathbb R^3$ and $\lambda\in\mathbb R$:

- $\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a$.
- $\mathbf a\times\mathbf a=\mathbf0$.
- $\mathbf a\times\mathbf b=\mathbf0$ iff $\mathbf a=\lambda\mathbf b$ for some $\lambda\in\mathbb R$, or $\mathbf b=\mathbf0$.
- $(\lambda\mathbf a)\times\mathbf b=\lambda(\mathbf a\times\mathbf b)=\mathbf a\times(\lambda\mathbf b)$.
- $\mathbf a\times(\mathbf b+\mathbf c)=\mathbf a\times\mathbf b+\mathbf a\times\mathbf c$.
- $\mathbf a\cdot(\mathbf a\times\mathbf b)=\mathbf b\cdot(\mathbf a\times\mathbf b)=0$.

### Vector area (page 11)

The vector $\mathbf a\times\mathbf b$ is the **vector area** of the parallelogram spanned by $\mathbf a,\mathbf b$. Its magnitude is the ordinary scalar area.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \coordinate (A) at (2.8,0);
  \coordinate (B) at (1.4,1.6);
  \coordinate (D) at (4.2,1.6);
  \begin{scope}
    \clip (O)--(A)--(D)--(B)--cycle;
    \foreach \x in {-0.5,-0.1,...,4.3} {
      \draw[blue] (\x,0)--(\x+0.65,1.6);
    }
  \end{scope}
  \draw[thick,->] (O)--(A) node[below right] {$\mathbf a$};
  \draw[thick,->] (O)--(B) node[above] {$\mathbf b$};
  \draw[red,thick,->] (B)--(D) node[midway,above] {$\mathbf a$};
  \draw[red,thick,->] (A)--(D) node[midway,below right] {$\mathbf b$};
  \draw (0.5,0) arc (0:48.814:0.5);
  \node at (0.65,0.25) {$\theta$};
  \node[below] at (1.4,-0.08) {$|\mathbf a|$};
  \node[above left] at (0.65,0.85) {$|\mathbf b|$};
  \node[below left] at (O) {$O$};
\end{tikzpicture}
\end{document}
```

For $0\le\theta\le\pi$, the base has length $|\mathbf a|$ and the height is $h=|\mathbf b|\sin\theta$. Therefore
$$\text{area}=|\mathbf a|\,|\mathbf b|\sin\theta=|\mathbf a\times\mathbf b|.$$
For non-parallel vectors, the normal direction records orientation. Interchanging $\mathbf a$ and $\mathbf b$ reverses that direction while preserving the scalar area.

For the triangle $OBA$,
$$S_{OBA}=\frac12\left|\overrightarrow{OA}\times\overrightarrow{OB}\right|.$$

### Scaling and rotation (page 12)

Fix $\mathbf a\ne\mathbf0$, and let $\mathbf x$ lie in the plane perpendicular to $\mathbf a$. The map
$$\mathbf x\longmapsto\mathbf a\times\mathbf x$$
takes the plane to itself, since $\mathbf a\times\mathbf x$ is perpendicular to $\mathbf a$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \draw[thick] (-1.4,-0.9)--(0.8,-0.9)--(1.8,0.9)--(-0.4,0.9)--cycle;
  \draw[red,thick,->] (O)--(0,1.7) node[above] {$\mathbf a$};
  \draw[blue,thick,->] (O)--(-0.45,-0.8) node[below] {$\mathbf x$};
  \draw[orange!85!yellow,thick,->] (O)--(1.3,0)
    node[above] {$\mathbf a\times\mathbf x$};
\end{tikzpicture}
\end{document}
```

Here
$$|\mathbf a\times\mathbf x|=|\mathbf a|\,|\mathbf x|,
\qquad\mathbf x\cdot(\mathbf a\times\mathbf x)=0.$$
For $\mathbf x\ne\mathbf0$, the map scales length by $|\mathbf a|$ and rotates through $\pi/2$ in the right-hand sense about the axis in the direction of $\mathbf a$. If $\mathbf a$ is a unit vector, it is a quarter-turn with no change of length.

### Coordinates in the standard basis (page 12)

For the standard right-handed orthonormal basis,
$$\begin{aligned}
\mathbf e_1\times\mathbf e_2&=\mathbf e_3=-(\mathbf e_2\times\mathbf e_1),\\
\mathbf e_2\times\mathbf e_3&=\mathbf e_1=-(\mathbf e_3\times\mathbf e_2),\\
\mathbf e_3\times\mathbf e_1&=\mathbf e_2=-(\mathbf e_1\times\mathbf e_3).
\end{aligned}$$
Thus, for $\mathbf a=(a_1,a_2,a_3)$ and $\mathbf b=(b_1,b_2,b_3)$,
$$\begin{aligned}
\mathbf a\times\mathbf b
&=(a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3)
\times(b_1\mathbf e_1+b_2\mathbf e_2+b_3\mathbf e_3)\\
&=(a_2b_3-a_3b_2)\mathbf e_1
+(a_3b_1-a_1b_3)\mathbf e_2
+(a_1b_2-a_2b_1)\mathbf e_3.
\end{aligned}$$
This is commonly written using the determinant mnemonic
$$\mathbf a\times\mathbf b=
\begin{vmatrix}
\mathbf e_1&\mathbf e_2&\mathbf e_3\\
a_1&a_2&a_3\\
b_1&b_2&b_3
\end{vmatrix}.$$

## 2.5 Triple products (page 13)

### 2.5.1 Scalar triple product

For $\mathbf a,\mathbf b,\mathbf c\in\mathbb R^3$, define
$$[\mathbf a,\mathbf b,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c).$$
Order matters. A cyclic permutation does not change the value:
$$\begin{aligned}
\mathbf a\cdot(\mathbf b\times\mathbf c)
&=\mathbf b\cdot(\mathbf c\times\mathbf a)
=\mathbf c\cdot(\mathbf a\times\mathbf b)\\
&=-\mathbf a\cdot(\mathbf c\times\mathbf b)
=-\mathbf b\cdot(\mathbf a\times\mathbf c)
=-\mathbf c\cdot(\mathbf b\times\mathbf a).
\end{aligned}$$
In particular, the scalar triple product is zero if two vectors are equal.

In a right-handed orthonormal basis,
$$[\mathbf a,\mathbf b,\mathbf c]=
\begin{vmatrix}
a_1&a_2&a_3\\
b_1&b_2&b_3\\
c_1&c_2&c_3
\end{vmatrix}.$$

### Geometric interpretation: volume

For $\mathbf a\nparallel\mathbf b$, their parallelogram is a base for the parallelepiped spanned by $\mathbf a,\mathbf b,\mathbf c$. The sketch shows the base, its normal, $\mathbf c$ and the perpendicular height.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \coordinate (O) at (0,0);
  \coordinate (A) at (2.4,-0.6);
  \coordinate (B) at (2.7,1.05);
  \coordinate (D) at (5.1,0.45);
  \coordinate (C) at (2,2.3);
  \coordinate (H) at (2,-0.05);
  \draw[thick,->] (O)--(A) node[midway,below] {$\mathbf a$};
  \draw[thick,->] (O)--(B) node[midway,below] {$\mathbf b$};
  \draw[red,thick] (A)--(D)--(B);
  \draw[thick,->] (O)--(C) node[midway,above left] {$\mathbf c$};
  \draw[red,thick,->] (O)--(0,2.6) node[above] {$\mathbf a\times\mathbf b$};
  \draw[blue] (C)--(H) node[midway,right] {$h$};
  \draw[blue] (1.94,-0.11)--(2.06,0.01);
  \draw[blue] (1.94,0.01)--(2.06,-0.11);
  \node[below left] at (O) {$O$};
  \node[below right] at (A) {$A$};
  \node[above right] at (B) {$B$};
  \node[above] at (C) {$C$};
\end{tikzpicture}
\end{document}
```

With
$$\widehat{\mathbf n}=\frac{\mathbf a\times\mathbf b}{|\mathbf a\times\mathbf b|},$$
the height is
$$h=\left|\mathbf c\cdot\frac{\mathbf a\times\mathbf b}{|\mathbf a\times\mathbf b|}\right|
=|\widehat{\mathbf n}\cdot\mathbf c|.$$
Hence
$$\begin{aligned}
V&=\text{base area}\times\text{height}\\
&=|\mathbf a\times\mathbf b|\,h\\
&=|\mathbf c\cdot(\mathbf a\times\mathbf b)|.
\end{aligned}$$

See [[Cross Products and Scalar Triple Products]] for these definitions, properties and interpretations together.
