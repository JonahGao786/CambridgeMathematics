---
title: Differential Equations - Chapter 4 First-Order Linear Differential Equations
course: Part IA Differential Equations
material_type: lecture notes
chapter: 4
source_file: Ch.4 First-order Linear Differential Equations.pdf
drive_file_id: 1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3
source_url: https://drive.google.com/file/d/1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3/view
source_pages: 10
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 4: First-Order Linear Differential Equations

> [!abstract] Overview
> Terminology for ODEs; the exponential function as the eigenfunction of $\frac d{dx}$; linear independence of functions; homogeneous linear ODEs with constant coefficients solved by $e^{\lambda x}$; forward Euler and its limit; series solutions; forced equations (particular integral + complementary function), with constant and eigenfunction forcing; non-constant coefficients via the integrating factor.
> Prerequisite: [[Differential Equations - Chapter 1 Introduction and Basic Calculus]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Terminology]] | order, linear, ordinary | 1 |
| [[#Definition — Exponential function]] | series; $\lim(1+\frac xk)^k$; solves $f'=f$, $f(0)=1$ | 1–2 |
| [[#Definition — Eigenfunction]] | $\frac{d}{dx}f=\lambda f$; $e^{\lambda x}$ | 2 |
| [[#Definition — Linear independence of functions]] | $\sum C_if_i=0\ \forall x\Rightarrow C_i=0$ | 3 |
| [[#Definition — Homogeneous ODE]] | every term involves $y$ | 3 |
| [[#Homogeneous linear ODEs with constant coefficients]] | try $y=Ae^{\lambda x}$; characteristic equation | 3–4 |
| [[#Discrete equations]] | forward Euler; recurrence relation; limit $n\to\infty$ | 4–5 |
| [[#Series solutions]] | $y=\sum a_nx^n$, recurrence for $a_n$ | 5–6 |
| [[#2.2 Forced equations]] | $y=y_p+y_c$ | 6 |
| [[#Constant forcing]] / [[#Eigenfunction forcing]] | try $y_p$ of the same form | 7–8 |
| [[#Non-constant coefficients — integrating factor]] | $\mu=\exp\int p$, $(\mu y)'=\mu f$ | 9–10 |

### Terminology

- **$n$th order** differential equation (DE): the highest-order derivative is $n$.
- **Linear**: the dependent variable appears linearly.
- **Ordinary**: involving a function of one variable.

E.g. $x^2y+y'=0$ is a first-order linear ordinary differential equation (ODE).

## 1 Prelude: the exponential function

### Definition — Exponential function

The exponential function is defined by the infinite series
$$\exp(x)=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots=\sum_{n=0}^\infty\frac{x^n}{n!}.$$
It can also be written (binomial theorem)
$$\exp(x)=\lim_{k\to\infty}\Big(1+\frac xk\Big)^k=\lim_{k\to\infty}\Big[1+\frac{kx}k+\frac{k(k-1)}{2!}\Big(\frac xk\Big)^2+\cdots\Big]=1+x+\frac{x^2}{2!}+\cdots.$$

**Differentiating the series:** $\dfrac d{dx}\exp(x)=1+\dfrac2{2!}x+\dfrac3{3!}x^2+\cdots=\exp(x)$. So we can **define** $\exp(x)$ to be the solution of the ODE
$$\frac{df}{dx}=f,\qquad f(0)=1.$$

**Key property:** $\exp(x_1)\exp(x_2)=\exp(x_1+x_2)$ (proof in the printed lecture notes; see also [[Vectors and Matrices - Chapter 1 Complex Numbers#Proposition — Properties of the exponential|V&M Ch.1]]). So we can write $\exp(x)=e^x$ with
$$e=\exp(1)=\lim_{k\to\infty}\Big(1+\frac1k\Big)^k\approx2.718\ldots$$
The inverse function: $\exp(\ln x)=x$. It follows that $a^x=(e^{\ln a})^x=e^{x\ln a}$, and so $\dfrac d{dx}a^x=\ln a\,e^{x\ln a}=a^x\ln a$.

### Definition — Eigenfunction

An **eigenfunction** of the derivative operator is a function that is unchanged, up to multiplicative scaling by the **eigenvalue** $\lambda$, under the action of the operator:
$$\frac d{dx}f=\lambda f.$$
The eigenfunctions of $\frac d{dx}$ are $e^{\lambda x}$.

## 2 First-order linear ODEs

An $n$th-order linear ODE has $n$ linearly independent solutions.

### Definition — Linear independence of functions

A set of $N$ functions $\{f_i(x)\}$ is **linearly dependent** if
$$\sum_{i=1}^NC_if_i(x)=0\quad\forall x$$
for $N$ constants $C_i$, not all of which are zero (cf. linear dependence of vectors, [[Vectors and Matrices - Chapter 2 Vectors#Definition — Linear independence|V&M Ch.2]]). Otherwise the functions are **linearly independent**. (Equivalently, if one or more of the functions can be written as a linear combination of the others, they are linearly dependent.)

### Definition — Homogeneous ODE

An ODE in which all terms involve the dependent variable or its derivatives. $y=0$ is a trivial solution. For any linear homogeneous ODE, any constant multiple of a solution is a solution.

## 2.1 Homogeneous linear ODEs with constant coefficients

### Homogeneous linear ODEs with constant coefficients

**Constant coefficients:** the independent variable does not appear explicitly. Any linear homogeneous ODE (any order) with constant coefficients has solutions of the form $e^{\lambda x}$ (possibly linear combinations, or $x^ne^{\lambda x}$, $\lambda=0$).

**Example.** $5\dfrac{dy}{dx}-3y=0$. Try $y=Ae^{\lambda x}$:
$$5\lambda Ae^{\lambda x}-3Ae^{\lambda x}=0\ \Longrightarrow\ 5\lambda-3=0\quad(A\ne0),$$
the **characteristic equation**. So $\lambda=\frac35$ and
$$y=Ae^{3x/5}\qquad(A\text{ constant}),$$
the **general solution**. To specify a unique solution we must apply suitable boundary/initial conditions ($n$ are needed for an $n$th-order ODE). E.g. $y(0)=y_0\Rightarrow A=y_0$.

### Discrete equations

It is sometimes useful to consider functions evaluated at discrete points. Consider again $5y'-3y=0$, $y(0)=y_0$, and approximate the equation by a discrete form at $\{x_n\}$ with $x_n=nh$, $x_0=0$:
$$\left.\frac{dy}{dx}\right|_{x_n}\approx\frac{y_{n+1}-y_n}h,\qquad y_n=y(x_n)$$
("**forward Euler scheme**" — not great).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[thick,->] (-0.15,0)--(5.3,0) node[right] {$x$};
  \draw[thick,->] (0,-0.12)--(0,3) node[above left] {$y$};
  \foreach \k/\l in {0/x_0,1/x_1,2/x_2,3/x_3} \draw[thick] ({0.8*\k},-0.055)--({0.8*\k},0.055) node[below=2pt] {$\l$};
  \foreach \k in {4,5,6} \draw[thick] ({0.8*\k},-0.055)--({0.8*\k},0.055);
  \draw[blue!65!cyan,thick] (0.8,1.05)--(1.6,1.55);
  \foreach \p in {(0.8,1.05),(1.6,1.55),(2.4,1.6)} \fill \p circle (1.4pt);
  \node[blue!65!cyan,above right] at (1.55,2.15) {approx.\ to deriv.};
  \draw[blue!65!cyan,thick,->] (1.5,2.12) to[out=215,in=100] (1.13,1.46);
  \draw[blue!65!cyan,thick,<->] (0,-0.65)--(0.8,-0.65) node[midway,below] {$h$};
\end{tikzpicture}
\end{document}
```

Then
$$5\Big(\frac{y_{n+1}-y_n}h\Big)-3y_n=0\quad\Longrightarrow\quad y_{n+1}=\Big(1+\frac{3h}5\Big)y_n,$$
a **recurrence relation**. Iterating,
$$y_n=\Big(1+\frac{3h}5\Big)y_{n-1}=\Big(1+\frac{3h}5\Big)^2y_{n-2}=\dots=\Big(1+\frac{3h}5\Big)^ny_0.$$
Now take $x_n=x$ ($n$ steps from $0$ to $x$, so $h=x/n$): $y_n=\big(1+\frac{3x}{5n}\big)^ny_0$, and as $n\to\infty$
$$\lim_{n\to\infty}y_n=y_0\exp\Big(\frac{3x}5\Big),$$
which agrees with the continuous case. See [[Forward Euler Method]].

### Series solutions

This illustrates a powerful way to solve ODEs (more later): look for a power series $y(x)=\sum_{n=0}^\infty a_nx^n$, with the $a_n$ determined by substitution into the ODE.

**Example.** $5\frac{dy}{dx}-3y=0$. We have $\frac{dy}{dx}=\sum_{n=0}^\infty na_nx^{n-1}=\sum_{n=1}^\infty na_nx^{n-1}$, so $x\frac{dy}{dx}=\sum_{n=0}^\infty na_nx^n$ and $xy=\sum_{n=0}^\infty a_nx^{n+1}=\sum_{n=1}^\infty a_{n-1}x^n$ (relabel $m=n+1\to n$). Multiplying the ODE by $x$ and substituting,
$$\sum_{n=1}^\infty(5na_n-3a_{n-1})x^n=0.$$
The bracket must vanish for $n\ge1$ (since true $\forall x$), giving the recurrence
$$a_n=\frac3{5n}a_{n-1}\ (n\ge1)\quad\Longrightarrow\quad a_n=\Big(\frac35\Big)^n\frac1{n!}a_0,\qquad y=a_0\sum_{n=0}^\infty\frac1{n!}\Big(\frac35\Big)^nx^n=a_0\exp\Big(\frac{3x}5\Big).$$

## 2.2 Forced equations

Forced (non-homogeneous) equations include terms not involving the dependent variable or its derivatives, so $y=0$ is no longer a solution. The method (general for **linear** forced ODEs):

1. Find *any* solution of the forced equation: a **particular integral** (PI) $y_p(x)$.
2. Write the general solution $y(x)=y_p(x)+y_c(x)$, where the **complementary function** (CF) $y_c(x)$ satisfies the corresponding homogeneous equation.
3. Combine $y_c$ and $y_p$ to get the general solution.

### Constant forcing

**Example.** $5\frac{dy}{dx}-3y=10$ (constant forcing term). Spot $y_p=-\frac{10}3$. The CF is $y_c=Ae^{3x/5}$ (solution of $5y'-3y=0$), so
$$y(x)=Ae^{3x/5}-\frac{10}3,$$
where $A$ is a constant that can be determined from a boundary condition (N.B. $y(0)\ne A$).

### Eigenfunction forcing

The forcing term is an eigenfunction of the differential operator.

**Example (radioactive decay).** Isotope $A$ decays to $B$ (rate coefficient $k_a$), which decays to $C$ (rate coefficient $k_b$); amounts $a(t),b(t),c(t)$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \node[draw,minimum size=0.9cm] (A) at (0,0) {$A$};
  \node[draw,minimum size=0.9cm] (B) at (3,0) {$B$};
  \node[draw,minimum size=0.9cm] (C) at (6,0) {$C$};
  \draw[->] (A)--(B) node[midway,below] {$k_a$};
  \draw[->] (B)--(C) node[midway,below] {$k_b$};
  \node[below] at (0,-0.6) {$a(t)$};
  \node[below] at (3,-0.6) {$b(t)$};
  \node[below] at (6,-0.6) {$c(t)$};
\end{tikzpicture}
\end{document}
```

Decay of $A$: $\frac{da}{dt}=-k_aa\Rightarrow a=a_0e^{-k_at}$. For $B$: production from $A$, decay of $B$:
$$\frac{db}{dt}=k_aa-k_bb\quad\Longrightarrow\quad\frac{db}{dt}+k_bb=k_aa_0e^{-k_at}\qquad(*)$$
(the forcing is an eigenfunction). Try the PI $b_p(t)=\beta e^{-k_at}$: $(*)$ gives $\beta=\dfrac{k_aa_0}{k_b-k_a}$ ($k_a\ne k_b$). The CF solves $\frac{db_c}{dt}+k_bb_c=0$, so $b_c=De^{-k_bt}$, and
$$b(t)=De^{-k_bt}+\frac{k_aa_0}{k_b-k_a}e^{-k_at}.$$
If $b=0$ at $t=0$:
$$b(t)=\frac{k_aa_0}{k_b-k_a}\big(e^{-k_at}-e^{-k_bt}\big).$$
For $k_b>k_a$, $a(t)$ decays from $a_0$ while $b(t)$ rises from $0$ to a maximum then decays. (Think about $k_b<k_a$ as an exercise.) If $k_a=k_b$, a different PI is needed (see later).

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,xscale=5,yscale=3]
  \draw[->] (0,0)--(1.1,0) node[right] {$t$};
  \draw[->] (0,0)--(0,1.15);
  \node[left] at (0,1) {$a_0$};
  \draw[blue,thick,domain=0:1,samples=40] plot (\x,{exp(-3*\x)}) node[right] {$a(t)$};
  \draw[red,thick,domain=0:1,samples=40] plot (\x,{exp(-3*\x)-exp(-6*\x)}) node[above] {$b(t)$};
\end{tikzpicture}
\end{document}
```
*Schematic ($k_b>k_a$); the curves use $k_a=3,\ k_b=6$ only to draw the shape.*

## 2.3 Non-constant coefficients

### Non-constant coefficients — integrating factor

Still first-order linear ODEs. General form $a(x)\frac{dy}{dx}+b(x)y=c(x)$; **standard form**
$$\frac{dy}{dx}+p(x)y=f(x).$$
Solve using an **integrating factor** (I.F.) $\mu(x)$: multiply the ODE by $\mu$,
$$\mu y'+\mu py=\mu f\qquad(\dagger)$$
The left side equals $(\mu y)'$ if $\mu'=p\mu$ (product rule). This requires $\frac{\mu'}{\mu}=p$, so $\int p\,dx=\int\frac{\mu'}\mu dx=\ln\mu$:
$$\mu(x)=\exp\Big[\int^xp(u)\,du\Big],$$
unique up to an irrelevant multiplicative constant factor. Then $(\dagger)\Rightarrow\frac d{dx}(\mu y)=\mu f$, so
$$\mu y=\int^x\mu(u)f(u)\,du.$$

**Example.** $xy'+(1-x)y=1$. In standard form $y'+\frac{1-x}xy=\frac1x$, so $p=\frac{1-x}x$, $f=\frac1x$. I.F.: $\ln\mu=\int^x\big(\frac1u-1\big)du=\ln x-x=\ln(xe^{-x})$ (dropping the irrelevant constant), so $\mu=xe^{-x}$. Then
$$\frac d{dx}\big(xe^{-x}y\big)=\frac xxe^{-x}=e^{-x}\ \Rightarrow\ xe^{-x}y=-e^{-x}+C\ \Rightarrow\ y=-\frac1x+\frac Cxe^x.$$
