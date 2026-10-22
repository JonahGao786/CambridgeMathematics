---
title: Implicit Differentiation
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Implicit Differentiation

> [!abstract] In one paragraph
> An equation $f(x,y,z)=c$ defines a surface on which each variable is implicitly a function of the other two, even when no formula is available. Setting $df=0$ gives their partial derivatives.

## Key results

- **Formula.** On $f(x,y,z)=c$: $\left.\frac{\partial z}{\partial x}\right|_y=-\dfrac{\left.\partial f/\partial x\right|_{y,z}}{\left.\partial f/\partial z\right|_{x,y}}$. *Idea:* differentiate $f(x,y,z(x,y))=c$ in $x$ at fixed $y$.
- **Cyclic rule.** $\left.\frac{\partial x}{\partial y}\right|_z\left.\frac{\partial y}{\partial z}\right|_x\left.\frac{\partial z}{\partial x}\right|_y=-1$.
- **Reciprocal rule.** $\left.\frac{\partial z}{\partial x}\right|_y=1\big/\left.\frac{\partial x}{\partial z}\right|_y$ — only with the **same** variable held fixed.

→ [[Differential Equations - Chapter 3 Partial Differentiation#Implicit differentiation|lecture]]

## Example

$xy+y^2z+z^5=1$: differentiating in $x$ at fixed $y$, $y+(y^2+5z^4)\left.\frac{\partial z}{\partial x}\right|_y=0$, so $\left.\frac{\partial z}{\partial x}\right|_y=-\frac{y}{y^2+5z^4}$.

## Pitfalls

- The cyclic rule has $-1$, not $+1$.
- $\left.\frac{\partial r}{\partial x}\right|_y\ne1\big/\left.\frac{\partial x}{\partial r}\right|_\theta$: different variables are held fixed.

## Related

[[Partial Derivatives and the Multivariate Chain Rule]]
