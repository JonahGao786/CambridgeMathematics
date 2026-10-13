---
title: Vectors and Matrices - Chapter 2 Vectors
material_type: handwritten lecture notes
course: Part IA Vectors and Matrices
date: null
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: 8
---

# Vectors and Matrices — Chapter 2: Vectors

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view). No date is supplied. The six drawings below preserve the labelled geometry and meaningful colours; their layout coordinates are schematic.

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
