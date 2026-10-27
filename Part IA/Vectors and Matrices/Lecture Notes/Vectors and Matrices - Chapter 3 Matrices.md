---
title: Vectors and Matrices - Chapter 3 Matrices
course: Part IA Vectors and Matrices
material_type: lecture notes
chapter: 3
source_file: Ch.3 Matrices.pdf
drive_file_id: 1iIWxXJono_3nn6eHinzhBzxxu_rR9iYA
source_url: https://drive.google.com/file/d/1iIWxXJono_3nn6eHinzhBzxxu_rR9iYA/view
source_pages: 4
tags: [lecture, vectors-and-matrices]
---

# Vectors and Matrices — Chapter 3: Matrices

> [!abstract] Overview
> Linear maps between vector spaces, their image and kernel, the rank–nullity theorem, and how a choice of bases represents a linear map by a matrix. Throughout, the scalar field $\mathbb F$ is $\mathbb R$ or $\mathbb C$.
> Prerequisite: [[Vectors and Matrices - Chapter 2 Vectors]] (bases, dimension).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Linear map]] | $T(\lambda\mathbf x+\mu\mathbf y)=\lambda T\mathbf x+\mu T\mathbf y$ | 1 |
| [[#Definition — Image, kernel, rank and nullity]] | $\operatorname{Im}T$, $\ker T$; injective $\iff\ker T=\{\mathbf 0\}$ | 1 |
| [[#Theorem — Rank-nullity theorem]] | $\operatorname{rank}T+\operatorname{null}T=\dim V$ | 2 |
| [[#Basic examples]] | zero map, identity, $(x_1,x_2)\mapsto x_1\mathbf v_1+x_2\mathbf v_2$ | 3 |
| [[#Linear combinations and composition]] | $\alpha T+\beta S$, $S\circ T$ linear; $\dim\mathcal L(V,W)=\dim V\dim W$ | 3 |
| [[#Definition — Matrix of a linear map]] | $T(\mathbf e_j)=\sum_iM_{ij}\mathbf f_i$; $[T\mathbf x]_C=M[\mathbf x]_B$ | 4 |

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
