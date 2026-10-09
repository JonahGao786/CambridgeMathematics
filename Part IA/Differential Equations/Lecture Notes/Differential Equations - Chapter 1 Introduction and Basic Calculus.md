---
title: Differential Equations - Chapter 1 Introduction and Basic Calculus
material_type: handwritten lecture notes
course: Part IA Differential Equations
date: null
source_file: Ch.1 Introduction.pdf
drive_file_id: 1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs
source_url: https://drive.google.com/file/d/1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs/view
source_pages: 8
---

# Differential Equations — Introduction and Basic Calculus

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs/view). No date is supplied.

For an expanded introduction requested alongside this transcription, see [[Limits, Big O and Little o - A First-Year Guide]]. The definitions and examples below follow the lecture source.

## 0. Introduction (page 1)

Differential equations appear in almost all branches of science and applied mathematics. For example,
$$m\frac{d^2x}{dt^2}=F(x,t),$$
where $m$ is the mass of the particle and $F$ is the force. The equation relates the rate of change of position $x$, the **dependent variable**, to time $t$, the **independent variable**.

How do we solve equations like these?

## 1. Basic calculus

### 1.1 Differentiation (page 2)

The derivative of $f$ with respect to its argument $x$ is given, when the limit exists, by
$$\frac{df}{dx}(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.$$

The secant slope between $x_0$ and $x_0+h$ is
$$\frac{f(x_0+h)-f(x_0)}{h}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.15,0)--(5,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,3.8) node[above] {$f(x)$};
  \draw[thick,domain=0.45:3.7,samples=60] plot (\x,{0.22*\x*\x+0.25}) node[above] {$f(x)$};
  \draw[blue,thick,domain=0.75:3.8] plot (\x,{0.99*\x-0.6212});
  \draw (1.2,0.06)--(1.2,-0.06) node[below,blue] {$x_0$};
  \draw (3.3,0.06)--(3.3,-0.06) node[below,blue] {$x_0+h$};
  \node[blue,right] at (3.55,1.7) {slope $=\frac{f(x_0+h)-f(x_0)}{h}$};
\end{tikzpicture}
\end{document}
```

### Aside: limits (pages 2–3)

Informally, $\lim_{x\to x_0}f(x)=A$ means that $f(x)$ can be made arbitrarily close to $A$ by making $x$ sufficiently close to $x_0$. We do not require $f(x_0)=A$. The limit describes behaviour near $x_0$, excluding the point itself.

For $f$ defined on an open interval containing $x_0$, except possibly at $x_0$,
$$\lim_{x\to x_0}f(x)=A$$
means
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x:
\quad 0<|x-x_0|<\delta\ \Longrightarrow\ |f(x)-A|<\varepsilon.$$
The right-hand limit uses $0<x-x_0<\delta$ instead of $0<|x-x_0|<\delta$.

At infinity,
$$\lim_{x\to+\infty}f(x)=A$$
means
$$\forall\varepsilon>0\ \exists X>0\ \forall x>X:
\quad |f(x)-A|<\varepsilon.$$

The lecture states the following properties; proofs are deferred to Analysis I:

- If a limit exists at a point, it is unique.
- If $\lim_{x\to x_0}f(x)=A$ and $\lim_{x\to x_0}g(x)=B$, then
  $$\lim_{x\to x_0}(f(x)+g(x))=A+B,$$
  $$\lim_{x\to x_0}f(x)g(x)=AB,$$
  $$\lim_{x\to x_0}\frac{f(x)}{g(x)}=\frac AB\qquad(B\ne0).$$

If $B=0$ and $A\ne0$, the quotient has no finite real limit (where it is defined near the limiting point). If $A=B=0$, this is an indeterminate case: a quotient limit may exist.

### One-sided derivatives and notation (page 4)

At an interior point, the derivative exists only when the left- and right-hand difference-quotient limits exist as finite real numbers and agree.

For example, $f(x)=|x|$ is differentiable away from $0$, but not at $0$:
$$\lim_{h\to0^-}\frac{|h|}{h}=-1,\qquad
\lim_{h\to0^+}\frac{|h|}{h}=1.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-2.5,0)--(2.5,0) node[right] {$x$};
  \draw[->] (0,-0.3)--(0,2.6) node[above] {$y$};
  \draw[thick] (-2.1,2.1)--(0,0)--(2.1,2.1);
  \node[below right] at (0,0) {$0$};
  \node[right] at (1.5,1.5) {$y=|x|$};
\end{tikzpicture}
\end{document}
```

The notation given is
$$\frac{df}{dx}=f'(x)=\dot f(x),$$
and, when higher derivatives exist,
$$\frac d{dx}\left(\frac{df}{dx}\right)=\frac{d^2f}{dx^2}=f''(x)=\ddot f(x),\qquad
\frac{d^nf}{dx^n}=f^{(n)}(x).$$

### Big $O$ notation (pages 5–6)

Big $O$ compares the size of functions near a limiting point: “can be bounded by”.

For finite $x_0$, $f(x)=O(g(x))$ as $x\to x_0$ means
$$\exists\delta>0\ \exists\mu>0\ \forall x:
\quad 0<|x-x_0|<\delta\ \Longrightarrow\ |f(x)|\le\mu|g(x)|.$$
Where $g(x)\ne0$, this says $|f(x)/g(x)|\le\mu$: the ratio is bounded.

Examples as $x\to0$:
$$x\ne O(x^2),\qquad x^2=O(x).$$
For $x\to0^+$,
$$x=O(\sqrt{x}).$$

The source sketch compares $x^2$ (red), $x$ (black), and $\sqrt{x}$ (blue) on the positive side:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.1,0)--(2.7,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,2.9) node[above] {$y$};
  \draw[red,thick,domain=0:1.6,samples=70] plot (\x,{\x*\x}) node[above] {$x^2$};
  \draw[thick] (0,0)--(2.4,2.4) node[right] {$x$};
  \draw[blue,thick,domain=0:2.3,samples=100] plot (\x,{sqrt(\x)}) node[right] {$\sqrt{x}$};
\end{tikzpicture}
\end{document}
```

Another example is
$$\sin(2x)=O(x)\quad(x\to0),$$
since $|\sin(2x)|\le2|x|$. The lecture's bound for sine uses
$$\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots.$$
For $0\le x\le1$,
$$\frac{x^3}{3!}\ge\frac{x^5}{5!}\ge\frac{x^7}{7!}\ge\cdots,$$
so grouping the subtracted pairs gives $\sin x\le x$, and $|\sin x|\le x$ on this interval. For $x>1$, $|\sin x|\le1<x$. Using oddness for negative $x$ gives $|\sin x|\le|x|$ for all real $x$.

At infinity, $f(x)=O(g(x))$ as $x\to+\infty$ means
$$\exists x_1\ \exists\mu>0\ \forall x>x_1:
\quad |f(x)|\le\mu|g(x)|.$$
For example,
$$2x^3+4x=O(x^3)\quad(x\to+\infty),$$
because for $x>1$,
$$|2x^3+4x|\le2|x^3|+4|x|\le6|x^3|.$$

### Little $o$ notation (page 6)

Little $o$ means “much smaller than”; the source sometimes underlines $o$ to distinguish it from $O$.

For finite $x_0$, $f(x)=o(g(x))$ as $x\to x_0$ means
$$\forall\varepsilon>0\ \exists\delta>0\ \forall x:
\quad 0<|x-x_0|<\delta\ \Longrightarrow\ |f(x)|\le\varepsilon|g(x)|.$$
If $g$ is non-zero in a punctured neighbourhood of $x_0$, this is equivalent to
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}=0.$$

Examples:
$$x^2=o(x)\quad(x\to0),\qquad \sqrt{x}=o(x)\quad(x\to+\infty).$$
For the first,
$$\lim_{x\to0}\frac{x^2}{x}=0.$$

### Remainders and differentiability (page 7)

Little $o$ is stronger than big $O$:
$$f=o(g)\ \Longrightarrow\ f=O(g),$$
but not conversely. For example, $2x=O(x)$ but $2x\ne o(x)$ as $x\to0$.

Non-zero constant factors do not change the order: if $f=O(g)$, then for any fixed $a\ne0$,
$$af=O(g),\qquad f=O(ag).$$

Write
$$f(x_0+h)-f(x_0)=hf'(x_0)+E(h),$$
where $E(h)$ is the remainder. From the definition of the derivative,
$$\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}h
=f'(x_0)+\lim_{h\to0}\frac{E(h)}h,$$
and the last limit is zero. Hence $E(h)=o(h)$, and
$$f(x_0+h)=f(x_0)+hf'(x_0)+o(h)\qquad(h\to0).$$

### 1.2 Rules for differentiation: chain rule (page 8)

For $f(x)=F(g(x))$, with $g$ differentiable at $x$ and $F$ differentiable at $g(x)$,
$$\frac{df}{dx}=F'(g(x))\frac{dg}{dx}
=\frac{dF}{dg}\frac{dg}{dx}.$$
Here $F'(g(x))$ is the derivative of $F$ with respect to its own argument, evaluated at $g(x)$. No proof is supplied in this PDF.
