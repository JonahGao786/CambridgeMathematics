---
title: First-Order Linear Differential Equations
material_type: concept note
course: Part IA Differential Equations
source_file: Ch.4 First-order Linear Differential Equations.pdf
drive_file_id: 1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3
source_url: https://drive.google.com/file/d/1WQLRtXlMNVEC8xnZlwGULErVVqAa5qL3/view
source_pages: [1, 2, 3, 4]
---

# First-Order Linear Differential Equations

An ODE has one independent variable. Its order is the order of the highest derivative. It is linear when the dependent variable and its derivatives appear linearly; thus $x^2y+y'=0$ is a first-order linear ODE.

A linear ODE is **homogeneous** when it has no independent forcing term. The zero function is a solution, and multiplying any solution by a constant gives another solution.

## Exponentials and eigenfunctions

The exponential has the series and limit representations
$$e^x=\sum_{n=0}^\infty\frac{x^n}{n!}
=\lim_{k\to\infty}\left(1+\frac{x}{k}\right)^k,$$
and the characterization $f'=f$, $f(0)=1$. It presents the series/limit calculations without the analytic justifications, and refers elsewhere for the exponential addition-law proof.

An **eigenfunction** of differentiation is a non-zero function satisfying
$$f'=\lambda f.$$
For example, $e^{\lambda x}$ has eigenvalue $\lambda$. This motivates trying exponential solutions for homogeneous linear equations with constant coefficients.

## Linear independence of functions

Functions $f_1,\ldots,f_N$ on a common domain are linearly dependent when constants $C_i$, not all zero, satisfy
$$\sum_{i=1}^N C_if_i(x)=0\qquad\text{for all }x.$$
They are linearly independent when the only such constants are all zero.

For an $n$th-order homogeneous linear ODE on an interval, continuous coefficients and a non-vanishing leading coefficient give $n$ independent solutions; all solutions are their linear combinations. For an inhomogeneous equation, add one particular solution. This general result is stated without proof here; the first-order example below shows how one initial value determines one constant.

## Constant-coefficient example

For
$$5y'-3y=0,$$
substituting $y=Ae^{\lambda x}$ with $A\ne0$ gives $5\lambda-3=0$. This gives
$$y(x)=Ae^{3x/5}$$
as the general solution, including $A=0$. The initial condition $y(0)=y_0$ fixes $A=y_0$.

[[Forward Euler Method]] gives a discrete approximation to this same initial-value problem.

See [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]], pages 1–4. Related: [[Differentiation Rules]], [[Complex Exponential and Trigonometric Functions]].
