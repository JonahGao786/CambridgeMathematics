---
title: Differential Equations - Chapter 1 Introduction and Basic Calculus
material_type: handwritten lecture notes with labelled mathematical corrections and supplements
course: Part IA Differential Equations
date: null
source_file: Ch.1 Introduction.pdf
drive_file_id: 1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs
source_url: https://drive.google.com/file/d/1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs/view
source_pages: 8
additional_sources:
  - source_file: Ch.1 Differentiation.pdf
    drive_file_id: 1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr
    source_url: https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view
    source_pages: 13
---

# Differential Equations — Introduction and Basic Calculus

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1hu9l9bS2XJpa1IA9AN4ddMDLBggMxSVs/view). No date is supplied.

Expanded source: [Ch.1 Differentiation.pdf](https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view), 13 pages. Its pages 1–7 match the introduction PDF page by page; page 8 retains the chain rule and adds an example, the product rule and the quotient rule. Pages 9–13 supply the subsequent material below. Page references from the differentiation rules onward refer to this expanded source.

For an expanded introduction requested alongside this transcription, see [[Limits, Big O and Little o - A First-Year Guide]]. The definitions and examples below follow the lecture source.

## 0. Introduction (page 1)

Differential equations appear in almost all branches of science and applied mathematics. For example,
$$m\frac{d^2x}{dt^2}=F(x,t),$$
where $m$ is the mass of the particle and $F$ is the force. The equation relates the acceleration (the second derivative of position) to the force. Here $x$ is the **dependent variable** and time $t$ is the **independent variable**.

How do we solve equations like these?

## 1. Basic calculus

### 1.1 Differentiation (page 2)

The derivative of $f$ with respect to its argument $x$ is given, when the limit exists, by
$$\frac{df}{dx}(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.$$

The secant slope between $x_0$ and $x_0+h$ is
$$\frac{f(x_0+h)-f(x_0)}{h}.$$

The curve in the secant diagram is schematic; no formula for $f$ is specified.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.15,0)--(4.3,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,4.3) node[above] {$f(x)$};
  \draw[thick] (0.45,0.35)
    .. controls (0.7,0.35) and (0.95,0.42) .. (1.2,0.6)
    .. controls (2.2,1.03) and (2.9,1.8) .. (3.3,2.7)
    .. controls (3.5,3.15) and (3.7,3.65) .. (3.8,4.15)
    node[above] {$f(x)$};
  \draw[blue,thick] (0.7,0.1)--(3.8,3.2);
  \draw (1.2,0.06)--(1.2,-0.06) node[below,blue] {$x_0$};
  \draw (3.3,0.06)--(3.3,-0.06) node[below,blue] {$x_0+h$};
  \node[blue,right] at (4,1.8) {slope $=\frac{f(x_0+h)-f(x_0)}{h}$};
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

Little $o$ means “much smaller than”.

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

### 1.2 Rules for differentiation (pages 8–9)

#### Chain rule (page 8)

For $f(x)=F(g(x))$, with $g$ differentiable at $x$ and $F$ differentiable at $g(x)$,
$$\frac{df}{dx}=F'(g(x))\frac{dg}{dx}
=\frac{dF}{dg}\frac{dg}{dx}.$$
Here $F'(g(x))$ is the derivative of $F$ with respect to its own argument, evaluated at $g(x)$.

For example,
$$\frac d{dx}\sin(x^2-x+2)=\cos(x^2-x+2)(2x-1).$$

#### Product and quotient rules (page 8)

For differentiable $u,v$ and $f(x)=u(x)v(x)$,
$$f'(x)=u'(x)v(x)+u(x)v'(x).$$

Applying the product rule to $u(1/v)$ gives, wherever $v(x)\ne0$,
$$\frac d{dx}\left(\frac uv\right)=\frac{vu'-uv'}{v^2}.$$

#### Leibniz's rule (page 9)

Repeated differentiation of a product gives
$$\begin{aligned}
(uv)'&=u'v+uv',\\
(uv)''&=u''v+2u'v'+uv'',\\
(uv)'''&=u'''v+3u''v'+3u'v''+uv'''.
\end{aligned}$$
The coefficients follow Pascal's triangle:
$$\begin{array}{ccccccc}
&&&1&&&\\
&&1&&1&&\\
&1&&2&&1&\\
1&&3&&3&&1
\end{array}$$

**Theorem — Leibniz's rule.** If $u,v$ are $n$ times differentiable, then
$$f^{(n)}(x)=\sum_{r=0}^{n}\binom nr u^{(n-r)}(x)v^{(r)}(x).$$
In expanded form,
$$\begin{aligned}
f^{(n)}&=u^{(n)}v+nu^{(n-1)}v'
+\frac{n(n-1)}{2!}u^{(n-2)}v''+\cdots\\
&\quad+\frac{n!}{m!(n-m)!}u^{(n-m)}v^{(m)}+\cdots+uv^{(n)}.
\end{aligned}$$
No proofs of the chain, product, quotient or Leibniz rules are supplied here. See [[Differentiation Rules]] and the separately supplied product-rule proof in [[Differential Equations - Examples Sheet 1 Handwritten Proofs]].

### 1.3 Taylor series (pages 10–11)

For a function infinitely differentiable near $x_0$, its **Taylor series** about $x_0$ is
$$T_f(x)=\sum_{k=0}^{\infty}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
=f(x_0)+(x-x_0)f'(x_0)+\frac{(x-x_0)^2}{2!}f''(x_0)+\cdots.$$
This defines a series; equality to $f(x)$ requires a convergence and remainder argument.

The **Taylor polynomial** through degree $n$ is
$$P_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k.$$
It matches the value of $f$ and its first $n$ derivatives at $x_0$. How good an approximation is it?

The first-order result is
$$f(x_0+h)=f(x_0)+hf'(x_0)+o(h)\qquad(h\to0).$$

**Taylor's theorem — Peano remainder (page 10).** If $f$ is $n$ times differentiable at $x_0$ (the lower derivatives being defined nearby), then
$$f(x_0+h)=f(x_0)+hf'(x_0)+\frac{h^2}{2!}f''(x_0)+\cdots+
\frac{h^n}{n!}f^{(n)}(x_0)+E_n(h),$$
where
$$E_n(h)=o(h^n)\qquad(h\to0).$$

**Stronger version — Lagrange remainder (page 10).** If $f^{(n+1)}$ is continuous on a neighbourhood containing the segment between $x_0$ and $x_0+h$, then, for some $\xi_n$ on that segment,
$$E_n(h)=\frac{f^{(n+1)}(\xi_n)}{(n+1)!}h^{n+1}.$$
For fixed $n$, continuity makes this derivative bounded locally, giving
$$E_n(h)=O(h^{n+1})\qquad(h\to0).$$
For $h>0$, the interval is $x_0\le\xi_n\le x_0+h$; for $h<0$, its endpoints are reversed. No proof of either version is supplied in this source.

**Comparison of errors (page 11).** $O(h^{n+1})$ is stronger than $o(h^n)$. For example,
$$|h|^{n+1/2}=o(h^n),\qquad |h|^{n+1/2}\ne O(h^{n+1})\qquad(h\to0).$$

Writing $x=x_0+h$ gives
$$f(x)=P_n(x)+E_n(h).$$
Thus $P_n$ gives a local approximation near $x_0$, with either of the stated error bounds under the corresponding hypotheses. For fixed $x$, if the remainders tend to zero as $n\to\infty$, the Taylor series converges to $f(x)$. A small-$h$ estimate for fixed $n$ alone does not establish this.

**Example — $e^x$ about $0$ (page 11).** For $h>0$,
$$E_n(h)=\frac{h^{n+1}}{(n+1)!}e^{\xi_n},\qquad0\le\xi_n\le h.$$
The fractional error at $x=h$ satisfies
$$\frac{E_n(h)}{e^h}
=\frac{h^{n+1}}{(n+1)!}e^{\xi_n-h}
\le\frac{h^{n+1}}{(n+1)!},$$
since $0<e^{\xi_n-h}\le1$. For a chosen $h$ and target accuracy, this bound specifies how large $n$ must be.

See [[Taylor Series and Taylor's Theorem]] and [[Limits, Big O and Little o - A First-Year Guide]].

### 1.4 L'Hôpital's rule (pages 12–13)

The rule evaluates limits of indeterminate forms.

**Theorem — $0/0$ form (page 12).** Let $f,g$ be differentiable on an open interval containing $x_0$, with $g'(x)\ne0$ for $x\ne x_0$ in that interval. Suppose
$$\lim_{x\to x_0}f(x)=0,\qquad\lim_{x\to x_0}g(x)=0.$$
Because these functions are differentiable at $x_0$, the limits are also $f(x_0)=g(x_0)=0$. Then, provided the right-hand limit exists,
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}=
\lim_{x\to x_0}\frac{f'(x)}{g'(x)}.$$

**Proof under stronger hypotheses (page 12).** The supplied proof additionally assumes $g'(x_0)\ne0$ and continuity of the first derivatives near $x_0$. First-order Taylor expansions give
$$\begin{aligned}
f(x)&=f(x_0)+(x-x_0)f'(x_0)+o(x-x_0),\\
g(x)&=g(x_0)+(x-x_0)g'(x_0)+o(x-x_0).
\end{aligned}$$
Using $f(x_0)=g(x_0)=0$ and cancelling $x-x_0$ for $x\ne x_0$,
$$\begin{aligned}
\lim_{x\to x_0}\frac{f(x)}{g(x)}
&=\lim_{x\to x_0}
\frac{f'(x_0)+o(x-x_0)/(x-x_0)}
{g'(x_0)+o(x-x_0)/(x-x_0)}\\
&=\frac{f'(x_0)}{g'(x_0)}
=\lim_{x\to x_0}\frac{f'(x)}{g'(x)}.
\end{aligned}$$
The last equality uses continuity of the first derivatives. This source proof establishes only the stronger special case. The following supplementary argument proves the theorem as stated without these extra assumptions.

**Mean-value prerequisite — supplementary.** Rolle's theorem says that if $H$ is continuous on $[u,v]$, differentiable on $(u,v)$ and $H(u)=H(v)$, then $H'(c)=0$ for some $c\in(u,v)$. A constant function satisfies this immediately; otherwise continuity gives a maximum or minimum in the interior, where differentiability forces the derivative to vanish. The ordinary mean value theorem follows by applying Rolle's theorem to $H(t)$ minus the straight line joining its endpoint values.

**Proof under the stated hypotheses — supplementary.** Fix $x\ne x_0$ sufficiently near $x_0$. Since $g(x_0)=0$, Rolle's theorem shows $g(x)\ne0$: otherwise some point strictly between $x_0$ and $x$ would have $g'=0$, contrary to the hypothesis.

Apply Cauchy's mean value theorem to $f,g$ on the closed segment between $x_0$ and $x$. There exists $\xi_x$ strictly between them with
$$\frac{f(x)-f(x_0)}{g(x)-g(x_0)}=\frac{f'(\xi_x)}{g'(\xi_x)}.$$
For completeness, this follows from Rolle's theorem applied to
$$H(t)=(f(x)-f(x_0))(g(t)-g(x_0))
-(g(x)-g(x_0))(f(t)-f(x_0)),$$
which vanishes at both endpoints. The denominators are non-zero by the preceding argument and the hypothesis on $g'$.

Thus $f(x)/g(x)=f'(\xi_x)/g'(\xi_x)$. Since $0<|\xi_x-x_0|<|x-x_0|$, $\xi_x\to x_0$. The assumed derivative-quotient limit therefore gives the desired quotient limit. The same argument covers a finite limit or a limit of $+\infty$ or $-\infty$, and works on each side. Continuity of $f',g'$ and $g'(x_0)\ne0$ are not required.

**Repeated application (page 13).** If $f'(x_0)=g'(x_0)=0$ and the rule's hypotheses apply again to the derivative quotient, it may be applied a second time:
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}
=\lim_{x\to x_0}\frac{f''(x)}{g''(x)}.$$
Further applications also require the corresponding hypotheses.

**Example (page 13).** Let
$$f(x)=3\sin x-\sin(3x),\qquad g(x)=2x-\sin(2x).$$
Both functions and their first two derivatives vanish at $0$. The third derivatives written are
$$f'''(x)=-3\cos x+27\cos(3x),\qquad g'''(x)=8\cos(2x).$$
The source evaluates
$$\lim_{x\to0}\frac{3\sin x-\sin(3x)}{2x-\sin(2x)}
=\frac{24}{8}=3.$$
The derivative quotients satisfy the conditions for the three applications in a sufficiently small punctured neighbourhood of $0$.

See [[L'Hôpital's Rule]].
