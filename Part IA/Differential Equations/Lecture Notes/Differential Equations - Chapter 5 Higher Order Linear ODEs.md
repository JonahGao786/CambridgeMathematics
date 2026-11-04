---
title: Differential Equations - Chapter 5 Higher Order Linear ODEs
course: Part IA Differential Equations
material_type: lecture notes
chapter: 5
source_file: Ch.5 Higher Order Linear ODEs.pdf
drive_file_id: 1zZMeu0U4PjDGE0fJuLsDnVFj5p1KfLcB
source_url: https://drive.google.com/file/d/1zZMeu0U4PjDGE0fJuLsDnVFj5p1KfLcB/view
source_pages: 10
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 5: Higher Order Linear ODEs

> [!abstract] Overview
> Second-order linear ODEs with constant coefficients. Linearity of the differential operator gives the general solution as complementary function plus particular integral. Complementary functions come from $e^{\lambda x}$ and the characteristic equation; complex roots give oscillations, and repeated roots are handled by detuning, which produces $xe^{\lambda x}$. For non-constant coefficients: reduction of order finds a second solution from a first; phase space and solution vectors; the Wronskian tests linear independence.
> Prerequisite: [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]] ($e^{\lambda x}$ as eigenfunction, CF + PI).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Linear differential operator]] | $D(\alpha y_1+\beta y_2)=\alpha Dy_1+\beta Dy_2$ (superposition) | 1 |
| [[#General solution — complementary function plus particular integral]] | $y=C_1y_{c_1}+C_2y_{c_2}+y_p$ | 1–2 |
| [[#Characteristic equation]] | $y_c=Ae^{\lambda x}$ with $a\lambda^2+b\lambda+c=0$; distinct vs repeated roots | 2–3 |
| [[#Detuning — repeated roots]] | repeated root $\lambda$: $y_c=\alpha e^{\lambda x}+\beta xe^{\lambda x}$ | 4–5 |
| [[#General rule — degenerate complementary functions]] | $y_{c_2}=xy_{c_1}$ | 5 |
| [[#Reduction of order]] | $y_2=vy_1$, $v'=\frac A{y_1^2}\exp\left(-\int^xp\right)$ | 6–7 |
| [[#Definition — Solution vector and phase space]] | $\mathbf Y=(y,y',\dots,y^{(n-1)})^{\mathsf T}$; trajectories | 7–8 |
| [[#Definition — Fundamental matrix and Wronskian]] | $W=\det(\mathbf Y_1\cdots\mathbf Y_n)$ | 9 |
| [[#Wronskian test for linear independence]] | dependent $\Rightarrow W\equiv0$; $W(x)\ne0$ somewhere $\Rightarrow$ independent | 9–10 |

Notes on scope:
- We focus on second order, but many methods apply to higher order.
- Closed-form solutions to second-order linear ODEs don't always exist (unlike first order).

## 1. Second-order ODEs with constant coefficients

The general form is
$$a\frac{d^2y}{dx^2}+b\frac{dy}{dx}+cy=f(x),\tag{$*$}$$
where $a,b,c$ are constants. This is $Dy=f$, where the differential operator
$$D\equiv a\frac{d^2}{dx^2}+b\frac d{dx}+c$$
is linear.

### Definition — Linear differential operator

A differential operator $D$ is **linear** if for any $y_1(x)$ and $y_2(x)$, and constants $\alpha$ and $\beta$,
$$D(\alpha y_1+\beta y_2)=\alpha Dy_1+\beta Dy_2$$
(the **principle of superposition**).

### General solution — complementary function plus particular integral

Exploit linearity to solve $(*)$:
1. Find **complementary functions** (C.F.s) $y_c$ that satisfy the homogeneous equation
$$a\frac{d^2y_c}{dx^2}+b\frac{dy_c}{dx}+cy_c=0.$$
2. Find a **particular integral** (P.I.) $y_p(x)$ that satisfies the full equation $(*)$.

Then a solution of the full equation is $y_c+y_p$:
$$D(y_c+y_p)=Dy_c+Dy_p=0+f(x).$$
A second-order ODE has two linearly independent C.F.s, so the general solution to the full equation is
$$y(x)=C_1y_{c_1}(x)+C_2y_{c_2}(x)+y_p(x),\qquad C_1,C_2\text{ constants}.$$

## 1.1 Complementary functions

### Characteristic equation

Recall $\frac d{dx}e^{\lambda x}=\lambda e^{\lambda x}$ ($e^{\lambda x}$ is an eigenfunction of $\frac d{dx}$). It is also an eigenfunction of $D$:
$$\begin{aligned}
De^{\lambda x}&=a\frac{d^2}{dx^2}e^{\lambda x}+b\frac d{dx}e^{\lambda x}+ce^{\lambda x}\\
&=\underbrace{(a\lambda^2+b\lambda+c)}_{\text{eigenvalue}}e^{\lambda x}.
\end{aligned}$$
The C.F.s of $(*)$ satisfy $Dy_c=0$, i.e. they are eigenfunctions with eigenvalue $0$. Therefore
$$y_c=Ae^{\lambda x}\qquad\text{with}\qquad a\lambda^2+b\lambda+c=0,$$
the **characteristic** (or **auxiliary**) **equation** of $D$, with roots $\lambda_1$ and $\lambda_2$.

**Case 1: $\lambda_1\ne\lambda_2$.** There are two linearly independent C.F.s,
$$y_{c_1}\propto e^{\lambda_1x},\qquad y_{c_2}\propto e^{\lambda_2x}.$$
The most general C.F. is
$$y_c(x)=C_1y_{c_1}(x)+C_2y_{c_2}(x);$$
$y_{c_1},y_{c_2}$ form a **basis** for the space of solutions of the homogeneous equation.

Note: the roots may be complex, which gives oscillations.

**Case 2: $\lambda_1=\lambda_2$.** There is only one linearly independent C.F. of the form $e^{\lambda_1x}$; see [[#Detuning — repeated roots]] for how to deal with this.

**Example (real, non-degenerate roots).**
$$\frac{d^2y}{dx^2}-5\frac{dy}{dx}+6y=0.$$
Characteristic equation: $\lambda^2-5\lambda+6=0$, so $\lambda=3$, $\lambda=2$. C.F.:
$$y_c(x)=Ae^{3x}+Be^{2x}.$$

**Example (complex roots).**
$$\frac{d^2y}{dx^2}+4y=0.$$
Characteristic equation: $\lambda^2=-4$, so $\lambda=\pm2i$. C.F.:
$$\begin{aligned}
y_c(x)&=Ae^{2ix}+Be^{-2ix} &&(e^{\pm2ix}=\cos2x\pm i\sin2x)\\
&=(A+B)\cos2x+(A-B)\,i\sin2x\\
&=\alpha\cos2x+\beta\,i\sin2x,
\end{aligned}$$
with $\alpha=A+B$, $\beta=A-B$ arbitrary constants.

### Detuning — repeated roots

**Example (degenerate roots).**
$$\frac{d^2y}{dx^2}-4\frac{dy}{dx}+4y=0.$$
Characteristic equation: $\lambda^2-4\lambda+4=0$, so $\lambda=2$, a degenerate (repeated) root. There is only one C.F. of the form $e^{2x}$.

**Detuning.** Remove the degeneracy by considering a slightly modified (**detuned**) equation:
$$\frac{d^2y}{dx^2}-4\frac{dy}{dx}+(4-\varepsilon^2)y=0\qquad(\varepsilon\ll1).$$
Then $\lambda^2-4\lambda+4-\varepsilon^2=0$, so $\lambda=2\pm\varepsilon$. The general C.F. is
$$\begin{aligned}
y_c&=Ae^{(2+\varepsilon)x}+Be^{(2-\varepsilon)x}\\
&=e^{2x}\left(Ae^{\varepsilon x}+Be^{-\varepsilon x}\right)\\
&=e^{2x}\left[(A+B)+\varepsilon(A-B)x+O(A\varepsilon^2x^2)+O(B\varepsilon^2x^2)\right]\qquad\text{as }\varepsilon\to0.
\end{aligned}$$
Consider initial conditions (for the original and the detuned equation)
$$y(0)=C,\qquad y'(0)=D.$$
Then
$$\begin{aligned}
A+B&=C,\\
2(A+B)+\varepsilon(A-B)&=D,\quad\text{so}\quad\varepsilon(A-B)=D-2C,
\end{aligned}$$
giving
$$A=\frac12\left(C+\frac{D-2C}\varepsilon\right),\qquad B=\frac12\left(C-\frac{D-2C}\varepsilon\right).$$
Therefore $O(A\varepsilon^2x^2)=O(\varepsilon x^2)\to0$ as $\varepsilon\to0$, and similarly for $B$, while
$$\alpha=A+B=O(1),\qquad\beta=\varepsilon(A-B)=O(1).$$
So the general C.F. of the original degenerate equation is
$$y=\alpha e^{2x}+\beta xe^{2x}.$$

> [!note] Explanation
> $A$ and $B$ each blow up like $\frac1\varepsilon$ as $\varepsilon\to0$, but in opposite directions, so their sum $A+B=C$ and the combination $\varepsilon(A-B)=D-2C$ stay fixed by the initial conditions. Those two finite numbers are the coefficients of $e^{2x}$ and $xe^{2x}$; every remaining term carries at least one extra factor of $\varepsilon$ and vanishes in the limit. The second, "missing" solution of the degenerate equation is therefore $xe^{2x}$.

### General rule — degenerate complementary functions

If $y_{c_1}(x)$ is a degenerate C.F. of a linear ODE with constant coefficients, then
$$y_{c_2}(x)=xy_{c_1}(x)$$
is a second linearly independent C.F. For the example above, the equation factorises as
$$\Big(\frac d{dx}-2\Big)\Big(\frac d{dx}-2\Big)y=0,\qquad\text{i.e.}\qquad\Big(\frac d{dx}-2\Big)u=0\quad\text{with}\quad u=\Big(\frac d{dx}-2\Big)y.$$

> [!note] Explanation
> The factorised form gives the general rule directly. First $u'-2u=0$ gives $u=Ce^{2x}$. Then $y'-2y=Ce^{2x}$; with the integrating factor $e^{-2x}$, $(e^{-2x}y)'=C$, so $y=(Cx+D)e^{2x}$. The repeated factor is what produces the extra $x$.

## 2. Homogeneous second-order ODEs with non-constant coefficients

The general form is
$$y''+p(x)y'+q(x)y=0.\tag{$*$}$$

## 2.1 Second C.F. — reduction of order

### Reduction of order

Find a second solution $y_2(x)$ given one solution $y_1(x)$. Try the form
$$y_2(x)=v(x)y_1(x),$$
with $v$ to be determined. Then
$$y_2'=v'y_1+vy_1',\qquad y_2''=v''y_1+2v'y_1'+vy_1''.$$
If $y_2$ satisfies $(*)$,
$$v''y_1+v'(2y_1'+py_1)+v\underbrace{(y_1''+py_1'+qy_1)}_{=0\text{ since }y_1\text{ solves }(*)}=0,$$
so
$$v''y_1+v'(2y_1'+py_1)=0,\qquad\text{i.e.}\qquad u'y_1+u(2y_1'+py_1)=0\quad\text{where }u=v',$$
a separable first-order ODE for $u$. Hence (assuming the right-hand side is non-zero)
$$\begin{aligned}
\frac{u'}u&=-\frac{2y_1'}{y_1}-p\\
\Rightarrow\quad\ln u&=-2\ln y_1-\int_0^xp(t)\,dt+\ln A\\
\Rightarrow\quad u(x)&=\frac A{y_1^2}\exp\Big(-\int_0^xp(t)\,dt\Big).
\end{aligned}$$
Integrate to get $v(x)$.

**Example.** $y''-4y'+4y=0$, so $p(x)=-4$, $q(x)=4$. One solution is $y_1=e^{2x}$. Then
$$\frac{u'}u=-\frac{2\cdot2e^{2x}}{e^{2x}}+4=0,$$
so $v'=u$ is constant, and $v(x)=Ax+B$. Thus
$$y_2(x)=(Ax+B)e^{2x},$$
where the $Be^{2x}$ part reproduces $y_1$. Therefore $xe^{2x}$ is a second linearly independent solution.

## 2.2 Phase space

### Definition — Solution vector and phase space

For an $n$th-order linear ODE
$$y^{(n)}+p(x)y^{(n-1)}+\dots+q(x)y=f(x),$$
$y^{(n)}(x)$ is determined by $y(x),y'(x),\dots,y^{(n-1)}(x)$, and higher derivatives of $y$ can be determined by differentiating the ODE. So we can construct the Taylor series about $x_0$ if $y(x_0),y'(x_0),\dots,y^{(n-1)}(x_0)$ are specified.

The **state of the system** is fully specified at any $x$ by the $n$-dimensional **solution vector**
$$\mathbf Y(x)=\begin{pmatrix}y(x)\\y'(x)\\\vdots\\y^{(n-1)}(x)\end{pmatrix}$$
(i.e. knowing this at one $x$ gives the solution at any $x$).
- At any $x$, $\mathbf Y(x)$ defines a point in $n$-dimensional **phase space**.
- As $x$ varies, $\mathbf Y(x)$ traces out a **trajectory** in phase space.

**Example.** $y''+4y=0$ with $y_1(x)=\cos2x$, $y_2(x)=\sin2x$:
$$\mathbf Y_1(x)=\begin{pmatrix}y_1\\y_1'\end{pmatrix}=\begin{pmatrix}\cos2x\\-2\sin2x\end{pmatrix},\qquad\mathbf Y_2(x)=\begin{pmatrix}y_2\\y_2'\end{pmatrix}=\begin{pmatrix}\sin2x\\2\cos2x\end{pmatrix}.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.1]
  \draw[->] (-2.2,0) -- (2.4,0) node[right] {$y$};
  \draw[->] (0,-2.5) -- (0,2.6) node[above] {$y'$};
  \draw[red,thick] (0,0) ellipse (1 and 2);
  \draw[blue,thick,->] (0,0) -- (0.878,-0.959) node[right] {$\mathbf Y_1(x)$};
  \draw[blue,thick,->] (0,0) -- (0.479,1.755) node[right] {$\mathbf Y_2(x)$};
\end{tikzpicture}
\end{document}
```
*2D phase space for $y''+4y=0$: both trajectories run round the ellipse $y^2+\frac{y'^2}4=1$; shown at the same $x$ (here $2x=0.5$).*

$\mathbf Y_1$ and $\mathbf Y_2$ are linearly independent vectors (in the linear-algebra sense), so we can use them as basis vectors for the 2D phase space.

## 2.3 Wronskian and linear dependence

**Recall.** $\{y_i(x)\}$ is linearly dependent if
$$\sum_{i=1}^nc_iy_i(x)=0\quad\text{for all }x,\qquad c_i\text{ not all zero}.$$
This must hold for all $x$, so we can differentiate $1,2,\dots,n-1$ times:
$$\sum_{i=1}^nc_i\mathbf Y_i(x)=\mathbf 0\quad\text{for all }x.$$

### Definition — Fundamental matrix and Wronskian

The **fundamental matrix** of solution vectors is $\mathsf M=\big(\mathbf Y_1\ \cdots\ \mathbf Y_n\big)$, with the $\mathbf Y_i$ as columns. The **Wronskian** $W(x)$ of $n$ functions $y_i(x)$ ($i=1,\dots,n$) is
$$W(x)=\det\big(\mathbf Y_1\ \cdots\ \mathbf Y_n\big)=\begin{vmatrix}y_1&\cdots&y_n\\y_1'&\cdots&y_n'\\\vdots&&\vdots\\y_1^{(n-1)}&\cdots&y_n^{(n-1)}\end{vmatrix}.$$

### Wronskian test for linear independence

The equation above for linear dependence reads $\mathsf M\mathbf c=\mathbf 0$. It has non-trivial solutions only if $\mathsf M$ is not invertible, i.e. $W=0$. Therefore
$$\{y_i(x)\}\text{ linearly dependent}\ \Rightarrow\ W(x)=0\ \text{ for all }x.$$
It follows that if **$W(x)\ne0$ for some $x$, then $\{y_i(x)\}$ is linearly independent.**

**N.B.** $W(x)=0$ for all $x$ does **not** necessarily imply that $\{y_i(x)\}$ are linearly dependent.

**Example.** $y''+4y=0$ gives $y_1=\cos2x$, $y_2=\sin2x$, and
$$\begin{aligned}
W(x)=\begin{vmatrix}y_1&y_2\\y_1'&y_2'\end{vmatrix}&=\begin{vmatrix}\cos2x&\sin2x\\-2\sin2x&2\cos2x\end{vmatrix}\\
&=2\cos^22x+2\sin^22x\\
&=2.
\end{aligned}$$
$W\ne0$, so $y_1,y_2$ are linearly independent.
