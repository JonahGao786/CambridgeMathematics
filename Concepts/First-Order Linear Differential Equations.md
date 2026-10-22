---
title: First-Order Linear Differential Equations
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# First-Order Linear Differential Equations

> [!abstract] In one paragraph
> $e^{\lambda x}$ is the eigenfunction of $\frac d{dx}$, so homogeneous linear ODEs with constant coefficients are solved by trying $y=Ae^{\lambda x}$: the ODE becomes an algebraic **characteristic equation** for $\lambda$. Initial conditions then fix the constants.

## Definitions

- **Order** = highest derivative; **linear** = the dependent variable appears linearly; **ordinary** = one independent variable.
- **Homogeneous**: every term involves the dependent variable or its derivatives; then $y=0$ is a solution and constant multiples of solutions are solutions.
- Functions $f_1,\dots,f_N$ are **linearly dependent** if $\sum C_if_i(x)=0$ for all $x$ with constants not all zero; otherwise independent.
- **Eigenfunction** of $\frac d{dx}$: $\frac{df}{dx}=\lambda f$; these are $e^{\lambda x}$.

→ [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Terminology|lecture]]

## Key facts

- $\exp$ is the solution of $f'=f$, $f(0)=1$; $\exp(x)=\sum\frac{x^n}{n!}=\lim(1+\frac xk)^k$.
- An $n$th-order linear ODE has $n$ linearly independent solutions; $n$ conditions are needed to fix one.
- Constant coefficients: solutions $e^{\lambda x}$ (or combinations, $x^ne^{\lambda x}$).

## Example

$5y'-3y=0$: $5\lambda-3=0$, so $y=Ae^{3x/5}$; $y(0)=y_0\Rightarrow A=y_0$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Homogeneous linear ODEs with constant coefficients|lecture]]

## Related

[[Forward Euler Method]] · [[Complex Exponential and Trigonometric Functions]] · [[Vectors and Linear Span]]
