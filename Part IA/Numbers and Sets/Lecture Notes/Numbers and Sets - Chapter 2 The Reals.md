---
title: Numbers and Sets - Chapter 2 The Reals
course: Part IA Numbers and Sets
material_type: lecture notes
chapter: 2
source_file: Ch.2 The Reals.pdf
drive_file_id: 1NXO09JT735Tr2NnPTWDvsrkXBMYgGyrC
source_url: https://drive.google.com/file/d/1NXO09JT735Tr2NnPTWDvsrkXBMYgGyrC/view
source_pages: 4
tags: [lecture, numbers-and-sets]
---

# Numbers and Sets — Chapter 2: The Reals

> [!abstract] Overview
> The rationals have a "gap": $\sqrt2$ is not rational, and the set $\{x:x^2<2\}$ has no least upper bound in $\mathbb Q$. The real numbers are defined by field and order axioms together with the least upper bound axiom.
> Prerequisite: [[Numbers and Sets - Chapter 1 Elementary Number Theory]] (unique factorization).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Proposition 1 — No rational square root of 2]] | there is no $x\in\mathbb Q$ with $x^2=2$ (two proofs) | 1 |
| [[#Definition — The real numbers]] | axioms (1)–(6), including the least upper bound axiom | 2 |
| [[#Definition — Upper bound and least upper bound]] | $\sup S$ | 2 |

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
2. $S=(0,1)=\{x\in\mathbb R:0<x<1\}$ is non-empty and bounded above. $\sup S=1$ because:
   - $1$ is an upper bound;
   - no upper bound $c$ satisfies $c<1$. Indeed $c>0$ (in fact $c\ge\frac12$ since $\frac12\in S$), so if $c<1$ then $0<c<1$, and so $\frac{c+1}2\in S$ with $\frac{c+1}2>c$, a contradiction.
