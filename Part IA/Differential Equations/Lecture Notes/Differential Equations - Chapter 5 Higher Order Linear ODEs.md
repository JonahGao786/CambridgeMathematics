---
title: Differential Equations - Chapter 5 Higher Order Linear ODEs
course: Part IA Differential Equations
material_type: lecture notes
chapter: 5
source_file: Ch.5 Higher Order Linear ODEs.pdf
drive_file_id: 1zZMeu0U4PjDGE0fJuLsDnVFj5p1KfLcB
source_url: https://drive.google.com/file/d/1zZMeu0U4PjDGE0fJuLsDnVFj5p1KfLcB/view
source_pages: 5
tags: [lecture, differential-equations]
---

# Differential Equations — Chapter 5: Higher Order Linear ODEs

> [!abstract] Overview
> Second-order linear ODEs with constant coefficients. Linearity of the differential operator gives the general solution as complementary function plus particular integral. Complementary functions come from $e^{\lambda x}$ and the characteristic equation; complex roots give oscillations, and repeated roots are handled by detuning, which produces $xe^{\lambda x}$.
> Prerequisite: [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]] ($e^{\lambda x}$ as eigenfunction, CF + PI).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Linear differential operator]] | $D(\alpha y_1+\beta y_2)=\alpha Dy_1+\beta Dy_2$ (superposition) | 1 |
| [[#General solution — complementary function plus particular integral]] | $y=C_1y_{c_1}+C_2y_{c_2}+y_p$ | 1–2 |
| [[#Characteristic equation]] | $y_c=Ae^{\lambda x}$ with $a\lambda^2+b\lambda+c=0$; distinct vs repeated roots | 2–3 |
| [[#Detuning — repeated roots]] | repeated root $\lambda$: $y_c=\alpha e^{\lambda x}+\beta xe^{\lambda x}$ | 4–5 |

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
