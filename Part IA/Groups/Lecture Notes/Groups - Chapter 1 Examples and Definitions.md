---
title: Groups - Chapter 1 Examples and Definitions
material_type: handwritten lecture notes
course: Part IA Groups
date: null
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: 6
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
  \draw[->] (1.4,0)--(2.6,0) node[midway,above] {$r$};
  \draw[->] (5.4,0)--(6.6,0) node[midway,above] {$s$};
  \draw[blue,dashed] (4,1.2)--(4,-0.6);
  \draw[->] (1.4,-3.7)--(2.6,-3.7) node[midway,above] {$s$};
  \draw[->] (5.4,-3.7)--(6.6,-3.7) node[midway,above] {$r$};
  \draw[blue,dashed] (0,-2.5)--(0,-4.3);
\end{tikzpicture}
\end{document}
```

**Exercise** (page 2): Which of the six listed symmetries is the first composite? No answer is supplied.

### Identity, inverses and associativity (page 3)

- There is one identity; composing with it does nothing extra.
- Every symmetry has one inverse. The two non-trivial rotations undo one another; the displayed reflection is its own inverse.
- Composition is associative: grouping the first two transformations or the last two gives the same final transformation.

The inverse examples compare the clockwise and anticlockwise rotation diagrams above, and two copies of the vertical reflection. The associativity sketch is:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \foreach \x in {0,3,6} {
    \draw (\x,0.7)--(\x-0.65,-0.5)--(\x+0.65,-0.5)--cycle;
    \draw (\x,-2.3)--(\x-0.65,-3.5)--(\x+0.65,-3.5)--cycle;
  }
  \draw[->] (0.9,0)--(2.1,0);
  \draw[->] (3.9,0)--(5.1,0);
  \draw[->] (0.9,-3)--(2.1,-3);
  \draw[->] (3.9,-3)--(5.1,-3);
  \draw (-1,0.95) to[bend right=20] (-1,-0.7);
  \draw (4,0.95) to[bend left=20] (4,-0.7);
  \draw (2,-2.05) to[bend right=20] (2,-3.7);
  \draw (7,-2.05) to[bend left=20] (7,-3.7);
  \node at (3,-1.45) {$=$};
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

No proof of Proposition 1.5 is present in this PDF.
