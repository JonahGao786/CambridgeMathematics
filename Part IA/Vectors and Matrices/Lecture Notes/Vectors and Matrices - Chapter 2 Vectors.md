---
title: Vectors and Matrices - Chapter 2 Vectors
course: Part IA Vectors and Matrices
material_type: lecture notes
chapter: 2
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: 29
tags: [lecture, vectors-and-matrices]
---

# Vectors and Matrices — Chapter 2: Vectors

> [!abstract] Overview
> Vectors in $\mathbb R^n$: addition, scalar multiplication, span; the dot product, Cauchy–Schwarz and the triangle inequality; orthonormal bases; cross and triple products; lines and planes; index notation ($\delta_{ij}$, $\varepsilon_{ijk}$, summation convention) with its applications; then general vector spaces over $\mathbb R$ or $\mathbb C$, subspaces and linear independence.
> Prerequisite: [[Vectors and Matrices - Chapter 1 Complex Numbers]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Vector, unit vector, vector space]] | $\overrightarrow{AB}$, $\hat{\mathbf v}=\mathbf v/\lvert\mathbf v\rvert$ | 1 |
| [[#Vector addition]] | parallelogram rule; abelian group | 1–2 |
| [[#Scalar multiplication]] | $\lvert\lambda\mathbf a\rvert=\lvert\lambda\rvert\lvert\mathbf a\rvert$ | 2–3 |
| [[#Definition — Linear combination, span, parallel]] | $\operatorname{span}\{\mathbf a,\mathbf b\}$ | 3 |
| [[#Definition — Dot product]] | $\mathbf a\cdot\mathbf b=\lvert\mathbf a\rvert\lvert\mathbf b\rvert\cos\theta$ | 4 |
| [[#Definition — Orthogonality and projection]] | $(\hat{\mathbf a}\cdot\mathbf b)\hat{\mathbf a}$ | 5 |
| [[#Cosine rule]] | from $\lvert\mathbf{AC}-\mathbf{AB}\rvert^2$ | 5 |
| [[#Definition — Inner product]] | symmetric, linear, positive definite | 6 |
| [[#Theorem — Cauchy-Schwarz inequality]] | $\lvert\mathbf x\cdot\mathbf y\rvert\le\lvert\mathbf x\rvert\lvert\mathbf y\rvert$ | 7–8 |
| [[#Theorem — Triangle inequality]] | $\lvert\mathbf x+\mathbf y\rvert\le\lvert\mathbf x\rvert+\lvert\mathbf y\rvert$ | 8 |
| [[#Definition — Orthonormal basis]] | $\mathbf e_i\cdot\mathbf e_j=\delta_{ij}$, $a_i=\mathbf e_i\cdot\mathbf a$ | 9–10 |
| [[#Definition — Cross product]] | $\lvert\mathbf a\rvert\lvert\mathbf b\rvert\sin\theta\,\hat{\mathbf n}$ | 10 |
| [[#Proposition — Properties of the cross product]] | antisymmetric, bilinear, $\perp$ to both | 11 |
| [[#Cross product in components]] | determinant formula | 12 |
| [[#Definition — Scalar triple product]] | $[\mathbf a,\mathbf b,\mathbf c]$, signed volume | 13–14 |
| [[#Vector triple product]] | $\mathbf a\times(\mathbf b\times\mathbf c)=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf c$ | 14 |
| [[#Lines]] | $\mathbf r=\mathbf a+\lambda\mathbf u$, $\mathbf u\times\mathbf r=\mathbf u\times\mathbf a$ | 14 |
| [[#Planes]] | $\mathbf n\cdot\mathbf r=k$ | 15 |
| [[#Intersection of a line and a plane]] | unique point iff $\mathbf u\cdot\mathbf n\ne0$ | 16 |
| [[#Shortest distance between two lines]] | $\lvert(\mathbf a_1-\mathbf a_2)\cdot\hat{\mathbf n}\rvert$ | 17 |
| [[#Vector equations]] | $\mathbf r+\mathbf a\times(\mathbf b\times\mathbf r)=\mathbf c$ | 18–19 |
| [[#Definition — Kronecker delta and Levi-Civita symbol]] | $\delta_{ij}$, $\varepsilon_{ijk}$ | 19–20 |
| [[#Einstein summation convention]] | repeated index is summed | 21 |
| [[#Proposition — Epsilon identities]] | $\varepsilon_{ijk}\varepsilon_{pqk}=\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp}$ | 22 |
| [[#Proof of the vector triple product identity]] | via epsilon identity | 22 |
| [[#Lagrange's identity]] | $(\mathbf a\times\mathbf b)\cdot(\mathbf b\times\mathbf c)$ | 23 |
| [[#Signed area in two dimensions]] | $[\mathbf a,\mathbf b]=a_1b_2-a_2b_1$ | 23–24 |
| [[#Spherical trigonometry]] | spherical cosine rule | 24 |
| [[#Spheres and balls]] | $\lvert\mathbf x-\mathbf a\rvert=r$ | 25 |
| [[#Definition — Vector space over a field]] | $\mathbb F=\mathbb R$ or $\mathbb C$; $\mathbb R^n$, $\mathbb C^n$ | 26–27 |
| [[#Definition — Subspace]] | closed under linear combinations | 27–28 |
| [[#Definition — Linear independence]] | $\sum\lambda_i\mathbf v_i=\mathbf 0\Rightarrow\lambda_i=0$ | 29 |

## 2.1 Vectors

### Definition — Vector, unit vector, vector space

A **vector** is specified by a positive magnitude and a direction in space. Represent it by $\mathbf v=\overrightarrow{AB}$, whose length is $|\mathbf v|$ and whose direction and sense run from $A$ to $B$. If $O$ is the origin, the **position vector** of $A$ is $\mathbf a=\overrightarrow{OA}$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[blue,thick,->] (0,0)--(2,1.6);
  \fill[red] (0,0) circle (1.5pt);
  \node[red,below left] at (0,0) {$A$};
  \node[red,above right] at (2,1.6) {$B$};
\end{tikzpicture}
\end{document}
```

A **unit vector** has length $1$ and is written $\hat{\mathbf v}$; for $\mathbf v\ne\mathbf 0$, $\hat{\mathbf v}=\mathbf v/|\mathbf v|$.

A **vector space** over $\mathbb R$ or $\mathbb C$ is a collection $V$ of vectors with vector addition and multiplication by scalars (from $\mathbb R$ or $\mathbb C$).

### Vector addition

For $\mathbf a=\overrightarrow{OA}$, $\mathbf b=\overrightarrow{OB}$ non-parallel: the line through $A$ parallel to $\mathbf b$ and the line through $B$ parallel to $\mathbf a$ meet at $C$, forming the parallelogram $OACB$. Then $\mathbf c=\overrightarrow{OC}=\mathbf a+\mathbf b$ (**parallelogram rule**).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(1,1.8) node[midway,left] {$\mathbf a$};
  \draw[thick,->] (0,0)--(2.3,0) node[midway,below] {$\mathbf b$};
  \draw[red,thick,->] (1,1.8)--(3.85,1.8);
  \draw[red,thick,->] (2.3,0)--(3.6,2.34);
  \draw[blue,thick,->] (0,0)--(3.3,1.8) node[midway,below right,black] {$\mathbf c$};
  \node[below left] at (0,0) {$O$};
  \node[above left] at (1,1.8) {$A$};
  \node[below right] at (2.3,0) {$B$};
  \node[red,below right] at (3.3,1.8) {$C$};
  \node[blue,right] at (4.2,1.2) {$\mathbf c=\mathbf a+\mathbf b$};
\end{tikzpicture}
\end{document}
```

**Properties.** (i) $\mathbf a+\mathbf b=\mathbf b+\mathbf a$; (ii) $(\mathbf a+\mathbf b)+\mathbf c=\mathbf a+(\mathbf b+\mathbf c)$; (iii) $\mathbf a+\mathbf 0=\mathbf a$; (iv) $\mathbf a+(-\mathbf a)=\mathbf 0$. So vectors under addition form an **abelian group** ([[Groups]]).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(2.3,-0.5) node[midway,below] {$\mathbf a$};
  \draw[thick,->] (0,0)--(1.25,0.5) node[midway,above] {$\mathbf b$};
  \draw[thick,->] (0,0)--(0.4,1.85) node[midway,left] {$\mathbf c$};
  \draw[blue,thick,->] (0,0)--(3.55,0) node[near end,above] {$\mathbf a+\mathbf b$};
  \draw[blue,thick,->] (0,0)--(1.65,2.35) node[above left] {$\mathbf b+\mathbf c$};
  \draw[red,thick,->] (0,0)--(3.95,1.85) node[near end,above] {$\mathbf a+\mathbf b+\mathbf c$};
  \node[below left] at (0,0) {$O$};
\end{tikzpicture}
\end{document}
```
*Associativity: both groupings give the same red vector.*

### Scalar multiplication

For $\lambda\in\mathbb R$, $\lambda\mathbf a$ has length $|\lambda\mathbf a|=|\lambda||\mathbf a|$ and points in the direction of $\mathbf a$ if $\lambda>0$, the opposite direction if $\lambda<0$. For $\mathbf a\ne\mathbf 0$, $\{\lambda\mathbf a:\lambda\in\mathbb R\}$ is the line through $O$ in the direction of $\mathbf a$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[red,thick,->] (0,0)--(2.3,2.3) node[midway,above left] {$\lambda\mathbf a$};
  \node[red,right] at (2.3,2.3) {$\lambda>0$};
  \draw[thick,->] (0,0)--(1.1,1.1) node[midway,below right] {$\mathbf a$};
  \draw[blue,thick,->] (0,0)--(-1.6,-1.6) node[midway,below right] {$\lambda\mathbf a$};
  \node[blue,below] at (-1.6,-1.6) {$\lambda<0$};
  \node[below right] at (0,0) {$O$};
\end{tikzpicture}
\end{document}
```

**Properties.** (i) $\lambda(\mathbf a+\mathbf b)=\lambda\mathbf a+\lambda\mathbf b$; (ii) $(\lambda+\mu)\mathbf a=\lambda\mathbf a+\mu\mathbf a$; (iii) $\lambda(\mu\mathbf a)=(\lambda\mu)\mathbf a$; (iv) $1\mathbf a=\mathbf a$.

### Definition — Linear combination, span, parallel

For vectors $\mathbf a,\mathbf b$ and scalars $\alpha,\beta$, $\alpha\mathbf a+\beta\mathbf b$ is a **linear combination** of $\mathbf a,\mathbf b$, and
$$\operatorname{span}\{\mathbf a,\mathbf b\}=\{\alpha\mathbf a+\beta\mathbf b:\ \alpha,\beta\in\mathbb R\}.$$
This extends to any number of vectors.

$\mathbf a,\mathbf b$ are **parallel**, $\mathbf a\parallel\mathbf b$, if $\mathbf a=\lambda\mathbf b$ or $\mathbf b=\lambda\mathbf a$ for some $\lambda\in\mathbb R$. If non-zero $\mathbf a,\mathbf b$ are not parallel ($\mathbf a\nparallel\mathbf b$), $\operatorname{span}\{\mathbf a,\mathbf b\}$ is the plane through their endpoints and the origin.

$\mathbb R^n$ with componentwise addition and scalar multiplication is a vector space. A line not containing the origin, e.g. $x+y=1$, is not.

## 2.2 Scalar or dot product

### Definition — Dot product

The **scalar (dot) product** of two vectors returns a scalar. For $\mathbf a,\mathbf b\in\mathbb R^n$ with angle $\theta$ between them,
$$\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(3,0) node[right] {$\mathbf a$};
  \draw[thick,->] (0,0)--(1,2) node[midway,left] {$\mathbf b$};
  \draw (0.55,0) arc (0:63.435:0.55) node[midway,right] {$\theta$};
  \draw[red,dashed] (1,2)--(1,0);
  \draw[red,|-|] (0,-0.15)--(1,-0.15) node[midway,below] {$|\mathbf b|\cos\theta$};
\end{tikzpicture}
\end{document}
```

**Properties.** (i) $\mathbf a\cdot\mathbf b=\mathbf b\cdot\mathbf a$; (ii) $\mathbf a\cdot\mathbf a=|\mathbf a|^2\ge0$, with equality iff $\mathbf a=\mathbf 0$; (iii) $(\lambda\mathbf a)\cdot\mathbf b=\lambda(\mathbf a\cdot\mathbf b)=\mathbf a\cdot(\lambda\mathbf b)$; (iv) $\mathbf a\cdot(\mathbf b+\mathbf c)=\mathbf a\cdot\mathbf b+\mathbf a\cdot\mathbf c$.

### Definition — Orthogonality and projection

$\mathbf a,\mathbf b$ are **orthogonal**, $\mathbf a\perp\mathbf b$, if $\mathbf a\cdot\mathbf b=0$. The zero vector is orthogonal to every vector.

For $\mathbf a\ne\mathbf 0$, the **orthogonal projection** of $\mathbf b$ onto the line in the direction of $\mathbf a$ is the part of $\mathbf b$ parallel to $\mathbf a$:
$$(\hat{\mathbf a}\cdot\mathbf b)\,\hat{\mathbf a}=\frac{\mathbf a\cdot\mathbf b}{|\mathbf a|^2}\,\mathbf a.$$
For $\mathbf b\ne\mathbf 0$ the signed component is $|\mathbf b|\cos\theta$, so the projection is $|\mathbf b|\cos\theta\,\hat{\mathbf a}$. The remaining part $\mathbf b-(\hat{\mathbf a}\cdot\mathbf b)\hat{\mathbf a}$ is orthogonal to $\mathbf a$.

### Cosine rule

With $\theta=\angle BAC$ and $\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$:
$$|\overrightarrow{BC}|^2=(\overrightarrow{AC}-\overrightarrow{AB})\cdot(\overrightarrow{AC}-\overrightarrow{AB})=|\overrightarrow{AC}|^2+|\overrightarrow{AB}|^2-2|\overrightarrow{AB}||\overrightarrow{AC}|\cos\theta.$$
If $\theta=\pi/2$ the last term vanishes: Pythagoras' theorem.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \fill[gray!20] (0,0)--(3.2,0)--(1.25,1.7)--cycle;
  \draw[thick,->] (0,0)--(3.2,0) node[midway,below,blue] {$|\overrightarrow{AB}|$};
  \draw[thick,->] (0,0)--(1.25,1.7) node[midway,above left,blue] {$|\overrightarrow{AC}|$};
  \draw[thick,->] (1.25,1.7)--(3.2,0) node[midway,above right,blue] {$|\overrightarrow{BC}|$};
  \draw (0.45,0) arc (0:53.673:0.45) node[midway,right] {$\theta$};
  \node[below left] at (0,0) {$A$};
  \node[below right] at (3.2,0) {$B$};
  \node[above] at (1.25,1.7) {$C$};
\end{tikzpicture}
\end{document}
```

### Definition — Inner product

Let $V$ be a real vector space. An **inner product** on $V$ is a map $V\times V\to\mathbb R$, written $\langle\mathbf x,\mathbf y\rangle$, such that for all $\mathbf x,\mathbf y,\mathbf z\in V$, $\alpha,\beta\in\mathbb R$:

1. **symmetry:** $\langle\mathbf x,\mathbf y\rangle=\langle\mathbf y,\mathbf x\rangle$;
2. **linearity in the second argument:** $\langle\mathbf x,\alpha\mathbf y+\beta\mathbf z\rangle=\alpha\langle\mathbf x,\mathbf y\rangle+\beta\langle\mathbf x,\mathbf z\rangle$;
3. **positive definiteness:** $\langle\mathbf x,\mathbf x\rangle\ge0$, and $\langle\mathbf x,\mathbf x\rangle=0\iff\mathbf x=\mathbf 0$.

By (1) and (2), inner products are **bilinear**. **Norm:** $\|\mathbf a\|=\sqrt{\mathbf a\cdot\mathbf a}=|\mathbf a|$.

### Theorem — Cauchy-Schwarz inequality

For all $\mathbf x,\mathbf y\in\mathbb R^n$: $|\mathbf x\cdot\mathbf y|\le|\mathbf x||\mathbf y|$.

**Proof.** Assume $\mathbf y\ne\mathbf 0$. For $\lambda\in\mathbb R$,
$$0\le|\mathbf x-\lambda\mathbf y|^2=(\mathbf x-\lambda\mathbf y)\cdot(\mathbf x-\lambda\mathbf y)=|\mathbf y|^2\lambda^2-2(\mathbf x\cdot\mathbf y)\lambda+|\mathbf x|^2.$$
This quadratic in $\lambda$ is never negative, so its discriminant satisfies
$$\big(2\,\mathbf x\cdot\mathbf y\big)^2-4|\mathbf y|^2|\mathbf x|^2\le0,\quad\text{i.e.}\quad(\mathbf x\cdot\mathbf y)^2\le|\mathbf x|^2|\mathbf y|^2.$$
Take non-negative square roots.

It also holds for any inner product on any real vector space: $|\langle\mathbf x,\mathbf y\rangle|\le\|\mathbf x\|\|\mathbf y\|$, with $\|\mathbf x\|=\sqrt{\langle\mathbf x,\mathbf x\rangle}$. **Equality** holds iff $\mathbf x=\lambda\mathbf y$ or $\mathbf y=\lambda\mathbf x$.

### Theorem — Triangle inequality

$|\mathbf x+\mathbf y|\le|\mathbf x|+|\mathbf y|$.

**Proof.**
$$|\mathbf x+\mathbf y|^2=|\mathbf x|^2+|\mathbf y|^2+2\,\mathbf x\cdot\mathbf y\le|\mathbf x|^2+|\mathbf y|^2+2|\mathbf x||\mathbf y|=(|\mathbf x|+|\mathbf y|)^2,$$
using Cauchy–Schwarz.

## 2.3 Orthonormal bases

### Definition — Orthonormal basis

In $\mathbb R^3$, $\mathbf e_1,\mathbf e_2,\mathbf e_3$ are **orthonormal** if each has length $1$ and distinct ones are perpendicular:
$$\mathbf e_i\cdot\mathbf e_j=\delta_{ij}=\begin{cases}1&i=j\\0&i\ne j.\end{cases}$$
This is equivalent to choosing Cartesian axes along these directions. $\{\mathbf e_1,\mathbf e_2,\mathbf e_3\}$ is a **basis** of $\mathbb R^3$: every $\mathbf a\in\mathbb R^3$ has a unique expansion
$$\mathbf a=a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3,\qquad a_i=\mathbf e_i\cdot\mathbf a,$$
written $\mathbf a=(a_1,a_2,a_3)$ or as a column. With $\mathbf b=b_1\mathbf e_1+b_2\mathbf e_2+b_3\mathbf e_3$,
$$\mathbf a\cdot\mathbf b=a_1b_1+a_2b_2+a_3b_3,$$
since the six mixed terms vanish ($\mathbf e_i\cdot\mathbf e_j=0$ for $i\ne j$). Taking $\mathbf a=\mathbf b$: $|\mathbf a|^2=a_1^2+a_2^2+a_3^2$.

The **standard basis** $\mathbf e_1=(1,0,0)$, $\mathbf e_2=(0,1,0)$, $\mathbf e_3=(0,0,1)$ is also written $\hat{\imath},\hat{\jmath},\hat k$.

## 2.4 Vector or cross product

### Definition — Cross product

The **vector product** of $\mathbf a,\mathbf b$ is written $\mathbf a\times\mathbf b$ or $\mathbf a\wedge\mathbf b$:
$$\mathbf a\times\mathbf b=|\mathbf a||\mathbf b|\sin\theta\,\hat{\mathbf n},$$
where $\hat{\mathbf n}$ is the unit vector perpendicular to both $\mathbf a$ and $\mathbf b$ chosen by the **right-hand rule**.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(2.8,1) node[above right] {$\mathbf a$};
  \draw[thick,->] (0,0)--(2.5,-0.95) node[below right] {$\mathbf b$};
  \draw[red,thick,->] (0,0)--(0,2) node[above] {$\mathbf a\times\mathbf b$};
  \draw (19.654:0.8) arc (19.654:-20.807:0.8);
  \node at (1.05,-0.03) {$\theta$};
  \node[below left] at (0,0) {$O$};
\end{tikzpicture}
\end{document}
```

- If $\mathbf a,\mathbf b$ are parallel, or either is $\mathbf 0$, then $\mathbf a\times\mathbf b=\mathbf 0$.
- Going the other way from $\mathbf a$ to $\mathbf b$, through $2\pi-\theta$, gives $\sin(2\pi-\theta)=-\sin\theta$ and $-\hat{\mathbf n}$, so $\mathbf a\times\mathbf b$ is the same.

### Proposition — Properties of the cross product

1. $\mathbf a\times\mathbf b=-\mathbf b\times\mathbf a$; $\mathbf a\times\mathbf a=\mathbf 0$;
2. $\mathbf a\times\mathbf b=\mathbf 0\iff\mathbf a=\lambda\mathbf b$ for some $\lambda\in\mathbb R$, or $\mathbf b=\mathbf 0$;
3. $(\lambda\mathbf a)\times\mathbf b=\lambda(\mathbf a\times\mathbf b)=\mathbf a\times(\lambda\mathbf b)$;
4. $\mathbf a\times(\mathbf b+\mathbf c)=\mathbf a\times\mathbf b+\mathbf a\times\mathbf c$;
5. $\mathbf a\cdot(\mathbf a\times\mathbf b)=\mathbf b\cdot(\mathbf a\times\mathbf b)=0$.

**Vector area.** $\mathbf a\times\mathbf b$ is the vector area of the parallelogram spanned by $\mathbf a,\mathbf b$; its magnitude is the usual area. Base $|\mathbf a|$, height $h=|\mathbf b|\sin\theta$ ($0\le\theta\le\pi$), so area $=|\mathbf a||\mathbf b|\sin\theta=|\mathbf a\times\mathbf b|$. For non-parallel vectors the normal direction records the orientation of the parallelogram; interchanging $\mathbf a,\mathbf b$ reverses it without changing the area. For the triangle $OBA$: $S_{OBA}=\frac12|\overrightarrow{OA}\times\overrightarrow{OB}|$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \begin{scope}
    \clip (0,0)--(2.8,0)--(4.2,1.6)--(1.4,1.6)--cycle;
    \foreach \x in {-0.5,-0.1,...,4.3} \draw[blue] (\x,0)--(\x+0.65,1.6);
  \end{scope}
  \draw[thick,->] (0,0)--(2.8,0) node[below right] {$\mathbf a$};
  \draw[thick,->] (0,0)--(1.4,1.6) node[above] {$\mathbf b$};
  \draw[red,thick,->] (1.4,1.6)--(4.2,1.6) node[midway,above] {$\mathbf a$};
  \draw[red,thick,->] (2.8,0)--(4.2,1.6) node[midway,below right] {$\mathbf b$};
  \draw[orange,thick] (1.4,1.6)--(1.4,0) node[midway,right] {$h$};
  \draw (0.5,0) arc (0:48.814:0.5);
  \node at (0.65,0.25) {$\theta$};
  \node[below left] at (0,0) {$O$};
\end{tikzpicture}
\end{document}
```

**Scaling and rotation.** Fix $\mathbf a\ne\mathbf 0$ and take $\mathbf x$ in the plane perpendicular to $\mathbf a$. The map $\mathbf x\mapsto\mathbf a\times\mathbf x$ takes this plane to itself (since $\mathbf a\times\mathbf x\perp\mathbf a$), with $|\mathbf a\times\mathbf x|=|\mathbf a||\mathbf x|$ and $\mathbf x\cdot(\mathbf a\times\mathbf x)=0$. So for $\mathbf x\ne\mathbf 0$ it scales length by $|\mathbf a|$ and rotates through $\pi/2$ in the right-hand sense about the direction of $\mathbf a$. If $\mathbf a$ is a unit vector it is just a quarter turn.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick] (-1.4,-0.9)--(0.8,-0.9)--(1.8,0.9)--(-0.4,0.9)--cycle;
  \draw[red,thick,->] (0,0)--(0,1.7) node[above] {$\mathbf a$};
  \draw[blue,thick,->] (0,0)--(-0.45,-0.8) node[below] {$\mathbf x$};
  \draw[orange,thick,->] (0,0)--(1.3,0) node[above] {$\mathbf a\times\mathbf x$};
\end{tikzpicture}
\end{document}
```

### Cross product in components

For the standard basis,
$$\mathbf e_1\times\mathbf e_2=\mathbf e_3=-(\mathbf e_2\times\mathbf e_1),\quad\mathbf e_2\times\mathbf e_3=\mathbf e_1=-(\mathbf e_3\times\mathbf e_2),\quad\mathbf e_3\times\mathbf e_1=\mathbf e_2=-(\mathbf e_1\times\mathbf e_3).$$
So for $\mathbf a=(a_1,a_2,a_3)$, $\mathbf b=(b_1,b_2,b_3)$,
$$\mathbf a\times\mathbf b=(a_2b_3-a_3b_2)\mathbf e_1+(a_3b_1-a_1b_3)\mathbf e_2+(a_1b_2-a_2b_1)\mathbf e_3=\begin{vmatrix}\mathbf e_1&\mathbf e_2&\mathbf e_3\\a_1&a_2&a_3\\b_1&b_2&b_3\end{vmatrix}\ \text{(formally)}.$$

## 2.5 Triple products

### Definition — Scalar triple product

For $\mathbf a,\mathbf b,\mathbf c\in\mathbb R^3$: $[\mathbf a,\mathbf b,\mathbf c]=\mathbf a\cdot(\mathbf b\times\mathbf c)$. The order matters; a cyclic permutation does not change it:
$$\mathbf a\cdot(\mathbf b\times\mathbf c)=\mathbf b\cdot(\mathbf c\times\mathbf a)=\mathbf c\cdot(\mathbf a\times\mathbf b)=-\mathbf a\cdot(\mathbf c\times\mathbf b)=-\mathbf b\cdot(\mathbf a\times\mathbf c)=-\mathbf c\cdot(\mathbf b\times\mathbf a).$$
In particular it is zero if two of the vectors are equal. In a right-handed orthonormal basis,
$$[\mathbf a,\mathbf b,\mathbf c]=\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}.$$

**Geometric interpretation.** $\mathbf a\times\mathbf b$ gives the base parallelogram; with $\hat{\mathbf n}=\frac{\mathbf a\times\mathbf b}{|\mathbf a\times\mathbf b|}$ the height is $h=|\hat{\mathbf n}\cdot\mathbf c|$. So
$$V=\text{base area}\times\text{height}=|\mathbf a\times\mathbf b|\left|\mathbf c\cdot\frac{\mathbf a\times\mathbf b}{|\mathbf a\times\mathbf b|}\right|=|\mathbf c\cdot(\mathbf a\times\mathbf b)|.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(2.4,-0.6) node[midway,below] {$\mathbf a$};
  \draw[thick,->] (0,0)--(2.7,1.05) node[midway,below] {$\mathbf b$};
  \draw[red,thick] (2.4,-0.6)--(5.1,0.45)--(2.7,1.05);
  \draw[thick,->] (0,0)--(2,2.3) node[midway,above left] {$\mathbf c$};
  \draw[red,thick,->] (0,0)--(0,2.6) node[above] {$\mathbf a\times\mathbf b$};
  \draw[orange,thick,->] (0,0)--(0,0.7) node[left] {$\hat{\mathbf n}$};
  \draw[blue] (2,2.3)--(2,-0.05) node[midway,right] {$h$};
  \node[below left] at (0,0) {$O$};
  \node[below right] at (2.4,-0.6) {$A$};
  \node[above] at (2,2.3) {$C$};
\end{tikzpicture}
\end{document}
```

So $[\mathbf a,\mathbf b,\mathbf c]$ is the **signed volume** of the parallelepiped spanned by $\mathbf a,\mathbf b,\mathbf c$ (take $|\cdot|$ for the volume):

- $[\mathbf a,\mathbf b,\mathbf c]>0$: $\mathbf c$ has a positive component along $\mathbf a\times\mathbf b$;
- $[\mathbf a,\mathbf b,\mathbf c]<0$: negative component;
- $[\mathbf a,\mathbf b,\mathbf c]=0$ $\iff$ $\mathbf a,\mathbf b,\mathbf c$ are coplanar $\iff$ one is a linear combination of the others.

### Vector triple product

For $\mathbf a,\mathbf b,\mathbf c\in\mathbb R^3$:
$$\mathbf a\times(\mathbf b\times\mathbf c)=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf c.$$
It is **not associative**: $(\mathbf a\times\mathbf b)\times\mathbf c=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf b\cdot\mathbf c)\mathbf a$. Proof: [[#Proof of the vector triple product identity]].

## 2.6 Lines, planes and vector equations

### Lines

A line through $\mathbf a$ with non-zero direction $\mathbf u$ has parametric form $\mathbf r=\mathbf a+\lambda\mathbf u$, $\lambda\in\mathbb R$. Equivalently
$$\mathbf u\times(\mathbf r-\mathbf a)=\mathbf 0,\qquad\text{or}\qquad\mathbf u\times\mathbf r=\mathbf b\ \text{ where }\mathbf b=\mathbf u\times\mathbf a.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[red,thick] (0.2,1.46)--(4,1.65);
  \draw[thick,->] (0,0)--(1,1.5) node[midway,left] {$\mathbf a$};
  \draw[blue,thick,->] (0,0)--(3,1.6) node[midway,below right] {$\mathbf r$};
  \draw[red,thick,->] (1,1.5)--(3,1.6) node[midway,above] {$\lambda\mathbf u$};
  \draw[red,thick,->] (3,1.6)--(3.8,1.64) node[midway,above] {$\mathbf u$};
  \node[below left] at (0,0) {$O$};
  \node[above left] at (1,1.5) {$A$};
\end{tikzpicture}
\end{document}
```

### Planes

A plane through $\mathbf a$ with non-parallel directions $\mathbf u,\mathbf v$: $\mathbf r=\mathbf a+\lambda\mathbf u+\mu\mathbf v$, $\lambda,\mu\in\mathbb R$. A **normal** is $\mathbf n=\mathbf u\times\mathbf v$, and equivalently
$$(\mathbf r-\mathbf a)\cdot\mathbf n=0,\qquad\text{i.e.}\qquad\mathbf n\cdot\mathbf r=k\ \text{ with }k=\mathbf n\cdot\mathbf a.$$
The perpendicular distance from the origin is $|k|/|\mathbf n|$, since $\hat{\mathbf n}\cdot\mathbf r=\frac{\mathbf n\cdot\mathbf r}{|\mathbf n|}=\frac k{|\mathbf n|}$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick] (2.4,-0.6)--(-1.4,-0.6)--(-0.2,1.6)--(2.8,1.6);
  \draw[red,thick,->] (-0.2,-0.95)--(0,0) node[midway,left] {$\mathbf a$};
  \draw[blue,thick,->] (-0.2,-0.95)--(1.6,0.75) node[above right] {$\mathbf r$};
  \draw[thick,->] (0,0)--(0.7,1) node[above] {$\mathbf u$};
  \draw[thick,->] (0,0)--(1.1,0) node[right] {$\mathbf v$};
  \draw[orange,thick,->] (0,0)--(0,1.3) node[above] {$\mathbf n=\mathbf u\times\mathbf v$};
  \node[red,below] at (-0.2,-0.95) {$O$};
  \node[red,left] at (0,0) {$A$};
\end{tikzpicture}
\end{document}
```

Through three non-collinear points $A,B,C$ (position vectors $\mathbf a,\mathbf b,\mathbf c$): take $\mathbf u=\mathbf c-\mathbf a$, $\mathbf v=\mathbf b-\mathbf a$, so
$$(\mathbf r-\mathbf a)\cdot\big[(\mathbf b-\mathbf a)\times(\mathbf c-\mathbf a)\big]=0.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (0,0)--(0.2,1.6) node[midway,left] {$\mathbf a$};
  \draw[thick,->] (0,0)--(1.9,3.1) node[pos=0.35,right] {$\mathbf b$};
  \draw[thick,->] (0,0)--(2.9,1.5) node[midway,below right] {$\mathbf c$};
  \draw[red,thick,->] (0.2,1.6)--(1.9,3.1) node[midway,above left] {$\mathbf v=\mathbf b-\mathbf a$};
  \draw[red,thick,->] (0.2,1.6)--(2.9,1.5) node[midway,above] {$\mathbf u=\mathbf c-\mathbf a$};
  \node[below left] at (0,0) {$O$};
  \node[left] at (0.2,1.6) {$A$};
  \node[above right] at (1.9,3.1) {$B$};
  \node[right] at (2.9,1.5) {$C$};
\end{tikzpicture}
\end{document}
```

### Intersection of a line and a plane

Line $\mathbf u\times\mathbf r=\mathbf u\times\mathbf a$; plane $\mathbf n\cdot\mathbf r=\mathbf n\cdot\mathbf b$. Cross the line equation with $\mathbf n$: $(\mathbf r\times\mathbf u)\times\mathbf n=(\mathbf a\times\mathbf u)\times\mathbf n$. By the vector triple product,
$$(\mathbf n\cdot\mathbf r)\mathbf u-(\mathbf n\cdot\mathbf u)\mathbf r=(\mathbf a\times\mathbf u)\times\mathbf n,$$
and substituting the plane equation, $(\mathbf n\cdot\mathbf b)\mathbf u-(\mathbf u\cdot\mathbf n)\mathbf r=(\mathbf a\times\mathbf u)\times\mathbf n$.

- If $\mathbf u\cdot\mathbf n\ne0$: $\mathbf r=\dfrac{(\mathbf n\cdot\mathbf b)\mathbf u-(\mathbf a\times\mathbf u)\times\mathbf n}{\mathbf u\cdot\mathbf n}$, a unique point.
- If $\mathbf u\cdot\mathbf n=0$ the line is parallel to the plane: if $\mathbf n\cdot\mathbf a=\mathbf n\cdot\mathbf b$ the line lies in the plane; otherwise there is no intersection.

### Shortest distance between two lines

For $\ell_1:\ \mathbf u_1\times(\mathbf r-\mathbf a_1)=\mathbf 0$ and $\ell_2:\ \mathbf u_2\times(\mathbf r-\mathbf a_2)=\mathbf 0$, the shortest distance is attained along a line perpendicular to both:
$$s=\left|(\mathbf a_1-\mathbf a_2)\cdot\frac{\mathbf u_1\times\mathbf u_2}{|\mathbf u_1\times\mathbf u_2|}\right|.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick] (0.1,1.45)--(3.2,2.38) node[right] {$\ell_1$};
  \draw[thick] (0.1,-0.1)--(3.5,-0.1) node[right] {$\ell_2$};
  \draw[green!55!black,thick,->] (0.4,1.54)--(1,1.72) node[midway,above] {$\mathbf u_1$};
  \draw[green!55!black,thick,->] (0.4,-0.1)--(1,-0.1) node[midway,below] {$\mathbf u_2$};
  \draw[red,thick,->] (3,1)--(2.6,2.2) node[midway,right] {$\mathbf a_1$};
  \draw[red,thick,->] (3,1)--(2.7,-0.1) node[midway,right] {$\mathbf a_2$};
  \draw[blue,thick,->] (3,1)--(1.6,1.9) node[midway,above] {$\mathbf p$};
  \draw[blue,thick,->] (3,1)--(1.9,-0.1) node[midway,left] {$\mathbf q$};
  \fill (1.6,1.9) circle (1.2pt) node[above left] {$P$};
  \fill (1.9,-0.1) circle (1.2pt) node[below] {$Q$};
  \node[red,above] at (2.6,2.2) {$A_1$};
  \node[red,below] at (2.7,-0.1) {$A_2$};
  \node[right] at (3,1) {$O$};
\end{tikzpicture}
\end{document}
```

**Proof.** Let $\hat{\mathbf n}$ be the unit vector along $\mathbf u_1\times\mathbf u_2$, and $\mathbf p=\mathbf a_1+\lambda\mathbf u_1\in\ell_1$, $\mathbf q=\mathbf a_2+\mu\mathbf u_2\in\ell_2$. Since $\hat{\mathbf n}\perp\mathbf u_1,\mathbf u_2$: $(\mathbf p-\mathbf q)\cdot\hat{\mathbf n}=(\mathbf a_1-\mathbf a_2)\cdot\hat{\mathbf n}$. By Cauchy–Schwarz,
$$|(\mathbf a_1-\mathbf a_2)\cdot\hat{\mathbf n}|\le|\mathbf p-\mathbf q|\qquad\forall\,\mathbf p\in\ell_1,\ \mathbf q\in\ell_2.$$
The lower bound is attained: write $\mathbf a_1-\mathbf a_2=\alpha\mathbf u_1+\beta\mathbf u_2+\gamma\hat{\mathbf n}$ with $\gamma=(\mathbf a_1-\mathbf a_2)\cdot\hat{\mathbf n}$. Then $\mathbf p-\mathbf q=(\alpha+\lambda)\mathbf u_1+(\beta-\mu)\mathbf u_2+\gamma\hat{\mathbf n}$; choosing $\lambda=-\alpha$, $\mu=\beta$ gives $\mathbf p-\mathbf q=\gamma\hat{\mathbf n}$ and $|\mathbf p-\mathbf q|=|\gamma|=s$.

### Vector equations

**Solve $\mathbf r+\mathbf a\times(\mathbf b\times\mathbf r)=\mathbf c$.** Expand the triple product:
$$\mathbf r+(\mathbf a\cdot\mathbf r)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf r=\mathbf c.\tag{$*$}$$
Dot with $\mathbf a$: $\mathbf a\cdot\mathbf r+(\mathbf a\cdot\mathbf r)(\mathbf a\cdot\mathbf b)-(\mathbf a\cdot\mathbf b)(\mathbf a\cdot\mathbf r)=\mathbf a\cdot\mathbf c$, so $\mathbf a\cdot\mathbf r=\mathbf a\cdot\mathbf c$. Substituting into $(*)$:
$$(1-\mathbf a\cdot\mathbf b)\,\mathbf r=\mathbf c-(\mathbf a\cdot\mathbf c)\mathbf b.$$

- If $\mathbf a\cdot\mathbf b\ne1$: $\mathbf r=\dfrac{\mathbf c-(\mathbf a\cdot\mathbf c)\mathbf b}{1-\mathbf a\cdot\mathbf b}$, a unique solution.
- If $\mathbf a\cdot\mathbf b=1$ and $\mathbf c-(\mathbf a\cdot\mathbf c)\mathbf b\ne\mathbf 0$: then $\mathbf 0=(1-\mathbf a\cdot\mathbf b)\mathbf r=\mathbf c-(\mathbf a\cdot\mathbf c)\mathbf b\ne\mathbf 0$, a contradiction — no solution.
- If $\mathbf a\cdot\mathbf b=1$ and $\mathbf c=(\mathbf a\cdot\mathbf c)\mathbf b$: $(*)$ reduces to $(\mathbf a\cdot\mathbf r-\mathbf a\cdot\mathbf c)\mathbf b=\mathbf 0$, so the solutions are the plane $\mathbf a\cdot\mathbf r=\mathbf a\cdot\mathbf c$.

## 2.7 Index notation and summation convention

Take a right-handed orthonormal basis $\{\mathbf e_1,\mathbf e_2,\mathbf e_3\}$, with indices $i,j,k$ ranging over $1,2,3$.

### Definition — Kronecker delta and Levi-Civita symbol

$$\delta_{ij}=\begin{cases}1&i=j\\0&i\ne j\end{cases},\qquad\varepsilon_{ijk}=\begin{cases}1&(i,j,k)\text{ an even permutation of }(1,2,3)\\-1&(i,j,k)\text{ an odd permutation of }(1,2,3)\\0&\text{otherwise.}\end{cases}$$

- $\mathbf e_i\cdot\mathbf e_j=\delta_{ij}$, and $\delta$ is **symmetric**: $\delta_{ij}=\delta_{ji}$. Hence $\mathbf a\cdot\mathbf b=\sum_{i,j}\delta_{ij}a_ib_j=\sum_ia_ib_i$.
- $\varepsilon_{123}=\varepsilon_{231}=\varepsilon_{312}=1$, $\varepsilon_{132}=\varepsilon_{213}=\varepsilon_{321}=-1$.
- $\varepsilon$ is **antisymmetric**: interchanging any two indices changes its sign; if two indices coincide it is $0$ (e.g. $\varepsilon_{112}=0$).
- $\mathbf e_i\times\mathbf e_j=\sum_k\varepsilon_{ijk}\mathbf e_k$ (e.g. $\mathbf e_1\times\mathbf e_2=\mathbf e_3$, $\mathbf e_2\times\mathbf e_1=-\mathbf e_3$), so $\mathbf a\times\mathbf b=\sum_{i,j,k}\varepsilon_{ijk}a_ib_j\mathbf e_k$.

### Einstein summation convention

A repeated index is summed:

- $a_i\delta_{ij}\ \big(=\sum_ia_i\delta_{ij}\big)=a_j$;
- $\mathbf a\cdot\mathbf b=\delta_{ij}a_ib_j=a_jb_j$;
- $(\mathbf a\times\mathbf b)_i=\varepsilon_{ijk}a_jb_k$.

**Examples.** $\mathbf a\cdot(\mathbf b\times\mathbf c)=\varepsilon_{ijk}a_ib_jc_k$; $\delta_{ii}=\delta_{11}+\delta_{22}+\delta_{33}=3$.

**Rules.**
- An index appearing once in a term is a **free** index.
- An index appearing twice in a term is a **contracted** (dummy) index — we sum over it.
- No index may appear more than twice in a term.

See [[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]] for practice.

### Proposition — Epsilon identities

$$\varepsilon_{ijk}\varepsilon_{pqr}=\begin{vmatrix}\delta_{ip}&\delta_{iq}&\delta_{ir}\\\delta_{jp}&\delta_{jq}&\delta_{jr}\\\delta_{kp}&\delta_{kq}&\delta_{kr}\end{vmatrix}=\delta_{ip}\delta_{jq}\delta_{kr}-\delta_{ip}\delta_{jr}\delta_{kq}+\delta_{iq}\delta_{jr}\delta_{kp}-\delta_{iq}\delta_{jp}\delta_{kr}+\delta_{ir}\delta_{jp}\delta_{kq}-\delta_{ir}\delta_{jq}\delta_{kp},$$
and contracting indices:
$$\varepsilon_{ijk}\varepsilon_{pqk}=\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp},\qquad\varepsilon_{ijk}\varepsilon_{pjk}=2\delta_{ip},\qquad\varepsilon_{ijk}\varepsilon_{ijk}=6.$$

### Proof of the vector triple product identity

$\mathbf a\times(\mathbf b\times\mathbf c)=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf c$.

**Proof.**
$$\begin{aligned}
[\mathbf a\times(\mathbf b\times\mathbf c)]_i&=\varepsilon_{ijk}a_j(\mathbf b\times\mathbf c)_k=\varepsilon_{ijk}\varepsilon_{kpq}a_jb_pc_q\\
&=(\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp})a_jb_pc_q&&(\varepsilon_{kpq}=\varepsilon_{pqk})\\
&=a_jb_ic_j-a_jb_jc_i=(\mathbf a\cdot\mathbf c)b_i-(\mathbf a\cdot\mathbf b)c_i.
\end{aligned}$$

### Lagrange's identity

$$(\mathbf a\times\mathbf b)\cdot(\mathbf b\times\mathbf c)=(\mathbf a\cdot\mathbf b)(\mathbf b\cdot\mathbf c)-(\mathbf a\cdot\mathbf c)|\mathbf b|^2.$$

**Proof.**
$$\begin{aligned}
(\mathbf a\times\mathbf b)\cdot(\mathbf b\times\mathbf c)&=\varepsilon_{ijk}a_jb_k\,\varepsilon_{ipq}b_pc_q=\varepsilon_{jki}\varepsilon_{pqi}\,a_jb_kb_pc_q\\
&=(\delta_{jp}\delta_{kq}-\delta_{jq}\delta_{kp})a_jb_kb_pc_q=a_jb_jb_kc_k-a_jc_jb_kb_k\\
&=(\mathbf a\cdot\mathbf b)(\mathbf b\cdot\mathbf c)-(\mathbf a\cdot\mathbf c)|\mathbf b|^2.
\end{aligned}$$

### Signed area in two dimensions

In $\mathbb R^2$ let $\varepsilon_{12}=1$, $\varepsilon_{21}=-1$, $\varepsilon_{11}=\varepsilon_{22}=0$. The scalar
$$[\mathbf a,\mathbf b]=\varepsilon_{ij}a_ib_j=a_1b_2-a_2b_1$$
is the **signed area** of the parallelogram generated by $\mathbf a,\mathbf b$: $[\mathbf a,\mathbf b]>0$ if turning from $\mathbf a$ to $\mathbf b$ is counterclockwise, $<0$ if clockwise.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \foreach \s/\l/\r/\sgn/\turn in {0/a/b/{$+$ Area}/counterclockwise, 5.5/b/a/{$-$ Area}/clockwise} {
    \begin{scope}[shift={(\s,0)}]
      \fill[gray!25] (0,0)--(2.2,0)--(2.8,1.4)--(0.6,1.4)--cycle;
      \draw (0,0)--(2.2,0)--(2.8,1.4)--(0.6,1.4)--cycle;
      \draw[blue,thick,->] (0,0)--(2.2,0) node[midway,below] {$\mathbf{\l}$};
      \draw[red,thick,->] (0,0)--(0.6,1.4) node[midway,left] {$\mathbf{\r}$};
      \node[right] at (3,1) {\sgn};
      \node at (1.4,-0.8) {\turn};
    \end{scope}
  }
  \draw[->] (0.5,0) arc (0:60:0.5);
  \draw[->] (5.75,0.433) arc (60:0:0.5);
\end{tikzpicture}
\end{document}
```
*Left: $[\mathbf a,\mathbf b]>0$ ($\mathbf b$ counterclockwise from $\mathbf a$). Right: $[\mathbf a,\mathbf b]<0$ ($\mathbf b$ clockwise from $\mathbf a$).*

**Remark.** If $\mathbf a,\mathbf b$ are linearly dependent then $[\mathbf a,\mathbf b]=0$ — they are collinear.

### Spherical trigonometry

Fix the unit sphere and points $A,B,C$ on it (position vectors $\mathbf a,\mathbf b,\mathbf c$) forming a non-degenerate spherical triangle. Let $\delta(A,B)=\angle AOB$; then $\mathbf a\cdot\mathbf b=\cos\delta(A,B)$ and $|\mathbf a\times\mathbf b|=\sin\delta(A,B)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.3]
  \draw (0,0) circle (1.5);
  \draw[dashed] (-1.5,0) arc (180:360:1.5 and 0.35);
  \draw[dashed] (1.5,0) arc (0:180:1.5 and 0.35);
  \coordinate (A) at (0,1.1); \coordinate (B) at (-0.95,-0.3); \coordinate (C) at (0.9,-0.35);
  \draw[thick] (A) to[bend right=15] (B) to[bend right=20] (C) to[bend right=15] (A);
  \foreach \P/\l in {A/a,B/b,C/c} \draw[blue,dashed,->] (0,0)--(\P) node[pos=0.55,right] {$\mathbf \l$};
  \node[red,above] at (A) {$A$}; \node[red,below left] at (B) {$B$}; \node[red,below right] at (C) {$C$};
  \node[red] at (-0.15,0.85) {$\alpha$};
  \node[below] at (0,0) {$O$};
\end{tikzpicture}
\end{document}
```
*Schematic: spherical triangle $ABC$ with angle $\alpha$ at $A$.*

The angle $\alpha$ at $A$ is the angle between the planes $OAB$ and $OAC$, so
$$\cos\alpha=\frac{(\mathbf a\times\mathbf b)\cdot(\mathbf a\times\mathbf c)}{|\mathbf a\times\mathbf b||\mathbf a\times\mathbf c|}.$$
By Lagrange's identity, $(\mathbf a\times\mathbf b)\cdot(\mathbf a\times\mathbf c)=|\mathbf a|^2(\mathbf b\cdot\mathbf c)-(\mathbf a\cdot\mathbf b)(\mathbf a\cdot\mathbf c)=\cos\delta(B,C)-\cos\delta(A,B)\cos\delta(A,C)$. Hence the **spherical cosine rule**
$$\cos\alpha=\frac{\cos\delta(B,C)-\cos\delta(A,B)\cos\delta(A,C)}{\sin\delta(A,B)\sin\delta(A,C)}.$$

> [!note] Explanation
> Here Lagrange's identity is used in the form $(\mathbf a\times\mathbf b)\cdot(\mathbf a\times\mathbf c)=(\mathbf a\cdot\mathbf a)(\mathbf b\cdot\mathbf c)-(\mathbf a\cdot\mathbf c)(\mathbf b\cdot\mathbf a)$, proved by the same contraction as above; $|\mathbf a|=1$ on the unit sphere.

### Spheres and balls

A sphere in $\mathbb R^3$ with centre $\mathbf 0$ and radius $r>0$ is $\{\mathbf x\in\mathbb R^3:|\mathbf x|=r\}$. In $\mathbb R^n$ the **hypersphere** with centre $\mathbf a$ and radius $r$ is
$$\{\mathbf x\in\mathbb R^n:\ |\mathbf x-\mathbf a|=r\},\qquad\text{i.e.}\qquad(x_1-a_1)^2+\dots+(x_n-a_n)^2=r^2.$$
$|\mathbf x-\mathbf a|\le r$ is the **closed ball**, $|\mathbf x-\mathbf a|<r$ the **open ball**.

## 2.8 Vector spaces over the real and complex numbers

**Coordinate spaces.** $\mathbb R^n=\{\mathbf x=(x_1,\dots,x_n):x_i\in\mathbb R\}$ with componentwise addition $\mathbf x+\mathbf y=(x_1+y_1,\dots,x_n+y_n)$ and $\lambda\mathbf x=(\lambda x_1,\dots,\lambda x_n)$, $\lambda\in\mathbb R$. Likewise $\mathbb C^n=\{\mathbf z=(z_1,\dots,z_n):z_i\in\mathbb C\}$ with scalars $\lambda\in\mathbb C$.

### Definition — Vector space over a field

For a field $\mathbb F$, a **vector space over $\mathbb F$** is a set $V$ with vector addition and multiplication by scalars in $\mathbb F$, satisfying the axioms seen before. Here $\mathbb F=\mathbb R$ or $\mathbb F=\mathbb C$.

**Examples.**
- $\mathbb C$ is a complex vector space (each $z$ is a scalar multiple of $1$) and also a real vector space (each $z=x+iy$ with $x,y$ real).
- Vectors need not be tuples of numbers: $V=\{f:[0,1]\to\mathbb R:\ f\text{ smooth},\ f(0)=f(1)=0\}$.

## 2.9 Subspaces, linear independence and bases

**Linear combination and span.** For $\mathbf v_1,\dots,\mathbf v_r\in V$, a **linear combination** is $\sum_{i=1}^r\lambda_i\mathbf v_i$ with $\lambda_i\in\mathbb F$; the **span** is the set of all of them,
$$\operatorname{span}\{\mathbf v_1,\dots,\mathbf v_r\}=\Big\{\sum_{i=1}^r\lambda_i\mathbf v_i:\ \lambda_i\in\mathbb F\Big\}.$$
The vectors **span** $V$ if this set equals $V$.

### Definition — Subspace

A non-empty subset $U\subseteq V$ is a **subspace** if $\lambda\mathbf u+\mu\mathbf w\in U$ whenever $\mathbf u,\mathbf w\in U$ and $\lambda,\mu\in\mathbb F$. Every span is a subspace. The trivial subspaces of $V$ are $V$ and $\{\mathbf 0\}$.

**Examples.**
- For $\mathbf 0\ne\mathbf u\in\mathbb R^3$, $\operatorname{span}\{\mathbf u\}=\{\lambda\mathbf u\}$ is a subspace of $\mathbb R^3$.
- For $\mathbf u,\mathbf v\in\mathbb R^3$ with $\mathbf u\nparallel\mathbf v$, $\operatorname{span}\{\mathbf u,\mathbf v\}$ is a plane and a subspace of $\mathbb R^3$.
- A line or plane not through the origin is not a subspace.
- $\mathbf v_1=(1,0,-2)$, $\mathbf v_2=(1,1,-3)$, $\mathbf v_3=(2,1,1)$: $\mathbf v_1,\mathbf v_2\perp\mathbf v_3$. Their combinations $\lambda\mathbf v_1+\mu\mathbf v_2=(\lambda+\mu,\ \mu,\ -2\lambda-3\mu)=(x,y,z)$ satisfy $2x+y+z=0$ (i.e. $\mathbf v_3\cdot\mathbf r=0$). But $P=\{\mathbf r\in\mathbb R^3:\mathbf v_3\cdot\mathbf r=4\}$ is not a subspace (it does not contain $\mathbf 0$).

### Definition — Linear independence

$\mathbf v_1,\dots,\mathbf v_n$ are **linearly independent** if $\lambda_1\mathbf v_1+\dots+\lambda_n\mathbf v_n=\mathbf 0$ implies $\lambda_i=0$ for all $i$. Otherwise they are **linearly dependent**: if $\lambda_j\ne0$ then
$$\mathbf v_j=-\sum_{i\ne j}\frac{\lambda_i}{\lambda_j}\mathbf v_i,$$
so at least one vector is a linear combination of the others.

**Example.** $\mathbf u=(1,0)$, $\mathbf v_2=(0,1)$, $\mathbf v_3=(0,2)$: $\mathbf v_3=2\mathbf v_2$, so the set is linearly dependent — yet $\mathbf u\ne\lambda\mathbf v_2+\mu\mathbf v_3$ for all $\lambda,\mu$. (Dependence means *some* vector is a combination of the others, not every one.)

Any set containing $\mathbf 0$ is linearly dependent.
