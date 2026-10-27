---
title: Separable and Exact First-Order ODEs
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Separable and Exact First-Order ODEs

> [!abstract] In one paragraph
> Two ways to solve a nonlinear first-order ODE $Q(x,y)\frac{dy}{dx}+P(x,y)=0$ in closed form: separate the variables, or recognise $P\,dx+Q\,dy$ as an exact differential $df$, in which case $f(x,y)=\text{const}$ is the solution.

## Definitions

- **Separable:** can be written $q(y)\,dy=p(x)\,dx$; integrate both sides. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Separable equations|lecture]]
- **Exact:** $P\,dx+Q\,dy=df$ for a single-valued $f$; solve $f_x=P$, $f_y=Q$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Definition — Exact equation|lecture]]
- **Simply connected** domain: path connected, and every closed curve shrinks to a point inside it. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Definition — Simply connected domain|lecture]]

## Key results

- Exact $\Rightarrow\ \frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}$ (commuting mixed partials); not sufficient in general. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Necessary condition for exactness|proof]]
- On a simply connected domain, $\frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x}$ implies exactness. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Theorem — Exactness on simply connected domains|lecture]]

## Method for exact equations

Integrate $f_x=P$ to get $f=\dots+h(y)$; match $f_y=Q$ to find $h'(y)$; the solution is $f(x,y)=\text{const}$. Example: $(2x-3y^2)\,dx+(6y^2-6xy)\,dy=0$ gives $x^2-3xy^2+2y^3=\text{const}$.

## Pitfalls

- The condition $P_y=Q_x$ on a domain with a hole does not guarantee a single-valued $f$.

## Related

[[First-Order Linear Differential Equations]] · [[Partial Derivatives and the Multivariate Chain Rule]]
