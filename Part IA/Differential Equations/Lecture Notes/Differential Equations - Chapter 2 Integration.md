---
title: Differential Equations - Chapter 2 Integration
course: Part IA Differential Equations
material_type: lecture notes
chapter: 2
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: 7
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 2: Integration

> [!abstract] Overview
> Reviews integration as "area under a curve" (Riemann sums) and as the "inverse of differentiation" (fundamental theorem of calculus), then the techniques of substitution and integration by parts.
> Prerequisite: [[Differential Equations - Chapter 1 Introduction and Basic Calculus]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Integral as a Riemann sum]] | $\int_a^bf=\lim\sum f(x_n)\Delta x$; Riemann integrable | 1 |
| [[#Relation to area under the curve]] | $A=\int_a^bf\,dx$ | 2–3 |
| [[#Theorem — Fundamental theorem of calculus]] | $\frac d{dx}\int_a^xf(t)\,dt=f(x)$ | 3 |
| [[#Corollaries]] | variable lower/upper limits; indefinite integrals | 4 |
| [[#Substitution]] | inner-function substitution | 5 |
| [[#Trigonometric and hyperbolic substitutions]] | table of substitutions | 5–6 |
| [[#Integration by parts]] | $\int uv'=uv-\int u'v$ | 7 |

## 2.1 Integral as Riemann sums

### Definition — Integral as a Riemann sum

The integral of a (suitably well defined) function $f(x)$ is the limit of a sum, e.g.
$$\int_a^bf(x)\,dx=\lim_{N\to\infty}\sum_{n=0}^{N-1}f(x_n)\,\Delta x,\qquad\Delta x=\frac{b-a}N,\quad x_n=a+n\Delta x.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.2,0)--(5.8,0);
  \draw[->] (0,-0.2)--(0,3.5);
  \foreach \x/\h in {1/0.5500,1.5/0.5952,2/0.6972,2.5/0.8701,3/1.1278,3.5/1.4844,4/1.9538} \draw (\x,0) rectangle (\x+0.5,\h);
  \draw (4.5,0)--(4.5,2.55);
  \draw[red,thick] (0.55,0.50) .. controls (0.70,0.51) and (0.86,0.536) .. (1,0.55)
    .. controls (2.166667,0.60) and (3.333333,1.00) .. (4.5,2.55)
    .. controls (4.65,2.76) and (4.78,2.99) .. (4.9,3.2);
  \node[below] at (1,0) {$a$};
  \node[below] at (4.5,0) {$b$};
  \draw[blue,<->] (2.5,1.4)--(3,1.4) node[midway,above] {$\Delta x$};
  \node[blue] at (3.25,-0.85) {$x_n$};
  \draw[blue,->] (3.05,-0.75) .. controls (2.65,-0.6) and (2.55,-0.35) .. (2.5,-0.08);
\end{tikzpicture}
\end{document}
```

$f$ is **Riemann integrable** if the generalised Riemann sum doesn't depend on exactly how we choose the rectangles ($\Delta x$ not uniform, heights not necessarily from the left-hand side, etc.) in the limit that all $\Delta x\to0$.

### Relation to area under the curve

Consider one strip from $x_n$ to $x_{n+1}$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \begin{scope}
    \clip (1.3,0)--(1.3,0.7) .. controls (2,0.88) and (2.55,1.15) .. (3.3,1.65) --(3.3,0)--cycle;
    \foreach \x in {0.4,0.7,...,3.4} \draw[blue] (\x,0)--(\x+0.9,1.9);
  \end{scope}
  \draw[->] (-0.15,0)--(5,0);
  \draw[->] (0,0)--(0,3.3);
  \draw (1.3,0)--(1.3,0.7)--(3.3,0.7);
  \draw (3.3,0)--(3.3,1.65);
  \draw[red,thick] (0.7,0.59) .. controls (1,0.62) and (1.11,0.65) .. (1.3,0.7)
    .. controls (2,0.88) and (2.55,1.15) .. (3.3,1.65)
    .. controls (3.8,2.03) and (4.1,2.55) .. (4.6,3.15) node[right] {$f(x)$};
  \node[below] at (1.3,0) {$x_n$};
  \node[below] at (3.3,0) {$x_{n+1}$};
  \draw[<->] (1.3,2.05)--(3.3,2.05) node[midway,above] {$\Delta x$};
\end{tikzpicture}
\end{document}
```

From the mean value theorem (MVT, Analysis I), for $f$ continuous, the area under the curve from $x_n$ to $x_{n+1}$ is
$$A_n=(x_{n+1}-x_n)f(c_n),\qquad x_n<c_n<x_{n+1}.$$
If $f$ is differentiable,
$$f(c_n)=f(x_n)+O(c_n-x_n)=f(x_n)+O(\Delta x)\qquad(\text{since }\Delta x>c_n-x_n),$$
so $A_n=\Delta x\,f(x_n)+O((\Delta x)^2)$ as $\Delta x\to0$. The total area from $x=a$ to $b$ is
$$A=\lim_{N\to\infty}\sum_{n=0}^{N-1}A_n=\underbrace{\lim_{N\to\infty}\sum_{n=0}^{N-1}f(x_n)\Delta x}_{\text{definition of integral}}+\lim_{N\to\infty}\underbrace{N\,O\Big(\big(\tfrac{b-a}N\big)^2\Big)}_{O(1/N)}=\int_a^bf(x)\,dx+0.$$

> [!note] Explanation
> Summing $N$ error terms of size $O((\Delta x)^2)=O(1/N^2)$ gives $O(1/N)\to0$. This needs one bound that works for every strip at once (e.g. $|f'|\le M$ on $[a,b]$); the general statement for continuous $f$ is proved in Analysis I.

## 2.2 Fundamental theorem of calculus (FTC)

"Inverse of differentiation."

### Theorem — Fundamental theorem of calculus

Let $F(x)=\int_a^xf(t)\,dt$. Then
$$\frac{dF}{dx}=\frac d{dx}\int_a^xf(t)\,dt=f(x).$$

**Proof.**
$$\begin{aligned}
\frac{dF}{dx}&=\lim_{h\to0}\frac1h\Big(\int_a^{x+h}f(t)\,dt-\int_a^xf(t)\,dt\Big)=\lim_{h\to0}\frac1h\int_x^{x+h}f(t)\,dt\\
&=\lim_{h\to0}\frac1h\big(f(x)h+O(h^2)\big)&&\text{(MVT + Taylor's theorem)}\\
&=\lim_{h\to0}\big(f(x)+O(h)\big)=f(x).
\end{aligned}$$

**Note.** $F(x)$ is a solution to $\dfrac{dF}{dx}=f(x)$ with $F(a)=0$.

### Corollaries

$$\frac d{dx}\int_x^bf(t)\,dt=-f(x),\qquad\frac d{dx}\int_a^{g(x)}f(t)\,dt=\frac d{dx}F(g(x))=\frac{dF}{dg}\frac{dg}{dx}=f(g(x))\frac{dg}{dx}.$$

**Notation — indefinite integral.** $\int f(x)\,dx$ or $\int^xf(t)\,dt$ (an unspecified lower limit means there is an integration constant).

## 2.3 Integration techniques

### Substitution

If the integrand contains a function of a function, it might help to substitute for the inner function.

**Example.** $I=\displaystyle\int\frac{1-2x}{\sqrt{x-x^2}}\,dx$. Let $u=x-x^2$, so $\frac{du}{dx}=1-2x$ and
$$I=\int\frac{du}{\sqrt u}=2\sqrt u+C=2\sqrt{x-x^2}+C.$$

### Trigonometric and hyperbolic substitutions

Recall $\cos^2\theta+\sin^2\theta=1$, $1+\tan^2\theta=\sec^2\theta$, $\cosh^2u-\sinh^2u=1$, $1-\tanh^2u=\operatorname{sech}^2u$.

| Integrand contains | Substitution |
| --- | --- |
| $\sqrt{1-x^2}$ | $x=\sin\theta$ |
| $1+x^2$ | $x=\tan\theta$ |
| $\sqrt{x^2-1}$ | $x=\cosh u$ |
| $\sqrt{x^2+1}$ | $x=\sinh u$ |
| $1-x^2$ | $x=\tanh u$ |

**Example.** $I=\displaystyle\int\sqrt{2x-x^2}\,dx=\int\sqrt{1-(x-1)^2}\,dx$. Try $x-1=\sin\theta$, so $dx=\cos\theta\,d\theta$, with $-\frac\pi2\le\theta\le\frac\pi2$ so the choice is unique for $0\le x\le2$ (and $\cos\theta\ge0$):
$$\begin{aligned}
I&=\int\sqrt{\cos^2\theta}\,\cos\theta\,d\theta=\int\cos^2\theta\,d\theta=\int\Big(\frac12\cos2\theta+\frac12\Big)d\theta=\frac14\sin2\theta+\frac12\theta+C\\
&=\frac12\arcsin(x-1)+\frac12(x-1)\sqrt{1-(x-1)^2}+C,
\end{aligned}$$
with $\arcsin$ on the branch $[-\frac\pi2,\frac\pi2]$.

### Integration by parts

Recall the product rule $(uv)'=u'v+uv'$, so
$$\int uv'\,dx=uv-\int u'v\,dx.$$

**Examples.**
1. $u=x$, $v'=e^{-x}$:
   $$I=\int_0^\infty xe^{-x}\,dx=\big[-xe^{-x}\big]_0^\infty-\int_0^\infty-e^{-x}\,dx=\big[-e^{-x}\big]_0^\infty=1.$$
2. $u=\log x$ ($du=\frac{dx}x$), $dv=dx$ ($v=x$):
   $$I=\int\log x\,dx=x\log x-\int dx=x(\log x-1)+C.$$

The method also works for inverse trigonometric and hyperbolic functions.
