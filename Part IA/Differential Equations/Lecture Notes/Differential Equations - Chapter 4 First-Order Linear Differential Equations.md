---
title: Differential Equations - Chapter 4 First-Order Linear Differential Equations
course: Part IA Differential Equations
material_type: lecture notes
chapter: 4
source_file: Ch.4 First-order Linear Differential Equations.pdf
drive_file_id: 1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3
source_url: https://drive.google.com/file/d/1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3/view
source_pages: 20
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 4: First-Order Linear Differential Equations

> [!abstract] Overview
> Terminology for ODEs; the exponential function as the eigenfunction of $\frac d{dx}$; linear independence of functions; homogeneous linear ODEs with constant coefficients solved by $e^{\lambda x}$; forward Euler and its limit; series solutions; forced equations (particular integral + complementary function), with constant and eigenfunction forcing; non-constant coefficients via the integrating factor; then nonlinear first-order ODEs: separable and exact equations, solution curves, slope fields and isoclines; then fixed points, their stability by perturbation analysis, and autonomous equations.
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
| [[#Radioactive decay revisited]] | integrating factor; resonance $k_a=k_b$ gives $te^{-k_bt}$ | 10–11 |
| [[#Separable equations]] | $q(y)\,dy=p(x)\,dx$ | 11–12 |
| [[#Definition — Exact equation]] | $P\,dx+Q\,dy=df$; solution $f=\text{const}$ | 12–13 |
| [[#Necessary condition for exactness]] | $\partial P/\partial y=\partial Q/\partial x$ | 13 |
| [[#Theorem — Exactness on simply connected domains]] | the condition is sufficient there | 13 |
| [[#Definition — Simply connected domain]] | path connected, loops shrink to a point | 13–14 |
| [[#Solution curves]] | trajectories of $y'=f(t,y)$; example $y'=t(1-y^2)$ | 15–16 |
| [[#Slope field and isoclines]] | tangent "sticks"; curves along which $y'$ is constant | 16–17 |
| [[#Definition — Fixed point]] | constant solution $y=c$ | 17 |
| [[#Definition — Stable and unstable fixed points]] | nearby solutions converge to / diverge from $c$ | 18 |
| [[#Perturbation analysis and stability]] | $\varepsilon'=\varepsilon\,\partial f/\partial y(t,c)$ | 18–19 |
| [[#Autonomous equations]] | $y'=f(y)$; stable iff $f'(c)<0$ | 19–20 |

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

**Example.** $5\dfrac{dy}{dx}-3y=0$. We have
$$\frac{dy}{dx}=\sum_{n=0}^\infty na_nx^{n-1}=\sum_{n=1}^\infty na_nx^{n-1},\qquad\text{so}\qquad x\frac{dy}{dx}=\sum_{n=0}^\infty na_nx^n,$$
and, relabelling $n+1\to n$,
$$xy=\sum_{n=0}^\infty a_nx^{n+1}=\sum_{n=1}^\infty a_{n-1}x^n.$$
Multiplying the ODE by $x$ and substituting,
$$\sum_{n=1}^\infty(5na_n-3a_{n-1})x^n=0.$$
The bracket must vanish for $n\ge1$ (since true $\forall x$), giving the recurrence
$$a_n=\frac3{5n}a_{n-1}\quad(n\ge1)\qquad\Longrightarrow\qquad a_n=\Big(\frac35\Big)^n\frac1{n!}\,a_0.$$
Hence
$$y=a_0\sum_{n=0}^\infty\frac1{n!}\Big(\frac35\Big)^nx^n=a_0\exp\Big(\frac{3x}5\Big).$$

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
For $k_b>k_a$, $a(t)$ decays from $a_0$ while $b(t)$ rises from $0$ to a maximum then decays. (Think about $k_b<k_a$ as an exercise.) If $k_a=k_b$, a different PI is needed (see [[#Radioactive decay revisited]]).

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

**Example.** $xy'+(1-x)y=1$. In standard form $y'+\dfrac{1-x}xy=\dfrac1x$, so $p=\dfrac{1-x}x$, $f=\dfrac1x$. The integrating factor satisfies
$$\ln\mu=\int^x\Big(\frac1u-1\Big)du=\ln x-x=\ln(xe^{-x})$$
(dropping the irrelevant constant), so $\mu=xe^{-x}$. Then
$$\frac d{dx}\big(xe^{-x}y\big)=\frac xxe^{-x}=e^{-x}\ \Rightarrow\ xe^{-x}y=-e^{-x}+C\ \Rightarrow\ y=-\frac1x+\frac Cxe^x.$$

### Radioactive decay revisited

The equation $\dfrac{db}{dt}+k_bb=k_aa_0e^{-k_at}$ has $p(t)=k_b$, $f(t)=k_aa_0e^{-k_at}$. Integrating factor $\mu(t)=e^{k_bt}$, so
$$\frac d{dt}\big(e^{k_bt}b\big)=k_aa_0e^{(k_b-k_a)t}.\qquad(*)$$

- $k_b\ne k_a$: the right side of $(*)$ depends on $t$, so $e^{k_bt}b=\dfrac{k_aa_0}{k_b-k_a}e^{(k_b-k_a)t}+C$, i.e. $b(t)=\dfrac{k_aa_0}{k_b-k_a}e^{-k_at}+Ce^{-k_bt}$, as before.
- $k_b=k_a$: the right side of $(*)$ is independent of $t$, so $e^{k_bt}b=k_aa_0t+C$, i.e.
$$b(t)=k_aa_0\,t\,e^{-k_bt}+Ce^{-k_bt}.$$

Note the particular integral is $\alpha te^{-k_bt}$, not just $e^{-k_bt}$ — the **resonance case**: the forcing has the same exponent as a complementary-function solution.

## 3 Nonlinear first-order ODEs

General form
$$Q(x,y)\frac{dy}{dx}+P(x,y)=0.\qquad(*)$$
It could be nonlinear in $\frac{dy}{dx}$, but that is not considered here. First, two special cases.

### Separable equations

A first-order ODE is **separable** if it can be written $q(y)\,dy=p(x)\,dx$. Solve by direct integration: $\int q(y)\,dy=\int p(x)\,dx$.

**Example.** $(x^2y-3y)\dfrac{dy}{dx}-2xy^2=4x$. Rearrange: $y(x^2-3)\dfrac{dy}{dx}=2x(2+y^2)$, so
$$\int\frac y{2+y^2}\,dy=\int\frac{2x}{x^2-3}\,dx\ \Rightarrow\ \tfrac12\ln(2+y^2)=\ln|x^2-3|+C\ \Rightarrow\ 2+y^2=A(x^2-3)^2,$$
with $A=e^{2C}$.

### Definition — Exact equation

The ODE $(*)$ is **exact** if $P(x,y)\,dx+Q(x,y)\,dy$ is an **exact differential**, i.e. there is a single-valued function $f(x,y)$ with
$$df=P\,dx+Q\,dy.$$
Then $(*)$ says $df=0$, so $f(x,y)=\text{const}$ is a solution. By the multivariate chain rule $df=\frac{\partial f}{\partial x}\big|_ydx+\frac{\partial f}{\partial y}\big|_xdy$, so we solve
$$\frac{\partial f}{\partial x}=P,\qquad\frac{\partial f}{\partial y}=Q.$$

### Necessary condition for exactness

Partial derivatives commute, so if $f_x=P$ and $f_y=Q$ then
$$\frac{\partial P}{\partial y}=\frac{\partial^2f}{\partial y\,\partial x}=\frac{\partial^2f}{\partial x\,\partial y}=\frac{\partial Q}{\partial x}.$$
So $\dfrac{\partial P}{\partial y}=\dfrac{\partial Q}{\partial x}$ is **necessary** (not sufficient) for exactness.

### Theorem — Exactness on simply connected domains

If $\dfrac{\partial P}{\partial y}=\dfrac{\partial Q}{\partial x}$ throughout a simply connected domain $\Omega$, then $P\,dx+Q\,dy$ is an exact differential of a single-valued function $f(x,y)$ in $\Omega$.

### Definition — Simply connected domain

A domain $\Omega$ is **path connected** if every pair of points of $\Omega$ can be joined by a path in $\Omega$. It is **simply connected** if it is path connected and every closed curve in $\Omega$ can be continuously shrunk to a point of $\Omega$ without leaving $\Omega$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.8]
  \begin{scope}
    \draw[blue,thick] (0,0) ellipse (1.2 and 0.9);
    \node at (0,-1.5) {path connected};
  \end{scope}
  \begin{scope}[shift={(4,0)}]
    \draw[blue,thick] (-0.8,0) ellipse (0.6 and 0.7);
    \draw[blue,thick] (0.9,0) ellipse (0.6 and 0.7);
    \node at (0,-1.5) {not path connected};
  \end{scope}
  \begin{scope}[shift={(8,0)}]
    \draw[blue,thick] (0,0) ellipse (1.2 and 0.9);
    \node at (0,-1.5) {simply connected};
  \end{scope}
  \begin{scope}[shift={(12,0)}]
    \draw[blue,thick] (0,0) ellipse (1.2 and 0.9);
    \draw[blue,thick] (0,0) ellipse (0.35 and 0.25);
    \draw[red,thick] (0,0) ellipse (0.8 and 0.58);
    \node at (0,-1.5) {not simply connected};
  \end{scope}
\end{tikzpicture}
\end{document}
```
*Schematic. Right: the red loop around the hole cannot be shrunk to a point inside the domain.*

**Example.** $6y(y-x)\dfrac{dy}{dx}+2x-3y^2=0$, i.e.
$$(2x-3y^2)\,dx+(6y^2-6xy)\,dy=0,\qquad P=2x-3y^2,\quad Q=6y^2-6xy.$$
Then
$$\frac{\partial P}{\partial y}=-6y=\frac{\partial Q}{\partial x},$$
so the equation is exact in any simply connected domain. Integrating $\dfrac{\partial f}{\partial x}=P=2x-3y^2$ gives
$$f(x,y)=x^2-3y^2x+h(y).$$
Then
$$\frac{\partial f}{\partial y}=-6xy+\frac{dh}{dy}=Q=6y^2-6xy\ \Longrightarrow\ \frac{dh}{dy}=6y^2\ \Longrightarrow\ h=2y^3+C.$$
The solution is
$$f(x,y)=x^2-3xy^2+2y^3=\text{const}.$$

### Solution curves

Nonlinear ODEs can often not be solved in simple closed form; their solutions can be analysed with graphical methods. Consider $\dfrac{dy}{dt}=f(t,y)$. Each initial condition (e.g. $y(0)=y_0$) generates a distinct **solution curve** (trajectory). Can we sketch solution curves without actually solving the ODE?

**Example (solved, to illustrate).** $\dfrac{dy}{dt}=t(1-y^2)$ is separable:
$$\frac{dy}{1-y^2}=t\,dt\ \Rightarrow\ \tfrac12\Big(\frac1{1+y}+\frac1{1-y}\Big)dy=t\,dt\ \Rightarrow\ \tfrac12\ln\Big|\frac{1+y}{1-y}\Big|=\tfrac12t^2+C\ \Rightarrow\ y=\frac{A-e^{-t^2}}{A+e^{-t^2}}.,\qquad A=\begin{cases}e^{2C}&|y|<1,\\-e^{2C}&|y|>1.\end{cases}$$

This is a family of solution curves parametrised by $A$. If $y(0)=y_0$ then
$$A=\frac{1+y_0}{1-y_0}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,xscale=2.4,yscale=0.9]
  \clip (-0.25,-4.2) rectangle (2.9,3.9);
  \draw[->] (0,-4) -- (0,3.4) node[above] {$y$};
  \draw[->] (-0.1,0) -- (2.35,0) node[right] {$t$};
  \draw[dashed] (0,1) -- (2.3,1);
  \node[left] at (0,1) {$1$};
  \node[left] at (0,-1) {$-1$};
  \draw[red,thick] (0,-1) -- (2.3,-1);
  \foreach \A in {0.3,1,4} \draw[red,thick,domain=0:2.3,samples=60] plot (\x,{(\A-exp(-\x*\x))/(\A+exp(-\x*\x))});
  \foreach \A in {-1.6,-3} \draw[red,thick,domain=0:2.3,samples=60] plot (\x,{(\A-exp(-\x*\x))/(\A+exp(-\x*\x))});
  \draw[red,thick,domain=0:0.80,samples=60] plot (\x,{(-0.5-exp(-\x*\x))/(-0.5+exp(-\x*\x))});
  \draw[red,thick,domain=0.87:2.3,samples=60] plot (\x,{(-0.5-exp(-\x*\x))/(-0.5+exp(-\x*\x))});
\end{tikzpicture}
\end{document}
```
*Schematic: solution curves of $y'=t(1-y^2)$ for several values of $A$. $A=0$ gives $y=-1$ for all $t$; for $A\ne0$ the curves tend to $y=1$ as $t\to\infty$, except $-1\le A<0$, which have a vertical asymptote.*

### Slope field and isoclines

$\dfrac{dy}{dt}=f(t,y)$ gives the gradient of the solution curve through $(t,y)$. Solution curves never cross if $f(t,y)$ is single valued.

The **slope field** represents this gradient field by short "sticks" centred on each point; each is tangent to the solution curve through that point.

**Example.** For $\dfrac{dy}{dt}=t(1-y^2)$ and $t>0$: $y'>0$ for $|y|<1$, and $y'<0$ for $|y|>1$.

**Isoclines** are curves along which $y'$ is constant, and are sometimes useful. Here $t(1-y^2)=D$ with $D$ constant, i.e.
$$y^2=1-\frac Dt,$$
which parametrises the isoclines by $D$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \foreach \t in {0.3,0.8,...,6.1} {
    \foreach \y in {-1.6,-1.3,...,1.65} {
      \pgfmathsetmacro{\s}{\t*(1-\y*\y)}
      \pgfmathsetmacro{\ny}{1.4*\s}
      \pgfmathsetmacro{\nrm}{sqrt(1.21+\ny*\ny)}
      \pgfmathsetmacro{\dx}{0.17*1.1/\nrm}
      \pgfmathsetmacro{\dy}{0.17*\ny/\nrm}
      \draw[gray,thick] ({1.1*\t-\dx},{1.4*\y-\dy}) -- ({1.1*\t+\dx},{1.4*\y+\dy});
    }
  }
  \draw[->] (0,-2.4) -- (0,2.5);
  \draw[->] (-0.1,0) -- (6.9,0) node[right] {$t$};
  \draw[dashed] (0,1.4) -- (6.8,1.4); \draw[dashed] (0,-1.4) -- (6.8,-1.4);
  \node[left] at (0,1.4) {$1$}; \node[left] at (0,-1.4) {$-1$};
  \foreach \D in {1,3} {
    \draw[blue,thick,domain=\D:6.2,samples=60] plot ({1.1*\x},{1.4*sqrt(1-\D/\x)});
    \draw[blue,thick,domain=\D:6.2,samples=60] plot ({1.1*\x},{-1.4*sqrt(1-\D/\x)});
  }
  \foreach \D in {-1,-3} {
    \draw[blue,thick,domain=0.65:6.2,samples=60] plot ({1.1*\x},{1.4*sqrt(1-\D/\x)});
    \draw[blue,thick,domain=0.65:6.2,samples=60] plot ({1.1*\x},{-1.4*sqrt(1-\D/\x)});
  }
\end{tikzpicture}
\end{document}
```
*Schematic: slope field of $y'=t(1-y^2)$ (grey sticks) with the isoclines $y^2=1-D/t$ (blue) for $D>0$ (open curves with vertex at $t=D$, approaching $y=\pm1$) and $D<0$ (curves outside the strip $|y|<1$). Along each isocline the sticks have the same slope $D$.

## 4 Fixed points and stability

Fixed points often reveal important features of ODEs.

### Definition — Fixed point

A **fixed point** (f.p.) or **equilibrium point** of the ODE $\dfrac{dy}{dt}=f(t,y)$ is a constant solution $y=c$, i.e. $\dfrac{dy}{dt}=0$ for all $t$.

**Example.** $\dfrac{dy}{dt}=t(1-y^2)$ has fixed points $y=\pm1$. They have very different character: solution curves approach $y=1$ as $t\to\infty$ (a **stable** fixed point), but diverge from $y=-1$ (an **unstable** fixed point).

### Definition — Stable and unstable fixed points

A fixed point $y=c$ is **stable** if whenever $y$ deviates slightly from $c$, $y$ converges to $y=c$ as $t\to\infty$. It is **unstable** if $y$ diverges from $y=c$ as $t\to\infty$.

### Perturbation analysis and stability

Let $y=c$ be a fixed point of $\dfrac{dy}{dt}=f(t,y)$, i.e. $f(t,c)=0$ for all $t$. Perturb about the fixed point:
$$y(t)=c+\varepsilon(t)\qquad(\varepsilon\text{ small}).$$
Then
$$\begin{aligned}
\frac{d\varepsilon}{dt}&=f(t,c+\varepsilon)\\
&=f(t,c)+\varepsilon\,\frac{\partial f}{\partial y}(t,c)+O(\varepsilon^2),
\end{aligned}$$
and $f(t,c)=0$ since $c$ is a fixed point. Linearising for small $\varepsilon$:
$$\frac{d\varepsilon}{dt}=\varepsilon\,\frac{\partial f}{\partial y}(t,c).$$
This is a linear ODE, so simpler to solve. (If $\frac{\partial f}{\partial y}(t,c)=0$, higher-order terms in the Taylor series are needed to determine stability.)

**Example.** $\dfrac{dy}{dt}=t(1-y^2)=f(t,y)$, with fixed points $y=\pm1$ and
$$\frac{\partial f}{\partial y}=-2ty=\begin{cases}-2t&y=1,\\2t&y=-1.\end{cases}$$
- Near $y=1$: $\dfrac{d\varepsilon}{dt}=-2t\varepsilon$, so $\varepsilon(t)=\varepsilon_0e^{-t^2}$. As $t\to\infty$, $\varepsilon\to0$: **stable** fixed point.
- Near $y=-1$: $\dfrac{d\varepsilon}{dt}\approx2t\varepsilon$, so $\varepsilon(t)=\varepsilon_0e^{t^2}$. As $t\to\infty$, $|\varepsilon|\to\infty$: **unstable** fixed point (solution curves diverge from it).

### Autonomous equations

An **autonomous system** is the special case
$$\frac{dy}{dt}=f(y),$$
with no explicit $t$ dependence. It is separable:
$$\int^y\frac{du}{f(u)}=t-t_0,$$
where $t_0$ is the integration constant. If $y(t)$ is a solution, so is $y(t-t_0)$ for every $t_0$ (the general solution, before applying initial or boundary conditions).

Near a fixed point $y=c$ (so $f(c)=0$), with $y=c+\varepsilon$,
$$\frac{d\varepsilon}{dt}\approx\frac{df}{dy}(c)\,\varepsilon=k\varepsilon\quad(k\text{ constant})\ \Rightarrow\ \varepsilon(t)=\varepsilon_0e^{kt}.$$
- $f'(c)<0$ $\Rightarrow$ **stable** fixed point;
- $f'(c)>0$ $\Rightarrow$ **unstable** fixed point.

**Example (chemical kinetics).** $A+B\to C+D$. Let the numbers of molecules be $a(t),b(t),c(t),d(t)$, with initial numbers $a_0,b_0,0,0$. Then
$$a(t)=a_0-c(t),\qquad b(t)=b_0-c(t),\qquad d(t)=c(t).$$
Assume the rate of reaction is proportional to $a(t)b(t)$ (e.g. a dilute gas):
$$\frac{dc}{dt}=\lambda\,a(t)b(t)=\lambda\,[a_0-c(t)][b_0-c(t)]=f(c),$$
with $\lambda$ constant.
