---
title: Groups - Chapter 1 Examples and Definitions
course: Part IA Groups
material_type: lecture notes
chapter: 1
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: 34
tags: [lecture, groups]
---

# Groups — Chapter 1: Examples and Definitions

> [!abstract] Overview
> Groups from symmetry and from algebra: the axioms and their first consequences, standard examples (numbers, roots of unity, $\mathbb Z_n$, symmetric groups), subgroups and generation, isometries and dihedral groups, products, homomorphisms and isomorphisms, image and kernel, and the classification of cyclic groups.
> Prerequisites: [[Complex Numbers]], [[Roots of Unity]], [[Numbers and Sets - Chapter 1 Elementary Number Theory]] (division with remainder).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definitions 1.1–1.3 — Set, function, binary operation]] | $\cdot:X\times X\to X$ | 4 |
| [[#Definition 1.4 — Group]] | (G1) associativity, (G2) right identity, (G3) right inverses | 5 |
| [[#Proposition 1.5 — Basic properties of groups]] | left = right inverses/identity; uniqueness | 6–9 |
| [[#Lemma 1.6 — Sock and shoe lemma]] | $(ab)^{-1}=b^{-1}a^{-1}$ | 10–11 |
| [[#Definition 1.7 — Abelian group]] | $ab=ba$ for all $a,b$ | 11 |
| [[#Definition 1.8 — Order of a group]] | $\lvert G\rvert$; $C_n$, $\mathbb Z_n$ | 12–13 |
| [[#Definition 1.9 — Bijection and permutation]] | two-sided inverse function | 13 |
| [[#Lemma 1.11 — Composition is associative]] | $(h\circ g)\circ f=h\circ(g\circ f)$ | 14 |
| [[#Lemma 1.12 — Composites of permutations]] | $f\circ f'\in\operatorname{Sym}(X)$ | 14–15 |
| [[#Proposition 1.13 — The symmetric group]] | $(\operatorname{Sym}(X),\circ,\operatorname{id}_X)$ is a group; $S_n$ | 15 |
| [[#Definition 1.15 — Subgroup]] | $H\le G$ | 16 |
| [[#Proposition 1.16 — Subgroups of the integers]] | they are $n\mathbb Z$, $n\ge0$ | 17 |
| [[#Definition 1.17 — Generated subgroup]] | $\langle X\rangle=\bigcap_{X\subseteq H\le G}H$ | 18 |
| [[#Lemma 1.18 — Elements of a generated group]] | words $x_1^{\pm1}\cdots x_m^{\pm1}$ | 18 |
| [[#Definition 1.19 — Isometry]] | distance-preserving bijection | 19 |
| [[#Proposition 1.20 — Isometries form a group]] | $\operatorname{Isom}(X)\le\operatorname{Sym}(X)$ | 20 |
| [[#Definition 1.21 — Dihedral group]] | $D_{2n}=\operatorname{Isom}(X_n)$ | 20–21 |
| [[#Lemma 1.22 — Rotations and reflections are isometries]] | $r_k,s_\ell\in D_{2n}$ | 21–22 |
| [[#Lemma 1.23 — Kite lemma]] | equal distances $\Rightarrow$ perpendicular diagonals | 22 |
| [[#Lemma 1.24 — Three point lemma]] | fixes 3 non-collinear points $\Rightarrow$ identity | 23 |
| [[#Proposition 1.25 — Elements of the dihedral group]] | $D_{2n}=\{r_k,s_\ell\}$, $\lvert D_{2n}\rvert=2n$ | 23 |
| [[#Lemma 1.26 — Dihedral relation]] | $sr=r^{-1}s$ | 24 |
| [[#Proposition 1.27 — Direct product]] | $G\times H$ componentwise | 25 |
| [[#Definition 1.28 — Homomorphism]] | $\varphi(gg')=\varphi(g)\varphi(g')$ | 25 |
| [[#Lemma 1.29 — Homomorphisms preserve identity and inverses]] | $\varphi(e)=e$, $\varphi(g^{-1})=\varphi(g)^{-1}$ | 26 |
| [[#Definition 1.30 — Isomorphism]] | bijective homomorphism; $\mathbb Z_n\cong C_n$ | 26–27 |
| [[#Lemma 1.31 — Composites and inverses of homomorphisms]] | $\cong$ is an equivalence relation | 28 |
| [[#Proposition 1.33 — Image and kernel are subgroups]] | $\operatorname{Im}\varphi\le H$, $\ker\varphi\le G$ | 28–29 |
| [[#Definition 1.34 — Injective and surjective]] | finite equal sizes: all equivalent | 29–30 |
| [[#Lemma 1.35 — Injective iff trivial kernel]] | $\ker\varphi=\{e_G\}$ | 30 |
| [[#Corollary 1.36 — Isomorphism criterion]] | onto and trivial kernel | 30 |
| [[#Definition — Cyclic group]] | $G=\{g^k\}$ | 30–31 |
| [[#Theorem 1.38 — Classification of cyclic groups]] | $G\cong C_n$ or $\mathbb Z$ | 31–32 |
| [[#Definition 1.39 — Order of an element]] | $o(g)=\lvert\langle g\rangle\rvert$ | 32 |
| [[#Lemma 1.40 — Homomorphisms out of dihedral groups]] | defined by $a^n=b^2=e$, $ab=ba^{-1}$ | 33–34 |
| [[#Corollary 1.41 — Recognising dihedral groups]] | such $a,b$ with $\lvert G\rvert=2n$ give $G\cong D_{2n}$ | 34 |

## 1.1 Symmetry and algebra

There are two ways of thinking about groups: symmetry and algebra. An equilateral triangle has rotational symmetries (e.g. rotation through $2\pi/3$) and reflective symmetries; doing nothing is also a symmetry, the **identity**. Its six symmetries: identity $e$, rotations $r,r^2$, reflections $s_1,s_2,s_3$ (blue arrows: rotations; blue dashed lines: reflection axes).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=0.85]
  \foreach \x/\y/\kind/\lab in {0/0/0/e,4/0/1/r,8/0/2/{r^2},0/-4/3/{s_1},4/-4/4/{s_2},8/-4/5/{s_3}} {
    \begin{scope}[shift={(\x,\y)}]
      \draw[thick] (0,1.4)--(-1.2,-0.7)--(1.2,-0.7)--cycle;
      \ifnum\kind=1
        \draw[blue,->,thick] (80:1.75) arc (80:200:1.75);
        \draw[blue,->,thick] (200:1.75) arc (200:320:1.75);
        \draw[blue,->,thick] (320:1.75) arc (320:440:1.75);
      \fi
      \ifnum\kind=2
        \draw[blue,->,thick] (100:1.75) arc (100:-20:1.75);
        \draw[blue,->,thick] (-20:1.75) arc (-20:-140:1.75);
        \draw[blue,->,thick] (-140:1.75) arc (-140:-260:1.75);
      \fi
      \ifnum\kind=3
        \draw[blue,dashed] (0,1.4)--(0,-0.7);
        \draw[blue,<->] (-0.55,0.2)--(0.55,0.2);
      \fi
      \ifnum\kind=4
        \draw[blue,dashed] (-1.2,-0.7)--(0.6,0.35);
        \draw[blue,<->] (-0.45,0.25)--(0.15,-0.75);
      \fi
      \ifnum\kind=5
        \draw[blue,dashed] (1.2,-0.7)--(-0.6,0.35);
        \draw[blue,<->] (-0.15,-0.75)--(0.45,0.25);
      \fi
      \node at (0,-2.1) {$\lab$};
    \end{scope}
  }
\end{tikzpicture}
\end{document}
```

**Exercises.** How many symmetries does a square have? A regular pentagon? A regular $n$-gon?

**Composition.** Symmetries can be composed. Label the vertices $1,2,3$ (top, lower left, lower right); let $r$ be the anticlockwise rotation and $s$ the vertical reflection. The upper row applies $r$ then $s$, the lower row $s$ then $r$: the results differ, so symmetries **do not commute**. (Exercise: which of the six symmetries is the first composite?)

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=0.85]
  \foreach \x/\y/\t/\l/\r in {0/0/1/2/3,4/0/3/1/2,8/0/3/2/1,0/-3.7/1/2/3,4/-3.7/1/3/2,8/-3.7/2/1/3} {
    \begin{scope}[shift={(\x,\y)}]
      \draw[thick] (0,1.2)--(-1,-0.6)--(1,-0.6)--cycle;
      \node[blue,above] at (0,1.2) {$\t$};
      \node[blue,below left] at (-1,-0.6) {$\l$};
      \node[blue,below right] at (1,-0.6) {$\r$};
    \end{scope}
  }
  \draw[->] (1.9,0)--(2.6,0) node[midway,above] {$r$};
  \draw[->] (5.4,0)--(6.6,0) node[midway,above] {$s$};
  \draw[blue,dashed] (4,1.2)--(4,-0.6);
  \draw[->] (1.4,-3.7)--(2.1,-3.7) node[midway,above] {$s$};
  \draw[->] (5.9,-3.7)--(6.6,-3.7) node[midway,above] {$r$};
  \draw[blue,dashed] (0,-2.5)--(0,-4.3);
  \foreach \x/\y in {0/0,4/-3.7} {
    \begin{scope}[shift={(\x,\y)}]
      \draw[blue,->] (105:1.6) arc (105:195:1.6);
      \draw[blue,->] (225:1.6) arc (225:315:1.6);
      \draw[blue,->] (345:1.6) arc (345:435:1.6);
    \end{scope}
  }
\end{tikzpicture}
\end{document}
```

**Identity, inverses, associativity.** There is one identity; every symmetry has one inverse (the two rotations undo one another, a reflection is its own inverse); and composition is associative.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=0.85]
  \foreach \x in {0,5} {
    \draw[thick] (\x,1.2)--(\x-1,-0.6)--(\x+1,-0.6)--cycle;
    \draw[thick] (\x,-2.5)--(\x-1,-4.3)--(\x+1,-4.3)--cycle;
    \draw[blue,dashed] (\x,-2.5)--(\x,-4.3);
    \draw[blue,<->] (\x-0.45,-3.5)--(\x+0.45,-3.5);
  }
  \begin{scope}
    \draw[blue,->,thick] (100:1.5) arc (100:-20:1.5);
    \draw[blue,->,thick] (-20:1.5) arc (-20:-140:1.5);
    \draw[blue,->,thick] (-140:1.5) arc (-140:-260:1.5);
  \end{scope}
  \begin{scope}[shift={(5,0)}]
    \draw[blue,->,thick] (80:1.5) arc (80:200:1.5);
    \draw[blue,->,thick] (200:1.5) arc (200:320:1.5);
    \draw[blue,->,thick] (320:1.5) arc (320:440:1.5);
  \end{scope}
  \draw[<->,thick] (1.9,0.15)--(3.1,0.15);
\end{tikzpicture}
\end{document}
```

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \foreach \x in {0,4,8} {
    \draw (\x,0.7)--(\x-0.65,-0.5)--(\x+0.65,-0.5)--cycle;
    \draw (\x,-2.3)--(\x-0.65,-3.5)--(\x+0.65,-3.5)--cycle;
  }
  \draw[->] (0.9,0)--(3.1,0);
  \draw[->] (5.55,0)--(7.1,0);
  \draw[->] (0.9,-3)--(2.45,-3);
  \draw[->] (4.9,-3)--(7.1,-3);
  \draw (-1.05,0.95)
    .. controls (-1.38,0.5) and (-1.38,-0.25) .. (-1.05,-0.7);
  \draw (5.05,0.95)
    .. controls (5.38,0.5) and (5.38,-0.25) .. (5.05,-0.7);
  \draw (2.95,-2.05)
    .. controls (2.62,-2.5) and (2.62,-3.25) .. (2.95,-3.7);
  \draw (9.05,-2.05)
    .. controls (9.38,-2.5) and (9.38,-3.25) .. (9.05,-3.7);
  \node at (4,-1.45) {$=$};
\end{tikzpicture}
\end{document}
```

**Question.** How can we encode the symmetries of a $77$-gon?

## 1.2 Groups

### Definitions 1.1–1.3 — Set, function, binary operation

- **1.1** A **set** $X$ is a collection of objects; $x\in X$ means $x$ is one of them (e.g. $3\in\mathbb N$, $\sqrt2\in\mathbb R$, $i\notin\mathbb R$).
- **1.2** A **function** from $X$ to $Y$ is a rule associating to each $x\in X$ an element $f(x)\in Y$. The Cartesian product is $X\times Y=\{(x,y):x\in X,\ y\in Y\}$.
- **1.3** A **binary operation** on $X$ is a function $\cdot:X\times X\to X$.

### Definition 1.4 — Group

A **group** is a triple $(G,\cdot,e)$ with $G$ a set, $\cdot$ a binary operation on $G$ and $e\in G$, such that

1. **(G1) associativity:** $(a\cdot b)\cdot c=a\cdot(b\cdot c)$ for all $a,b,c\in G$;
2. **(G2) right identity:** $a\cdot e=a$ for all $a\in G$;
3. **(G3) right inverses:** for every $a\in G$ there is $b\in G$ with $a\cdot b=e$.

Closure is part of "$\cdot$ is a binary operation on $G$". The symmetries of an equilateral triangle form a group under composition. **Exercise:** $(\mathbb Z,+,0)$ is a group.

### Proposition 1.5 — Basic properties of groups

Let $(G,\cdot,e)$ be a group.

1. If $a\cdot b=e$ then $b\cdot a=e$ (right inverses are left inverses).
2. $e\cdot a=a$ for all $a$ (the right identity is a left identity).
3. If $a\cdot b=e=a\cdot b'$ then $b=b'$ (inverses are unique).
4. If $a\cdot e'=a$ for all $a\in G$ then $e'=e$ (the identity is unique).

**Proof.** **(i)** Suppose $a\cdot b=e$. Then $b=b\cdot e=b\cdot(a\cdot b)=(b\cdot a)\cdot b$ by (G2), assumption, (G1). By (G3) choose $c$ with $b\cdot c=e$; multiplying on the right by $c$,
$$e=b\cdot c=((b\cdot a)\cdot b)\cdot c=(b\cdot a)\cdot(b\cdot c)=(b\cdot a)\cdot e=b\cdot a.$$

**(ii)** By (G3) and (i) choose $b$ with $a\cdot b=e=b\cdot a$. Then $e\cdot a=(a\cdot b)\cdot a=a\cdot(b\cdot a)=a\cdot e=a$.

**(iii)** If $a\cdot b=e=a\cdot b'$, then by (i) $b\cdot a=e$, and
$$b'=e\cdot b'\overset{\text{(ii)}}=(b\cdot a)\cdot b'\overset{\text{(G1)}}=b\cdot(a\cdot b')=b\cdot e\overset{\text{(G2)}}=b.$$

**(iv)** Suppose $a\cdot e'=a$ for all $a$. Given $a$, choose $b$ with $b\cdot a=e$ (by (G3) and (i)). From $a=a\cdot e'$, multiply on the left by $b$: $e=b\cdot a=b\cdot(a\cdot e')=(b\cdot a)\cdot e'=e\cdot e'=e'$, using (ii).

**Remark.** There are many logically equivalent definitions of a group; this course uses Definition 1.4.

**Inverses and powers.** By 1.5(iii), if $a\cdot b=e$ write $b=a^{-1}$; then $a\cdot a^{-1}=e=a^{-1}\cdot a$. Define $a^0=e$, $a^n=a\cdot a^{n-1}$ ($n\in\mathbb N$), $a^n=(a^{-1})^{-n}$ ($n<0$). **Exercise:** $a^ma^n=a^{m+n}$ and $(a^m)^n=a^{mn}$ for $m,n\in\mathbb Z$. Recall $ab\ne ba$ in general (triangle symmetries); similarly $a^{-1}b^{-1}$ need not equal $(ab)^{-1}$:

### Lemma 1.6 — Sock and shoe lemma

For all $a,b\in G$: $(a\cdot b)^{-1}=b^{-1}\cdot a^{-1}$.

**Proof.** $(a\cdot b)\cdot(b^{-1}\cdot a^{-1})=(a\cdot(b\cdot b^{-1}))\cdot a^{-1}=(a\cdot e)\cdot a^{-1}=a\cdot a^{-1}=e$, so $b^{-1}\cdot a^{-1}$ is the inverse by uniqueness (1.5).

### Definition 1.7 — Abelian group

$(G,\cdot,e)$ is **abelian** (after Niels Abel) if $a\cdot b=b\cdot a$ for all $a,b\in G$; such $a,b$ **commute**. If $G=\{e\}$, the only operation is $e\cdot e=e$: the **trivial group**.

**Examples.**
1. $(\mathbb Z,+,0)$, $(\mathbb Q,+,0)$, $(\mathbb R,+,0)$, $(\mathbb C,+,0)$ are abelian groups; the inverse of $x$ is $-x$.
2. $(\mathbb N,+,0)$ is not a group. **Exercise:** why not?
3. $(\mathbb R,\times,1)$ is not a group ($0$ has no inverse), but $(\mathbb R\setminus\{0\},\times,1)$, $(\mathbb C\setminus\{0\},\times,1)$, $(\mathbb Q\setminus\{0\},\times,1)$ are abelian groups.

### Definition 1.8 — Order of a group

The **order** of $(G,\cdot,e)$ is its number of elements $|G|$; $G$ is **finite** if $|G|<\infty$, otherwise infinite. Examples: the trivial group; the triangle symmetries.

- $C_n=\{z\in\mathbb C:z^n=1\}$, the $n$th [[Roots of Unity|roots of unity]]. **Exercise:** $(C_n,\times,1)$ is an abelian group.
- $\mathbb Z_n=\{0,1,\dots,n-1\}$ with $a+_nb$ the remainder of $a+b$ on division by $n$. **Exercise:** $(\mathbb Z_n,+_n,0)$ is an abelian group.

## 1.3 Symmetric groups

### Definition 1.9 — Bijection and permutation

A **bijection** is a function $f:X\to Y$ for which there is $g:Y\to X$ with $f\circ g=\operatorname{id}_Y$ and $g\circ f=\operatorname{id}_X$, where $(f\circ g)(y)=f(g(y))$; $g$ is the set-theoretic inverse of $f$. A bijection $X\to X$ is a **permutation**.

**Definition 1.10.** $\operatorname{Sym}(X)$ is the set of permutations of $X$.

### Lemma 1.11 — Composition is associative

For maps of sets

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \node (W) at (0,0) {$W$};
  \node (X) at (2,0) {$X$};
  \node (Y) at (4,0) {$Y$};
  \node (Z) at (6,0) {$Z$};
  \draw[->] (W)--(X) node[midway,above] {$f$};
  \draw[->] (X)--(Y) node[midway,above] {$g$};
  \draw[->] (Y)--(Z) node[midway,above] {$h$};
\end{tikzpicture}
\end{document}
```

$(h\circ g)\circ f=h\circ(g\circ f)$.

**Proof.** For every $w\in W$: $((h\circ g)\circ f)(w)=(h\circ g)(f(w))=h(g(f(w)))=h((g\circ f)(w))=(h\circ(g\circ f))(w)$.

### Lemma 1.12 — Composites of permutations

If $f,f'\in\operatorname{Sym}(X)$ then $f\circ f'\in\operatorname{Sym}(X)$.

**Proof.** Let $g,g'$ be the inverses of $f,f'$. By associativity, $(f\circ f')\circ(g'\circ g)=f\circ((f'\circ g')\circ g)=f\circ(\operatorname{id}_X\circ g)=f\circ g=\operatorname{id}_X$; similarly $(g'\circ g)\circ(f\circ f')=\operatorname{id}_X$. So $f\circ f'$ is a bijection with inverse $g'\circ g$.

### Proposition 1.13 — The symmetric group

For every set $X$, $(\operatorname{Sym}(X),\circ,\operatorname{id}_X)$ is a group.

**Proof.** $\circ$ is a binary operation on $\operatorname{Sym}(X)$ by Lemma 1.12; associative by Lemma 1.11; $\operatorname{id}_X$ is an identity; inverses exist by definition of a permutation.

**Definition 1.14.** For $X=\{1,\dots,n\}$, $S_n=\operatorname{Sym}(X)$. E.g. $S_3$: rearrangements of three positions in a row; $S_{52}$: shuffles of a deck of cards. **Exercise:** calculate $|S_n|$.

**Notation.** From now on write $G$ for $(G,\cdot,e)$; when several groups occur, write $\circ_G$ and $e_G$.

## 1.4 Subgroups

Sometimes we restrict attention to a smaller group, e.g. $\mathbb Z$ inside $\mathbb R$ under addition, or the rotations of a triangle inside all its symmetries.

### Definition 1.15 — Subgroup

$H\subseteq G$ is a **subgroup**, $H\le G$, if (1) $e_G\in H$; (2) $ab\in H$ for all $a,b\in H$; (3) $a^{-1}\in H$ for all $a\in H$. Then $H$ is a group with the same operation and identity.

**Examples.** (1) $G\le G$. (2) $I_G=\{e_G\}$, the **trivial subgroup**. (3) $\mathbb Z\le\mathbb Q\le\mathbb R\le\mathbb C$ under $+$. (4) $C_n\le C_m$ if $n\mid m$. (5) The rotations through $0,2\pi/3,4\pi/3$ form a subgroup of the triangle symmetries.

**Terminology.** In this course a **proper** subgroup is neither $G$ nor $I_G$ (other texts only require $H\ne G$).

### Proposition 1.16 — Subgroups of the integers

The subgroups of $(\mathbb Z,+,0)$ are precisely $n\mathbb Z=\{nk:k\in\mathbb Z\}$, $n\in\mathbb Z_{\ge0}$ (with $0\mathbb Z=\{0\}$).

**Proof.** *$n\mathbb Z$ is a subgroup:* $0\in n\mathbb Z$; $nk+n\ell=n(k+\ell)$; $-(nk)=n(-k)$.

*No others:* let $S\le\mathbb Z$. If $S=\{0\}$, $S=0\mathbb Z$. Otherwise $S$ contains a positive integer (a non-zero element or its inverse); let $n$ be the smallest. Since $n\in S$, closure gives $n\mathbb Z\subseteq S$. If $x\in S\setminus n\mathbb Z$, divide: $x=nq+r$ with $0<r<n$; then $r=x-nq\in S$, contradicting minimality of $n$. So $S=n\mathbb Z$.

### Definition 1.17 — Generated subgroup

If $H,K\le G$ then $H\cap K\le G$ (see [[Groups - Example Sheet 1 2025]], Q2); more generally $\bigcap_{i\in I}H_i\le G$ for any family $H_i\le G$. For $X\subseteq G$, the **subgroup generated by $X$** is
$$\langle X\rangle=\bigcap_{X\subseteq H\le G}H,$$
intuitively the smallest subgroup containing $X$. If $G=\langle X\rangle$, $X$ **generates** $G$.

### Lemma 1.18 — Elements of a generated group

If $X$ generates $G$, every $g\in G$ can be written $g=x_1^{\varepsilon_1}x_2^{\varepsilon_2}\cdots x_m^{\varepsilon_m}$ with $x_i\in X$, $\varepsilon_i\in\{\pm1\}$, $m\ge0$ (the empty product is $e$). *Proof: Example Sheet 1, Q9.*

## 1.5 Isometries and dihedral groups

Equip $\mathbb C$ with the distance $d(z,w)=|z-w|=\sqrt{(x-u)^2+(y-v)^2}$ for $z=x+iy$, $w=u+iv$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.15,0)--(5.3,0);
  \draw[->] (0,-0.15)--(0,3);
  \coordinate (z) at (1.2,2.2);
  \coordinate (w) at (3.6,1.1);
  \draw[thick] (z)--(w) node[midway,above right] {$|z-w|$};
  \node[above left] at (z) {$z$};
  \node[right] at (w) {$w$};
\end{tikzpicture}
\end{document}
```

### Definition 1.19 — Isometry

For $X\subseteq\mathbb C$, an **isometry** of $X$ is a bijection $f:X\to X$ with $|f(x)-f(y)|=|x-y|$ for all $x,y\in X$.

### Proposition 1.20 — Isometries form a group

$\operatorname{Isom}(X)\le\operatorname{Sym}(X)$; in particular it is a group under composition.

**Proof.** $\operatorname{id}$ is an isometry. For $f,g\in\operatorname{Isom}(X)$: $|f(g(x))-f(g(y))|=|g(x)-g(y)|=|x-y|$. For the inverse, put $x'=f^{-1}(x)$, $y'=f^{-1}(y)$: $|f^{-1}(x)-f^{-1}(y)|=|x'-y'|=|f(x')-f(y')|=|x-y|$.

### Definition 1.21 — Dihedral group

For $n\ge3$ let $X_n=\{e^{2\pi ik/n}:k=0,\dots,n-1\}\subseteq\mathbb C$ (the vertices of a regular $n$-gon). The **$n$th dihedral group** is $D_{2n}=\operatorname{Isom}(X_n)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (1.2,0)--(-0.6,1.04)--(-0.6,-1.04)--cycle;
  \node[above] at (0,1.4) {$n=3$};
  \node[right] at (1.6,0) {$\mathrm{Isom}(X_3)=D_6$};
  \begin{scope}[shift={(7,0)}]
    \draw[thick] (0,1.2)--(-1.2,0)--(0,-1.2)--(1.2,0)--cycle;
    \node[above] at (0,1.4) {$n=4$};
    \node[right] at (1.6,0) {$\mathrm{Isom}(X_4)=D_8$};
  \end{scope}
\end{tikzpicture}
\end{document}
```

**Question.** What are the elements of $D_{2n}$? For $n=4$: rotations by $\pi/2$ and four reflection axes; for $n=5$: rotations $2\pi/5,4\pi/5,\dots$ and five reflection axes.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick] (0,1.2)--(-1.2,0)--(0,-1.2)--(1.2,0)--cycle;
  \draw[blue,->,thick] (1.28,0.12) arc (5:85:1.28);
  \node[blue] at (1.25,1.15) {$\pi/2$};
  \node[blue,right] at (1.9,0.35) {rotations};
  \begin{scope}[shift={(6,0)}]
    \draw[thick] (0,1.2)--(-1.2,0)--(0,-1.2)--(1.2,0)--cycle;
    \draw[dashed] (0,-1.2)--(0,1.2);
    \draw[dashed] (-1.2,0)--(1.2,0);
    \draw[dashed] (-0.6,-0.6)--(0.6,0.6);
    \draw[dashed] (-0.6,0.6)--(0.6,-0.6);
    \node[blue,right] at (1.65,0.35) {4 reflections};
  \end{scope}
\end{tikzpicture}
\end{document}
```

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (90:1.3)--(162:1.3)--(234:1.3)--(306:1.3)--(18:1.3)--cycle;
  \node[above] at (0,1.65) {$n=5$};
  \node[right] at (2,0.45) {Rotations: $2\pi/5,\ 4\pi/5,\ldots$};
  \node[right] at (2,-0.45) {5 reflection axes};
\end{tikzpicture}
\end{document}
```

**Candidates.** Rotations $r_k:z\mapsto e^{2\pi ik/n}z$ ($k=0,\dots,n-1$; $r_0=\operatorname{id}$) and reflections $s_\ell:z\mapsto\overline{e^{-\ell\pi i/n}z}\,e^{\ell\pi i/n}=e^{2\pi i\ell/n}\bar z$ ($\ell=0,\dots,n-1$). **Exercise:** $s_\ell$ is reflection in the line $\{re^{\pi i\ell/n}:r\in\mathbb R\}$. The rotations $r_0,\dots,r_{n-1}$ are distinct.

### Lemma 1.22 — Rotations and reflections are isometries

$r_k,s_\ell\in\operatorname{Isom}(X_n)$ for all $k,\ell$.

**Proof.** With $\zeta=e^{2\pi i/n}$: $r_k(\zeta^j)=\zeta^{j+k}$, $s_\ell(\zeta^j)=\zeta^{\ell-j}$, so both map $X_n$ bijectively to itself. And $|r_k(z)-r_k(w)|=|e^{2\pi ik/n}(z-w)|=|z-w|$, $|s_\ell(z)-s_\ell(w)|=|\bar z-\bar w|=|z-w|$.

The goal is to show these are the only elements of $D_{2n}$.

### Lemma 1.23 — Kite lemma

Let $z_1,z_2,w_1,w_2\in\mathbb C$ with $|w_1-z_1|=|w_2-z_1|$ and $|w_1-z_2|=|w_2-z_2|$. Then $(z_1-z_2)\perp(w_1-w_2)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \coordinate (z1) at (-1.2,0.9);
  \coordinate (z2) at (2,-1.5);
  \coordinate (w1) at (1.2,1.6);
  \coordinate (w2) at (-1.2,-1.6);
  \draw[thick] (z1)--(w1)--(z2)--(w2)--cycle;
  \draw (z1)--(z2);
  \draw (w1)--(w2);
  \draw (0.12,0.16)--(-0.04,0.28)--(-0.16,0.12);
  \node[below left] at (0,0) {$t$};
  \node[above left] at (z1) {$z_1$};
  \node[below right] at (z2) {$z_2$};
  \node[above right] at (w1) {$w_1$};
  \node[below left] at (w2) {$w_2$};
  \begin{scope}[shift={(0,1.25)},rotate=16.26]
    \draw[blue,thick] (-0.05,-0.1)--(-0.05,0.1);
    \draw[blue,thick] (0.05,-0.1)--(0.05,0.1);
  \end{scope}
  \draw[blue,thick] (-1.3,-0.3)--(-1.1,-0.3);
  \draw[blue,thick] (-1.3,-0.4)--(-1.1,-0.4);
  \begin{scope}[shift={(1.6,0.05)},rotate=-75.53]
    \draw[red,thick] (0,-0.12)--(0,0.12);
  \end{scope}
  \begin{scope}[shift={(0.4,-1.55)},rotate=1.79]
    \draw[red,thick] (0,-0.12)--(0,0.12);
  \end{scope}
\end{tikzpicture}
\end{document}
```

**Proof.** Let the diagonals meet at $t$. By symmetry $\angle z_1tw_1=\angle z_1tw_2$; these sum to $\pi$ ($w_1,t,w_2$ collinear), so each is $\pi/2$.

> [!note] Explanation
> The picture assumes the diagonals cross. A configuration-free check: squaring the two equalities and subtracting gives $\langle z_1-z_2,\,w_1-w_2\rangle=0$, with $\langle z,w\rangle=\operatorname{Re}(z\bar w)$.

### Lemma 1.24 — Three point lemma

Let $X\subseteq\mathbb C$, $f\in\operatorname{Isom}(X)$, and suppose $f(z_i)=z_i$ for three non-collinear $z_1,z_2,z_3\in X$. Then $f=\operatorname{id}_X$.

**Proof.** Suppose $f(y)\ne y$ for some $y\in X$. For each $i$, $|f(y)-z_i|=|f(y)-f(z_i)|=|y-z_i|$. By the kite lemma (twice), $z_1-z_2$ and $z_2-z_3$ are both perpendicular to $f(y)-y\ne0$, so $z_1,z_2,z_3$ are collinear — contradiction.

**Remark.** This generalises to an "$(n+1)$-point lemma" in $\mathbb R^n$.

### Proposition 1.25 — Elements of the dihedral group

For $n\ge3$: $D_{2n}=\{r_k,s_\ell:\ k,\ell=0,\dots,n-1\}$, and $|D_{2n}|=2n$.

**Proof.** "$\supseteq$" is Lemma 1.22. Conversely let $f\in D_{2n}$.

**Claim:** $f$ sends corners (the roots of unity) to corners. *Proof of the claim: exercise.* Idea: diagonals (skew diagonals) maximise the distance between points, and isometries preserve distances:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (-0.8,0.8)--(0.8,0.8)--(0.8,-0.8)--(-0.8,-0.8)--cycle;
  \draw[dashed] (-0.8,0.8)--(0.8,-0.8);
  \begin{scope}[shift={(3.3,0)}]
    \draw[thick] (90:1)--(162:1)--(234:1)--(306:1)--(18:1)--cycle;
    \draw[dashed] (162:1)--(18:1);
    \draw[dashed] (162:1)--(306:1);
  \end{scope}
  \begin{scope}[shift={(6.6,0)}]
    \draw[thick] (120:1)--(60:1)--(0:1)--(300:1)--(240:1)--(180:1)--cycle;
    \draw[dashed] (120:1)--(300:1);
  \end{scope}
\end{tikzpicture}
\end{document}
```

So $f(1)=\zeta^m$ for some $m$, and $f$ maps the two neighbours $\{\zeta,\zeta^{-1}\}$ of $1$ to the two neighbours $\{\zeta^{m-1},\zeta^{m+1}\}$ of $\zeta^m$. If the order is kept, $f$ agrees with $r_m$ on $1,\zeta,\zeta^{-1}$; if swapped, with $s_m$. These three points are non-collinear, so by the three point lemma (applied to $q^{-1}\circ f$, $q\in\{r_m,s_m\}$), $f=r_m$ or $f=s_m$.

> [!note] Explanation
> On the vertex set, $|\zeta^a-\zeta^b|=2\sin(\pi d/n)$ with $d$ the number of steps between them, so the nearest vertices to $\zeta^a$ are exactly $\zeta^{a\pm1}$ — this is why an isometry preserves adjacency. The $2n$ maps are distinct: rotations differ at $1$, reflections differ at $1$, and $r_k$, $s_k$ differ at $\zeta$ ($\zeta^{k+1}\ne\zeta^{k-1}$ as $n\ge3$).

### Lemma 1.26 — Dihedral relation

Write $r=r_1$, $s=s_0$. Then $r_k=r^k$ and $s_\ell=r^\ell s$, so $\{r,s\}$ generates $D_{2n}$, and $sr=r^{-1}s$.

**Proof.** Both routes send $z$ to $e^{-2\pi i/n}\bar z$:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \node (z1) at (0,0) {$z$};
  \node (r) at (3,0) {$e^{2\pi i/n}z$};
  \node (sr) at (8,0) {$\overline{e^{2\pi i/n}z}=e^{-2\pi i/n}\overline z$};
  \draw[->] (z1)--(r) node[midway,above] {$r$};
  \draw[->] (r)--(sr) node[midway,above] {$s$};
  \node (z2) at (0,-1.5) {$z$};
  \node (s) at (3,-1.5) {$\overline z$};
  \node (rs) at (8,-1.5) {$e^{-2\pi i/n}\overline z$};
  \draw[->] (z2)--(s) node[midway,above] {$s$};
  \draw[->] (s)--(rs) node[midway,above] {$r^{-1}$};
\end{tikzpicture}
\end{document}
```

## 1.6 Products and homomorphisms

### Proposition 1.27 — Direct product

If $G,H$ are groups, $G\times H$ is a group under $(g_1,h_1)(g_2,h_2)=(g_1g_2,h_1h_2)$ with identity $(e_G,e_H)$. **Exercise:** verify the axioms.

### Definition 1.28 — Homomorphism

Groups may have the same structure without being the same objects (permuting $52$ cards vs. $52$ apples). $\varphi:G\to H$ is a **homomorphism** if $\varphi(gg')=\varphi(g)\varphi(g')$ for all $g,g'\in G$.

**Examples.** (1) $g\mapsto e_H$, the **trivial homomorphism**. (2) For $H\le G$, the inclusion $h\mapsto h$. (3) **Exercise:** if $n\mid m$, $C_m\to C_n$, $z\mapsto z^{m/n}$.

### Lemma 1.29 — Homomorphisms preserve identity and inverses

If $\varphi:G\to H$ is a homomorphism, $\varphi(e_G)=e_H$ and $\varphi(g^{-1})=\varphi(g)^{-1}$.

**Proof.** $\varphi(e_G)\varphi(e_G)=\varphi(e_Ge_G)=\varphi(e_G)$; multiply by $\varphi(e_G)^{-1}$. And $\varphi(g)\varphi(g^{-1})=\varphi(gg^{-1})=\varphi(e_G)=e_H$.

### Definition 1.30 — Isomorphism

A bijective homomorphism is an **isomorphism**; then $G$ and $H$ are **isomorphic**, $G\cong H$.

**Example: $\mathbb Z_n\cong C_n$.** $\varphi:\mathbb Z_n\to C_n$, $k\mapsto e^{2\pi ik/n}$ is a bijection. Writing $k+\ell=(k+_n\ell)+np$,
$$\varphi(k+_n\ell)=e^{2\pi i(k+_n\ell)/n}=e^{2\pi i(k+\ell)/n}=e^{2\pi ik/n}e^{2\pi i\ell/n}=\varphi(k)\varphi(\ell).$$

**Example: $\exp:(\mathbb R,+,0)\to(\mathbb R_{>0},\times,1)$** is an isomorphism: $\exp(x+y)=\exp(x)\exp(y)$, with inverse $\log$.

### Lemma 1.31 — Composites and inverses of homomorphisms

1. If $\varphi:G\to H$ and $\psi:H\to K$ are homomorphisms, so is $\psi\circ\varphi$:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \node (G) at (0,0) {$G$};
  \node (H) at (2.5,0) {$H$};
  \node (K) at (5,0) {$K$};
  \draw[->] (G)--(H) node[midway,above] {$\varphi$};
  \draw[->] (H)--(K) node[midway,above] {$\psi$};
\end{tikzpicture}
\end{document}
```

2. If $\varphi$ is an isomorphism, so is $\varphi^{-1}$.
3. $\cong$ is an equivalence relation.

*Proofs: exercise.*

**Definition 1.32.** For a homomorphism $\varphi:G\to H$: $\operatorname{Im}(\varphi)=\{h\in H:\exists g,\ \varphi(g)=h\}$ and $\ker(\varphi)=\{g\in G:\varphi(g)=e_H\}$.

### Proposition 1.33 — Image and kernel are subgroups

$\operatorname{Im}(\varphi)\le H$ and $\ker(\varphi)\le G$.

**Proof.** *Image:* $e_H=\varphi(e_G)$; $\varphi(g_1)\varphi(g_2)=\varphi(g_1g_2)$; $\varphi(g)^{-1}=\varphi(g^{-1})$. *Kernel:* $\varphi(e_G)=e_H$; $\varphi(g_1g_2)=e_He_H=e_H$; $\varphi(g^{-1})=\varphi(g)^{-1}=e_H$.

### Definition 1.34 — Injective and surjective

$f:X\to Y$ is **injective** if $f(x_1)=f(x_2)\Rightarrow x_1=x_2$, and **surjective** if every $y\in Y$ is some $f(x)$. If $X,Y$ are finite with $|X|=|Y|$: bijective $\iff$ injective $\iff$ surjective.

### Lemma 1.35 — Injective iff trivial kernel

A homomorphism $\varphi$ is injective iff $\ker(\varphi)=\{e_G\}=I_G$.

**Proof.** ($\Rightarrow$) $\varphi^{-1}(\{e_H\})$ has at most one element and contains $e_G$. ($\Leftarrow$) If $\varphi(g_1)=\varphi(g_2)$ then $\varphi(g_1g_2^{-1})=\varphi(g_1)\varphi(g_2)^{-1}=e_H$, so $g_1g_2^{-1}=e_G$, i.e. $g_1=g_2$.

### Corollary 1.36 — Isomorphism criterion

A homomorphism $\varphi:G\to H$ is an isomorphism iff $\operatorname{Im}(\varphi)=H$ and $\ker(\varphi)=\{e_G\}$.

## 1.7 Cyclic groups

### Definition — Cyclic group

$G$ is **cyclic** if $G=\{g^k:k\in\mathbb Z\}$ for some $g\in G$, a **generator** (different exponents need not give different elements).

**Examples.** (1) $C_n$ (generator $e^{2\pi i/n}$) and $\mathbb Z_n$ (generator $1$). (2) The trivial group. (3) $\mathbb Z$ (generator $1$).

### Theorem 1.38 — Classification of cyclic groups

If $G$ is cyclic then $G\cong C_n$ for some $n\in\mathbb N$, or $G\cong\mathbb Z$.

**Proof.** Let $g$ generate $G$ and $S=\{k\in\mathbb N:g^k=e_G\}$.

*$S=\varnothing$:* $\varphi:\mathbb Z\to G$, $k\mapsto g^k$ is a homomorphism ($g^{k+\ell}=g^kg^\ell$) and surjective. If $0\ne k\in\ker\varphi$, then (replacing $k$ by $-k$ if needed) $k>0$ and $g^k=e$, so $k\in S$ — impossible. So $\ker\varphi=\{0\}$ and $G\cong\mathbb Z$ by Corollary 1.36.

*$S\ne\varnothing$, $n=\min S$:* $\varphi:\mathbb Z_n\to G$, $k\mapsto g^k$. Writing $k+\ell=qn+(k+_n\ell)$ and using $g^n=e$: $\varphi(k)\varphi(\ell)=g^{k+\ell}=g^{k+_n\ell}=\varphi(k+_n\ell)$. Surjective: any $g^k$ with $k=nq+r$, $0\le r<n$, equals $g^r=\varphi(r)$. Injective: $g^k=e$ with $0\le k<n$ forces $k=0$ by minimality of $n$. So $G\cong\mathbb Z_n\cong C_n$.

### Definition 1.39 — Order of an element

For $g\in G$, $\langle g\rangle=\{g^k:k\in\mathbb Z\}\le G$ is cyclic. The **order** $o(g)$ is $n$ if $\langle g\rangle\cong C_n$ and $\infty$ if $\langle g\rangle\cong\mathbb Z$; i.e. $o(g)=|\langle g\rangle|$, the least positive $n$ with $g^n=e$ when finite.

## 1.8 More on dihedral groups

$D_{2n}$ is generated by $r(z)=e^{2\pi i/n}z$ and $s(z)=\bar z$ with $sr=r^{-1}s$. Then $sr^2=r^{-1}sr=r^{-2}s$, and by induction $sr^k=r^{-k}s$ for $k\in\mathbb Z$.

### Lemma 1.40 — Homomorphisms out of dihedral groups

Suppose $G$ is a group and $a,b\in G$ satisfy (i) $a^n=e$, (ii) $b^2=e$, (iii) $ab=ba^{-1}$. Then $\varphi(r^k)=a^k$, $\varphi(r^ks)=a^kb$ defines a homomorphism $\varphi:D_{2n}\to G$.

**Proof.** By induction, $a^kb=ba^{-k}$ for all $k\in\mathbb Z$. There are four cases to check ($k,\ell\in\mathbb Z$); in each, the relation $sr^k=r^{-k}s$ ($\dagger$) in $D_{2n}$ and $ba^k=a^{-k}b$ ($\ddagger$) in $G$ correspond:

1. $\varphi(r^k)\varphi(r^\ell)=a^ka^\ell=a^{k+\ell}=\varphi(r^{k+\ell})$.
2. $\varphi(r^k)\varphi(r^\ell s)=a^ka^\ell b=a^{k+\ell}b=\varphi(r^{k+\ell}s)$.
3. $\varphi(r^ks)\varphi(r^\ell)=a^kba^\ell\overset{(\ddagger)}=a^{k-\ell}b=\varphi(r^{k-\ell}s)\overset{(\dagger)}=\varphi(r^ksr^\ell)$.
4. $\varphi(r^ks)\varphi(r^\ell s)=a^kba^\ell b\overset{(\ddagger)}=a^{k-\ell}bb=a^{k-\ell}=\varphi(r^{k-\ell})=\varphi(r^{k-\ell}ss)\overset{(\dagger)}=\varphi(r^ksr^\ell s)$.

So $\varphi$ is a homomorphism.

### Corollary 1.41 — Recognising dihedral groups

Suppose $G$ is a group with generating set $\{a,b\}$ such that (i) $\operatorname{ord}(a)\mid n$, (ii) $\operatorname{ord}(b)\mid2$, (iii) $ab=ba^{-1}$, (iv) $|G|=2n$. Then $G\cong D_{2n}$.

**Proof.** By Lemma 1.40 there is a homomorphism $\varphi:D_{2n}\to G$. It is surjective as $\{a,b\}$ generates $G$. As $|D_{2n}|=|G|$ (finite), $\varphi$ is also injective, hence bijective.
