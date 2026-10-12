---
title: Groups - Chapter 1 Examples and Definitions
material_type: handwritten lecture notes
course: Part IA Groups
date: null
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: 13
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

A bijection $X\to X$ is a **permutation**. See [[Bijections and Permutations]]. The source ends with this definition; no subsequent theorem about symmetric groups is supplied.
