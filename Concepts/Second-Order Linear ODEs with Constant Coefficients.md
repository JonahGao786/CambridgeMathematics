---
title: Second-Order Linear ODEs with Constant Coefficients
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Second-Order Linear ODEs with Constant Coefficients

> [!abstract] In one paragraph
> For $ay''+by'+cy=f(x)$ the operator is linear, so the general solution is two independent complementary functions plus one particular integral. Trying $e^{\lambda x}$ gives the characteristic equation $a\lambda^2+b\lambda+c=0$. Distinct roots give $e^{\lambda_1x},e^{\lambda_2x}$ (complex roots give oscillations); a repeated root $\lambda$ gives $e^{\lambda x}$ and $xe^{\lambda x}$.

## Definitions

- **Linear operator:** $D(\alpha y_1+\beta y_2)=\alpha Dy_1+\beta Dy_2$ (superposition). → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#Definition — Linear differential operator|lecture]]
- **Complementary function** solves $Dy_c=0$; **particular integral** solves $Dy_p=f$. → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#General solution — complementary function plus particular integral|lecture]]

## Key results

- **General solution** $y=C_1y_{c_1}+C_2y_{c_2}+y_p$. → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#General solution — complementary function plus particular integral|lecture]]
- **Characteristic equation.** $De^{\lambda x}=(a\lambda^2+b\lambda+c)e^{\lambda x}$, so $e^{\lambda x}$ is a C.F. exactly when $a\lambda^2+b\lambda+c=0$. → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#Characteristic equation|lecture]]
- **Repeated roots by detuning.** Shift the equation so the roots are $\lambda\pm\varepsilon$, fix initial conditions, let $\varepsilon\to0$: the C.F. becomes $\alpha e^{\lambda x}+\beta xe^{\lambda x}$. → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#Detuning — repeated roots|derivation]]
- **General rule.** A degenerate C.F. $y_{c_1}$ gives a second one $xy_{c_1}$ (factorise $(\frac d{dx}-\lambda)^2$). → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#General rule — degenerate complementary functions|lecture]]

## Non-constant coefficients

- **Reduction of order.** Given $y_1$ for $y''+py'+qy=0$, put $y_2=vy_1$; then $u=v'$ solves a separable equation, $u=\frac A{y_1^2}e^{-\int^xp}$. → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#Reduction of order|derivation]]
- **Phase space.** The state is the solution vector $\mathbf Y=(y,y',\dots,y^{(n-1)})^{\mathsf T}$; as $x$ varies it traces a trajectory. → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#Definition — Solution vector and phase space|lecture]]
- **Wronskian** $W=\det(\mathbf Y_1\cdots\mathbf Y_n)$: dependent $\Rightarrow W\equiv0$, so $W(x)\ne0$ somewhere $\Rightarrow$ independent (the converse fails). → [[Differential Equations - Chapter 5 Higher Order Linear ODEs#Wronskian test for linear independence|lecture]]

## Examples

- $y''-5y'+6y=0$: $\lambda=2,3$, $y=Ae^{3x}+Be^{2x}$.
- $y''+4y=0$: $\lambda=\pm2i$, $y=\alpha\cos2x+\beta\,i\sin2x$.
- $y''-4y'+4y=0$: $\lambda=2$ (repeated), $y=\alpha e^{2x}+\beta xe^{2x}$ (also by reduction of order).
- $\cos2x,\sin2x$ have Wronskian $2$, so they are independent.

## Related

[[First-Order Linear Differential Equations]] · [[Complex Exponential and Trigonometric Functions]] · [[Taylor Series and Taylor's Theorem]]
