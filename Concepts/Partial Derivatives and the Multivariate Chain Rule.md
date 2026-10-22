---
title: Partial Derivatives and the Multivariate Chain Rule
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Partial Derivatives and the Multivariate Chain Rule

> [!abstract] In one paragraph
> A partial derivative is the slope in one coordinate direction with the other variables held fixed. A small change in $f$ is the sum of the changes due to each variable, $df=f_x\,dx+f_y\,dy$; dividing by $dt$ along a path gives the chain rule.

## Definitions

- $\left.\frac{\partial f}{\partial x}\right|_y=\lim_{\delta x\to0}\frac{f(x+\delta x,y)-f(x,y)}{\delta x}$; writing just $\frac{\partial f}{\partial x}$ means **all other** variables are fixed.
- $f_x=\frac{\partial f}{\partial x}$, $f_{xy}=\frac{\partial^2 f}{\partial y\,\partial x}$ ($x$ first, then $y$).
- **Differential** $df=f_x\,dx+f_y\,dy$.

→ [[Differential Equations - Chapter 3 Partial Differentiation#Definition — Partial derivative|lecture]]

## Key results

- **Schwarz.** Continuous second derivatives $\Rightarrow f_{xy}=f_{yx}$.
- **Chain rule.** Along $x(t),y(t)$: $\frac{df}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}$; along $y(x)$: $\frac d{dx}f(x,y(x))=f_x+f_y\frac{dy}{dx}$. → [[Differential Equations - Chapter 3 Partial Differentiation#Theorem — Chain rule for partial derivatives|derivation]]
- **Integral form.** $\Delta f=\int(f_x\,dx+f_y\,dy)$ along a given path.
- **Polar coordinates.** $f_r=f_x\cos\theta+f_y\sin\theta$, $f_\theta=-r\sin\theta\,f_x+r\cos\theta\,f_y$. → [[Differential Equations - Chapter 3 Partial Differentiation#Change of variables|lecture]]

## Pitfalls

- For $f(x,y,z)$, $\left.\frac{\partial f}{\partial x}\right|_{y,z}\ne\left.\frac{\partial f}{\partial x}\right|_y$ in general — always know which variables are held fixed.

## Related

[[Implicit Differentiation]] · [[Differentiation Under the Integral Sign]] · [[Differentiation Rules]]
