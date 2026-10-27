---
title: First-Order Linear Differential Equations
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# First-Order Linear Differential Equations

> [!abstract] In one paragraph
> $e^{\lambda x}$ is the eigenfunction of $\frac d{dx}$, so homogeneous linear ODEs with constant coefficients are solved by trying $y=Ae^{\lambda x}$: the ODE becomes an algebraic **characteristic equation** for $\lambda$. Forced equations add a particular integral; non-constant coefficients use an integrating factor.

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

## Forced equations and the integrating factor

- **Forced:** $y=y_p+y_c$ — a **particular integral** (spot a solution of the same form as the forcing) plus the **complementary function** (general solution of the homogeneous equation). E.g. $5y'-3y=10$: $y=Ae^{3x/5}-\frac{10}3$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#2.2 Forced equations|lecture]]
- **Eigenfunction forcing** (radioactive decay $A\to B\to C$): $b'+k_bb=k_aa_0e^{-k_at}$ has $b_p=\frac{k_aa_0}{k_b-k_a}e^{-k_at}$ when $k_a\ne k_b$.
- **Non-constant coefficients:** for $y'+p(x)y=f(x)$ take $\mu=\exp\int p$; then $(\mu y)'=\mu f$. E.g. $xy'+(1-x)y=1$: $\mu=xe^{-x}$, $y=-\frac1x+\frac Cxe^x$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Non-constant coefficients — integrating factor|lecture]]
- **Resonance:** if the forcing has the same exponent as a complementary-function solution (e.g. $b'+k_bb=ke^{-k_bt}$), the particular integral is $\alpha te^{-k_bt}$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Radioactive decay revisited|lecture]]
- **Series solutions:** substitute $y=\sum a_nx^n$ and solve the recurrence for $a_n$ (for $5y'-3y=0$: $a_n=\frac3{5n}a_{n-1}$).

## Example

$5y'-3y=0$: $5\lambda-3=0$, so $y=Ae^{3x/5}$; $y(0)=y_0\Rightarrow A=y_0$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Homogeneous linear ODEs with constant coefficients|lecture]]

## Related

[[Separable and Exact First-Order ODEs]] · [[Forward Euler Method]] · [[Complex Exponential and Trigonometric Functions]] · [[Vectors and Linear Span]]
