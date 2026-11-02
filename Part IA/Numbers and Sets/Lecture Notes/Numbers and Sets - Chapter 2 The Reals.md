---
title: Numbers and Sets - Chapter 2 The Reals
course: Part IA Numbers and Sets
material_type: lecture notes
chapter: 2
source_file: Ch.2 The Reals.pdf
drive_file_id: 1NXO09JT735Tr2NnPTWDvsrkXBMYgGyrC
source_url: https://drive.google.com/file/d/1NXO09JT735Tr2NnPTWDvsrkXBMYgGyrC/view
source_pages: 8
tags: [lecture, numbers-and-sets]
---

# Numbers and Sets — Chapter 2: The Reals

> [!abstract] Overview
> The rationals have a "gap": $\sqrt2$ is not rational, and the set $\{x:x^2<2\}$ has no least upper bound in $\mathbb Q$. The real numbers are defined by field and order axioms together with the least upper bound axiom. Consequences: $\mathbb N$ is unbounded (Archimedes), infima exist, $\sqrt2$ exists in $\mathbb R$, and both the rationals and the irrationals are dense.
> Prerequisite: [[Numbers and Sets - Chapter 1 Elementary Number Theory]] (unique factorization).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Proposition 1 — No rational square root of 2]] | there is no $x\in\mathbb Q$ with $x^2=2$ (two proofs) | 1 |
| [[#Definition — The real numbers]] | axioms (1)–(6), including the least upper bound axiom | 2 |
| [[#Definition — Upper bound and least upper bound]] | $\sup S$ | 2 |
| [[#Proposition 2 — Axiom of Archimedes]] | $\mathbb N$ is not bounded above in $\mathbb R$ | 5 |
| [[#Corollary 3 — Arbitrarily small 1 over n]] | $t>0\Rightarrow\exists n\in\mathbb N,\ \frac1n<t$ | 5 |
| [[#Definition — Lower bound and greatest lower bound]] | $\inf S=-\sup(-S)$ | 5–6 |
| [[#Theorem 4 — Existence of square root of 2]] | there is $x\in\mathbb R$ with $x^2=2$; likewise $\sqrt[n]x$ | 6–7 |
| [[#Definition — Irrational numbers]] | reals that are not rational; e.g. $2+3\sqrt5$ | 7 |
| [[#Density of the rationals]] | $a<b\Rightarrow\exists c\in\mathbb Q,\ a<c<b$ | 7–8 |
| [[#Density of the irrationals]] | $a<b\Rightarrow\exists c\in\mathbb R\setminus\mathbb Q,\ a<c<b$ | 8 |

## 2.1 Why not stop at the rationals?

We have seen $\mathbb N\subset\mathbb Z\subset\mathbb Q$. Why not stop here?

### Proposition 1 — No rational square root of 2

There is no rational $x$ with $x^2=2$.

**Proof 1.** Suppose $x^2=2$. We may assume $x>0$, since $(-x)^2=x^2$. If $x$ is rational then $x=\frac ab$ for some $a,b\in\mathbb N$, so
$$\frac{a^2}{b^2}=2,\qquad\text{i.e.}\qquad a^2=2b^2.$$
But the exponent of $2$ in the prime factorization of $a^2$ is even, while the exponent of $2$ in that of $2b^2$ is odd, contradicting the Fundamental Theorem of Arithmetic.

**Note.** The same proof shows that if there is $x\in\mathbb Q$ with $x^2=n$ for some $n\in\mathbb N$, then $n$ is a square.

**Proof 2.** Suppose $x^2=2$ for some $x=\frac ab$ with $a,b\in\mathbb N$. Then for any $c,d\in\mathbb Z$, $cx+d$ has the form $\frac eb$ for some $e\in\mathbb Z$. Thus
$$cx+d>0\ \Longrightarrow\ cx+d\ge\frac1b.$$
But $1<x<2$, so $0<x-1<1$, and hence for $n$ sufficiently large
$$0<(x-1)^n<\frac1b.$$
Yet for every $n\in\mathbb N$, $(x-1)^n$ has the form $cx+d$ for some $c,d\in\mathbb Z$, because $x^2=2$. This is a contradiction.

So "$\mathbb Q$ has a gap". How do we express this fact making reference only to $\mathbb Q$? $2$ is an upper bound for the set of $x$ with $x^2<2$, but so is $1.5$, and $1.42,\dots$ The crucial point: **in $\mathbb Q$ there is no least upper bound** (the "gap").

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.2]
  \draw[->] (-2.8,0) -- (2.9,0) node[right] {$Q$};
  \foreach \x in {-2,-1,0,1,2} {\draw (\x,0.07) -- (\x,-0.07) node[below] {$\x$};}
  \draw[red,thick] (-1.414,0.25) -- (-1.414,0.12) -- (1.414,0.12) -- (1.414,0.25);
  \node[red,above] at (0,0.25) {all $x$ with $x^2<2$};
\end{tikzpicture}
\end{document}
```
*The set of $x$ with $x^2<2$; $2$, $1.5$, $1.42,\dots$ are all upper bounds in $\mathbb Q$, but there is no least one.*


## 2.2 The real numbers

### Definition — The real numbers

The **real numbers**, written $\mathbb R$, are a set with elements $0$ and $1$ ($0\ne1$), equipped with operations $+$ and $\cdot$, and an ordering "$<$", satisfying:

1. $+$ is commutative and associative with identity $0$, and every $x$ has an inverse under $+$;
2. $\cdot$ is commutative and associative with identity $1$, and every $x\ne0$ has an inverse under $\cdot$;
3. $\cdot$ is distributive over $+$: $a\cdot(b+c)=a\cdot b+a\cdot c$ for all $a,b,c$;
4. for all $a,b$, exactly one of $a<b$, $a=b$, $b<a$ holds;
5. for all $a,b,c$: $a<b\Rightarrow a+c<b+c$, and $a<b\Rightarrow ac<bc$ if $c>0$;
6. (**least upper bound axiom**) every non-empty set $S$ of reals that is bounded above has a least upper bound.

### Definition — Upper bound and least upper bound

A set $S\subseteq\mathbb R$ is **bounded above** if there is $x\in\mathbb R$ with $x\ge y$ for all $y\in S$; such an $x$ is an **upper bound** for $S$. We say $x$ is the **least upper bound** for $S$ if $x$ is an upper bound for $S$ and every other upper bound $x'$ satisfies $x'\ge x$. Then we write $x=\operatorname{LUB}(S)$, "$x=$ supremum$(S)$" or $x=\sup(S)$.

**Remarks.**
1. From axioms (1)–(5) we can check, for example, that $0<1$. If not, then $1<0$ (as $0\ne1$), so $0=1-1<0-1=-1$, hence $0=0\times(-1)<(-1)\cdot(-1)=1$, a contradiction.
2. We may regard $\mathbb Q$ as contained in $\mathbb R$ by identifying $\frac ab\in\mathbb Q$ with $a\cdot b^{-1}\in\mathbb R$.
3. $\mathbb Q$ does not satisfy (6): e.g. the set of $x$ with $x^2<2$ has no supremum in $\mathbb Q$.
4. In (6) the words "non-empty" and "bounded above" are crucial. If $S$ is empty, every $x\in\mathbb R$ is an upper bound, so there is no *least* upper bound. If $S$ is not bounded above, it has no upper bound, and certainly no least upper bound.
5. It is possible to construct $\mathbb R$ "out of" $\mathbb Q$ and check that (1)–(6) hold, but it takes effort.

**Examples.**
1. $S=[0,1]=\{x\in\mathbb R:0\le x\le1\}$.
   - $2$ is an upper bound, since $x\le2$ for all $x\in S$.
   - $\frac34$ is not: $\frac78>\frac34$ and $\frac78\in S$.
   - $\sup S=1$: $1$ is an upper bound (all $x\in S$ satisfy $x\le1$), and every other upper bound $y$ satisfies $y\ge1$ because $1\in S$.


```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.2]
  \draw[->] (-2.8,0) -- (2.9,0) node[right] {$R$};
  \foreach \x in {-2,-1,0,1,2} {\draw (\x,0.07) -- (\x,-0.07) node[below] {$\x$};}
  \draw[very thick,blue] (0,0) -- (1,0);
  \fill[blue] (0,0) circle (1.8pt); \fill[blue] (1,0) circle (1.8pt);
  \node[blue,above] at (0.5,0.1) {$S$};
\end{tikzpicture}
\end{document}
```
*$S=[0,1]$.*

2. $S=(0,1)=\{x\in\mathbb R:0<x<1\}$ is non-empty and bounded above. $\sup S=1$ because:
   - $1$ is an upper bound;
   - no upper bound $c$ satisfies $c<1$. Indeed $c>0$ (in fact $c\ge\frac12$ since $\frac12\in S$), so if $c<1$ then $0<c<1$, and so $\frac{c+1}2\in S$ with $\frac{c+1}2>c$, a contradiction.


```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.3,0) -- (4.6,0);
  \draw (0,0.07) -- (0,-0.07) node[below] {$0$};
  \draw (4,0.07) -- (4,-0.07) node[below] {$1$};
  \draw (2.2,0.07) -- (2.2,-0.07) node[below] {$c$};
  \draw[red,->] (3.1,0.6) node[above] {$\frac{c+1}2$} -- (3.1,0.1);
  \draw[very thick,blue] (0,0) -- (4,0);
  \draw[blue,fill=white] (0,0) circle (1.8pt); \draw[blue,fill=white] (4,0) circle (1.8pt);
\end{tikzpicture}
\end{document}
```
*$S=(0,1)$: for $c<1$ the midpoint $\frac{c+1}2$ of $c$ and $1$ lies in $S$ and exceeds $c$.*

## 2.3 Consequences of the least upper bound axiom

**Recap.** $x\in\mathbb R$ is the least upper bound of $S$ if $x$ is an upper bound for $S$ and every other upper bound $y$ satisfies $y\ge x$. If $S$ has a greatest element, then $\sup S=\max S\in S$. But $\sup S$ can exist when $\max S$ doesn't, in which case $\sup S\notin S$.

**Example 3.** Let
$$S=\left\{0,\tfrac12,\tfrac23,\tfrac34,\dots\right\}=\left\{1-\tfrac1n:n\in\mathbb N\right\}.$$
Clearly $1$ is an upper bound. Is there an upper bound $<1$? (Answered after Corollary 3.)

### Proposition 2 — Axiom of Archimedes

$\mathbb N$ is not bounded above in $\mathbb R$.

**Proof.** Suppose on the contrary that $\mathbb N$ is bounded above, and let $c=\sup\mathbb N$. By definition $c-1$ is not an upper bound for $\mathbb N$, so there is $n\in\mathbb N$ with $n>c-1$. But then $n+1\in\mathbb N$ with $n+1>c$, contradicting the fact that $c$ is an upper bound for $\mathbb N$. $\square$

### Corollary 3 — Arbitrarily small 1 over n

For any real $t>0$ there is $n\in\mathbb N$ with $\frac1n<t$.

**Proof.** Given $t>0$, by Proposition 2 there is $n\in\mathbb N$ with $n>\frac1t$. Hence $\frac1n<t$. $\square$

### Definition — Lower bound and greatest lower bound

A set $S$ is **bounded below** if there is $x$ with $x\le y$ for all $y\in S$; such an $x$ is a **lower bound** for $S$.

If $S$ is non-empty and bounded below, then $-S=\{-y:y\in S\}$ is non-empty and bounded above, so it has a least upper bound, $c$ say. Hence $-c$ is the **greatest lower bound** for $S$, written $\operatorname{GLB}(S)$, "infimum$(S)$" or $\inf(S)$.

- Corollary 3 immediately gives $\inf\left\{\frac1n:n\in\mathbb N\right\}=0$.
- Proposition 2 and Corollary 3 show that there are no "infinitely large" or "infinitely small" numbers in $\mathbb R$.

**Back to Example 3.** $\sup S=1$. Suppose $c<1$ is an upper bound for $S$. Then $1-\frac1n\le c$ for all $n\in\mathbb N$, so
$$0<1-c\le\frac1n\qquad\text{for all }n\in\mathbb N,$$
contradicting Corollary 3 (take $t=1-c$). Note $\sup S=1\notin S$: $S$ has no greatest element.

### Theorem 4 — Existence of square root of 2

There exists $x\in\mathbb R$ with $x^2=2$.

**Proof.** Let $S=\{x\in\mathbb R:x^2<2\}$. $S$ is non-empty, since e.g. $1\in S$, and bounded above, e.g. by $2$. Hence $S$ has a supremum, $c$ say. Observe that $1<c<2$. We claim $c^2=2$.

*Suppose $c^2<2$.* For $0<t<1$,
$$\begin{aligned}
(c+t)^2&=c^2+2ct+t^2\\
&<c^2+4t+t &&(c<2,\ t^2<t)\\
&=c^2+5t\\
&<2 &&\text{for sufficiently small }t\text{, e.g. }t<\tfrac{2-c^2}5.
\end{aligned}$$
So $c+t\in S$ with $c+t>c$, contradicting that $c$ is an upper bound for $S$.

*Suppose $c^2>2$.* For $0<t<1$,
$$\begin{aligned}
(c-t)^2&=c^2-2ct+t^2\\
&>c^2-4t+0 &&(c<2)\\
&>2 &&\text{for sufficiently small }t\text{, e.g. }t<\tfrac{c^2-2}4.
\end{aligned}$$
Then $c-t$ is an upper bound for $S$ with $c-t<c$, contradicting that $c$ is the *least* upper bound.

Hence $c^2=2$. $\square$

> [!note] Explanation
> Why is $c-t$ an upper bound in the second case? Take $t$ also below $1$, so $c-t>0$. If some $x\in S$ had $x>c-t>0$, then $x^2>(c-t)^2>2$, contradicting $x^2<2$. So every $x\in S$ satisfies $x\le c-t$.

**Remark.** The same proof shows that $\sqrt[n]x$ exists for all $n\in\mathbb N$ and all $x\in\mathbb R$ with $x>0$, i.e. for all such $n,x$ there is $y\in\mathbb R$ with $y^n=x$.

### Definition — Irrational numbers

A real that is not rational is called **irrational**. E.g. $\sqrt2,\sqrt3,\sqrt5,\dots$ are irrational.

**Example.** $2+3\sqrt5$ is irrational. Indeed, if $2+3\sqrt5=\frac ab$ with $a,b\in\mathbb N$, then
$$\sqrt5=\frac{a-2b}{3b}\in\mathbb Q,$$
a contradiction.

### Density of the rationals

The rationals are **dense** in $\mathbb R$: for all $a<b$ in $\mathbb R$ there is $c\in\mathbb Q$ with $a<c<b$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.2]
  \draw[->] (-0.6,0) -- (5.2,0) node[right] {$R$};
  \draw (0,0.08) -- (0,-0.08) node[below] {$0$};
  \draw (1.2,0.08) -- (1.2,-0.08) node[below] {$a$};
  \draw (3.8,0.08) -- (3.8,-0.08) node[below] {$b$};
  \draw[red] (2.6,0.08) -- (2.6,-0.08) node[below] {$c$};
  \draw[red,<->] (2.6,0.35) -- (3.15,0.35) node[midway,above] {$\frac1n$};
\end{tikzpicture}
\end{document}
```
*$0\le a<b$; the rational $c=\frac{m-1}n$ is the last multiple of $\frac1n$ below $b$, and steps of length $\frac1n<b-a$ cannot jump over $(a,b)$.*

**Proof.** We may assume $a\ge0$. By Corollary 3 there is $n\in\mathbb N$ with $\frac1n<b-a$. Let
$$T=\left\{k\in\mathbb N:\tfrac kn\ge b\right\}.$$
By the Axiom of Archimedes there is $N\in\mathbb N$ with $N>b$; hence $Nn\in T$, so $T\ne\varnothing$. By the well-ordering principle $T$ has a least element $m$. Set $c=\frac{m-1}n$. Since $m-1\notin T$, $c<b$. If $c\le a$, then
$$\frac mn=c+\frac1n<a+(b-a)=b,$$
contradicting $m\in T$. So $a<c<b$. $\square$

### Density of the irrationals

The irrationals are also dense in $\mathbb R$: for all $a<b$ in $\mathbb R$ there is $c\in\mathbb R\setminus\mathbb Q$ with $a<c<b$.

**Proof.** Take a rational $c$ with $a\sqrt2<c<b\sqrt2$. Then
$$a<\frac c{\sqrt2}<b,$$
and $\frac c{\sqrt2}$ is irrational (choosing $c\ne0$, e.g. by applying density of $\mathbb Q$ to a subinterval avoiding $0$). $\square$
