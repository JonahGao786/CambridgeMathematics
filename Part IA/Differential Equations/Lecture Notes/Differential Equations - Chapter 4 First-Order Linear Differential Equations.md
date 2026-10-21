---
title: Differential Equations - Chapter 4 First-Order Linear Differential Equations
material_type: handwritten lecture notes with brief scope clarifications
course: Part IA Differential Equations
date: null
source_file: Ch.4 First-order Linear Differential Equations.pdf
drive_file_id: 1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3
source_url: https://drive.google.com/file/d/1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3/view
source_pages: 5
---

# Differential Equations — Chapter 4: First-Order Linear Differential Equations

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3/view), five pages. No date is supplied.

## Terminology (page 1)

- The **order** of a differential equation is the order of its highest derivative.
- A differential equation is **linear** when the dependent variable and its derivatives appear linearly.
- An **ordinary differential equation (ODE)** involves a function of one independent variable.

For example,
$$x^2y+y'=0$$
is a first-order linear ODE. The coefficient $x^2$ does not make it nonlinear in $y$.

## 1. Prelude: the exponential function (pages 1–2)

The source defines the exponential by the infinite series
$$\exp(x)=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
=\sum_{n=0}^\infty\frac{x^n}{n!}.$$
It also gives
$$\exp(x)=\lim_{k\to\infty}\left(1+\frac{x}{k}\right)^k.$$
The displayed binomial calculation is
$$\left(1+\frac{x}{k}\right)^k
=1+k\frac{x}{k}
+\frac{k(k-1)}{2!}\left(\frac{x}{k}\right)^2+\cdots,$$
followed by the limit $1+x+x^2/2!+\cdots$.

**Differentiation of the series (page 1).**
$$\frac{d}{dx}\exp(x)
=1+2\frac{x}{2!}+3\frac{x^2}{3!}+\cdots
=\exp(x).$$
The binomial-limit passage and termwise differentiation are presented as calculations; their convergence and interchange justifications are not supplied here.

The source also describes $\exp$ as the solution of
$$f'=f,\qquad f(0)=1.$$
No existence or uniqueness proof is supplied.

### Exponential laws and logarithms (page 2)

The key property is
$$\exp(x_1)\exp(x_2)=\exp(x_1+x_2).$$
The source refers to lecture notes for the proof. Thus one writes $\exp(x)=e^x$, where
$$e=\exp(1)=\lim_{k\to\infty}\left(1+\frac1k\right)^k
\approx2.718\ldots.$$
The logarithm is the inverse on positive real inputs:
$$\exp(\ln x)=x\qquad(x>0).$$
For $a>0$,
$$a^x=(e^{\ln a})^x=e^{x\ln a},$$
and hence
$$\frac{d}{dx}a^x
=\ln a\,e^{x\ln a}=a^x\ln a.$$
See [[Complex Exponential and Trigonometric Functions]] for related exponential material.

### Eigenfunctions of differentiation (page 2)

A non-zero function $f$ is an **eigenfunction** of the derivative operator if
$$\frac{d}{dx}f=\lambda f$$
for a constant $\lambda$, its **eigenvalue**. The function is preserved up to multiplication by that scalar. For example,
$$\frac{d}{dx}e^{\lambda x}=\lambda e^{\lambda x},$$
so $e^{\lambda x}$ is an eigenfunction with eigenvalue $\lambda$.

## 2. First-order linear ODEs (page 3)

The source states: “An $n$th-order linear ODE has $n$ linearly independent solutions.”

**Scope of the statement.** For a homogeneous linear equation on an interval, with continuous coefficients and a leading coefficient that never vanishes, there are $n$ linearly independent solutions; every solution is a linear combination of them. For an inhomogeneous equation, add one particular solution to a general homogeneous solution. The general theorem is stated here without proof; the first-order example below illustrates the idea.

### Linear dependence and independence of functions (page 3)

Functions $f_1,\ldots,f_N$ on a common domain are **linearly dependent** if there are constants $C_1,\ldots,C_N$, not all zero, such that
$$\sum_{i=1}^N C_if_i(x)=0\qquad\text{for every }x.$$
Otherwise they are **linearly independent**: the only such constants are all zero.

Equivalently, dependence means that at least one function can be written as a linear combination of the others. This parallels linear dependence of vectors.

### Homogeneous equations (page 3)

For a linear ODE, **homogeneous** means that every term involves the dependent variable or one of its derivatives, with no independent forcing term. The zero function is a trivial solution.

For any linear homogeneous ODE, a constant multiple of a solution is also a solution.

## 2.1 Homogeneous linear ODEs with constant coefficients (pages 3–4)

With **constant coefficients**, the independent variable does not appear explicitly in the coefficients. The source says to look for exponential solutions $e^{\lambda x}$. It notes that solutions of higher-order equations may involve linear combinations and polynomial factors such as $x^2e^{\lambda x}$, including the case $\lambda=0$. No general higher-order method is developed here.

### Example (page 4)

Solve
$$5\frac{dy}{dx}-3y=0.$$
Try $y=Ae^{\lambda x}$. Substitution gives
$$5\lambda Ae^{\lambda x}-3Ae^{\lambda x}=0.$$
For $A\ne0$, this gives the **characteristic equation**
$$5\lambda-3=0.$$
Thus $\lambda=3/5$, and the source identifies the general solution as
$$y(x)=Ae^{3x/5},\qquad A\text{ constant}.$$
The value $A=0$ includes the zero solution.

Under the conditions above, $n$ initial values $y(x_0),\ldots,y^{(n-1)}(x_0)$ at one point determine a solution. Boundary conditions at different points need a separate check. For this first-order example, one initial value fixes the one constant:
$$y(0)=y_0\quad\Longrightarrow\quad A=y_0.$$
See [[First-Order Linear Differential Equations]].

## Discrete equations and forward Euler (pages 4–5)

It can be useful to evaluate a function at discrete points. For the same example with $y(0)=y_0$, take a grid
$$x_n=nh,\qquad x_0=0,\qquad h>0.$$
For sampled values, the forward-difference approximation is
$$\left.\frac{dy}{dx}\right|_{x_n}
\approx\frac{y_{n+1}-y_n}{h}.$$
The source writes $y_n=y(x_n)$. When the difference equation is used as a numerical scheme, $y_n$ denotes an approximation to that sampled value.

The sketch shows sampled points, a blue secant between the samples at $x_1,x_2$, and the grid spacing $h$. The point at $x_3$ remains unjoined. This is a qualitative sketch, not an exact plot of a specified function.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (-0.15,0)--(5.3,0) node[right] {$x$};
  \draw[thick,->] (0,-0.12)--(0,3) node[above left] {$y$};
  \foreach \k in {0,1,2,3,4,5,6} {
    \draw[thick] ({0.8*\k},-0.055)--({0.8*\k},0.055);
  }
  \node[below] at (0,-0.08) {$x_0$};
  \node[below] at (0.8,-0.08) {$x_1$};
  \node[below] at (1.6,-0.08) {$x_2$};
  \node[below] at (2.4,-0.08) {$x_3$};
  \draw[blue!65!cyan,thick] (0.8,1.05)--(1.6,1.55);
  \fill (0,0.55) circle (1.4pt);
  \fill (0.8,1.05) circle (1.4pt);
  \fill (1.6,1.55) circle (1.4pt);
  \fill (2.4,1.6) circle (1.4pt);
  \node[blue!65!cyan,above right] at (1.55,2.15) {approx.\ to derivative};
  \draw[blue!65!cyan,thick,->] (1.5,2.12)
    to[out=215,in=100] (1.13,1.46);
  \draw[blue!65!cyan,thick,<->] (0,-0.65)--(0.8,-0.65)
    node[midway,below] {$h$};
\end{tikzpicture}
\end{document}
```

Imposing the discretized equation gives
$$5\left(\frac{y_{n+1}-y_n}{h}\right)-3y_n=0,$$
so
$$y_{n+1}=\left(1+\frac{3h}{5}\right)y_n.$$
This is a **recurrence relation**. Iterating,
$$\begin{aligned}
y_n
&=\left(1+\frac{3h}{5}\right)y_{n-1}\\
&=\left(1+\frac{3h}{5}\right)^2y_{n-2}\\
&=\left(1+\frac{3h}{5}\right)^ny_0.
\end{aligned}$$
The PDF ends after this expression. It supplies no error or convergence analysis. See [[Forward Euler Method]].
