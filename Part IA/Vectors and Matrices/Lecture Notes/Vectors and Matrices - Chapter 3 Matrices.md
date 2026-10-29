---
title: Vectors and Matrices - Chapter 3 Matrices
course: Part IA Vectors and Matrices
material_type: lecture notes
chapter: 3
source_file: Ch.3 Matrices.pdf
drive_file_id: 1iIWxXJono_3nn6eHinzhBzxxu_rR9iYA
source_url: https://drive.google.com/file/d/1iIWxXJono_3nn6eHinzhBzxxu_rR9iYA/view
source_pages: 8
tags: [lecture, vectors-and-matrices]
---

# Vectors and Matrices — Chapter 3: Matrices

> [!abstract] Overview
> Linear maps between vector spaces, their image and kernel, the rank–nullity theorem, how a choice of bases represents a linear map by a matrix, and the standard geometric maps (rotations, reflections, dilations, shears) as matrices. Throughout, the scalar field $\mathbb F$ is $\mathbb R$ or $\mathbb C$.
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
