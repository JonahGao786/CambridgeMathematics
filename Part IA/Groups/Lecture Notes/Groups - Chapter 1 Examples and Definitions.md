---
title: Groups - Chapter 1 Examples and Definitions
material_type: handwritten lecture notes with labelled mathematical corrections and supplements
course: Part IA Groups
date: null
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: 23
---

# Groups — Chapter 1: Examples and Definitions

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view). No date is supplied.

## Symmetry and algebra (pages 1–4)

There are two ways of thinking about groups: symmetry and algebra.

An equilateral triangle has rotational symmetries, for example a rotation through $2\pi/3$, and reflective symmetries. Doing nothing is also a symmetry: the **identity**.

The six symmetries are the identity, the two non-trivial rotations, and the three reflections below. Blue arrows indicate rotation; blue dashed lines are reflection axes. Coordinates specify schematic layouts.

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

**Exercises** (page 2): How many symmetries does a square have? A regular pentagon? A regular $n$-gon? No answers are supplied.

### Composition and its order (pages 2 and 4)

Symmetries can be composed. Label the vertices $1,2,3$, initially at the top, lower left and lower right. Let $r$ be the anticlockwise rotation and $s$ the vertical reflection used in the examples.

The upper row applies $r$ then $s$ (page 2); the lower row applies $s$ then $r$ (page 4). The resulting labels differ: symmetries **do not commute**.

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

**Exercise** (page 2): Which of the six listed symmetries is the first composite? No answer is supplied.

### Identity, inverses and associativity (page 3)

- There is one identity; composing with it does nothing extra.
- Every symmetry has one inverse. The two non-trivial rotations undo one another; the displayed reflection is its own inverse.
- Composition is associative: grouping the first two transformations or the last two gives the same final transformation.

The inverse examples pair the clockwise and anticlockwise rotations, and show two copies of the same vertical reflection:

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

The associativity sketch is:

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

**Question** (page 4): How can we encode the symmetries of a $77$-gon? No answer is supplied.

## Definitions 1.1–1.3 (page 4)

**Definition 1.1 — Set.** A set $X$ is a collection of objects. Write $x\in X$ to mean that $x$ is one of the objects of $X$. Examples:
$$3\in\mathbb N,\qquad \sqrt2\in\mathbb R,\qquad i\notin\mathbb R.$$

**Definition 1.2 — Function.** A function from a set $X$ to a set $Y$ is a rule associating to each $x\in X$ an element $f(x)\in Y$.

The Cartesian product is the set of ordered pairs
$$X\times Y=\{(x,y):x\in X,\ y\in Y\}.$$

**Definition 1.3 — Binary operation.** A binary operation on $X$ is a function
$$\cdot:X\times X\longrightarrow X.$$

## Definition 1.4 — Group (page 5)

A [[Groups|group]] is a triple $(G,\cdot,e)$, where $G$ is a set, $\cdot$ is a binary operation on $G$, and $e\in G$, such that:

1. **(G1) Associativity:** for all $a,b,c\in G$,
   $$(a\cdot b)\cdot c=a\cdot(b\cdot c).$$
2. **(G2) Right identity:** for every $a\in G$,
   $$a\cdot e=a.$$
3. **(G3) Right inverses:** for every $a\in G$, there is a $b\in G$ such that
   $$a\cdot b=e.$$

Closure is included in the requirement that $\cdot$ is a binary operation on $G$. The definition starts with right identity and right inverses; Proposition 1.5 states that they are also left identity and left inverses.

## Example, exercise and Proposition 1.5 (page 6)

The symmetries of an equilateral triangle form a group under composition, satisfying (G1), (G2) and (G3).

**Exercise:** Show that $(\mathbb Z,+,0)$ forms a group. No proof is supplied.

**Proposition 1.5.** Let $(G,\cdot,e)$ be a group.

1. If $a\cdot b=e$, then $b\cdot a=e$: right inverses are also left inverses.
2. For every $a\in G$, $e\cdot a=a$: the right identity is also a left identity.
3. If $a\cdot b=e=a\cdot b'$, then $b=b'$: inverses are unique.
4. If $e'\in G$ satisfies $a\cdot e'=a$ for every $a\in G$, then $e'=e$: the identity is unique.

### Proof of Proposition 1.5 (pages 7–9)

**(i) Right inverses are left inverses (page 7).** Suppose $a\cdot b=e$. Then
$$b=b\cdot e=b\cdot(a\cdot b)=(b\cdot a)\cdot b,$$
using (G2), the assumption and (G1). By (G3), choose $c\in G$ with $b\cdot c=e$. Multiplying the displayed equality on the right by $c$ gives
$$\begin{aligned}
b\cdot c&=((b\cdot a)\cdot b)\cdot c\\
&=(b\cdot a)\cdot(b\cdot c).
\end{aligned}$$
Thus $e=(b\cdot a)\cdot e=b\cdot a$ by (G2).

**(ii) The right identity is a left identity (page 8).** By (G3) and (i), choose $b\in G$ such that $a\cdot b=e=b\cdot a$. Then
$$e\cdot a=(a\cdot b)\cdot a=a\cdot(b\cdot a)=a\cdot e=a.$$

**(iii) Inverses are unique (page 8).** If $a\cdot b=e=a\cdot b'$, then (i) gives $b\cdot a=e$, and
$$\begin{aligned}
b'&=e\cdot b'&&\text{by (ii)}\\
&=(b\cdot a)\cdot b'&&\text{by (i)}\\
&=b\cdot(a\cdot b')&&\text{by (G1)}\\
&=b\cdot e&&\text{by the assumption}\\
&=b&&\text{by (G2)}.
\end{aligned}$$

**(iv) The identity is unique (page 9).** Suppose $a\cdot e'=a$ for every $a\in G$. For an $a\in G$, use (G3) and (i) to choose $b$ with $b\cdot a=e$. From $a=a\cdot e'$, multiplication on the left by $b$ gives
$$b\cdot a=b\cdot(a\cdot e')=(b\cdot a)\cdot e'=e\cdot e'=e',$$
where the last step uses (ii). Since $b\cdot a=e$, we have $e=e'$.

**Remark (page 9).** There are many logically equivalent definitions of a group; this course uses Definition 1.4.

## Inverse notation and powers (page 10)

By Proposition 1.5(iii), if $a\cdot b=e$, write $b=a^{-1}$. Then
$$a\cdot a^{-1}=e=a^{-1}\cdot a.$$

For $a\in G$, define
$$a^0=e,\qquad a^n=a\cdot a^{n-1}\quad(n\in\mathbb N),\qquad
a^n=(a^{-1})^{-n}\quad(n<0).$$

**Exercise.** For $a\in G$ and $m,n\in\mathbb Z$, show
$$a^m\cdot a^n=a^{m+n},\qquad(a^m)^n=a^{mn}.$$
No proof is supplied.

Recall that $ab=ba$ need not hold, as the triangle symmetries show. Similarly, $a^{-1}b^{-1}$ need not equal $(ab)^{-1}$.

## Lemma 1.6 — Sock and shoe lemma (pages 10–11)

For all $a,b\in G$,
$$(a\cdot b)^{-1}=b^{-1}\cdot a^{-1}.$$

**Proof (page 11).**
$$\begin{aligned}
(a\cdot b)\cdot(b^{-1}\cdot a^{-1})
&=(a\cdot(b\cdot b^{-1}))\cdot a^{-1}\\
&=(a\cdot e)\cdot a^{-1}\\
&=a\cdot a^{-1}=e.
\end{aligned}$$
Therefore $b^{-1}\cdot a^{-1}$ is the inverse, by uniqueness in Proposition 1.5. The nickname is “sock and shoe lemma”.

## Definition 1.7 — Abelian groups (page 11)

A group $(G,\cdot,e)$ is **abelian** if
$$a\cdot b=b\cdot a\qquad\text{for all }a,b\in G.$$
The name is after Niels Abel. When $a\cdot b=b\cdot a$, the elements $a$ and $b$ **commute**.

If $G=\{e\}$, the only possible binary operation is $e\cdot e=e$. This is the **trivial group**.

### Examples from arithmetic (pages 11–12)

1. $(\mathbb Z,+,0)$, $(\mathbb Q,+,0)$, $(\mathbb R,+,0)$ and $(\mathbb C,+,0)$ are abelian groups. The inverse of $x$ is $-x$.
2. $(\mathbb N,+,0)$ is not a group. **Exercise:** why not? No answer is supplied.
3. $(\mathbb R,\times,1)$ is not a group: $0$ has no inverse. However,
   $$(\mathbb R\setminus\{0\},\times,1),\quad
   (\mathbb C\setminus\{0\},\times,1),\quad
   (\mathbb Q\setminus\{0\},\times,1)$$
   are abelian groups.

## Finite groups — Definition 1.8 (page 12)

The **order** of a group $(G,\cdot,e)$ is its number of elements, denoted $|G|$. The group is finite if $|G|<\infty$ and infinite otherwise.

Examples listed are the trivial group and the symmetries of an equilateral triangle.

For $n\in\mathbb N$, let
$$C_n=\{z\in\mathbb C:z^n=1\},$$
the set of [[Roots of Unity|$n$th roots of unity]].

**Exercise:** $(C_n,\times,1)$ is an abelian group. No proof is supplied.

For $n\in\mathbb N$, let
$$\mathbb Z_n=\{0,1,2,\ldots,n-1\}.$$
For $a,b\in\mathbb Z_n$, define $a+_n b$ as the remainder when $a+b$ is divided by $n$.

**Exercise (page 13):** $(\mathbb Z_n,+_n,0)$ is an abelian group. No proof is supplied.

## Symmetric groups — Definition 1.9 (page 13)

Let $X,Y$ be sets. A **bijection** is a function $f:X\to Y$ for which there is a function $g:Y\to X$ satisfying
$$f\circ g=\operatorname{id}_Y,\qquad g\circ f=\operatorname{id}_X.$$
Here $\operatorname{id}_Y$ is the identity function on $Y$, and composition means
$$(f\circ g)(y)=f(g(y)).$$
The function $g$ is the set-theoretic inverse of $f$.

A bijection $X\to X$ is a **permutation**. See [[Bijections and Permutations]].

## Symmetric groups and composition (pages 14–15)

**Definition 1.10 (page 14).** For a set $X$, $\operatorname{Sym}(X)$ is the set of permutations of $X$.

**Lemma 1.11 — Associativity of composition (page 14).** Consider maps of sets:

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

Then
$$(h\circ g)\circ f=h\circ(g\circ f).$$

**Proof.** For every $w\in W$,
$$\begin{aligned}
((h\circ g)\circ f)(w)
&=(h\circ g)(f(w))\\
&=h(g(f(w)))\\
&=h((g\circ f)(w))\\
&=(h\circ(g\circ f))(w).
\end{aligned}$$

**Lemma 1.12 (pages 14–15).** If $f,f'\in\operatorname{Sym}(X)$, then $f\circ f'\in\operatorname{Sym}(X)$.

**Proof.** Let $g$ and $g'$ be the set-theoretic inverses of $f$ and $f'$, respectively. By associativity,
$$\begin{aligned}
(f\circ f')\circ(g'\circ g)
&=f\circ((f'\circ g')\circ g)\\
&=f\circ(\operatorname{id}_X\circ g)\\
&=f\circ g=\operatorname{id}_X.
\end{aligned}$$
Similarly,
$$(g'\circ g)\circ(f\circ f')=\operatorname{id}_X.$$
Thus $f\circ f'$ is a bijection, with inverse $g'\circ g$.

**Proposition 1.13 (page 15).** For every set $X$,
$$(\operatorname{Sym}(X),\circ,\operatorname{id}_X)$$
is a group.

**Proof.** Composition is a binary operation on $\operatorname{Sym}(X)$ by Lemma 1.12. Associativity follows from Lemma 1.11. The identity axiom holds for $\operatorname{id}_X$, and inverses exist by the definition of a permutation.

**Definition 1.14 (page 15).** If $X=\{1,2,\ldots,n\}$, write
$$S_n=\operatorname{Sym}(X).$$

Examples:

- $S_3$ describes the ways of rearranging three positions in a row.
- $S_{52}$ describes the ways of shuffling a standard deck of cards.

**Exercise:** Calculate $|S_n|$. No answer is supplied.

**Notation convention (page 15).** From now on, the lecture usually writes $G$ instead of $(G,\cdot,e)$. Where ambiguity is possible, for example when two groups occur, write $\circ_G$ for the group operation and $e_G$ for its identity.

## Subgroups — Definition 1.15 (page 16)

Sometimes we restrict attention to a smaller group, such as $\mathbb Z$ inside $\mathbb R$ under addition, or the rotations of a triangle inside all its symmetries.

Let $G$ be a group and $H\subseteq G$. The subset $H$ is a **subgroup** of $G$, written $H\le G$, if:

1. $e_G\in H$.
2. $ab\in H$ for every $a,b\in H$.
3. $a^{-1}\in H$ for every $a\in H$.

Then $H$ is also a group, with the same operation and identity as $G$. See [[Subgroups and Generated Subgroups]].

Examples (pages 16–17):

1. Every group $G$ is a subgroup of itself.
2. $I_G=\{e_G\}$ is a subgroup, called the **trivial subgroup**.
3. With addition and identity $0$,
   $$\mathbb Z\le\mathbb Q\le\mathbb R\le\mathbb C.$$
4. If $n\mid m$, then $C_n\le C_m$, where these are the groups of roots of unity.
5. The triangle rotations through $0$, $2\pi/3$ and $4\pi/3$ form a subgroup of its symmetry group.

**Source terminology (page 16).** The lecture calls subgroups other than both $G$ and $I_G$ “proper subgroups”. In standard usage, “proper” means $H\ne G$ and may include the trivial subgroup; the lecture's narrower convention is retained here.

## Proposition 1.16 — Subgroups of the integers (page 17)

The subgroups of $(\mathbb Z,+,0)$ are precisely
$$n\mathbb Z=\{nk:k\in\mathbb Z\},\qquad n\in\mathbb Z_{\ge0}.$$
Here $0\mathbb Z=\{0\}$.

**Proof that $n\mathbb Z$ is a subgroup.** We have $0\in n\mathbb Z$. If $x=nk$ and $y=n\ell$, then
$$x+y=n(k+\ell)\in n\mathbb Z.$$
If $x=nk$, then $-x=n(-k)\in n\mathbb Z$.

**Proof that there are no other subgroups.** Let $S\le\mathbb Z$. If $S=\{0\}$, then $S=0\mathbb Z$. Otherwise $S$ contains a positive integer: a non-zero element or its additive inverse is positive. Let $n$ be the smallest positive integer in $S$.

**Claim:** $S=n\mathbb Z$. Since $n\in S$, repeated addition and additive inverses give $nk\in S$ for every $k\in\mathbb Z$. Thus $n\mathbb Z\subseteq S$.

If $n\mathbb Z\ne S$, choose $x\in S\setminus n\mathbb Z$. Divide by $n$:
$$x=nq+r,\qquad q\in\mathbb Z,\qquad 0<r<n.$$
But $r=x-nq\in S$, contradicting the minimality of $n$.

## Intersections and generated subgroups (page 18)

If $H,K\le G$, then $H\cap K\le G$. The lecture refers to Example Sheet 1, question 2; see [[Groups - Example Sheet 1 2025]]. No exercise proof is supplied in these lecture notes.

More generally, for a family $H_i\le G$ indexed by $i\in I$,
$$\bigcap_{i\in I}H_i
=\{a\in G:a\in H_i\text{ for every }i\in I\}\le G.$$

**Definition 1.17.** For a subset $X$ of a group $G$, the **subgroup generated by $X$** is
$$\langle X\rangle=\bigcap_{X\subseteq H\le G}H,$$
the intersection of all subgroups of $G$ containing $X$.


Intuitively, $\langle X\rangle$ is the smallest subgroup of $G$ containing $X$. If $G=\langle X\rangle$, then $X$ is a **generating set** for $G$, or $X$ **generates** $G$.

**Lemma 1.18 (page 18).** If $X$ generates $G$, every $g\in G$ can be written
$$g=x_1^{\varepsilon_1}x_2^{\varepsilon_2}\cdots x_m^{\varepsilon_m},
\qquad x_i\in X,\quad\varepsilon_i\in\{1,-1\},\quad m\in\mathbb Z_{\ge0}.$$
The empty product is the identity. The proof is assigned as Example Sheet 1, question 9; no proof is supplied here.

## Geometric examples and isometries (pages 19–20)

Equip the complex plane $\mathbb C$ with its usual Euclidean distance $|z-w|$. The source draws a segment from $z$ to $w$ on unlabelled coordinate axes. This reconstruction is schematic.

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

**Corrected distance formula (page 19).** For $z=x+iy$ and $w=u+iv$,
$$d(z,w)=|z-w|=\sqrt{(x-u)^2+(y-v)^2}.$$
This follows by taking the modulus of $(x-u)+i(y-v)$. The source's radical $\sqrt{(z+w)^2+(z-w)^2}$ was incorrect; for example, it need not vanish when $z=w$. The formula above is used throughout the isometry arguments.

**Definition 1.19.** For any $X\subseteq\mathbb C$, an **isometry of $X$** is a bijection $f:X\to X$ preserving distances:
$$|f(x)-f(y)|=|x-y|\qquad\text{for all }x,y\in X.$$

**Proposition 1.20.** The set $\operatorname{Isom}(X)$ of isometries of $X$ is a subgroup of $\operatorname{Sym}(X)$. In particular, it is a group under composition.

**Proof.** The identity is an isometry. If $f,g\in\operatorname{Isom}(X)$, their composite is a bijection and
$$\begin{aligned}
|(f\circ g)(x)-(f\circ g)(y)|
&=|f(g(x))-f(g(y))|\\
&=|g(x)-g(y)|=|x-y|.
\end{aligned}$$
Thus $f\circ g\in\operatorname{Isom}(X)$.

For the inverse, put $x'=f^{-1}(x)$ and $y'=f^{-1}(y)$. Then
$$\begin{aligned}
|f^{-1}(x)-f^{-1}(y)|
&=|x'-y'|\\
&=|f(x')-f(y')|\\
&=|(f\circ f^{-1})(x)-(f\circ f^{-1})(y)|\\
&=|x-y|.
\end{aligned}$$
Hence $f^{-1}\in\operatorname{Isom}(X)$, proving the subgroup conditions. See [[Isometries and Dihedral Groups]].

## Dihedral groups — Definition 1.21 (pages 20–21)

For $n\in\mathbb N$, $n\ge3$, use the vertex-set model of the regular $n$-gon:
$$X_n=\left\{e^{2\pi i k/n}:k=0,1,\ldots,n-1\right\}\subseteq\mathbb C.$$
Here $X_n$ denotes the vertices, and the drawn edges visualize their cyclic order. This makes the domain of the following isometries explicit.
The **$n$th dihedral group** is
$$D_{2n}=\operatorname{Isom}(X_n).$$

The examples show a triangle pointing right and a square with a vertex at the top:

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

**Question:** What are the elements of $D_{2n}$?

For $n=4$, the source illustrates a quarter-turn and four reflection axes. The blue arrow is anticlockwise; the four dashed black lines are reflection axes.

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

For $n=5$, the rotations include angles $2\pi/5,4\pi/5,\ldots$, and there are five reflection axes. The pentagon sketch itself has no axes drawn:

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

### Candidate rotations and reflections (page 21)

The proposed elements are:

- **Rotations:** $r_k:z\mapsto e^{2\pi ik/n}z$, for $k=0,\ldots,n-1$; $r_0$ is the identity.
- **Reflections:** for $\ell=0,\ldots,n-1$,
  $$s_\ell:z\mapsto\overline{e^{-\ell\pi i/n}z}\,e^{\ell\pi i/n}
  =e^{2\pi i\ell/n}\overline z.$$

**Exercise:** Check that $s_\ell$ is reflection in the line
$$\{re^{\pi i\ell/n}:r\in\mathbb R\}.$$
No proof is supplied. The source observes that the rotations $r_0,r_1,\ldots,r_{n-1}$ are pairwise distinct.

**Lemma 1.22 (pages 21–22).** For every $k,\ell\in\{0,\ldots,n-1\}$,
$$r_k,s_\ell\in\operatorname{Isom}(X_n).$$

**Proof.** With $\zeta=e^{2\pi i/n}$, these maps send vertices as
$$r_k(\zeta^j)=\zeta^{j+k},\qquad s_\ell(\zeta^j)=\zeta^{\ell-j},$$
with indices modulo $n$, so they map $X_n$ bijectively onto itself. The source checks distance preservation:
$$\begin{aligned}
|r_k(z)-r_k(w)|&=|e^{2\pi ik/n}(z-w)|=|z-w|,\\
|s_\ell(z)-s_\ell(w)|&=|e^{2\pi i\ell/n}(\overline z-\overline w)|\\
&=|\overline z-\overline w|=|\overline{z-w}|=|z-w|.
\end{aligned}$$
The goal is to show that these are the only elements of $D_{2n}$.

## Lemma 1.23 — Kite lemma (page 22)

Let $z_1,z_2,w_1,w_2\in\mathbb C$. If
$$|w_1-z_1|=|w_2-z_1|,\qquad |w_1-z_2|=|w_2-z_2|,$$
then
$$(z_1-z_2)\perp(w_1-w_2).$$

The blue double ticks mark the equal sides meeting at $z_1$; red single ticks mark those meeting at $z_2$. Both diagonals and the right-angle marker are present in the source. Coordinates are schematic and satisfy these constraints.

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

**Geometric proof.** In the depicted non-degenerate case, let the diagonals meet at $t$. By symmetry,
$$\angle z_1tw_1=\angle z_1tw_2.$$
Since $w_1,t,w_2$ lie on a straight line, these angles sum to $\pi$, so each is $\pi/2$. If either difference vector is zero, orthogonality holds immediately in the dot-product sense.

**Complete algebraic proof — supplementary correction.** The hypotheses do not ensure that the diagonal segments intersect, so the depicted angle argument is not a proof for every configuration. Regard complex numbers as vectors in $\mathbb R^2$. Squaring each distance equality and cancelling $\|z_i\|^2$ gives
$$2\langle z_i,w_1-w_2\rangle=\|w_1\|^2-\|w_2\|^2\qquad(i=1,2).$$
Subtracting the two equations yields
$$\langle z_1-z_2,w_1-w_2\rangle=0.$$
This proves the lemma in all cases, including zero difference vectors. The real inner product is $\langle z,w\rangle=\operatorname{Re}(z\overline w)$.

## Lemma 1.24 — Three point lemma (page 23)

Let $X\subseteq\mathbb C$ and $f\in\operatorname{Isom}(X)$. Suppose there are three non-collinear points $z_1,z_2,z_3\in X$ with
$$f(z_i)=z_i\qquad(i=1,2,3).$$
Then $f=\operatorname{id}_X$.

**Proof by contradiction.** Suppose $f(y)\ne y$ for some $y\in X$. For each $i=1,2,3$,
$$|f(y)-z_i|=|f(y)-f(z_i)|=|y-z_i|,$$
using the fixed-point hypotheses and distance preservation. Applying the kite lemma twice shows that $z_1-z_2$ and $z_2-z_3$ are both perpendicular to the non-zero vector $f(y)-y$. Hence $z_1,z_2,z_3$ are collinear, contradicting the hypothesis.

**Remark.** This generalizes to an “$(n+1)$-point lemma” in $\mathbb R^n$; the source gives no further statement or proof.

## Proposition 1.25 — Classification of dihedral isometries (page 23)

The source states
$$D_{2n}=\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}=\operatorname{Isom}(X_n).$$

**Proof.** Lemma 1.22 proves
$$\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}\subseteq\operatorname{Isom}(X_n).$$
The following supplementary argument completes the reverse inclusion missing from the source.

Put $\zeta=e^{2\pi i/n}$. Distances between vertices satisfy
$$|\zeta^a-\zeta^b|=2\sin\left(\frac{\pi d}{n}\right),\qquad
d=\min\{|a-b|,n-|a-b|\},$$
using representatives $0\le a,b<n$. Since sine is strictly increasing on $[0,\pi/2]$, the closest other vertices to $\zeta^a$ are exactly $\zeta^{a-1},\zeta^{a+1}$ (indices modulo $n$). Thus every isometry preserves adjacency.

Take $f\in\operatorname{Isom}(X_n)$. Write $f(1)=\zeta^k$. Adjacency forces
$$f(\zeta)=\zeta^{k+1}\quad\text{or}\quad f(\zeta)=\zeta^{k-1}.$$
In the first case choose $q=r_k$; in the second choose $q=s_k$. In either case $q$ agrees with $f$ at both $1$ and $\zeta$. Then $h=q^{-1}\circ f$ is an isometry fixing these two vertices.

The vertex $\zeta^2$ is a neighbour of $\zeta$. Its image under $h$ must be either $1$ or $\zeta^2$. Injectivity excludes $1$, already the image of $1$, so $h(\zeta^2)=\zeta^2$. For $n\ge3$, the distinct points $1,\zeta,\zeta^2$ are non-collinear (a line meets a circle in at most two points). The three point lemma gives $h=\operatorname{id}_{X_n}$ and hence $f=q$. This proves the reverse inclusion, including the case $n=3$.

The $n$ rotations are distinct by their values at $1$, and the same is true for the $n$ reflections. A rotation and reflection with equal values at $1$ have the same index $k$, but their values at $\zeta$ are $\zeta^{k+1}$ and $\zeta^{k-1}$, which differ because $n\ge3$. Therefore the displayed list contains exactly $2n$ elements:
$$|D_{2n}|=2n.$$

## Review cross-reference — supplementary note

The distance formula, the general kite lemma and the dihedral classification now have corrected or complete arguments above. [[Isometries and Dihedral Groups]] summarizes them. The original diagrams are unchanged; supplementary proof steps are labelled separately from the lecture source.
