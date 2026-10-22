---
title: Forward Euler Method
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Forward Euler Method

> [!abstract] In one paragraph
> Replace $\frac{dy}{dx}$ at grid points $x_n=nh$ by the forward difference $\frac{y_{n+1}-y_n}h$. The ODE becomes a recurrence relation that can be iterated from the initial value. Simple, but not very accurate ("not great").

## Method

$$\left.\frac{dy}{dx}\right|_{x_n}\approx\frac{y_{n+1}-y_n}h,\qquad y_n\approx y(x_n).$$

## Example

$5y'-3y=0$, $y(0)=y_0$:
$$5\,\frac{y_{n+1}-y_n}h-3y_n=0\ \Longrightarrow\ y_{n+1}=\Big(1+\frac{3h}5\Big)y_n\ \Longrightarrow\ y_n=\Big(1+\frac{3h}5\Big)^ny_0.$$
→ [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Discrete equations|lecture]]

> [!note] Explanation
> At $x=nh$ fixed, $\big(1+\frac{3x}{5n}\big)^n\to e^{3x/5}$ as $n\to\infty$ — the exact solution — using $\exp(x)=\lim_k(1+\frac xk)^k$ from the same chapter.

## Related

[[First-Order Linear Differential Equations]]
