---
title: Differential Equations - Chapter 3 Partial Differentiation
course: Part IA Differential Equations
material_type: lecture notes
chapter: 3
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: 11
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 3: Partial Differentiation

> [!abstract] Overview
> Partial derivatives of functions of several variables, the multivariate chain rule (differential and integral forms), and its applications: change of variables, implicit differentiation (cyclic and reciprocal rules), and differentiating an integral with respect to a parameter.
> Prerequisites: [[Differential Equations - Chapter 1 Introduction and Basic Calculus]], [[Differential Equations - Chapter 2 Integration]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Partial derivative]] | $\left.\frac{\partial f}{\partial x}\right\rvert_y$ | 1–2 |
| [[#Theorem — Schwarz's theorem]] | $f_{xy}=f_{yx}$ for continuous second derivatives | 2 |
| [[#Theorem — Chain rule for partial derivatives]] | $df=f_x\,dx+f_y\,dy$; $\frac{df}{dt}=f_x\dot x+f_y\dot y$ | 3–4 |
| [[#Integral form of the chain rule]] | $\Delta f=\int(f_x\,dx+f_y\,dy)$ along a path | 4 |
| [[#Change of variables]] | Cartesian $\to$ polar | 5 |
| [[#Implicit differentiation]] | $\left.\frac{\partial z}{\partial x}\right\rvert_y=-\frac{f_x}{f_z}$ | 6–8 |
| [[#Cyclic rule]] | product of three derivatives $=-1$ | 8 |
| [[#Reciprocal rule]] | same variable held fixed | 9 |
| [[#Theorem — Differentiating an integral with respect to a parameter]] | Leibniz integral rule | 9–10 |

## 3.1 Functions of several variables

Generalise differentiation to functions of more than one independent variable: **multivariate functions**. E.g. the height of a terrain $h(x,y)$; the temperature in a room $T(x,y,z,t)$; the pressure of a gas as a function of volume and temperature.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.1,0)--(5.4,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,3.8) node[above] {$y$};
  \draw[thick] (0.65,1.2) .. controls (0.5,1.9) and (0.65,2.9) .. (1.25,3.1)
    .. controls (1.9,3.25) and (2.45,3.45) .. (2.95,3.1)
    .. controls (3.5,2.7) and (4.6,2.45) .. (4.65,1.8)
    .. controls (4.75,1.1) and (3.45,0.6) .. (2.6,0.65)
    .. controls (1.8,0.6) and (1.2,0.85) .. (0.65,1.2)--cycle;
  \draw (1.05,1.5) .. controls (0.95,2.05) and (1.15,2.65) .. (1.65,2.7)
    .. controls (2.25,2.78) and (2.75,2.8) .. (3.15,2.52)
    .. controls (3.6,2.25) and (4.08,1.95) .. (3.87,1.55)
    .. controls (3.4,1.05) and (2.8,0.8) .. (2.25,1.1)
    .. controls (1.8,1.4) and (1.35,1.25) .. (1.05,1.5)--cycle;
  \draw (1.55,1.9) .. controls (1.42,2.25) and (1.85,2.4) .. (2.3,2.4)
    .. controls (2.72,2.4) and (3.35,2.55) .. (3.2,2.15)
    .. controls (3,1.75) and (1.8,1.55) .. (1.55,1.9)--cycle;
  \draw (2.08,2.05) .. controls (2.3,2.22) and (2.65,2.25) .. (2.7,2.15)
    .. controls (2.65,1.99) and (2.15,1.92) .. (2.08,2.05)--cycle;
  \fill[red] (4.03,1.25) circle (1.5pt) node[above right] {$A$};
  \node at (6.25,3.45) {$f(x,y)$};
  \node[right] (level) at (5.65,2.6) {$f(x,y)=\mathrm{const.}$};
  \draw[->] (level.west)--(4.55,2.2);
\end{tikzpicture}
\end{document}
```
*Contour plot of $f(x,y)$.*

The slope at $A$ depends on direction. First, what happens along the coordinate directions?

## 3.2 Partial derivatives

### Definition — Partial derivative

The derivative of a multivariate function with respect to one variable, holding the others fixed. For $f(x,y)$, the **partial derivative** of $f$ with respect to $x$ at fixed $y$ is
$$\left.\frac{\partial f}{\partial x}\right|_y=\lim_{\delta x\to0}\frac{f(x+\delta x,y)-f(x,y)}{\delta x}$$
— "the slope of $f$ when moving in the $+x$ direction". $\left.\frac{\partial f}{\partial y}\right|_x$ is defined similarly.

**Example.** $f(x,y)=x^2+y^3+e^{xy^2}$:
$$\left.\frac{\partial f}{\partial x}\right|_y=2x+y^2e^{xy^2},\qquad\left.\frac{\partial f}{\partial y}\right|_x=3y^2+2yxe^{xy^2},\qquad\left.\frac{\partial^2f}{\partial x^2}\right|_y=2+y^4e^{xy^2},$$
and the mixed derivatives
$$\frac\partial{\partial x}\Big(\left.\frac{\partial f}{\partial y}\right|_x\Big)\Big|_y=2ye^{xy^2}+2y^3xe^{xy^2}=\frac\partial{\partial y}\Big(\left.\frac{\partial f}{\partial x}\right|_y\Big)\Big|_x\quad\text{(equal).}$$

**Notation.** Usually we omit $|_x$ etc.; $\partial$ implies **all other variables held fixed**. E.g. $\frac\partial{\partial x}\big(\frac{\partial f}{\partial y}\big|_x\big)\big|_y=\frac{\partial^2f}{\partial x\partial y}$. Alternatively $f_x=\frac{\partial f}{\partial x}$ and $f_{xy}=\frac{\partial^2f}{\partial y\,\partial x}$ — the $x$ derivative is taken first.

### Theorem — Schwarz's theorem

If $f$ has continuous second derivatives, $\dfrac{\partial^2f}{\partial x\,\partial y}=\dfrac{\partial^2f}{\partial y\,\partial x}$.

**N.B.** For $f(x,y,z)$: $\frac{\partial f}{\partial x}=\left.\frac{\partial f}{\partial x}\right|_{y,z}\ne\left.\frac{\partial f}{\partial x}\right|_y$ in general.

## 3.3 Multivariate chain rule

Given a path $x(t),y(t)$ and $f(x,y)$, what is $\frac{df}{dt}$ along the path? Consider the change in $f$ under $(x,y)\to(x+\delta x,y+\delta y)$:
$$\delta f=f(x+\delta x,y+\delta y)-f(x,y)=\big[f(x+\delta x,y+\delta y)-f(x+\delta x,y)\big]+\big[f(x+\delta x,y)-f(x,y)\big].$$
By Taylor's theorem, as $\delta x,\delta y\to0$,
$$f(x+\delta x,y)-f(x,y)=f_x(x,y)\,\delta x+o(\delta x),$$
$$f(x+\delta x,y+\delta y)-f(x+\delta x,y)=f_y(x+\delta x,y)\,\delta y+o(\delta y),\qquad f_y(x+\delta x,y)=f_y(x,y)+f_{yx}(x,y)\,\delta x+o(\delta x).$$
Therefore
$$\delta f=f_y(x,y)\,\delta y+f_x(x,y)\,\delta x+f_{yx}(x,y)\,\delta x\,\delta y+\delta y\,o(\delta x)+o(\delta y)+o(\delta x).$$

Define the **differential** $df$ as $\lim_{\delta x,\delta y\to0}\delta f$ (meaning $\delta x,\delta y$ are infinitesimal, and so $\delta f$ is as well).

> [!note] Explanation
> Only the terms linear in $\delta x,\delta y$ survive in $df$; the product $\delta x\,\delta y$ and the $o(\cdot)$ terms are of higher order. This is why $df=f_x\,dx+f_y\,dy$.

### Theorem — Chain rule for partial derivatives

**Differential form:**
$$df=\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy.$$
**Along a path** $x(t),y(t)$:
$$\frac d{dt}f(x(t),y(t))=\lim_{\delta x,\delta y,\delta t\to0}\Big(\frac{\partial f}{\partial x}\frac{\delta x}{\delta t}+\frac{\partial f}{\partial y}\frac{\delta y}{\delta t}\Big)=\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}.$$
If instead the path is parametrised by the coordinate $x$, so $y(x)$:
$$\frac d{dx}f(x,y(x))=\frac{\partial f}{\partial x}\frac{dx}{dx}+\frac{\partial f}{\partial y}\frac{dy}{dx}=f_x+f_y\frac{dy}{dx}.$$

### Integral form of the chain rule

$$\Delta f=\int df=\int\Big(\frac{\partial f}{\partial x}dx+\frac{\partial f}{\partial y}dy\Big),$$
where $\Delta f$ is the change in $f$ between the end points (we need to integrate along a given path). For $f(x(t),y(t))$:
$$\Delta f=\int\Big(\frac{\partial f}{\partial x}\frac{dx}{dt}+\frac{\partial f}{\partial y}\frac{dy}{dt}\Big)dt.$$

## 3.4 Applications of the multivariate chain rule

### Change of variables

It is often useful to write a (differential) equation in a different coordinate system before solving. E.g. Cartesian $(x,y)\to$ polar $(r,\theta)$, $x=r\cos\theta$, $y=r\sin\theta$:

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.15,0)--(4,0) node[right] {$x$};
  \draw[->] (0,-0.15)--(0,2.8) node[above] {$y$};
  \draw[red,thick] (0,0)--(2.5,1.4) node[midway,above] {$r$};
  \fill (2.5,1.4) circle (1.2pt) node[above right] {$(x,y)$};
  \draw (0.6,0) arc (0:29.25:0.6);
  \node at (0.9,0.23) {$\theta$};
\end{tikzpicture}
\end{document}
```

Think of $f(x,y)$ as $f(x(r,\theta),y(r,\theta))$. From the chain rule,
$$\left.\frac{\partial f}{\partial r}\right|_\theta=\left.\frac{\partial f}{\partial x}\right|_y\underbrace{\left.\frac{\partial x}{\partial r}\right|_\theta}_{\cos\theta}+\left.\frac{\partial f}{\partial y}\right|_x\underbrace{\left.\frac{\partial y}{\partial r}\right|_\theta}_{\sin\theta},\qquad\left.\frac{\partial f}{\partial\theta}\right|_r=\left.\frac{\partial f}{\partial x}\right|_y\underbrace{\left.\frac{\partial x}{\partial\theta}\right|_r}_{-r\sin\theta}+\left.\frac{\partial f}{\partial y}\right|_x\underbrace{\left.\frac{\partial y}{\partial\theta}\right|_r}_{r\cos\theta}.$$

### Implicit differentiation

First generalise the chain rule: for $f(x,y,z)$,
$$df=\left.\frac{\partial f}{\partial x}\right|_{y,z}dx+\left.\frac{\partial f}{\partial y}\right|_{x,z}dy+\left.\frac{\partial f}{\partial z}\right|_{x,y}dz.$$
$f(x,y,z)=\text{const.}$ is a surface in 3D space.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (0,0)--(0,3.2) node[above] {$z$};
  \draw[->] (0,0)--(3,-0.9) node[right] {$x$};
  \draw[->] (0,0)--(2.9,1.4) node[right] {$y$};
  \draw[blue,thick] (1.5,1.4) ellipse (0.85 and 1);
  \draw[blue] (0.72,1.78) .. controls (1.1,1.5) and (1.9,1.5) .. (2.28,1.78);
  \draw[blue] (0.65,1.4) .. controls (1.05,1.05) and (1.95,1.05) .. (2.35,1.4);
  \draw[blue] (0.8,0.85) .. controls (1.2,0.65) and (1.9,0.65) .. (2.2,0.85);
  \draw[blue] (1.18,2.33) .. controls (0.92,1.7) and (0.92,1) .. (1.18,0.47);
  \draw[blue] (1.82,2.33) .. controls (2.08,1.7) and (2.08,1) .. (1.82,0.47);
  \node[blue,right] (level) at (3.3,2.7) {$f(x,y,z)=\mathrm{const.}$};
  \draw[blue,->] (level.west)--(2.05,2.13);
\end{tikzpicture}
\end{document}
```

It implicitly defines $z=z(x,y)$, $x=x(y,z)$, $y=y(x,z)$, but we may not be able to find them explicitly.

**Example.** $xy+y^2z+z^5=1\quad(*)$. We can't find $z(x,y)$ explicitly, but can still evaluate e.g. $\left.\frac{\partial z}{\partial x}\right|_y$: differentiate $(*)$ with respect to $x$ holding $y$ fixed,
$$y+y^2\left.\frac{\partial z}{\partial x}\right|_y+5z^4\left.\frac{\partial z}{\partial x}\right|_y=0\quad\Longrightarrow\quad\left.\frac{\partial z}{\partial x}\right|_y=\frac{-y}{y^2+5z^4}.$$
(N.B. $\left.\frac{\partial(*)}{\partial x}\right|_y\ne\left.\frac{\partial(*)}{\partial x}\right|_z$.)

**General formula.** If $f(x,y,z)=\text{const.}$, the chain rule gives
$$0=df=\left.\frac{\partial f}{\partial x}\right|_{y,z}dx+\left.\frac{\partial f}{\partial y}\right|_{x,z}dy+\left.\frac{\partial f}{\partial z}\right|_{x,y}dz:$$
we can't vary $x,y,z$ independently and stay on the surface.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (0,0)--(0,3.2) node[above] {$z$};
  \draw[->] (0,0)--(3.5,-1.2) node[right] {$x$};
  \draw[->] (0,0)--(3.5,1.55) node[above right] {$y$};
  \draw[red,thick] (0.6,1.4) .. controls (1.5,2.35) and (2.5,2.35) .. (3.2,1.7)
    .. controls (2.65,1.5) and (2.2,0.9) .. (2.2,0.3)
    .. controls (1.7,1.35) and (1,1.5) .. (0.6,1.4);
  \draw[blue,thick] (1.05,1.58) .. controls (1.5,1.62) and (1.85,1.45) .. (2,1.18);
  \draw[green!60!black,thick] (1.05,1.58)--(2,1.18);
  \draw[blue,dotted] (1.05,1.58)--(1.05,0.4)--(2,0)--(2,1.18);
  \node[red] (level) at (2.2,3) {$f=c$};
  \draw[red,->] (level.south) .. controls (1.9,2.7) and (1.9,2.4) .. (1.8,2.1);
  \node[blue,right] (on) at (4,1.25) {curve on the surface: $\left.\frac{\partial f}{\partial x}\right|_y=0$};
  \draw[blue,->] (on.west) .. controls (3.5,1.9) and (2.7,1.8) .. (2.15,1.55);
  \node[green!60!black,right] (off) at (3.8,-0.35) {$\left.\frac{\partial f}{\partial x}\right|_{y,z}\ne0$ (not on surface)};
  \draw[green!60!black,->] (3.05,-0.3) .. controls (2.15,0.05) and (1.65,0.6) .. (1.65,1.2);
\end{tikzpicture}
\end{document}
```

On the surface, with $y$ fixed and $z=z(x,y)$ not fixed:
$$0=\left.\frac{\partial f}{\partial x}\right|_y=\left.\frac{\partial f}{\partial x}\right|_{y,z}\underbrace{\left.\frac{\partial x}{\partial x}\right|_y}_{1}+\left.\frac{\partial f}{\partial y}\right|_{x,z}\underbrace{\left.\frac{\partial y}{\partial x}\right|_y}_{0}+\left.\frac{\partial f}{\partial z}\right|_{x,y}\left.\frac{\partial z}{\partial x}\right|_y,$$
so
$$\left.\frac{\partial z}{\partial x}\right|_y=-\frac{\left.\partial f/\partial x\right|_{y,z}}{\left.\partial f/\partial z\right|_{x,y}}.$$

### Cyclic rule

Similarly for $\left.\frac{\partial x}{\partial y}\right|_z$ and $\left.\frac{\partial y}{\partial z}\right|_x$; multiplying the three formulas,
$$\left.\frac{\partial x}{\partial y}\right|_z\left.\frac{\partial y}{\partial z}\right|_x\left.\frac{\partial z}{\partial x}\right|_y=-1.$$

### Reciprocal rule

Applies if the same variables are held fixed:
$$\left.\frac{\partial z}{\partial x}\right|_y=\frac1{\left.\partial x/\partial z\right|_y}.$$
(Prove by first showing $\left.\frac{\partial x}{\partial z}\right|_y=-\dfrac{\left.\partial f/\partial z\right|_{x,y}}{\left.\partial f/\partial x\right|_{y,z}}$, similarly to above.)

**N.B.** For $(r,\theta)\to(x,y)$: $\left.\frac{\partial r}{\partial x}\right|_y=\dfrac1{\left.\partial x/\partial r\right|_y}$, but $\left.\frac{\partial r}{\partial x}\right|_y\ne\dfrac1{\left.\partial x/\partial r\right|_\theta}$.

## 3.5 Differentiation of an integral with respect to a parameter

Consider a family of functions $f(x;c)$ with parameter $c$, and define $I(c)=\displaystyle\int_{a(c)}^{b(c)}f(x;c)\,dx$. What is $\frac{dI}{dc}$?

### Theorem — Differentiating an integral with respect to a parameter

$$\frac{dI}{dc}=\int_{a(c)}^{b(c)}\frac{\partial f}{\partial c}(x;c)\,dx+f(b(c);c)\frac{db}{dc}-f(a(c);c)\frac{da}{dc}.$$

**Proof.**
$$\frac{dI}{dc}=\lim_{\delta c\to0}\frac1{\delta c}\Big[\int_{a(c+\delta c)}^{b(c+\delta c)}f(x;c+\delta c)\,dx-\underbrace{\int_{a(c)}^{b(c)}f(x;c)\,dx}_{④}\Big].$$
Split the first integral as
$$\underbrace{\int_{a(c)}^{b(c)}}_{①}+\underbrace{\int_{b(c)}^{b(c+\delta c)}}_{②}-\underbrace{\int_{a(c)}^{a(c+\delta c)}}_{③}.$$
Then:

- ① + ④:
$$\lim_{\delta c\to0}\frac1{\delta c}\int_{a(c)}^{b(c)}\big(f(x;c+\delta c)-f(x;c)\big)dx=\int_{a(c)}^{b(c)}\frac{\partial f}{\partial c}(x;c)\,dx.$$
- ②:
$$\lim_{\delta c\to0}\frac1{\delta c}\int_{b(c)}^{b(c+\delta c)}f(x;c+\delta c)\,dx.$$
By the mean value theorem the integral is $[b(c+\delta c)-b(c)]\,f(\bar x;c+\delta c)$ with $b(c)<\bar x<b(c+\delta c)$, so
$$②=\frac{db}{dc}\,f(b(c);c).$$
- ③: the same trick gives $-\dfrac{da}{dc}\,f(a(c);c)$.

**Examples.**
1. $I(\lambda)=\displaystyle\int_0^\lambda e^{-\lambda x^2}dx$:
   $$\frac{dI}{d\lambda}=\int_0^\lambda-x^2e^{-\lambda x^2}dx+e^{-\lambda^3}\underbrace{\frac{d\lambda}{d\lambda}}_{1}.$$
2. Evaluate $J_n=\displaystyle\int_0^\infty x^ne^{-x}dx$. Let $I(\lambda)=\displaystyle\int_0^\infty e^{-\lambda x}dx=\frac1\lambda$ ($\lambda>0$). Then
   $$\frac{d^nI}{d\lambda^n}=\int_0^\infty(-x)^ne^{-\lambda x}dx\qquad\text{and}\qquad\frac{d^nI}{d\lambda^n}=(-1)^n\frac{n!}{\lambda^{n+1}}.$$
   These are equal, so setting $\lambda=1$: $(-1)^nJ_n=(-1)^nn!$, i.e. $J_n=n!$.
