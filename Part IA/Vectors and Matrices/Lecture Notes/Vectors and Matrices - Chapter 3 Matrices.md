---
title: Vectors and Matrices - Chapter 3 Matrices
course: Part IA Vectors and Matrices
material_type: lecture notes
chapter: 3
source_file: Ch.3 Matrices.pdf
drive_file_id: 1iIWxXJono_3nn6eHinzhBzxxu_rR9iYA
source_url: https://drive.google.com/file/d/1iIWxXJono_3nn6eHinzhBzxxu_rR9iYA/view
source_pages: 25
tags: [lecture, vectors-and-matrices]
---

# Vectors and Matrices — Chapter 3: Matrices

> [!abstract] Overview
> Linear maps between vector spaces, their image and kernel, the rank–nullity theorem, how a choice of bases represents a linear map by a matrix, the standard geometric maps (rotations, reflections, dilations, shears) as matrices, matrix algebra (products, inverses, transpose, adjoint, trace), orthogonal and unitary matrices, and determinants: 2D and 3D, permutations and their sign, alternating forms, and the general (Leibniz) formula with its properties. Throughout, the scalar field $\mathbb F$ is $\mathbb R$ or $\mathbb C$.
> Prerequisite: [[Vectors and Matrices - Chapter 2 Vectors]] (bases, dimension).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Linear map]] | $T(\lambda\mathbf x+\mu\mathbf y)=\lambda T\mathbf x+\mu T\mathbf y$ | 1 |
| [[#Definition — Image, kernel, rank and nullity]] | $\operatorname{Im}T$, $\ker T$; injective $\iff\ker T=\{\mathbf 0\}$ | 1 |
| [[#Theorem — Rank-nullity theorem]] | $\operatorname{rank}T+\operatorname{null}T=\dim V$ | 2 |
| [[#Basic examples]] | zero map, identity, $(x_1,x_2)\mapsto x_1\mathbf v_1+x_2\mathbf v_2$ | 3 |
| [[#Linear combinations and composition]] | $\alpha T+\beta S$, $S\circ T$ linear; $\dim\mathcal L(V,W)=\dim V\dim W$ | 3 |
| [[#Definition — Matrix of a linear map]] | $T(\mathbf e_j)=\sum_iM_{ij}\mathbf f_i$; $[T\mathbf x]_C=M[\mathbf x]_B$ | 4–5 |
| [[#Rotations in the plane]] | $R(\theta)$; $R(\theta_1)R(\theta_2)=R(\theta_1+\theta_2)$ | 5 |
| [[#Reflections in the plane]] | $H(\theta)$; $H(\theta)^2=I$, $R(\varphi)H(\theta)=H(\theta+\varphi/2)$, $H(\theta_1)H(\theta_2)=R(2(\theta_1-\theta_2))$ | 6 |
| [[#Rotations in space and Rodrigues' formula]] | $R_z(\theta)$; $R(\theta,\mathbf n)\mathbf x=\cos\theta\,\mathbf x+(1-\cos\theta)(\mathbf n\cdot\mathbf x)\mathbf n+\sin\theta\,\mathbf n\times\mathbf x$ | 7 |
| [[#Reflections, dilations and shears in space]] | $H=I-2\mathbf n\mathbf n^{\mathsf T}$; dilation; shear | 8 |
| [[#Definition — Matrix addition and scalar multiplication]] | $\operatorname{Mat}_{m\times n}(\mathbb F)$ is a vector space | 9–10 |
| [[#Definition — Matrix product]] | $(MN)_{ij}=\sum_kM_{ik}N_{kj}=R_i(M)\cdot C_j(N)$; associative, distributive | 10–11 |
| [[#Definition — Identity matrix]] | $I_n=(\delta_{ij})$; $MI_n=I_mM=M$ | 11 |
| [[#Definition — Left, right and two-sided inverses]] | $NM=I_n$, $ML=I_m$; $(MN)^{-1}=N^{-1}M^{-1}$ | 12–13 |
| [[#Definition — Transpose]] | $(M^{\mathsf T})_{ij}=M_{ji}$; $(MN)^{\mathsf T}=N^{\mathsf T}M^{\mathsf T}$ | 13 |
| [[#Definition — Complex conjugate and adjoint]] | $M^\dagger=\overline M^{\mathsf T}$; $(MN)^\dagger=N^\dagger M^\dagger$ | 14 |
| [[#Definition — Symmetric and antisymmetric matrices]] | $M=\frac12(M+M^{\mathsf T})+\frac12(M-M^{\mathsf T})$ | 14 |
| [[#Definition — Hermitian and anti-Hermitian matrices]] | $M=\frac12(M+M^\dagger)+\frac12(M-M^\dagger)$ | 14 |
| [[#Antisymmetric matrices in 3D]] | $A_{ij}=\varepsilon_{ijk}a_k$, $A\mathbf x=\mathbf x\times\mathbf a$ | 15 |
| [[#Definition — Trace]] | $\operatorname{tr}M=\sum_iM_{ii}$; linear, cyclic | 15–16 |
| [[#Separating the trace]] | $M=S_0+\frac{\operatorname{tr}M}nI_n+A$ | 16 |
| [[#Definition — Orthogonal and unitary matrices]] | $Q^{\mathsf T}Q=I$, $U^\dagger U=I$; preserve inner products | 16–17 |
| [[#Proposition — Orthogonal matrices in 2D]] | every real $2\times2$ orthogonal matrix is $R(\theta)$ or $H(\theta/2)$ | 17–18 |
| [[#Definition — Determinant in 2D]] | $\det M=ad-bc$; $M^{-1}=\frac1{\det M}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ | 19 |
| [[#Definition — Determinant in 3D]] | $\det(\mathbf a,\mathbf b,\mathbf c)=\mathbf a\cdot(\mathbf b\times\mathbf c)$; Sarrus' rule | 19 |
| [[#Definition — Permutation and sign]] | $S_n$, $\operatorname{sgn}(p)=(-1)^{N(p)}$ | 20 |
| [[#Disjoint cycle decomposition]] | cycles; $\operatorname{sgn}(p)=(-1)^{n-c}$; $\operatorname{sgn}(p\sigma)=\operatorname{sgn}p\operatorname{sgn}\sigma$ | 20–21 |
| [[#Definition — Alternating symbol]] | $\varepsilon_{i_1\cdots i_n}$ generalises $\varepsilon_{ijk}$ | 21 |
| [[#Definition — Alternating n-linear form]] | unique $w$ with $w(\mathbf e_1,\dots,\mathbf e_n)=1$; $[\mathbf v_1,\dots,\mathbf v_n]=\det(\mathbf v_1\cdots\mathbf v_n)$ | 21–22 |
| [[#Proposition — Alternating forms and linear independence]] | $[\mathbf v_1,\dots,\mathbf v_n]\ne0\iff$ independent | 22–24 |
| [[#Leibniz's formula]] | $\det M=\sum_{p\in S_n}\operatorname{sgn}(p)\prod_iM_{ip(i)}$ | 24 |
| [[#Properties of the determinant]] | multilinear, alternating, $\det(\lambda M)=\lambda^n\det M$, $\det M^{\mathsf T}=\det M$, $\det(MN)=\det M\det N$ | 24–25 |

## 3.1 Linear maps

Let $V,W$ be vector spaces over the same field $\mathbb F$.

### Definition — Linear map

A map $T:V\to W$ is **linear** if
$$T(\lambda\mathbf x+\mu\mathbf y)=\lambda T(\mathbf x)+\mu T(\mathbf y)\qquad\text{for all }\mathbf x,\mathbf y\in V,\ \lambda,\mu\in\mathbb F.$$
In particular $T(\mathbf 0)=\mathbf 0$.

### Definition — Image, kernel, rank and nullity

For a linear map $T:V\to W$, the **image** and **kernel** are
$$\operatorname{Im}T:=\{T(\mathbf x):\mathbf x\in V\}\subseteq W,\qquad\ker T:=\{\mathbf x\in V:T(\mathbf x)=\mathbf 0\}\subseteq V.$$
Both are vector subspaces. The **rank** and **nullity** are
$$\operatorname{rank}T:=\dim(\operatorname{Im}T),\qquad\operatorname{null}T:=\dim(\ker T).$$
A linear map is **injective** iff $\ker T=\{\mathbf 0\}$, and **surjective** iff $\operatorname{Im}T=W$. It is an **isomorphism** when it is both injective and surjective.

### Theorem — Rank-nullity theorem

If $T:V\to W$ is linear and $\dim V=n$, then $\operatorname{rank}T+\operatorname{null}T=n$.

**Proof.** Let $\{\mathbf e_1,\dots,\mathbf e_k\}$ be a basis of $\ker T$ and extend it to a basis $\{\mathbf e_1,\dots,\mathbf e_k,\mathbf e_{k+1},\dots,\mathbf e_n\}$ of $V$.

*The images span $\operatorname{Im}T$.* If $\mathbf x=\sum_{j=1}^nx_j\mathbf e_j$, then, because $T(\mathbf e_j)=\mathbf 0$ for $j\le k$,
$$T(\mathbf x)=\sum_{j=k+1}^nx_jT(\mathbf e_j).$$
So $\{T(\mathbf e_{k+1}),\dots,T(\mathbf e_n)\}$ spans $\operatorname{Im}T$.

*They are linearly independent.* Suppose
$$\sum_{j=k+1}^n\alpha_jT(\mathbf e_j)=\mathbf 0.$$
Then $\sum_{j=k+1}^n\alpha_j\mathbf e_j$ lies in $\ker T$, so there are $\beta_1,\dots,\beta_k$ with
$$\sum_{j=k+1}^n\alpha_j\mathbf e_j=\sum_{j=1}^k\beta_j\mathbf e_j\iff\sum_{j=1}^k(-\beta_j)\mathbf e_j+\sum_{j=k+1}^n\alpha_j\mathbf e_j=\mathbf 0.$$
This is a linear combination of a basis of $V$, so all coefficients vanish; in particular $\alpha_j=0$ for $j=k+1,\dots,n$.

Hence $\{T(\mathbf e_{k+1}),\dots,T(\mathbf e_n)\}$ is a basis of $\operatorname{Im}T$, so $\operatorname{rank}T=n-k$ and $\operatorname{null}T=k$.

### Basic examples

1. The **zero map** $T(\mathbf x):=\mathbf 0$ has $\operatorname{Im}T=\{\mathbf 0\}$ and $\ker T=V$.
2. The **identity map** $I_V(\mathbf x):=\mathbf x$ has $\operatorname{Im}I_V=V$ and $\ker I_V=\{\mathbf 0\}$.
3. For fixed $\mathbf v_1,\mathbf v_2\in V$, the map $T:\mathbb F^2\to V$, $T(x_1,x_2):=x_1\mathbf v_1+x_2\mathbf v_2$ is linear. Its image is $\operatorname{span}\{\mathbf v_1,\mathbf v_2\}$, and its kernel records the linear relations between them.

### Linear combinations and composition

If $S,T:V\to W$ are linear and $\alpha,\beta\in\mathbb F$, then
$$(\alpha T+\beta S)(\mathbf x):=\alpha T(\mathbf x)+\beta S(\mathbf x)$$
is linear. If $T:V\to W$ and $S:W\to U$ are linear, their **composition**
$$S\circ T:V\to U,\qquad(S\circ T)(\mathbf x):=S(T(\mathbf x))$$
is linear. The vector space of linear maps from $V$ to $W$ is denoted $\mathcal L(V,W)$. If $V$ and $W$ are finite-dimensional, then
$$\dim\mathcal L(V,W)=(\dim V)(\dim W).$$

## 3.2 Matrices as linear maps

### Definition — Matrix of a linear map

Choose ordered bases $B=(\mathbf e_1,\dots,\mathbf e_n)$ of $V$ and $C=(\mathbf f_1,\dots,\mathbf f_m)$ of $W$. For a linear map $T:V\to W$, write
$$T(\mathbf e_j)=\sum_{i=1}^mM_{ij}\mathbf f_i.$$
The numbers $M_{ij}$ form the $m\times n$ **matrix** of $T$ in these bases,
$$[T]_{C\leftarrow B}=M:=\begin{pmatrix}M_{11}&\cdots&M_{1j}&\cdots&M_{1n}\\\vdots&&\vdots&&\vdots\\M_{m1}&\cdots&M_{mj}&\cdots&M_{mn}\end{pmatrix}.$$
The $j$th column is the **coordinate vector** of $T(\mathbf e_j)$ relative to $C$.

For $\mathbf x=\sum_jx_j\mathbf e_j$, write $[\mathbf x]_B=(x_1,\dots,x_n)^{\mathsf T}$. Then
$$\begin{aligned}
T(\mathbf x)&=T\Big(\sum_jx_j\mathbf e_j\Big)\\
&=\sum_jx_jT(\mathbf e_j)\\
&=\sum_i\Big(\sum_jM_{ij}x_j\Big)\mathbf f_i,
\end{aligned}\qquad\text{i.e.}\qquad[T(\mathbf x)]_C=M[\mathbf x]_B.$$
Thus every linear map is represented by a matrix once bases are chosen, and every matrix defines a linear map between coordinate spaces. When working in $\mathbb F^n$ and $\mathbb F^m$ with their standard bases, we identify vectors with their coordinate columns and write $T(\mathbf x)=M\mathbf x$. The image, kernel and rank of a matrix refer to those of its associated linear map.

### Rotations in the plane

A counterclockwise rotation about the origin through angle $\theta$ is given by
$$R(\theta):=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.$$


```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.1]
  \draw[->] (-0.2,0) -- (3.2,0) node[right] {$x_1$};
  \draw[->] (0,-0.2) -- (0,3) node[above] {$x_2$};
  \draw[blue,thick,->] (0,0) -- (22:2.4) node[right] {$\mathbf x$};
  \draw[red,thick,->] (0,0) -- (22+40:2.4) node[above] {$R(\theta)\mathbf x$};
  \draw[black,->] (0,0) -- (1,0); \draw[black,->] (0,0) -- (0,1);
  \draw[black,dashed,->] (0,0) -- (40:1) node[right] {$R(\theta)\mathbf e_1$};
  \draw[black,dashed,->] (0,0) -- (130:1) node[left] {$R(\theta)\mathbf e_2$};
  \draw[green!50!black] (22:1.5) arc (22:62:1.5);
  \node[green!50!black] at (42:1.8) {$\theta$};
\end{tikzpicture}
\end{document}
```
*Rotation $R(	heta)$ turns $\mathbf x$ and the basis vectors $\mathbf e_1,\mathbf e_2$ counterclockwise through $\theta$ without changing lengths.*

Take $\mathbf e_1=(1,0)^{\mathsf T}$, $\mathbf e_2=(0,1)^{\mathsf T}$. After $R(\theta)$ their lengths are still $1$:
$$R(\theta)\mathbf e_1=\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix},\qquad R(\theta)\mathbf e_2=\begin{pmatrix}\cos(\theta+\frac\pi2)\\\sin(\theta+\frac\pi2)\end{pmatrix}=\begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix},$$
and these are the columns of $R(\theta)$.

For angles $\theta_1,\theta_2$:
1. $R(\theta_1)R(\theta_2)=R(\theta_1+\theta_2)$;
2. $R(\theta)^{-1}=R(-\theta)$;
3. $R(\theta)R(\theta)=R(2\theta)=\begin{pmatrix}\cos2\theta&-\sin2\theta\\\sin2\theta&\cos2\theta\end{pmatrix}$.

### Reflections in the plane

A reflection in the line through the origin making angle $\theta$ with the positive $x_1$-axis is
$$H(\theta)=\begin{pmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{pmatrix}.$$
Indeed
$$H(\theta)\mathbf e_1=\begin{pmatrix}\cos2\theta\\\sin2\theta\end{pmatrix},\qquad H(\theta)\mathbf e_2=\begin{pmatrix}\cos(2\theta-\frac\pi2)\\\sin(2\theta-\frac\pi2)\end{pmatrix}=\begin{pmatrix}\sin2\theta\\-\cos2\theta\end{pmatrix},$$
which are the columns of $H(\theta)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.1]
  \draw[->] (-0.3,0) -- (3.4,0) node[right] {$x_1$};
  \draw[->] (0,-1.6) -- (0,3.2) node[above] {$x_2$};
  \draw[green!50!black,thick] (-30:0.0) -- (30:3.3) node[right] {$\ell$};
  \draw[green!50!black] (0.9,0) arc (0:30:0.9); \node[green!50!black] at (15:1.2) {$\theta$};
  \draw[blue,thick,->] (0,0) -- (70:2.4) node[above] {$\mathbf x$};
  \draw[red,thick,->] (0,0) -- (-10:2.4) node[right] {$H(\theta)\mathbf x$};
  \draw[dashed,gray] (70:2.4) -- (-10:2.4);
  \draw[black,->] (0,0) -- (1.1,0) node[below] {$\mathbf e_1$};
  \draw[black,->] (0,0) -- (0,1.1) node[left] {$\mathbf e_2$};
  \draw[black,dashed,->] (0,0) -- (60:1.1) node[above right] {$H(\theta)\mathbf e_1$};
  \draw[black,dashed,->] (0,0) -- (-30:1.1) node[below] {$H(\theta)\mathbf e_2$};
\end{tikzpicture}
\end{document}
```
*Reflection $H(\theta)$ in the line $\ell$ at angle $\theta$ to the $x_1$-axis; $H(\theta)\mathbf e_1$ is at angle $2\theta$.*

1. $H(\theta)^2=I$.
2. For $R(\varphi)$: $R(\varphi)H(\theta)=H\big(\theta+\frac\varphi2\big)$.
3. For $\theta_1,\theta_2$: $H(\theta_1)H(\theta_2)=R\big(2(\theta_1-\theta_2)\big)$.

For (2): reflecting $\mathbf x$ in the line $\ell$ at angle $\theta$ and then rotating through $\varphi$ is the same as reflecting in the line $\ell'$ at angle $\theta+\frac\varphi2$. For (3): the composite of reflections in two lines at angles $\theta_1,\theta_2$ is a rotation through twice the angle between them.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.05]
  \draw[->] (-0.3,0) -- (3.4,0) node[right] {$x_1$};
  \draw[->] (0,-1.4) -- (0,3.2) node[above] {$x_2$};
  \draw[green!50!black,thick] (0,0) -- (25:3.2) node[right] {$\ell$};
  \draw[orange,thick] (0,0) -- (45:3.2) node[right] {$\ell'$};
  \draw[blue,thick,->] (0,0) -- (75:2.4) node[above] {$\mathbf x$};
  \draw[blue,thick,->] (0,0) -- (-25:2.4) node[right] {$H(\theta)\mathbf x$};
  \draw[red,thick,->] (0,0) -- (15:2.4) node[right] {$R(\varphi)H(\theta)\mathbf x$};
  \draw[red] (-25:1.0) arc (-25:15:1.0); \node[red] at (-5:1.3) {$\varphi$};
\end{tikzpicture}
\end{document}
```
*(2) Reflect in $\ell$ (angle $\theta$), then rotate through $\varphi$: the result is the reflection in $\ell'$ at angle $\theta+\varphi/2$.*

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.0]
  \draw[->] (-0.3,0) -- (3.4,0) node[right] {$x_1$};
  \draw[->] (0,-2) -- (0,3.2) node[above] {$x_2$};
  \draw[green!50!black,thick] (0,0) -- (20:3.2) node[right] {$\ell_1$};
  \draw[orange,thick] (0,0) -- (60:3.2) node[right] {$\ell_2$};
  \draw[blue,thick,->] (0,0) -- (40:2.4) node[right] {$\mathbf x$};
  \draw[blue,dashed,->] (0,0) -- (80:2.4) node[above] {$H(\theta_2)\mathbf x$};
  \draw[red,thick,->] (0,0) -- (-40:2.4) node[right] {$H(\theta_1)H(\theta_2)\mathbf x$};
\end{tikzpicture}
\end{document}
```
*(3) $H(\theta_1)H(\theta_2)\mathbf x$ is $\mathbf x$ rotated through $2(\theta_1-\theta_2)$ (here $\theta_1=20^\circ$, $\theta_2=60^\circ$, a rotation through $-80^\circ$).*

### Rotations in space and Rodrigues' formula

Rotation through angle $\theta$ about the $x_3$-axis:
$$R_z(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}.$$
More generally, rotation about the line in the direction of the unit vector $\mathbf n$ is given by **Rodrigues' formula**
$$R(\theta,\mathbf n)\mathbf x:=\cos\theta\,\mathbf x+(1-\cos\theta)(\mathbf n\cdot\mathbf x)\mathbf n+\sin\theta\,\mathbf n\times\mathbf x.$$

**Derivation.** Split $\mathbf x=\mathbf x_\perp+\mathbf x_\parallel$ with
$$\mathbf x_\parallel=(\mathbf n\cdot\mathbf x)\mathbf n,\qquad\mathbf x_\perp=\mathbf x-\mathbf x_\parallel=\mathbf x-(\mathbf n\cdot\mathbf x)\mathbf n.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.2]
  \draw[gray] (0,0) ellipse (2.1 and 0.8);
  \draw[green!50!black,thick,->] (0,0) -- (0,2.3) node[above] {$\mathbf n$};
  \draw[red,thick,->] (0,0) -- (1.5,-0.45) node[below right] {$\mathbf x_\perp$};
  \draw[blue,thick,->] (0,0) -- (0.9,0.25) node[right] {$\mathbf n\times\mathbf x_\perp$};
  \draw[orange,thick,->] (0,0) -- (0,1.2) node[left] {$\mathbf x_\parallel$};
  \draw[black,thick,->] (0,0) -- (1.5,0.95) node[above right] {$\mathbf x$};
  \draw[dashed] (1.5,-0.45) -- (1.5,0.95) -- (0,1.2);
\end{tikzpicture}
\end{document}
```
*Schematic: $\mathbf x=\mathbf x_\parallel+\mathbf x_\perp$, with $\mathbf x_\parallel$ along $\mathbf n$; $\mathbf x_\perp$ and $\mathbf n\times\mathbf x_\perp$ span the plane (ellipse) perpendicular to $\mathbf n$.*

- $\mathbf n\cdot\mathbf x_\perp=\mathbf n\cdot\mathbf x-(\mathbf n\cdot\mathbf x)|\mathbf n|^2=0$.
- If $\mathbf x_\perp\ne\mathbf 0$, then $\mathbf n\times\mathbf x_\perp$ is perpendicular to both $\mathbf n$ and $\mathbf x_\perp$.
- The rotation acts in the plane spanned by $\mathbf x_\perp$ and $\mathbf n\times\mathbf x_\perp$:
$$R(\theta,\mathbf n)\mathbf x_\perp=\cos\theta\,\mathbf x_\perp+\sin\theta\,(\mathbf n\times\mathbf x_\perp).$$
- $\mathbf n\times\mathbf x_\parallel=\mathbf 0$, so $\mathbf n\times\mathbf x=\mathbf n\times\mathbf x_\perp$.

Therefore
$$\begin{aligned}
R(\theta,\mathbf n)\mathbf x&=R(\theta,\mathbf n)(\mathbf x_\parallel+\mathbf x_\perp)\\
&=\mathbf x_\parallel+R(\theta,\mathbf n)\mathbf x_\perp\\
&=\mathbf x_\parallel+\cos\theta\,\mathbf x_\perp+\sin\theta\,(\mathbf n\times\mathbf x_\perp)\\
&=(\mathbf n\cdot\mathbf x)\mathbf n+\cos\theta\,\big(\mathbf x-(\mathbf n\cdot\mathbf x)\mathbf n\big)+\sin\theta\,(\mathbf n\times\mathbf x)\\
&=\cos\theta\,\mathbf x+(1-\cos\theta)(\mathbf n\cdot\mathbf x)\mathbf n+\sin\theta\,(\mathbf n\times\mathbf x).
\end{aligned}$$

### Reflections, dilations and shears in space

**Reflections.** Reflection in the plane through the origin with unit normal $\mathbf n$ sends
$$\mathbf x'=\mathbf x-2(\mathbf n\cdot\mathbf x)\mathbf n,\qquad\text{i.e.}\qquad H:=I-2\mathbf n\mathbf n^{\mathsf T}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.1]
  \draw[gray] (-2.4,-0.5) -- (0.2,0.7) -- (2.6,0.7) -- (0.0,-0.5) -- cycle;
  \draw[black,thick,->] (0,0.1) -- (0,2.2) node[above] {$\mathbf n$};
  \draw[blue,thick,->] (0,0.1) -- (-0.8,1.5) node[left] {$\mathbf x$};
  \draw[red,thick,->] (0,0.1) -- (0,1.5) node[right] {$(\mathbf n\cdot\mathbf x)\mathbf n$};
  \draw[blue,dashed,->] (0,0.1) -- (-0.8,-1.3) node[below left] {$H\mathbf x$};
  \draw[dotted] (0,-1.5) -- (0,0.1);
\end{tikzpicture}
\end{document}
```
*Reflection in a plane with unit normal $\mathbf n$: the component of $\mathbf x$ along $\mathbf n$ is reversed.*

**Dilations.** Dilation along the $x_1$-axis by a factor $\lambda>0$:
$$\begin{pmatrix}x_1'\\x_2'\\x_3'\end{pmatrix}=\begin{pmatrix}\lambda&0&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,x={(1.5cm,0cm)},y={(0.7cm,0.5cm)},z={(0cm,1.5cm)}]
  \draw[->] (0,0,0) -- (4.6,0,0) node[right] {$x_1$};
  \draw[->] (0,0,0) -- (0,3.4,0) node[below right] {$x_2$};
  \draw[->] (0,0,0) -- (0,0,2.2) node[above] {$x_3$};

  % original unit cube (grey)
  \draw[gray] (0,0,0) -- (1,0,0) -- (1,0,1) -- (0,0,1) -- cycle;
  \draw[gray] (0,1,1) -- (1,1,1) -- (1,1,0);
  \draw[gray] (0,0,1) -- (0,1,1); \draw[gray] (1,0,1) -- (1,1,1); \draw[gray] (1,0,0) -- (1,1,0);
  \draw[gray,dashed] (0,1,0) -- (1,1,0); \draw[gray,dashed] (0,1,0) -- (0,1,1); \draw[gray,dashed] (0,0,0) -- (0,1,0);
  % dilated box, factor 2 along x_1 (red)
  \draw[red,thick] (0,0,0) -- (2.2,0,0) -- (2.2,0,1) -- (0,0,1) -- cycle;
  \draw[red,thick] (0,1,1) -- (2.2,1,1) -- (2.2,1,0);
  \draw[red,thick] (0,0,1) -- (0,1,1); \draw[red,thick] (2.2,0,1) -- (2.2,1,1); \draw[red,thick] (2.2,0,0) -- (2.2,1,0);
  \draw[red,dashed] (0,1,0) -- (2.2,1,0); \draw[red,dashed] (0,1,0) -- (0,1,1); \draw[red,dashed] (0,0,0) -- (0,1,0);
  \draw[red,->] (1.1,0,1.55) -- (2.2,0,1.55) node[midway,above] {$\lambda>1$};
\end{tikzpicture}
\end{document}
```
*Dilation along the $x_1$-axis by a factor $\lambda$: the unit cube (grey) becomes a box stretched along $x_1$ (red), unchanged in $x_2,x_3$.*

**Shears.** Shear parallel to the $x_1$-axis:
$$x_1'=x_1+\alpha x_2,\qquad x_2'=x_2,\qquad x_3'=x_3,$$
with matrix
$$S=\begin{pmatrix}1&\alpha&0\\0&1&0\\0&0&1\end{pmatrix},\qquad\alpha\in\mathbb R.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,x={(1.5cm,0cm)},y={(0.7cm,0.5cm)},z={(0cm,1.5cm)}]
  \draw[->] (0,0,0) -- (4.6,0,0) node[right] {$x_1$};
  \draw[->] (0,0,0) -- (0,3.4,0) node[below right] {$x_2$};
  \draw[->] (0,0,0) -- (0,0,2.2) node[above] {$x_3$};

  % original unit cube (grey)
  \draw[gray] (0,0,0) -- (1,0,0) -- (1,0,1) -- (0,0,1) -- cycle;
  \draw[gray] (0,1,1) -- (1,1,1) -- (1,1,0);
  \draw[gray] (0,0,1) -- (0,1,1); \draw[gray] (1,0,1) -- (1,1,1); \draw[gray] (1,0,0) -- (1,1,0);
  \draw[gray,dashed] (0,1,0) -- (1,1,0); \draw[gray,dashed] (0,1,0) -- (0,1,1); \draw[gray,dashed] (0,0,0) -- (0,1,0);
  % sheared cube (red): x_1' = x_1 + alpha x_2, alpha = 1
  \draw[red,thick] (0,0,0) -- (1,0,0) -- (1,0,1) -- (0,0,1) -- cycle;
  \draw[red,thick] (1,1,1) -- (2,1,1) -- (2,1,0);
  \draw[red,thick] (1,1,1) -- (1,1,0);
  \draw[red,thick] (0,0,1) -- (1,1,1); \draw[red,thick] (1,0,1) -- (2,1,1); \draw[red,thick] (1,0,0) -- (2,1,0);
  \draw[red,dashed] (1,1,0) -- (2,1,0); \draw[red,dashed] (0,0,0) -- (1,1,0);
  \draw[red,->] (1,1,1.55) -- (2,1,1.55) node[midway,above] {$\alpha x_2$};
\end{tikzpicture}
\end{document}
```
*Shear parallel to the $x_1$-axis, $x_1'=x_1+\alpha x_2$ (here $\alpha=1$): the face $x_2=0$ stays fixed while the face $x_2=1$ slides by $\alpha$ along $x_1$; the unit cube (grey) becomes a slanted box (red).*

## 3.3 Matrices in general

**Recap.** Let $V,W$ be vector spaces over $\mathbb F$ with bases $\{\mathbf e_i\}$ and $\{\mathbf f_j\}$ respectively. Then
- $V$ is identified with $\mathbb F^n$ ($\mathbb R^n$ or $\mathbb C^n$);
- $W$ is identified with $\mathbb F^m$;
- a linear map $T:V\to W$ is identified with an $m\times n$ matrix $M$.

### 3.3.1 Definitions and operations

An $m\times n$ **matrix** over $\mathbb F$ is a rectangular array
$$M=(M_{ij})=\begin{pmatrix}M_{11}&\cdots&M_{1n}\\\vdots&&\vdots\\M_{m1}&\cdots&M_{mn}\end{pmatrix}$$
with all entries in $\mathbb F$, $m$ rows and $n$ columns. $\operatorname{Mat}_{m\times n}(\mathbb F)$ denotes the vector space of $m\times n$ matrices with entries in $\mathbb F$.

### Definition — Matrix addition and scalar multiplication

- **Addition:** for $M,N\in\operatorname{Mat}_{m\times n}(\mathbb F)$, $M+N\in\operatorname{Mat}_{m\times n}(\mathbb F)$ with
$$(M+N)_{ij}=M_{ij}+N_{ij}.$$
- **Multiplication by scalars:** for $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$ and $\lambda\in\mathbb F$, $\lambda M\in\operatorname{Mat}_{m\times n}(\mathbb F)$ with
$$(\lambda M)_{ij}:=\lambda M_{ij}.$$

### Definition — Matrix product

For $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$ and $N\in\operatorname{Mat}_{n\times p}(\mathbb F)$, the **matrix product** $MN\in\operatorname{Mat}_{m\times p}(\mathbb F)$ is
$$(MN)_{ij}:=\sum_{k=1}^nM_{ik}N_{kj}=M_{i1}N_{1j}+M_{i2}N_{2j}+\dots+M_{in}N_{nj}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  % MN
  \draw (0,1.2) .. controls (-0.25,0.6) and (-0.25,-0.6) .. (0,-1.2);
  \draw (2.4,1.2) .. controls (2.65,0.6) and (2.65,-0.6) .. (2.4,-1.2);
  \node[red] at (-0.35,0) {$i$};
  \draw[red,->] (0.2,0) -- (1.0,0);
  \draw (1.1,-0.15) rectangle (1.7,0.15);
  \draw[->] (1.4,1.0) -- (1.4,0.2);
  \node[red] at (1.4,1.25) {$j$};
  \node[below] at (1.4,-0.2) {\small$(MN)_{ij}$};
  \node[red] at (1.2,1.7) {$MN$};
  \node at (3.0,0) {$=$};
  % M
  \draw (4.1,1.2) .. controls (3.85,0.6) and (3.85,-0.6) .. (4.1,-1.2);
  \draw (6.5,1.2) .. controls (6.75,0.6) and (6.75,-0.6) .. (6.5,-1.2);
  \node[red] at (3.75,0) {$i$};
  \draw[->] (4.2,0) -- (6.4,0);
  \node[red] at (5.3,1.7) {$M$};
  % N
  \draw (7.1,1.2) .. controls (6.85,0.6) and (6.85,-0.6) .. (7.1,-1.2);
  \draw (8.7,1.2) .. controls (8.95,0.6) and (8.95,-0.6) .. (8.7,-1.2);
  \draw[->] (7.9,1.1) -- (7.9,-1.1);
  \node[red] at (7.9,1.45) {$j$};
  \node[red] at (7.9,1.85) {$N$};
\end{tikzpicture}
\end{document}
```
*Entry $(i,j)$ of $MN$ comes from row $i$ of $M$ and column $j$ of $N$.*

Writing $R_i(M)$ for the $i$-th row of $M$ and $C_j(N)$ for the $j$-th column of $N$,
$$(MN)_{ij}=R_i(M)\cdot C_j(N),$$
the dot product of a row and a column in $\mathbb F^n$.

**Properties.**
- Associativity: $(MN)P=M(NP)$ for $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$, $N\in\operatorname{Mat}_{n\times p}(\mathbb F)$, $P\in\operatorname{Mat}_{p\times q}(\mathbb F)$.
- Distributivity: $M(N+P)=MN+MP$ for $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$, $N,P\in\operatorname{Mat}_{n\times p}(\mathbb F)$; and $(M+N)P=MP+NP$ for $M,N\in\operatorname{Mat}_{m\times n}(\mathbb F)$, $P\in\operatorname{Mat}_{n\times p}(\mathbb F)$.

**Recap — composition.** If $S:U\to V$ and $T:V\to W$ have matrices $N$ and $M$ respectively, where

| | $U$ | $V$ | $W$ |
| --- | --- | --- | --- |
| dimension | $p$ | $n$ | $m$ |
| basis | $\{\mathbf u_r\}$ | $\{\mathbf e_i\}$ | $\{\mathbf f_j\}$ |

then $T\circ S$ has matrix $MN$.

### Definition — Identity matrix

The **identity matrix** is
$$I_n:=(\delta_{ij})_{1\le i,j\le n}=\underbrace{\begin{pmatrix}1&0&\cdots&0\\0&1&&\vdots\\\vdots&&\ddots&\\0&\cdots&&1\end{pmatrix}}_{n\text{ columns}}\quad(n\text{ rows}).$$
For $M\in\operatorname{Mat}_{n\times n}(\mathbb F)$, $MI_n=I_nM=M$; for $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$, $MI_n=I_mM=M$.

### 3.3.2 Matrix inverses

### Definition — Left, right and two-sided inverses

Consider $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$ and $N,L\in\operatorname{Mat}_{n\times m}(\mathbb F)$.
- $N$ is a **left inverse** for $M$ if $NM=I_n$.
- $L$ is a **right inverse** for $M$ if $ML=I_m$.

If $m=n$ and both exist, then $N=L=M^{-1}$, with
$$MM^{-1}=M^{-1}M=I_n.$$

> [!note] Explanation
> $N=NI_n=N(ML)=(NM)L=I_nL=L$. The same argument shows the inverse is unique: any two inverses of $M$ are equal.

**Remark.** Not every matrix has an inverse. If $M$ has an inverse, it is called **invertible** or **non-singular**.
- The inverse is unique.
- For $M,N$ invertible of the same size:
$$(MN)^{-1}=N^{-1}M^{-1},\qquad(M^{-1})^{-1}=M,\qquad(M^k)^{-1}=(M^{-1})^k\ \ (k\in\mathbb N).$$
- An invertible matrix represents an isomorphism: trivial kernel (injective) and full rank (surjective).

**Examples.**
1. Rotation $R(\theta)$ about $\mathbf n$: $R(\theta)^{-1}=R(-\theta)$.
2. Shear $S(\lambda)$: $S(\lambda)^{-1}=S(-\lambda)$.
3. Reflection $H$: $H^{-1}=H$.

### 3.3.3 Transpose, conjugate and adjoint

### Definition — Transpose

For $M\in\operatorname{Mat}_{m\times n}(\mathbb F)$, the **transpose** $M^{\mathsf T}\in\operatorname{Mat}_{n\times m}(\mathbb F)$ is
$$(M^{\mathsf T})_{ij}:=M_{ji}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  % M^T
  \draw (0,1) .. controls (-0.2,0.5) and (-0.2,-0.5) .. (0,-1);
  \draw (2.2,1) .. controls (2.4,0.5) and (2.4,-0.5) .. (2.2,-1);
  \node at (1.1,0) {$\cdots\,M^{\mathsf T}_{ij}\,\cdots$};
  \draw[dotted] (1.1,0.25) -- (1.1,0.85); \draw[dotted] (1.1,-0.25) -- (1.1,-0.85);
  \draw[->] (-0.75,0) node[left] {$i$} -- (-0.25,0);
  \draw[->] (1.1,1.55) node[above] {$j$} -- (1.1,1.05);
  \node[red] at (1.6,1.4) {$M^{\mathsf T}$};
  \node at (2.9,0) {$=$};
  % M
  \draw (3.6,1) .. controls (3.4,0.5) and (3.4,-0.5) .. (3.6,-1);
  \draw (5.8,1) .. controls (6.0,0.5) and (6.0,-0.5) .. (5.8,-1);
  \node at (4.7,0) {$\cdots\,M_{ji}\,\cdots$};
  \draw[dotted] (4.7,0.25) -- (4.7,0.85); \draw[dotted] (4.7,-0.25) -- (4.7,-0.85);
  \draw[->] (6.55,0) node[right] {$j$} -- (6.05,0);
  \draw[->] (4.7,1.55) node[above] {$i$} -- (4.7,1.05);
  \node[red] at (5.2,1.4) {$M$};
\end{tikzpicture}
\end{document}
```
*Row $i$, column $j$ of $M^{\mathsf T}$ is row $j$, column $i$ of $M$.*

**Properties.**
$$(M^{\mathsf T})^{\mathsf T}=M,\qquad(MN)^{\mathsf T}=N^{\mathsf T}M^{\mathsf T},\qquad(\alpha M+\beta N)^{\mathsf T}=\alpha M^{\mathsf T}+\beta N^{\mathsf T}.$$

### Definition — Complex conjugate and adjoint

For complex matrices, **entrywise conjugation** is $(\overline M)_{ij}:=\overline{M_{ij}}$.

The **adjoint**, or **conjugate transpose**, is
$$M^\dagger:=\overline M^{\mathsf T}\qquad(\text{also written }M^*).$$
**Properties.** $(MN)^\dagger=N^\dagger M^\dagger$ and $(M^\dagger)^\dagger=M$.

### Definition — Symmetric and antisymmetric matrices

A real square matrix $M$ is **symmetric** if $M^{\mathsf T}=M$, and **antisymmetric** if $M^{\mathsf T}=-M$.

Every real square matrix has a unique decomposition
$$M=S+A,\qquad S=\tfrac12(M+M^{\mathsf T})\ \text{(symmetric)},\qquad A=\tfrac12(M-M^{\mathsf T})\ \text{(antisymmetric)}.$$

### Definition — Hermitian and anti-Hermitian matrices

A complex square matrix $M$ is **Hermitian** if $M^\dagger=M$, and **anti-Hermitian** if $M^\dagger=-M$.

$M$ has a unique decomposition
$$M=H+K,\qquad H=\tfrac12(M+M^\dagger)\ \text{(Hermitian)},\qquad K=\tfrac12(M-M^\dagger)\ \text{(anti-Hermitian)}.$$

### Antisymmetric matrices in 3D

**Examples.** For $\mathbf a=(a_1,a_2,a_3)^{\mathsf T}$, let
$$A=\begin{pmatrix}0&a_3&-a_2\\-a_3&0&a_1\\a_2&-a_1&0\end{pmatrix}.$$
Equivalently,
$$A_{ij}=\sum_{k=1}^3\varepsilon_{ijk}a_k,\qquad a_i=\frac12\sum_{j,k=1}^3\varepsilon_{ijk}A_{jk},$$
and
$$A\mathbf x=\mathbf x\times\mathbf a.$$

> [!note] Explanation
> $(A\mathbf x)_i=\sum_jA_{ij}x_j=\sum_{j,k}\varepsilon_{ijk}x_ja_k=(\mathbf x\times\mathbf a)_i$. For the inverse formula, $\sum_{j,k}\varepsilon_{ijk}A_{jk}=\sum_{j,k,l}\varepsilon_{ijk}\varepsilon_{jkl}a_l=2a_i$, since $\sum_{j,k}\varepsilon_{ijk}\varepsilon_{ljk}=2\delta_{il}$. So every antisymmetric $3\times3$ matrix is "cross product with a fixed vector".

### 3.3.4 Trace

### Definition — Trace

For a square matrix $M$, the **trace** is
$$\operatorname{tr}M:=\sum_iM_{ii}\qquad(\text{also written }\operatorname{tr}[M]),$$
the sum of the diagonal entries $M_{11},\dots,M_{nn}$.

**Properties.**
- Trace is linear: $\operatorname{tr}(\alpha M+\beta N)=\alpha\operatorname{tr}(M)+\beta\operatorname{tr}(N)$.
- $\operatorname{tr}I_n=n$.
- Cyclic: $\operatorname{tr}(MN)=\operatorname{tr}(NM)$; this holds for $M$ of size $m\times n$ and $N$ of size $n\times m$. More generally
$$\operatorname{tr}(M_1M_2\cdots M_k)=\operatorname{tr}(M_2\cdots M_kM_1)=\operatorname{tr}(M_3\cdots M_kM_1M_2)=\cdots.$$
- $\operatorname{tr}(M^{\mathsf T})=\operatorname{tr}(M)$.

### Separating the trace

An antisymmetric $A$ has zero diagonal, so $\operatorname{tr}A=0$. For a real $n\times n$ matrix $M=S+A$ (symmetric plus antisymmetric),
$$\operatorname{tr}M=\operatorname{tr}(S+A)=\operatorname{tr}S+\operatorname{tr}A=\operatorname{tr}S.$$
Write
$$S_0=S-\frac{\operatorname{tr}M}nI_n.$$
- $S_0$ is symmetric.
- $S_0$ is **traceless**:
$$\operatorname{tr}S_0=\operatorname{tr}\Big(S-\frac{\operatorname{tr}M}nI_n\Big)=\operatorname{tr}S-\frac{\operatorname{tr}M}n\operatorname{tr}I_n=\operatorname{tr}M-\operatorname{tr}M=0.$$

So $S=S_0+\frac{\operatorname{tr}M}nI_n$, and
$$M=\underbrace{S_0}_{\text{symmetric, traceless}}+\underbrace{\frac{\operatorname{tr}M}nI_n}_{\text{multiple of }I_n}+\underbrace{A}_{\text{antisymmetric (traceless)}}.$$

### 3.3.5 Orthogonal and unitary matrices

### Definition — Orthogonal and unitary matrices

A real square matrix $Q$ is **orthogonal** if
$$Q^{\mathsf T}Q=QQ^{\mathsf T}=I,\qquad\text{so}\qquad Q^{\mathsf T}=Q^{-1}.$$
A complex square matrix $U$ is **unitary** if
$$U^\dagger U=UU^\dagger=I,\qquad\text{so}\qquad U^\dagger=U^{-1}.$$

**Properties.**
- They preserve the standard inner product (and the induced norm): for all $\mathbf x,\mathbf y\in\mathbb C^n$,
$$\langle U\mathbf x,U\mathbf y\rangle=\langle\mathbf x,\mathbf y\rangle,\qquad\|U\mathbf x\|=\|\mathbf x\|.$$
- Equivalently, their columns (and rows) form an orthonormal basis.
- **Example:** rotations and reflections are orthogonal transformations.
- **Converse.** Suppose $\langle U\mathbf x,U\mathbf y\rangle=\langle\mathbf x,\mathbf y\rangle$ for all $\mathbf x,\mathbf y\in\mathbb C^n$. Since $\langle U\mathbf x,U\mathbf y\rangle=\mathbf x^\dagger U^\dagger U\mathbf y$ and $\langle\mathbf x,\mathbf y\rangle=\mathbf x^\dagger\mathbf y$,
$$\begin{aligned}
&\mathbf x^\dagger U^\dagger U\mathbf y=\mathbf x^\dagger\mathbf y\ \text{ for all }\mathbf x,\mathbf y\\
\iff\ &U^\dagger U=I &&(\text{choose }\mathbf x=\mathbf e_i,\ \mathbf y=\mathbf e_j\text{ for all }i,j)\\
\iff\ &UU^\dagger=I.
\end{aligned}$$

### Proposition — Orthogonal matrices in 2D

Every real $2\times2$ orthogonal matrix is either a **rotation** about the origin or a **reflection** in a line through the origin.

**Proof.** Let $Q=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ be orthogonal. Then
$$Q^{\mathsf T}Q=I\iff\begin{pmatrix}a&c\\b&d\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}a^2+c^2&ab+cd\\ab+cd&b^2+d^2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}.$$
Write $\mathbf C_1=(a,c)^{\mathsf T}$ and $\mathbf C_2=(b,d)^{\mathsf T}$ for the columns, so $\|\mathbf C_1\|=\|\mathbf C_2\|=1$ and $\mathbf C_1\cdot\mathbf C_2=0$.
- $a^2+c^2=1$: $\mathbf C_1$ lies on the unit circle, so $a=\cos\theta$, $c=\sin\theta$, i.e. $\mathbf C_1=\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}$.
- $\mathbf C_2=\begin{pmatrix}b\\d\end{pmatrix}$ with $b^2+d^2=1$ and $ab+cd=0$, so
$$\mathbf C_2=(-\sin\theta,\cos\theta)^{\mathsf T}\qquad\text{or}\qquad\mathbf C_2=(\sin\theta,-\cos\theta)^{\mathsf T}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.6]
  \draw[thick] (0,0) circle (1);
  \draw[dotted] (0,0) -- (1.15,0);
  \draw[blue,thick,->] (0,0) -- (35:1) node[above right] {$(\cos\theta,\sin\theta)$};
  \node[blue] at (35:0.55) [above left] {$\mathbf C_1$};
  \draw[red,thick,->] (0,0) -- (125:1) node[above left] {$(-\sin\theta,\cos\theta)$};
  \draw[red,thick,->] (0,0) -- (-55:1) node[below right] {$(\sin\theta,-\cos\theta)$};
  \node[red] at (125:0.5) [left] {$\mathbf C_2$};
  \draw (0.3,0) arc (0:35:0.3); \node at (17:0.42) {$\theta$};
\end{tikzpicture}
\end{document}
```
*$\mathbf C_1$ is a unit vector at angle $\theta$; $\mathbf C_2$ is a unit vector perpendicular to it, and there are exactly two choices.*

Hence
$$Q=R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}\qquad\text{or}\qquad Q=H\Big(\frac\theta2\Big)=\begin{pmatrix}\cos\theta&\sin\theta\\\sin\theta&-\cos\theta\end{pmatrix}.\qquad\square$$

## 3.4 Determinants

### 3.4.1 2D

### Definition — Determinant in 2D

For $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, the **determinant** is
$$\det M=ad-bc.$$
For real entries it is the signed area (of the parallelogram spanned by the columns).
- $M$ is invertible if and only if $\det M\ne0$, and then
$$M^{-1}=\frac1{\det M}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$
(Check: $MM^{-1}=M^{-1}M=I$.)

### 3.4.2 3D

### Definition — Determinant in 3D

For $\mathbf a,\mathbf b,\mathbf c\in\mathbb R^3$,
$$\det(\mathbf a,\mathbf b,\mathbf c)=\mathbf a\cdot(\mathbf b\times\mathbf c)=\varepsilon_{ijk}a_ib_jc_k.$$
For $M=(M_{ij})_{1\le i,j\le3}$,
$$\begin{aligned}
\det M={}&M_{11}M_{22}M_{33}+M_{12}M_{23}M_{31}+M_{13}M_{21}M_{32}\\
&-M_{13}M_{22}M_{31}-M_{12}M_{21}M_{33}-M_{11}M_{23}M_{32}.
\end{aligned}$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1]
  \foreach \r in {1,2,3} {
    \foreach \c in {1,2,3} {\node (m\r\c) at (1.2*\c,-0.75*\r) {$M_{\r\c}$};}
    \node[gray] (m\r4) at (4.8,-0.75*\r) {$M_{\r1}$};
    \node[gray] (m\r5) at (6.0,-0.75*\r) {$M_{\r2}$};
  }
  \draw[thick] (0.75,-0.35) -- (0.6,-0.35) -- (0.6,-2.6) -- (0.75,-2.6);
  \draw[thick] (4.15,-0.35) -- (4.3,-0.35) -- (4.3,-2.6) -- (4.15,-2.6);
  \foreach \c in {1,2,3} {
    \pgfmathtruncatemacro{\b}{\c+1}\pgfmathtruncatemacro{\d}{\c+2}
    \draw[green!60!black,thick,opacity=0.7,shorten <=9pt,shorten >=9pt] (m1\c.center) -- (m3\d.center);
    \draw[red,thick,opacity=0.7,shorten <=9pt,shorten >=9pt] (m3\c.center) -- (m1\d.center);
  }
\end{tikzpicture}
\end{document}
```
*Sarrus' rule: repeat the first two columns (grey). The three green down-right diagonals give the $+$ terms, the three red up-right diagonals the $-$ terms.*

### 3.4.3 Permutations and alternating forms

### Definition — Permutation and sign

- A **permutation** $p$ of $\{1,\dots,n\}$ is a bijection of the set to itself.
- The **symmetric group** $S_n$ is the group of all permutations of $n$ elements (under composition). There are $n!$ permutations of $n$ elements.
- The **sign** of $p$ is
$$\operatorname{sgn}(p)=(-1)^{N(p)},$$
with $N(p)$ the number of **inversions**: pairs $i<j$ such that $p(i)>p(j)$.
- **Even** permutations have sign $+1$; **odd** permutations have sign $-1$.

### Disjoint cycle decomposition

The **cycle** $(a_1,\dots,a_n)$ sends $a_1$ to $a_2$, $a_2$ to $a_3$, and so on, with $a_n$ sent to $a_1$.
- Denote by $c$ the number of disjoint cycles of $p$ (if $k$ is mapped to itself, a fixed point, it is a cycle of length $1$). Let $\ell_1,\ell_2,\dots,\ell_c$ be the lengths of all the cycles; then $\ell_1+\ell_2+\dots+\ell_c=n$.
- A cycle of length $k$ is a product of $k-1$ transpositions:
$$(a_1,\dots,a_k)=(a_1,a_k)(a_1,a_{k-1})\cdots(a_1,a_2).$$
- Each transposition reverses the sign, so
$$\operatorname{sgn}(p)=\prod_{r=1}^c(-1)^{\ell_r-1}=(-1)^{n-c}.$$
- The cycle lengths determine the parity of the inversion count:
$$N(p)\equiv\sum_{r=1}^c(\ell_r-1)=n-c\pmod2.$$

**Example.** $p=(1\,3)(2)$, i.e. $(1,2,3)\mapsto(3,2,1)$. Then $N(p)=3$, while $n=3$, $c=2$, $n-c=1$; both are odd.

- $\operatorname{sgn}(p\sigma)=\operatorname{sgn}(p)\operatorname{sgn}(\sigma)$.
- $\operatorname{sgn}(p^{-1})=\operatorname{sgn}(p)$.

### Definition — Alternating symbol

In dimension $n$, the **alternating symbol** generalises $\varepsilon_{ijk}$ ($n=3$):
$$\varepsilon_{i_1\cdots i_n}=\begin{cases}\operatorname{sgn}(p)&\text{if }(i_1,\dots,i_n)=(p(1),\dots,p(n))\text{ for some }p\in S_n,\\0&\text{if two indices coincide.}\end{cases}$$
**Example.** $\varepsilon_{123}=1$, $\varepsilon_{213}=-1$. Interchanging any two indices changes the sign.

### Definition — Alternating n-linear form

- An **$n$-linear form** is a scalar-valued map $w:V^n\to\mathbb F$ that is linear in each argument separately.
- It is **alternating** if it changes sign when two arguments are interchanged.
- In an $n$-dimensional space with basis $\{\mathbf e_1,\dots,\mathbf e_n\}$, there is a **unique** alternating $n$-linear form $w$ with $w(\mathbf e_1,\dots,\mathbf e_n)=1$.

For vectors $\mathbf v_1,\dots,\mathbf v_n$ write
$$[\mathbf v_1,\dots,\mathbf v_n]:=w(\mathbf v_1,\dots,\mathbf v_n)=\sum_{i_1,\dots,i_n=1}^n\varepsilon_{i_1\cdots i_n}(\mathbf v_1)_{i_1}\cdots(\mathbf v_n)_{i_n}=\det\big(\mathbf v_1\ \cdots\ \mathbf v_n\big).$$
- Linear in each argument: $[\dots,\alpha\mathbf u+\beta\mathbf w,\dots]=\alpha[\dots,\mathbf u,\dots]+\beta[\dots,\mathbf w,\dots]$.
- $[\mathbf v_{p(1)},\dots,\mathbf v_{p(n)}]=\operatorname{sgn}(p)[\mathbf v_1,\dots,\mathbf v_n]$.
- $[\mathbf e_1,\dots,\mathbf e_n]=1$ determines the form.

More generally, if $\mathbf v_j=\sum_{i=1}^nV_{ij}\mathbf e_i$ and $M:=(V_{ij})$ is the matrix with the $\mathbf v_j$ as columns, then
$$w(\mathbf v_1,\dots,\mathbf v_n)=(\det M)\,w(\mathbf e_1,\dots,\mathbf e_n).$$

### Proposition — Alternating forms and linear independence

$$[\mathbf v_1,\dots,\mathbf v_n]\ne0\iff\mathbf v_1,\dots,\mathbf v_n\text{ are linearly independent.}$$

**Proof.** *Dependent $\Rightarrow$ zero.* Suppose $\mathbf v_1,\dots,\mathbf v_n$ are linearly dependent: there are scalars $\alpha_1,\dots,\alpha_n$, not all zero, with $\sum_{j=1}^n\alpha_j\mathbf v_j=\mathbf 0$. Choose $p$ with $\alpha_p\ne0$; then
$$\mathbf v_p=-\sum_{j\ne p}\frac{\alpha_j}{\alpha_p}\mathbf v_j.$$
By linearity,
$$[\mathbf v_1,\dots,\mathbf v_p,\dots,\mathbf v_n]=-\sum_{j\ne p}\frac{\alpha_j}{\alpha_p}[\mathbf v_1,\dots,\underbrace{\mathbf v_j}_{p\text{th position}},\dots,\mathbf v_n]=0,$$
since each bracket on the right contains $\mathbf v_j$ twice.

*Independent $\Rightarrow$ non-zero.* If $\{\mathbf v_1,\dots,\mathbf v_n\}$ is linearly independent in dimension $n$, it is a basis, so $\mathbf e_i=\sum_{j=1}^n\alpha_{ji}\mathbf v_j$ for $i=1,\dots,n$. Then
$$\begin{aligned}
1=[\mathbf e_1,\dots,\mathbf e_n]&=\Big[\sum_{j=1}^n\alpha_{j1}\mathbf v_j,\ \dots,\ \sum_{j=1}^n\alpha_{jn}\mathbf v_j\Big]\\
&=\sum_{j_1,\dots,j_n=1}^n\alpha_{j_11}\cdots\alpha_{j_nn}[\mathbf v_{j_1},\dots,\mathbf v_{j_n}].
\end{aligned}$$
Terms with repeated indices vanish, so $(j_1,\dots,j_n)$ is a permutation of $(1,\dots,n)$ and each remaining bracket is $\pm[\mathbf v_1,\dots,\mathbf v_n]$. Hence $[\mathbf v_1,\dots,\mathbf v_n]\ne0$. $\square$

> [!note] Explanation
> An alternating form vanishes whenever two arguments are equal: swapping them changes nothing but must flip the sign, so the value $x$ satisfies $x=-x$, i.e. $x=0$. That is why every bracket with a repeated vector drops out in both halves of the proof. In the second half, if $[\mathbf v_1,\dots,\mathbf v_n]$ were $0$, every surviving term would be $0$ and the sum could not equal $1$.

### 3.4.4 General formula and properties

### Leibniz's formula

For $M=(M_{ij})\in\operatorname{Mat}_{n\times n}(\mathbb F)$,
$$\det M=\sum_{p\in S_n}\operatorname{sgn}(p)\prod_{i=1}^nM_{ip(i)}.$$
Writing $M=\big(\mathbf C_1\ \mathbf C_2\ \cdots\ \mathbf C_n\big)$ with columns $\mathbf C_i=\mathbf C_i(M)$,
$$\det M=[\mathbf C_1,\dots,\mathbf C_n]=\varepsilon_{i_1\cdots i_n}M_{i_11}\cdots M_{i_nn}.$$

### Properties of the determinant

Fix $n\times n$ matrices $M,N$ over $\mathbb F$ and $\alpha,\beta,\lambda\in\mathbb F$; $M'$ denotes the output matrix of each operation.

*Rows and columns.*
1. **Multilinearity:** $\det(\dots,\alpha\mathbf u+\beta\mathbf v,\dots)=\alpha\det(\dots,\mathbf u,\dots)+\beta\det(\dots,\mathbf v,\dots)$.
2. **Interchanging columns:** $\mathbf C_i\leftrightarrow\mathbf C_j\ \Rightarrow\ \det M'=-\det M$.
3. **Linear dependence:** if the columns are linearly dependent, the determinant vanishes: $\mathbf C_1,\dots,\mathbf C_n$ linearly dependent $\Rightarrow\det M=0$.
4. **Adding a multiple of another column:** $\mathbf C_i\mapsto\mathbf C_i+\lambda\mathbf C_j$ ($i\ne j$) $\Rightarrow\det M'=\det M$.
5. **Scaling:** $\mathbf C_i\mapsto\lambda\mathbf C_i\ \Rightarrow\ \det M'=\lambda\det M$. Multiplying the whole matrix by $\lambda$: $\det(\lambda M)=\lambda^n\det M$.

Everything holds as well for rows.

*Matrix operations.*

6. **Identity:** $\det I_n=1$.
7. **Transpose:** $\det(M^{\mathsf T})=\det M$.
8. **Conjugation and adjoint:** $\det(\overline M)=\overline{\det M}$, $\det(M^\dagger)=\overline{\det M}$.
9. **Products:** $\det(MN)=\det M\det N$.
