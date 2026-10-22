---
title: Integration by Substitution and by Parts
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Integration by Substitution and by Parts

> [!abstract] In one paragraph
> Substitution reverses the chain rule: replace an inner function by a new variable. Integration by parts reverses the product rule: $\int uv'=uv-\int u'v$.

## Substitution

If the integrand contains a function of a function, substitute for the inner function. E.g. $u=x-x^2$: $\int\frac{1-2x}{\sqrt{x-x^2}}dx=\int\frac{du}{\sqrt u}=2\sqrt{x-x^2}+C$.

| Integrand contains | Substitution | Identity used |
| --- | --- | --- |
| $\sqrt{1-x^2}$ | $x=\sin\theta$ | $\cos^2+\sin^2=1$ |
| $1+x^2$ | $x=\tan\theta$ | $1+\tan^2=\sec^2$ |
| $\sqrt{x^2-1}$ | $x=\cosh u$ | $\cosh^2-\sinh^2=1$ |
| $\sqrt{x^2+1}$ | $x=\sinh u$ | $\cosh^2-\sinh^2=1$ |
| $1-x^2$ | $x=\tanh u$ | $1-\tanh^2=\operatorname{sech}^2$ |

**Example.** $\int\sqrt{2x-x^2}\,dx$ with $x-1=\sin\theta$, $\theta\in[-\frac\pi2,\frac\pi2]$: $=\frac12\arcsin(x-1)+\frac12(x-1)\sqrt{1-(x-1)^2}+C$. → [[Differential Equations - Chapter 2 Integration#Trigonometric and hyperbolic substitutions|lecture]]

## Integration by parts

$$\int uv'\,dx=uv-\int u'v\,dx.$$
- $\int_0^\infty xe^{-x}dx=1$ ($u=x$, $v'=e^{-x}$).
- $\int\log x\,dx=x(\log x-1)+C$ ($u=\log x$, $v'=1$) — the same trick works for inverse trig/hyperbolic functions.

→ [[Differential Equations - Chapter 2 Integration#Integration by parts|lecture]]

## Pitfalls

- With a trigonometric substitution, fix the branch of $\theta$ so the substitution is one-to-one and $\sqrt{\cos^2\theta}=\cos\theta$.

## Related

[[Riemann Integration and the Fundamental Theorem of Calculus]] · [[Differentiation Rules]]
