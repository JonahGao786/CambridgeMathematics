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

## Examples

- $y''-5y'+6y=0$: $\lambda=2,3$, $y=Ae^{3x}+Be^{2x}$.
- $y''+4y=0$: $\lambda=\pm2i$, $y=\alpha\cos2x+\beta\,i\sin2x$.
- $y''-4y'+4y=0$: $\lambda=2$ (repeated), $y=\alpha e^{2x}+\beta xe^{2x}$.

## Related

[[First-Order Linear Differential Equations]] · [[Complex Exponential and Trigonometric Functions]] · [[Taylor Series and Taylor's Theorem]]
