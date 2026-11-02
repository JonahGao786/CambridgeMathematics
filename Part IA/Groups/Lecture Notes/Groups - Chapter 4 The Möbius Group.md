---
title: Groups - Chapter 4 The Möbius Group
course: Part IA Groups
material_type: lecture notes
chapter: 4
source_file: Ch.4 The Möbius Group.pdf
drive_file_id: 1cD6n9aI-_mW-bAMZOGvUBNHr3V2QzJue
source_url: https://drive.google.com/file/d/1cD6n9aI-_mW-bAMZOGvUBNHr3V2QzJue/view
source_pages: 3
tags: [lecture, groups]
---

# Groups — Chapter 4: The Möbius Group

> [!abstract] Overview
> The Riemann sphere $\hat{\mathbb C}=\mathbb C\cup\{\infty\}$, pictured by stereographic projection. Möbius transformations $z\mapsto\frac{az+b}{cz+d}$ with $ad-bc\ne0$ compose like $2\times2$ matrices multiply, and they form a subgroup of $\operatorname{Sym}(\hat{\mathbb C})$: the Möbius group.
> Prerequisites: [[Groups - Chapter 1 Examples and Definitions]] (subgroups, $\operatorname{Sym}(X)$); [[Complex Numbers]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition 4.1 — Riemann sphere]] | $\hat{\mathbb C}=\mathbb C\cup\{\infty\}$; stereographic projection | 1 |
| [[#Definition 4.2 — Möbius transformation]] | $\mu(z)=\frac{az+b}{cz+d}$, $ad-bc\ne0$, with the conventions at $\infty$ and $-\frac dc$ | 1–2 |
| [[#Composition of Möbius transformations]] | $\mu_1\circ\mu_2$ has the coefficients of the matrix product | 2 |
| [[#Theorem 4.3 — The Möbius group]] | Möbius transformations form a subgroup $\mathcal M\le\operatorname{Sym}(\hat{\mathbb C})$ | 2–3 |

## 4.1 The Riemann sphere

### Definition 4.1 — Riemann sphere

The **Riemann sphere** is
$$\hat{\mathbb C}=\mathbb C\cup\{\infty\}\qquad(\text{also written }\mathbb C_\infty),$$
where $\infty$ is a formal extra point "at infinity".

**Why is this a "sphere"? Stereographic projection.**

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.4]
  % plane C through the equator
  \draw[blue] (-2.2,-0.45) -- (2.6,-0.45) -- (3.4,0.35) -- (-1.4,0.35) -- cycle;
  \node[blue] at (-1.75,-0.25) {$C$};
  % sphere
  \draw[thick] (0,0) circle (1);
  \draw[blue,dashed] (-1,0) arc (180:0:1 and 0.22);
  \draw[blue] (-1,0) arc (180:360:1 and 0.22);
  % north pole and projection line
  \fill (0,1) circle (1.2pt) node[above,red] {$N$};
  \draw[red,thick] (0,1) -- (1.9,-0.35);
  \fill (0.944,0.329) circle (1.2pt) node[above right] {$P$};
  \fill[red] (1.9,-0.35) circle (1.2pt) node[right,red] {$\pi(P)=z$};
\end{tikzpicture}
\end{document}
```
*Stereographic projection: the line from the north pole $N$ through $P$ meets the plane $\mathbb C$ at $z=\pi(P)$.*

For $P\ne N$ on the unit sphere $S^2$, $z=\pi(P)\in\mathbb C$ is the unique intersection point of the line in $\mathbb R^3$ through $N$ and $P$ with $\mathbb C$. This gives a one-to-one correspondence between $S^2\setminus\{N\}$ and $\mathbb C$, and $N$ corresponds to $\infty\in\hat{\mathbb C}$.

## 4.2 Möbius transformations

### Definition 4.2 — Möbius transformation

Let $a,b,c,d\in\mathbb C$ with $ad-bc\ne0$. The corresponding **Möbius transformation** $\mu:\hat{\mathbb C}\to\hat{\mathbb C}$ is:

for $c\ne0$,
$$z\mapsto\begin{cases}\dfrac{az+b}{cz+d}&\text{if }z\in\mathbb C\setminus\{-\frac dc\},\\[2mm]\infty&\text{if }z=-\frac dc,\\[1mm]\dfrac ac&\text{if }z=\infty;\end{cases}$$
for $c=0$,
$$z\mapsto\begin{cases}\dfrac{az+b}d&\text{if }z\in\mathbb C,\\[2mm]\infty&\text{if }z=\infty.\end{cases}$$

**Notation.** We usually write $\mu(z)=\frac{az+b}{cz+d}$ for all cases.

**N.B.** $ad-bc=\det\begin{pmatrix}a&b\\c&d\end{pmatrix}$. We'll see: $ad-bc\ne0\Rightarrow\mu$ invertible.

### Composition of Möbius transformations

Say
$$\mu_1(z)=\frac{a_1z+b_1}{c_1z+d_1},\qquad\mu_2(z)=\frac{a_2z+b_2}{c_2z+d_2}.$$
**Exercise.**
$$\mu_1\circ\mu_2(z)=\frac{(a_1a_2+b_1c_2)z+(a_1b_2+b_1d_2)}{(c_1a_2+d_1c_2)z+(c_1b_2+d_1d_2)}.\tag{$*$}$$
Compare the formula for matrix multiplication:
$$\begin{pmatrix}a_1&b_1\\c_1&d_1\end{pmatrix}\begin{pmatrix}a_2&b_2\\c_2&d_2\end{pmatrix}=\begin{pmatrix}a_1a_2+b_1c_2&a_1b_2+b_1d_2\\c_1a_2+d_1c_2&c_1b_2+d_1d_2\end{pmatrix}.$$

> [!note] Explanation
> To get $(*)$, substitute $w=\mu_2(z)$ into $\mu_1(w)=\frac{a_1w+b_1}{c_1w+d_1}$ and multiply top and bottom by $c_2z+d_2$. The four coefficients that come out are exactly the entries of the matrix product, so composing Möbius transformations corresponds to multiplying their coefficient matrices.

### Theorem 4.3 — The Möbius group

Let
$$\mathcal M=\{f:\hat{\mathbb C}\to\hat{\mathbb C}:f\text{ is a Möbius transformation}\}.$$
Then $\mathcal M$ is a subgroup of $\operatorname{Sym}(\hat{\mathbb C})$, called the **Möbius group**.

**Proof.** *$\mathcal M\subseteq\operatorname{Sym}(\hat{\mathbb C})$?* Given $\mu:z\mapsto\frac{az+b}{cz+d}$ in $\mathcal M$, let
$$\nu:z\mapsto\frac{dz-b}{-cz+a},$$
also in $\mathcal M$ (its determinant is $da-bc\ne0$). By $(*)$,
$$\mu\circ\nu(z)=\frac{(ad-bc)z}{ad-bc}=z,\tag{$\dagger$}$$
using $ad-bc\ne0$. Similarly $\nu\circ\mu(z)=z$, so $\mu$ is a bijection: $\mu\in\operatorname{Sym}(\hat{\mathbb C})$.
- $\operatorname{id}_{\hat{\mathbb C}}\in\mathcal M$ (take $a=d=1$, $b=c=0$).
- $\mathcal M$ is closed under composition, by $(*)$ and the product formula for determinants:
$$\det\left[\begin{pmatrix}a_1&b_1\\c_1&d_1\end{pmatrix}\begin{pmatrix}a_2&b_2\\c_2&d_2\end{pmatrix}\right]=\det\begin{pmatrix}a_1&b_1\\c_1&d_1\end{pmatrix}\det\begin{pmatrix}a_2&b_2\\c_2&d_2\end{pmatrix}\ne0.$$
- $\mathcal M$ has inverses, by $(\dagger)$. $\square$
