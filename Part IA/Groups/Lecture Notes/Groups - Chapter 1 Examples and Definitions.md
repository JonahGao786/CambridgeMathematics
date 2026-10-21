---
title: Groups - Chapter 1 Examples and Definitions
material_type: lecture notes
course: Part IA Groups
date: null
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: 33
---

# Groups — Chapter 1: Examples and Definitions

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

**Exercises** (page 2): How many symmetries does a square have? A regular pentagon? A regular $n$-gon?

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

**Exercise** (page 2): Which of the six listed symmetries is the first composite?

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

**Question** (page 4): How can we encode the symmetries of a $77$-gon?

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

**Exercise:** Show that $(\mathbb Z,+,0)$ forms a group.

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
Proof omitted.

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
2. $(\mathbb N,+,0)$ is not a group. **Exercise:** why not?
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

**Exercise:** $(C_n,\times,1)$ is an abelian group.

For $n\in\mathbb N$, let
$$\mathbb Z_n=\{0,1,2,\ldots,n-1\}.$$
For $a,b\in\mathbb Z_n$, define $a+_n b$ as the remainder when $a+b$ is divided by $n$.

**Exercise (page 13):** $(\mathbb Z_n,+_n,0)$ is an abelian group.

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

**Exercise:** Calculate $|S_n|$.

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

**Terminology (page 16).** Here “proper subgroup” excludes both $G$ and $I_G$. Standard usage excludes only $G$, so it may include the trivial subgroup.

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

If $H,K\le G$, then $H\cap K\le G$. For a proof exercise, see question 2 of [[Groups - Example Sheet 1 2025]].

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
The empty product is the identity. The proof is assigned as Example Sheet 1, question 9.

## Geometric examples and isometries (pages 19–20)

Equip the complex plane $\mathbb C$ with its usual Euclidean distance $|z-w|$. The sketch shows the segment joining $z$ to $w$.

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

**Distance formula.** For $z=x+iy$ and $w=u+iv$,
$$d(z,w)=|z-w|=\sqrt{(x-u)^2+(y-v)^2}.$$
This follows by taking the modulus of $(x-u)+i(y-v)$.

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

For $n=4$, the diagram illustrates a quarter-turn and four reflection axes. The blue arrow is anticlockwise; the four dashed black lines are reflection axes.

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
Proof omitted. Note that the rotations $r_0,r_1,\ldots,r_{n-1}$ are pairwise distinct.

**Lemma 1.22 (pages 21–22).** For every $k,\ell\in\{0,\ldots,n-1\}$,
$$r_k,s_\ell\in\operatorname{Isom}(X_n).$$

**Proof.** With $\zeta=e^{2\pi i/n}$, these maps send vertices as
$$r_k(\zeta^j)=\zeta^{j+k},\qquad s_\ell(\zeta^j)=\zeta^{\ell-j},$$
with indices modulo $n$, so they map $X_n$ bijectively onto itself. Distance preservation follows from:
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

The blue double ticks mark the equal sides meeting at $z_1$; red single ticks mark those meeting at $z_2$. The diagonals meet at a right angle in this diagram.

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

**Algebraic proof.** The hypotheses do not ensure that the diagonal segments intersect, so the depicted angle argument is not a proof for every configuration. Regard complex numbers as vectors in $\mathbb R^2$. Squaring each distance equality and cancelling $\|z_i\|^2$ gives
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

**Remark.** This generalizes to an “$(n+1)$-point lemma” in $\mathbb R^n$.

## Proposition 1.25 — Classification of dihedral isometries (page 23)

For $n\ge3$,
$$D_{2n}=\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}=\operatorname{Isom}(X_n).$$

**Proof.** Lemma 1.22 proves
$$\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}\subseteq\operatorname{Isom}(X_n).$$
For the reverse inclusion, take $f\in D_{2n}$.

**Corner preservation.** An isometry sends the corners, the $n$th roots of unity, to corners.

Distance-preserving maps preserve the longest diagonals. Examples for the square, pentagon and hexagon are shown below:

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

**Corner preservation.** In the vertex-set model $X_n=\{\zeta^j:0\le j<n\}$ used above, every point of the domain is already a vertex. When “polygon” denotes the boundary or the filled polygon, corner preservation requires a proof. The same classification holds for either interpretation, as follows.

Let $X$ be that boundary or filled polygon and $f:X\to X$ an isometry. Choose three non-collinear points $u_0,u_1,u_2\in X$ and write $v_i=f(u_i)$. The two vectors $u_i-u_0$ ($i=1,2$) are a basis of $\mathbb R^2$. Define a linear map $Q$ by $Q(u_i-u_0)=v_i-v_0$. Distance preservation and
$$2\langle a,b\rangle=\|a\|^2+\|b\|^2-\|a-b\|^2$$
show that these two pairs have identical dot products. By bilinearity $Q$ preserves all dot products, so it is invertible and orthogonal. The affine isometry $T(x)=v_0+Q(x-u_0)$ agrees with $f$ at the three chosen points. For any $x\in X$, the points $T(x)$ and $f(x)$ have equal distances to all three $v_i$. Subtracting their squared-distance equations shows that $T(x)-f(x)$ is perpendicular to both independent differences $v_1-v_0,v_2-v_0$, hence zero. Thus $f=T|_X$.

Since $f$ is onto, $T(X)=X$. Affine maps preserve convex combinations, so $T$ maps the convex hull of $X$ (the filled polygon) onto itself. An invertible affine map preserves extreme points: a point that is not a non-trivial convex combination of two distinct polygon points has the same property after applying $T$ or $T^{-1}$. The extreme points of this polygon are exactly its vertices. A non-vertex boundary point lies inside an edge and an interior point lies inside a segment; neither is extreme. Each vertex is extreme because the polygon lies in the unit disk and a non-trivial convex combination of distinct disk points has norm strictly less than $1$ when it could equal a unit vertex. Therefore $f$ sends vertices to vertices. It remains to classify the induced permutation of the vertices.

Write $\zeta=e^{2\pi i/n}$. The claim gives $f(1)=\zeta^m$ for some $m\in\{0,\ldots,n-1\}$. Distance preservation then gives
$$f(\{\zeta,\zeta^{-1}\})=\{\zeta^{m-1},\zeta^{m+1}\},$$
because these are the two corners adjacent to $f(1)$. If their order is preserved, $f$ agrees with $r_m$ on $1,\zeta,\zeta^{-1}$; if their order is swapped, it agrees with $s_m$ there. These three vertices are non-collinear. Composing with the inverse of the matching isometry and applying the three point lemma gives $f=r_m$ or $f=s_m$.

### Classification on the vertex set

Lemma 1.22 proves
$$\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}\subseteq\operatorname{Isom}(X_n).$$
To prove the reverse inclusion, first show that an isometry preserves adjacency.

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

See [[Isometries and Dihedral Groups]].

## Generators and a dihedral relation (page 24)

Write $r=r_1$ and $s=s_0$. Since
$$r_k=r^k,\qquad s_\ell=r^\ell s,$$
the pair $\{r,s\}$ generates $D_{2n}$.

**Lemma 1.26.** $sr=r^{-1}s$.

**Proof by composition.** The two routes have the same final value:

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

## Products of groups — Proposition 1.27 (page 25)

If $G,H$ are groups, their Cartesian product $G\times H$ is a group under
$$(g_1,h_1)(g_2,h_2)=(g_1g_2,h_1h_2),$$
with identity $(e_G,e_H)$. **Exercise:** verify the group axioms.

## Homomorphisms — Definition 1.28 (page 25)

Groups may have the same structure without being literally the same objects: compare permutations of a deck of $52$ cards with permutations of a bag of $52$ apples.

A function $\varphi:G\to H$ is a **homomorphism** if it respects the group operations:
$$\varphi(gg')=\varphi(g)\varphi(g')\qquad(g,g'\in G).$$
See [[Homomorphisms and Isomorphisms]].

Examples:

1. For any groups $G,H$, the map $g\mapsto e_H$ is the **trivial homomorphism**.
2. If $H\le G$, the inclusion $i:H\to G$, $h\mapsto h$, is a homomorphism.
3. **Exercise (page 26).** If $n\mid m$, the map
   $$\varphi:C_m\to C_n,\qquad z\mapsto z^{m/n}$$
   is a homomorphism. Proof omitted.

## Lemma 1.29 — Identities and inverses (page 26)

If $\varphi:G\to H$ is a homomorphism, then
$$\varphi(e_G)=e_H,\qquad
\varphi(g^{-1})=\varphi(g)^{-1}\quad(g\in G).$$

**Proof.** We have
$$\varphi(e_G)\varphi(e_G)=\varphi(e_Ge_G)=\varphi(e_G).$$
Multiplying by the inverse of $\varphi(e_G)$ gives $\varphi(e_G)=e_H$. Also,
$$\varphi(g)\varphi(g^{-1})=\varphi(gg^{-1})=\varphi(e_G)=e_H,$$
so $\varphi(g^{-1})$ is the inverse of $\varphi(g)$.

## Isomorphisms — Definition 1.30 (pages 26–27)

A bijective homomorphism $\varphi:G\to H$ is an **isomorphism**. The groups are **isomorphic**, written $G\cong H$.

### Example: addition modulo $n$ and roots of unity (page 27)

Recall $C_n=\{z\in\mathbb C:z^n=1\}$ under multiplication, and $\mathbb Z_n=\{0,\ldots,n-1\}$ under $+_n$. Define
$$\varphi:\mathbb Z_n\to C_n,\qquad k\mapsto e^{2\pi ik/n}.$$
The map is well-defined and bijective because the residues correspond exactly to the $n$th roots of unity. To check preservation of the operation, for $k,\ell\in\mathbb Z_n$, write
$$k+\ell=(k+_n\ell)+np,\qquad p\in\mathbb Z.$$
Then
$$\begin{aligned}
\varphi(k+_n\ell)
&=\exp\!\left(\frac{2\pi i(k+_n\ell)}n\right)\\
&=\exp\!\left(\frac{2\pi i(k+\ell)}n\right)\\
&=e^{2\pi ik/n}e^{2\pi i\ell/n}
=\varphi(k)\varphi(\ell).
\end{aligned}$$
Thus $\mathbb Z_n\cong C_n$.

### Example: the real exponential (page 27)

The exponential is an isomorphism
$$\exp:(\mathbb R,+,0)\to(\mathbb R_{>0},\times,1),\qquad x\mapsto e^x.$$
It respects the operations because $\exp(x+y)=\exp(x)\exp(y)$, and it is bijective because $\log$ is its set-theoretic inverse.

## Lemma 1.31 — Composition, inverses and equivalence (page 28)

1. If $\varphi:G\to H$ and $\psi:H\to K$ are homomorphisms, then $\psi\circ\varphi:G\to K$ is a homomorphism:

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

2. If $\varphi:G\to H$ is an isomorphism, its set-theoretic inverse $\varphi^{-1}:H\to G$ is also an isomorphism.
3. Isomorphism is an equivalence relation: $G\cong G$; $G\cong H$ implies $H\cong G$; and $G\cong H$, $H\cong K$ imply $G\cong K$.

All three proofs are assigned as an exercise.

## Image and kernel — Definition 1.32 and Proposition 1.33 (pages 28–29)

For a homomorphism $\varphi:G\to H$,
$$\operatorname{Im}(\varphi)=\{h\in H:\text{there is a }g\in G\text{ with }\varphi(g)=h\},$$
$$\ker(\varphi)=\{g\in G:\varphi(g)=e_H\}.$$

**Proposition 1.33.**
$$\operatorname{Im}(\varphi)\le H,\qquad\ker(\varphi)\le G.$$

**Proof (page 29).** For the image:

- $\varphi(e_G)=e_H$, so $e_H\in\operatorname{Im}(\varphi)$.
- If $\varphi(g_1),\varphi(g_2)$ belong to the image, then
  $$\varphi(g_1)\varphi(g_2)=\varphi(g_1g_2)\in\operatorname{Im}(\varphi).$$
- The inverse of $\varphi(g)$ is $\varphi(g^{-1})$, which also belongs to the image.

Thus $\operatorname{Im}(\varphi)\le H$. For the kernel:

- $\varphi(e_G)=e_H$, so $e_G\in\ker(\varphi)$.
- If $g_1,g_2\in\ker(\varphi)$, then
  $$\varphi(g_1g_2)=\varphi(g_1)\varphi(g_2)=e_He_H=e_H,$$
  so $g_1g_2\in\ker(\varphi)$.
- If $g\in\ker(\varphi)$, then
  $$\varphi(g^{-1})=\varphi(g)^{-1}=e_H^{-1}=e_H,$$
  so $g^{-1}\in\ker(\varphi)$.

Hence $\ker(\varphi)\le G$.

## Injective and surjective functions — Definition 1.34 (pages 29–30)

A function $f:X\to Y$ is:

1. **Injective** if, for all $x_1,x_2\in X$,
   $$f(x_1)=f(x_2)\Longrightarrow x_1=x_2.$$
2. **Surjective** if, for every $y\in Y$, there is an $x\in X$ with $f(x)=y$.

**Observation (page 30).** If $X,Y$ are finite and $|X|=|Y|$, then
$$f\text{ bijective}\quad\Longleftrightarrow\quad
f\text{ injective}\quad\Longleftrightarrow\quad
f\text{ surjective}.$$

## Injectivity and the kernel — Lemma 1.35 (page 30)

A group homomorphism $\varphi:G\to H$ is injective if and only if
$$\ker(\varphi)=\{e_G\}=I_G.$$

**Proof.** If $\varphi$ is injective, the inverse image $\varphi^{-1}(\{e_H\})$ has at most one element. Since it contains $e_G$, the kernel is $\{e_G\}$.

Conversely, suppose $\ker(\varphi)=\{e_G\}$ and $\varphi(g_1)=\varphi(g_2)$. Then
$$\varphi(g_1g_2^{-1})
=\varphi(g_1)\varphi(g_2)^{-1}=e_H.$$
Thus $g_1g_2^{-1}\in\ker(\varphi)=\{e_G\}$, so $g_1=g_2$. Hence $\varphi$ is injective.

**Corollary 1.36.** A homomorphism $\varphi:G\to H$ is an isomorphism if and only if
$$\operatorname{Im}(\varphi)=H,\qquad
\ker(\varphi)=\{e_G\}.$$
See [[Homomorphisms and Isomorphisms]].

## Cyclic groups (pages 30–31)

A group $G$ is **cyclic** if there is a $g\in G$ such that
$$G=\{g^k:k\in\mathbb Z\}.$$
The element $g$ is a **generator** of $G$. Different integer exponents need not give different elements.

Examples (page 31):

1. $C_n=\{z\in\mathbb C:z^n=1\}$ is cyclic with generator $e^{2\pi i/n}$; the additive group $\mathbb Z_n$ has generator $1$ (read modulo $n$).
2. The trivial group is cyclic.
3. The additive group $\mathbb Z$ is cyclic with generator $1$.

See [[Cyclic Groups and Element Orders]].

## Classification of cyclic groups — Theorem 1.38 (pages 31–32)

If $G$ is cyclic, then either $G\cong C_n$ for some $n\in\mathbb N$, or $G\cong\mathbb Z$.

**Proof.** Let $g$ generate $G$ and set
$$S=\{k\in\mathbb N:g^k=e_G\}.$$
If $S\ne\varnothing$, let $n=\min S$; otherwise write $n=\infty$.

### Infinite case (page 31)

If $S=\varnothing$, define
$$\varphi:\mathbb Z\to G,\qquad k\mapsto g^k.$$
It is a homomorphism because
$$\varphi(k+\ell)=g^{k+\ell}=g^kg^\ell=\varphi(k)\varphi(\ell).$$
It is surjective because $g$ generates $G$.

If a non-zero integer $k$ belonged to $\ker(\varphi)$, closure of the kernel under additive inverses would let us replace $k$ by $-k$ if necessary and assume $k>0$. Then $g^k=e_G$, so $k\in S$, a contradiction. Therefore $\ker(\varphi)=\{0\}$. Corollary 1.36 gives $G\cong\mathbb Z$.

### Finite case (page 32)

If $n=\min S<\infty$, define
$$\varphi:\mathbb Z_n\to G,\qquad k\mapsto g^k.$$
For $k,\ell\in\{0,\ldots,n-1\}$, write
$$k+\ell=qn+(k+_n\ell),\qquad q\in\mathbb Z.$$
Since $g^n=e_G$,
$$\begin{aligned}
\varphi(k)\varphi(\ell)
&=g^{k+\ell}
=g^{qn+(k+_n\ell)}\\
&=g^{k+_n\ell}
=\varphi(k+_n\ell).
\end{aligned}$$
Thus $\varphi$ is a homomorphism.

For surjectivity, every element of $G$ has form $g^k$ for some $k\in\mathbb Z$. Divide $k$ by $n$:
$$k=nq+r,\qquad q\in\mathbb Z,\quad0\le r\le n-1.$$
Then $g^k=(g^n)^qg^r=g^r=\varphi(r)$.

For injectivity, if $k\in\ker(\varphi)$, then $g^k=e_G$ with $0\le k\le n-1$. The minimality of the positive exponent $n$ forces $k=0$. Lemma 1.35 gives injectivity. Thus $G\cong\mathbb Z_n$, and the earlier isomorphism $\mathbb Z_n\cong C_n$ gives the stated classification.

## Order of an element — Definition 1.39 (page 32)

For a group $G$ and an element $g\in G$,
$$\langle g\rangle=\{g^k:k\in\mathbb Z\}\le G.$$
This subgroup is cyclic. The **order of $g$**, written $o(g)$, is $n$ if $\langle g\rangle\cong C_n$, and $\infty$ if $\langle g\rangle\cong\mathbb Z$. Equivalently, it is $|\langle g\rangle|$; in the finite case the classification proof identifies it as the least positive $n$ with $g^n=e_G$.

## More on dihedral groups (page 33)

Recall that $D_{2n}$ is generated by $r,s$, where
$$r(z)=e^{2\pi i/n}z,\qquad s(z)=\overline z,$$
and Lemma 1.26 gives $sr=r^{-1}s$. Then
$$sr^2=r^{-1}sr=r^{-2}s.$$
Induction gives
$$sr^k=r^{-k}s\qquad(k\in\mathbb Z).$$

**Lemma 1.40 (statement only).** Suppose $G$ is a group and $a,b\in G$ satisfy
$$a^n=e_G,\qquad b^2=e_G,\qquad ab=ba^{-1}.$$
Then
$$\varphi(r^k)=a^k,\qquad\varphi(r^ks)=a^kb$$
defines a homomorphism $\varphi:D_{2n}\to G$.

Proof omitted. See [[Isometries and Dihedral Groups]].
