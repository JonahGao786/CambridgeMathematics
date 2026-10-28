---
title: Fixed Points and Stability
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Fixed Points and Stability

> [!abstract] In one paragraph
> A fixed point of $y'=f(t,y)$ is a constant solution $y=c$. It is stable if nearby solutions converge to it and unstable if they move away. Linearising about $c$ turns the question into the sign of $\partial f/\partial y$.

## Definitions

- **Fixed point:** constant solution $y=c$, i.e. $f(t,c)=0$ for all $t$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Definition — Fixed point|lecture]]
- **Stable / unstable:** nearby solutions converge to / diverge from $c$ as $t\to\infty$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Definition — Stable and unstable fixed points|lecture]]
- **Autonomous:** $y'=f(y)$, no explicit $t$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Autonomous equations|lecture]]

## Key results

- **Perturbation analysis.** Put $y=c+\varepsilon$; then $\varepsilon'\approx\varepsilon\,\frac{\partial f}{\partial y}(t,c)$. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Perturbation analysis and stability|lecture]]
- **Autonomous case.** $\varepsilon'\approx f'(c)\varepsilon$, so $\varepsilon=\varepsilon_0e^{kt}$ with $k=f'(c)$: stable if $f'(c)<0$, unstable if $f'(c)>0$. If $f'(c)=0$, higher-order terms decide.
- **Example.** $y'=t(1-y^2)$: $y=1$ is stable ($\varepsilon=\varepsilon_0e^{-t^2}$), $y=-1$ is unstable ($\varepsilon=\varepsilon_0e^{t^2}$).

## Slope fields and isoclines

The slope field draws the gradient $f(t,y)$ at each point as a short stick tangent to solution curves; isoclines are the curves $f(t,y)=\text{const}$. Solution curves never cross when $f$ is single valued. → [[Differential Equations - Chapter 4 First-Order Linear Differential Equations#Slope field and isoclines|lecture]]

## Related

[[Separable and Exact First-Order ODEs]] · [[First-Order Linear Differential Equations]] · [[Taylor Series and Taylor's Theorem]]
