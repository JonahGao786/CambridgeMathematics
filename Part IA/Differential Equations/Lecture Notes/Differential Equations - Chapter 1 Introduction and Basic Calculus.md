---
title: Differential Equations - Chapter 1 Introduction and Basic Calculus
course: Part IA Differential Equations
material_type: lecture notes
chapter: 1
source_file: Ch.1 Differentiation.pdf
drive_file_id: 1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr
source_url: https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view
source_pages: 13
additional_sources:
  - source_file: Ch.1 Introduction.pdf
    drive_file_id: 1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs
    source_url: https://drive.google.com/file/d/1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs/view
    source_pages: 8
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 1: Introduction and Basic Calculus

> [!abstract] Overview
> Derivatives as limits; the order notation $O$ and $o$; chain, product, quotient and Leibniz rules; Taylor's theorem with its two remainder forms; L'Hôpital's rule.
> *Ch.1 Introduction.pdf* is an earlier copy of pages 1–8 of *Ch.1 Differentiation.pdf* (pages 1–7 identical); page references are to the latter.

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Derivative]] | $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h$ | 2 |
| [[#Aside — Limits]] | $\varepsilon$–$\delta$ definition; algebra of limits | 2–3 |
| [[#Definition — Big O]] | bounded ratio | 5–6 |
| [[#Definition — Little o]] | ratio $\to0$ | 6–7 |
| [[#Remainder of the first-order approximation]] | $f(x_0+h)=f(x_0)+hf'(x_0)+o(h)$ | 7 |
| [[#Theorem — Chain rule]] | $\frac{df}{dx}=F'(g(x))\frac{dg}{dx}$ | 8 |
| [[#Theorem — Product rule]] | $(uv)'=u'v+uv'$; quotient rule | 8 |
| [[#Theorem — Leibniz's rule]] | $(uv)^{(n)}=\sum\binom nru^{(n-r)}v^{(r)}$ | 9 |
| [[#Theorem — Taylor's theorem]] | $E_n=o(h^n)$; Lagrange form $O(h^{n+1})$ | 10–11 |
| [[#Theorem — L'Hopital's rule]] | $\lim\frac fg=\lim\frac{f'}{g'}$ | 12–13 |

## 0 Introduction

Differential equations appear in almost all branches of science and applied maths. E.g.
$$m\frac{d^2x}{dt^2}=F(x,t)$$
($m$ the mass of the particle, $F$ the force) relates the rate of change of position $x$, the **dependent variable**, with time $t$, the **independent variable**. How do we solve equations like these?

## 1.1 Differentiation

### Definition — Derivative

The derivative of $f(x)$ with respect to its argument $x$ is the function given by the limit
$$\frac{df}{dx}=\lim_{h\to0}\frac{f(x+h)-f(x)}h.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.15,0)--(4.3,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,4.3) node[above] {$f(x)$};
  \draw[thick] (0.45,0.35) .. controls (0.95,0.42) .. (1.2,0.6)
    .. controls (2.2,1.03) and (2.9,1.8) .. (3.3,2.7)
    .. controls (3.5,3.15) and (3.7,3.65) .. (3.8,4.15) node[above] {$f(x)$};
  \draw[blue,thick] (0.7,0.1)--(3.8,3.2);
  \draw (1.2,0.06)--(1.2,-0.06) node[below,blue] {$x_0$};
  \draw (3.3,0.06)--(3.3,-0.06) node[below,blue] {$x_0+h$};
  \node[blue,right] at (4,1.8) {slope $=\frac{f(x_0+h)-f(x_0)}{h}$};
\end{tikzpicture}
\end{document}
```
*Secant through $x_0$ and $x_0+h$; curve schematic.*

### Aside — Limits

(See more in Analysis I.) Informally, $\lim_{x\to x_0}f(x)=A$ means $f(x)$ can be made arbitrarily close to $A$ by making $x$ sufficiently close to $x_0$. We don't require $f(x_0)=A$: the limit is a statement about the behaviour of $f$ near $x_0$, not at $x_0$.

More formally, for $f$ defined on an open interval containing $x_0$ (not necessarily at $x_0$), $\lim_{x\to x_0}f(x)=A$ means
$$\forall\varepsilon>0\ \exists\delta>0:\quad|f(x)-A|<\varepsilon\quad\forall\,0<|x-x_0|<\delta.$$
The **right-hand limit** replaces $0<|x-x_0|<\delta$ by $0<x-x_0<\delta$. **Limits at infinity:** $\lim_{x\to\infty}f(x)=A$ means $\forall\varepsilon>0\ \exists X>0$ with $|f(x)-A|<\varepsilon$ for all $x>X$.

Properties (proved in Analysis I):
- If $f$ has a limit at a point, it is unique.
- If $\lim f=A$ and $\lim g=B$ (as $x\to x_0$), then $\lim(f+g)=A+B$, $\lim fg=AB$, $\lim\frac fg=\frac AB$ for $B\ne0$.
- If $B=0$: the limit of the quotient does not exist if $A\ne0$, but may exist in the indeterminate case $A=B=0$.

**N.B.** For the derivative to exist, the left-hand ($h\to0^-$) and right-hand ($h\to0^+$) limits must exist and be equal. E.g. $|x|$ is not differentiable at $x=0$ (but is elsewhere): $\lim_{h\to0^-}\frac{|h|}h=-1$, $\lim_{h\to0^+}\frac{|h|}h=1$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=0.8]
  \draw[->] (-2.5,0)--(2.5,0) node[right] {$x$};
  \draw[->] (0,-0.3)--(0,2.6) node[above] {$y$};
  \draw[thick] (-2.1,2.1)--(0,0)--(2.1,2.1) node[right] {$y=|x|$};
\end{tikzpicture}
\end{document}
```

**Notation.** $\frac{df}{dx}=f'(x)=\dot f(x)$. Higher derivatives (for sufficiently smooth $f$): $\frac d{dx}\big(\frac{df}{dx}\big)=\frac{d^2f}{dx^2}=f''(x)=\ddot f(x)$; $n$th derivative $\frac{d^nf}{dx^n}=f^{(n)}(x)$.

## Big-O and little-o notation

These compare the behaviour of functions close to a limiting point $x_0$.

### Definition — Big O

"$O$" loosely means "can be bounded by".

**(a) $x_0$ finite.** $f(x)$ is $O(g(x))$ as $x\to x_0$ if
$$\exists\delta>0,\ \mu>0\ \text{ s.t. }\ \forall x\text{ with }0<|x-x_0|<\delta:\quad|f(x)|\le\mu|g(x)|.$$
Written $f(x)=O(g(x))$. It follows that $f/g$ is bounded as $x\to x_0$: $|f(x)|\le\mu|g(x)|\iff\left|\frac{f(x)}{g(x)}\right|\le\mu$.

**Examples** ($x_0=0$): $x\ne O(x^2)$ and $x^2=O(x)$ as $x\to0$; $x=O(\sqrt x)$ as $x\to0^+$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.2]
  \draw[->] (-0.1,0)--(2.7,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,2.9);
  \draw[red,thick,domain=0:1.6,samples=70] plot (\x,{\x*\x}) node[above] {$x^2$};
  \draw[thick] (0,0)--(2.4,2.4) node[right] {$x$};
  \draw[blue,thick,domain=0:2.3,samples=100] plot (\x,{sqrt(\x)}) node[right] {$\sqrt{x}$};
\end{tikzpicture}
\end{document}
```

**Example.** $\sin2x=O(x)$ as $x\to0$, since $|\sin2x|\le2|x|$ for all $x$. Indeed $\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots$, and for $0\le x\le1$, $\frac{x^3}{3!}\ge\frac{x^5}{5!}\ge\frac{x^7}{7!}\ge\cdots$, so
$$\sin x=x-\Big(\frac{x^3}{3!}-\frac{x^5}{5!}\Big)-\cdots\le x,\qquad\text{so }|\sin x|\le x\ (0\le x\le1).$$
For $x>1$, $|\sin x|\le1<x$. Thus $|\sin x|\le|x|$ for all $x\in\mathbb R$ (using that $\sin$ is odd).

**(b) $x_0=\infty$.** $f(x)$ is $O(g(x))$ as $x\to\infty$ if $\exists x_1$ and $\mu>0$ such that $|f(x)|\le\mu|g(x)|$ for all $x>x_1$. E.g. $2x^3+4x=O(x^3)$ as $x\to\infty$, since for $x>1$, $|2x^3+4x|\le2|x^3|+4|x|\le6|x^3|$.

### Definition — Little o

"$o$" loosely means "much smaller than" (often written $\underline{o}$ to distinguish it from $O$). For finite $x_0$: $f(x)$ is $o(g(x))$ as $x\to x_0$ if
$$\forall\varepsilon>0\ \exists\delta>0\ \text{ s.t. }\ \forall\,0<|x-x_0|<\delta:\quad|f(x)|\le\varepsilon|g(x)|.$$
If $g(x)\ne0$ near $x_0$, equivalently $\left|\frac{f(x)}{g(x)}\right|\le\varepsilon$, i.e. $\displaystyle\lim_{x\to x_0}\frac{f(x)}{g(x)}=0$.

**Examples.** $x^2=o(x)$ as $x\to0$ ($\lim x^2/x=0$); $\sqrt x=o(x)$ as $x\to\infty$.

**Notes.**
- $f=o(g)$ is stronger than $f=O(g)$: $o(g)\Rightarrow O(g)$, but not the other way round. E.g. $f(x)=2x$ is $O(x)$ as $x\to0$ but not $o(x)$.
- Constants don't matter: if $f=O(g)$ then $af=O(g)$ and $f=O(ag)$ for any non-zero constant $a$.

### Remainder of the first-order approximation

Order symbols are useful to classify remainder terms before taking limits. Write $f(x_0+h)-f(x_0)=hf'(x_0)+E(h)$. Then
$$\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}h=f'(x_0)+\lim_{h\to0}\frac{E(h)}h,$$
and the last limit is zero. So $E(h)=o(h)$ as $h\to0$:
$$f(x_0+h)=f(x_0)+hf'(x_0)+o(h)\qquad(h\to0).$$

## 1.2 Rules for differentiation

### Theorem — Chain rule

Given $f(x)=F(g(x))$,
$$\frac{df}{dx}=F'(g(x))\frac{dg}{dx}=\frac{dF}{dg}\cdot\frac{dg}{dx},$$
where $F'(g(x))$ is the derivative of $F$ with respect to its argument, evaluated at $g(x)$. E.g. $\frac d{dx}\sin(x^2-x+2)=\cos(x^2-x+2)\,(2x-1)$.

### Theorem — Product rule

Given $f(x)=u(x)v(x)$: $\dfrac{df}{dx}=u'(x)v(x)+u(x)v'(x)$.

**Quotient rule** (special case $v\to1/v$): $\dfrac d{dx}\Big(\dfrac uv\Big)=\dfrac{vu'-uv'}{v^2}$.

### Theorem — Leibniz's rule

(Generalisation of the product rule.) For $f=uv$: $f'=u'v+uv'$, $f''=u''v+2u'v'+uv''$, $f'''=u'''v+3u''v'+3u'v''+uv'''$ — cf. Pascal's triangle $1;\ 1\ 1;\ 1\ 2\ 1;\ 1\ 3\ 3\ 1$. In general
$$f^{(n)}(x)=\sum_{r=0}^n\binom nr u^{(n-r)}(x)\,v^{(r)}(x)=u^{(n)}v+nu^{(n-1)}v^{(1)}+\frac{n(n-1)}{2!}u^{(n-2)}v^{(2)}+\cdots+\frac{n!}{m!(n-m)!}u^{(n-m)}v^{(m)}+\cdots+uv^{(n)}.$$

## 1.3 Taylor series

For $f$ infinitely differentiable at $x_0$, the **Taylor series** about $x_0$ is the infinite series
$$T_f(x)=f(x_0)+(x-x_0)f'(x_0)+\frac1{2!}(x-x_0)^2f''(x_0)+\cdots.$$
The **Taylor polynomial** of degree $n$ about $x_0$,
$$P_n(x)=f(x_0)+(x-x_0)f'(x_0)+\cdots+\frac{(x-x_0)^n}{n!}f^{(n)}(x_0),$$
matches the first $n$ derivatives at $x_0$. How good an approximation is it? Last time: $f(x_0+h)=f(x_0)+hf'(x_0)+o(h)$. This extends to:

### Theorem — Taylor's theorem

For $f$ $n$-times differentiable at $x_0$,
$$f(x_0+h)=f(x_0)+hf'(x_0)+\frac{h^2}2f''(x_0)+\cdots+\frac{h^n}{n!}f^{(n)}(x_0)+E_n,\qquad E_n=o(h^n)\ \text{ as }h\to0.$$

**Stronger version.** If $f^{(n+1)}(x)$ exists for all $x\in(x_0,x_0+h)$ and is continuous there,
$$E_n=f^{(n+1)}(x_n)\frac{h^{n+1}}{(n+1)!}=O(h^{n+1})\quad\text{as }h\to0,\qquad\text{for some }x_n\text{ with }x_0\le x_n\le x_0+h.$$

**Note.** $E_n=O(h^{n+1})$ is stronger than $o(h^n)$: e.g. $h^{n+1/2}$ is $o(h^n)$ but not $O(h^{n+1})$ as $h\to0$.

With $x=x_0+h$, Taylor's theorem gives $f(x)=P_n(x)+E_n$: $P_n$ is a **local approximation** to $f$ near $x_0$ with error $o(h^n)$ or $O(h^{n+1})$. If $\lim_{n\to\infty}E_n=0$, the Taylor series converges to $f(x)$.

**Example.** $f(x)=e^x$ about $x_0=0$: $E_n=\frac{h^{n+1}}{(n+1)!}e^{x_n}$ with $0\le x_n\le h$ ($h>0$). The fractional error at $x=h$ is
$$\frac{E_n}{e^h}=\frac{h^{n+1}}{(n+1)!}\,e^{x_n-h}\le\frac{h^{n+1}}{(n+1)!}\qquad(0<e^{x_n-h}\le1).$$
For a given target accuracy at $x=h$, this specifies how large $n$ must be.

## 1.4 L'Hôpital's rule

This deals with limits of indeterminate forms.

### Theorem — L'Hopital's rule

Let $f,g$ be differentiable on an open interval containing $x_0$, with $g'(x)\ne0$ for $x\ne x_0$ in the interval, and suppose $\lim_{x\to x_0}f(x)=0=f(x_0)$ and $\lim_{x\to x_0}g(x)=0=g(x_0)$. Then
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{x\to x_0}\frac{f'(x)}{g'(x)},$$
provided the limit on the right exists.

**Proof** (under the more stringent conditions $g'(x_0)\ne0$ and $f',g'$ continuous). By Taylor's theorem, as $x\to x_0$,
$$f(x)=\underbrace{f(x_0)}_{=0}+(x-x_0)f'(x_0)+o(x-x_0),\qquad g(x)=\underbrace{g(x_0)}_{=0}+(x-x_0)g'(x_0)+o(x-x_0).$$
So
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{x\to x_0}\frac{f'(x_0)+\frac{o(x-x_0)}{x-x_0}}{g'(x_0)+\frac{o(x-x_0)}{x-x_0}}=\frac{f'(x_0)}{g'(x_0)}=\lim_{x\to x_0}\frac{f'(x)}{g'(x)}$$
by continuity of the first derivatives.

**Generalisation.** E.g. if also $f'(x_0)=g'(x_0)=0$, then $\lim\frac fg=\lim\frac{f''}{g''}$.

**Example.** $f(x)=3\sin x-\sin3x$, $g(x)=2x-\sin2x$. Here $f,f',f''$ and $g,g',g''$ all vanish at $0$, and $f'''(x)=-3\cos x+27\cos3x$, $g'''(x)=8\cos2x$, so
$$\lim_{x\to0}\frac{f(x)}{g(x)}=\frac{24}8=3.$$
