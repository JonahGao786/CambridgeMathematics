---
title: Limits, Big O and Little o - A First-Year Guide
material_type: explanatory supplement requested by the user
course: Part IA Differential Equations and Analysis I
date: 2026-10-09
related_source_note: Differential Equations - Chapter 1 Introduction and Basic Calculus
---

# Limits, Big O and Little o — A First-Year Guide

This is an explanatory supplement requested alongside the GoodNotes sync. It expands the definitions in [[Differential Equations - Chapter 1 Introduction and Basic Calculus]], pages 2–7; the worked examples and explanatory proofs here are additional teaching material, separate from the faithful source note.

## 1. What a limit promises

The statement
$$\lim_{x\to a}f(x)=L$$
promises that we can make the output error $|f(x)-L|$ as small as we please by restricting the input distance $|x-a|$ sufficiently.

Here $|u-v|$ is the distance between real numbers $u$ and $v$. Thus $|f(x)-L|<\varepsilon$ says that the output lies in the interval $(L-\varepsilon,L+\varepsilon)$.

The formal definition, for $f:D\to\mathbb R$ and an accumulation point $a$ of $D$, is
$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:
\quad 0<|x-a|<\delta\ \Longrightarrow\ |f(x)-L|<\varepsilon.
$$

An accumulation point means that $D$ has points other than $a$ arbitrarily close to $a$. This prevents the condition being vacuously true because there are no nearby inputs.

Read the symbols from left to right:

1. **For every $\varepsilon>0$:** someone specifies an output tolerance, however small.
2. **There exists $\delta>0$:** you choose an input tolerance that achieves it.
3. **For every $x\in D$:** your choice must work for every allowed input within that tolerance.

The order matters. You may choose $\delta$ after seeing $\varepsilon$, and it may depend on the fixed function, point $a$ and proposed limit $L$. It must not depend on the individual $x$ that is checked afterwards. Finding one nearby $x$ with a small error is not enough.

The condition $0<|x-a|$ excludes $x=a$. Consequently, a limit does not require $f(a)$ to exist, or to equal $L$. **Continuity at $a$** adds the requirements that $f(a)$ exists and that $\lim_{x\to a}f(x)=f(a)$.

For instance, $(x^2-1)/(x-1)=x+1$ for $x\ne1$, so
$$\lim_{x\to1}\frac{x^2-1}{x-1}=2,$$
although the displayed quotient is undefined at $1$. Defining its value there to be $100$ leaves its limit unchanged but makes the resulting function discontinuous at $1$.

## 2. How to choose delta

### A linear example

Prove $\lim_{x\to1}(2x+1)=3$. Calculate the output error:
$$|(2x+1)-3|=2|x-1|.$$
To make this smaller than $\varepsilon$, choose $\delta=\varepsilon/2$.

A finished proof reads: Let $\varepsilon>0$. Set $\delta=\varepsilon/2>0$. If $0<|x-1|<\delta$, then
$$|(2x+1)-3|=2|x-1|<2\delta=\varepsilon.$$
This establishes the required implication for every such $x$.

The picture uses $\varepsilon=0.8$ and $\delta=0.4$. All points of the line with $0<|x-1|<0.4$ lie inside the horizontal output band.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,xscale=2.8,yscale=0.8]
  \fill[blue!10] (0.6,0) rectangle (1.4,5);
  \fill[red!10,opacity=0.6] (0,2.2) rectangle (2,3.8);
  \draw[->] (0,0)--(2.2,0) node[right] {$x$};
  \draw[->] (0,0)--(0,5.2) node[above] {$y$};
  \draw[thick,domain=0:2] plot (\x,{2*\x+1});
  \draw[blue,dashed] (0.6,0)--(0.6,5);
  \draw[blue,dashed] (1.4,0)--(1.4,5);
  \draw[red,dashed] (0,2.2)--(2,2.2);
  \draw[red,dashed] (0,3.8)--(2,3.8);
  \draw[dotted] (1,0)--(1,3)--(0,3);
  \node[left] at (0,3) {$L=3$};
  \node[left,red] at (0,2.2) {$L-\varepsilon$};
  \node[left,red] at (0,3.8) {$L+\varepsilon$};
  \node[below] at (1,0) {$a=1$};
  \node[below,blue] at (0.6,-0.6) {$a-\delta$};
  \node[below,blue] at (1.4,-0.6) {$a+\delta$};
  \node[right] at (2,5) {$y=2x+1$};
\end{tikzpicture}
\end{document}
```

### A quadratic example

Prove $\lim_{x\to2}x^2=4$. Factoring gives
$$|x^2-4|=|x-2||x+2|.$$
The factor $|x+2|$ depends on $x$, so first restrict $|x-2|<1$. Then
$$|x+2|\le|x-2|+4<5.$$
Choose
$$\delta=\min\{1,\varepsilon/5\}.$$
Whenever $0<|x-2|<\delta$,
$$|x^2-4|<5|x-2|<5\delta\le\varepsilon.$$

The minimum imposes two requirements at once: stay in a region where the extra factor is bounded, and make the final error small enough. Delta is not unique; any smaller positive choice also works.

For a proof, do the estimate first on scratch paper, then present the finished argument starting with “Let $\varepsilon>0$” and your choice of $\delta$.

## 3. One-sided limits, infinity and sequences

For a **right-hand limit** $x\to a^+$, replace $0<|x-a|<\delta$ by $0<x-a<\delta$. For a left-hand limit, use $0<a-x<\delta$. When the function is defined on both sides of $a$, an ordinary two-sided limit exists when both one-sided limits exist and agree.

For **$x\to+\infty$**, the input is made sufficiently large:
$$
\lim_{x\to+\infty}f(x)=L
\quad\Longleftrightarrow\quad
\forall\varepsilon>0\ \exists X\in\mathbb R\ \forall x\in D:
\quad x>X\ \Longrightarrow\ |f(x)-L|<\varepsilon.
$$
The domain must be unbounded above. For example, $1/x\to0$: choose $X=\max\{1,1/\varepsilon\}$.

For a **sequence** $(u_n)$,
$$
u_n\to L
\quad\Longleftrightarrow\quad
\forall\varepsilon>0\ \exists N\in\mathbb N\ \forall n\ge N:
\quad |u_n-L|<\varepsilon.
$$
“Close enough to $a$” becomes “far enough along the sequence”. For $u_n=1/n$, choose any integer $N>1/\varepsilon$.

A limit of **$+\infty$** has a different output condition:
$$
f(x)\to+\infty\text{ as }x\to a
\quad\Longleftrightarrow\quad
\forall M>0\ \exists\delta>0\ \forall x\in D:
\quad 0<|x-a|<\delta\ \Longrightarrow\ f(x)>M.
$$
Infinity here is not a real value $L$; it means eventually exceeding every positive bound.

Negating the finite-limit definition gives a useful way to disprove a proposed limit:
$$
\exists\varepsilon_0>0\ \forall\delta>0\ \exists x\in D:
\quad 0<|x-a|<\delta
\quad\text{and}\quad |f(x)-L|\ge\varepsilon_0.
$$
There is one fixed output tolerance that fails, however tightly we restrict the input.

## 4. Big O: one fixed bound on relative size

For a specified limit $x\to a$,
$$f(x)=O(g(x))$$
means
$$
\exists C>0\ \exists\delta>0\ \forall x\in D:
\quad 0<|x-a|<\delta\ \Longrightarrow\ |f(x)|\le C|g(x)|.
$$

The constant $C$ is fixed throughout the neighbourhood. If $g(x)\ne0$ there, this is equivalent to the ratio $|f(x)/g(x)|$ being bounded near $a$. **The ratio need not converge.**

For $x\to+\infty$, replace the neighbourhood condition with $x>X$ for some fixed threshold $X$. Always specify the limiting regime: the same pair of functions can behave differently near zero and at infinity.

Examples:

- $3x=O(x)$ as $x\to0$, with $C=3$.
- $x^2=O(x)$ as $x\to0$, since $|x^2|\le|x|$ for $|x|<1$.
- $x$ is not $O(x^2)$ as $x\to0$, since $|x/x^2|=1/|x|$ is unbounded.
- $x=O(x^2)$ as $x\to+\infty$, since $x\le x^2$ for $x\ge1$.
- $2x^3+4x=O(x^3)$ as $x\to+\infty$, with $C=6$ and $X=1$.

Big $O$ gives an upper bound, not an exact rate or a lower bound. For example, $x=O(x^2)$ at infinity does not mean that $x$ grows as fast as $x^2$.

## 5. Little o: every positive relative bound

For $x\to a$,
$$f(x)=o(g(x))$$
means
$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:
\quad 0<|x-a|<\delta\ \Longrightarrow\ |f(x)|\le\varepsilon|g(x)|.
$$

Compare this with big $O$: one fixed multiplier $C$ is replaced by **every positive multiplier $\varepsilon$**, with the neighbourhood allowed to shrink for each choice.

Where $g$ is non-zero near the limiting point,
$$f=o(g)\quad\Longleftrightarrow\quad\frac fg\to0.$$
This is a relative statement. At infinity, $x=o(x^2)$ even though $x\to+\infty$: $x$ becomes negligible compared with $x^2$.

For example, $x^2=o(x)$ as $x\to0$. Given $\varepsilon>0$, choose $\delta=\varepsilon$. Then, for $0<|x|<\delta$,
$$|x^2|=|x||x|<\varepsilon|x|.$$
By contrast, $3x$ is not $o(x)$: its ratio to $x$ is always $3$, so the bound fails for $\varepsilon=1$ at every non-zero $x$.

| Statement, as $x\to0$ | Formal requirement |
| --- | --- |
| $f(x)\to0$ | For every $\varepsilon>0$, eventually $|f(x)|<\varepsilon$. |
| $f(x)=O(x)$ | For one fixed $C>0$, eventually $|f(x)|\le C|x|$. |
| $f(x)=o(x)$ | For every $\varepsilon>0$, eventually $|f(x)|\le\varepsilon|x|$. |

Both $O(x)$ and $o(x)$ imply $f(x)\to0$ here, but convergence to zero alone is weaker: $\sqrt{|x|}\to0$ while $\sqrt{|x|}$ is not $O(x)$.

Little $o$ implies big $O$ by choosing $\varepsilon=1$. The converse is false. Even an oscillating ratio can satisfy big $O$: $x\sin(1/x)=O(x)$ near zero because $|\sin(1/x)|\le1$, but it is not $o(x)$ since the ratio repeatedly equals $1$ at $x=1/(\pi/2+2\pi n)$.

For powers on the positive side:

| Regime | $x^\alpha=o(x^\beta)$ exactly when |
| --- | --- |
| $x\to0^+$ | $\alpha>\beta$ |
| $x\to+\infty$ | $\alpha<\beta$ |

This follows by examining $x^{\alpha-\beta}$. Larger powers vanish faster near zero and grow faster at infinity.

## 6. Why the derivative has an o(h) remainder

For a function defined on an open interval about $a$, the derivative at $a$ is the limit
$$f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h.$$
Its epsilon–delta definition is
$$
\forall\varepsilon>0\ \exists\delta>0\ \forall h:
\quad 0<|h|<\delta
\ \Longrightarrow\
\left|\frac{f(a+h)-f(a)}h-f'(a)\right|<\varepsilon,
$$
for allowed increments $h$ with $a+h$ in the domain.

Define the error in the linear approximation by
$$R(h)=f(a+h)-f(a)-hf'(a).$$
Then the preceding condition says exactly that $R(h)/h\to0$. Thus
$$f(a+h)=f(a)+hf'(a)+o(h).$$
The error is negligible **relative to the increment** $h$, rather than merely small in absolute size.

For $f(x)=x^2$,
$$f(a+h)=a^2+2ah+h^2.$$
Here $f'(a)=2a$, and the remainder $h^2$ is $o(h)$ because $h^2/h=h\to0$.

An $O(h)$ error alone is insufficient. For $f(x)=|x|$ at $0$, the remainder after subtracting the candidate linear term $0h$ is $|h|=O(h)$, but
$$\frac{|h|}{h}=
\begin{cases}
1,&h>0,\\
-1,&h<0.
\end{cases}$$
It is not $o(h)$, and the derivative does not exist.

## 7. Notation details that matter

The equality signs in $f=O(g)$ and $f=o(g)$ mean “has this bound/order”, not equality to a single function named $O(g)$. Writing
$$F(x)=A(x)+O(g(x))$$
means that the actual remainder $F(x)-A(x)$ satisfies the big-$O$ condition. The analogous interpretation applies to $o(g)$.

Use absolute values: a very negative value can still have large magnitude. Check that the quotient $f/g$ is defined before using it. If $g$ has zeros arbitrarily near the limiting point, use the inequality definitions directly; they also require $f=0$ at those zeros within the relevant neighbourhood.

In the limit definition, using $\le\varepsilon$ instead of $<\varepsilon$ gives the same notion: apply the non-strict version with $\varepsilon/2$ to obtain a strict bound by $\varepsilon$. For little $o$, the same argument applies wherever $g(x)\ne0$. At zeros of $g$, retain the non-strict formulation $|f|\le\varepsilon|g|$, which permits $f=g=0$; the strict inequality would fail there.

The two questions to ask when reading any $O$ or $o$ statement are: **“As the variable approaches what?”** and **“Compared with which function?”**
