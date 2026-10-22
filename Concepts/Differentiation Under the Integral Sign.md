---
title: Differentiation Under the Integral Sign
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Differentiation Under the Integral Sign

> [!abstract] In one paragraph
> When an integral depends on a parameter $c$ — through the integrand and through the limits — its derivative has three parts: differentiate inside, plus the integrand at each moving endpoint times that endpoint's speed.

## Statement

For $I(c)=\int_{a(c)}^{b(c)}f(x;c)\,dx$:
$$\frac{dI}{dc}=\int_{a(c)}^{b(c)}\frac{\partial f}{\partial c}(x;c)\,dx+f(b(c);c)\frac{db}{dc}-f(a(c);c)\frac{da}{dc}.$$
*Idea:* split the difference quotient into the change of integrand on the old interval plus two thin end strips; apply the mean value theorem to each strip. → [[Differential Equations - Chapter 3 Partial Differentiation#Theorem — Differentiating an integral with respect to a parameter|proof]]

## Examples

- $I(\lambda)=\int_0^\lambda e^{-\lambda x^2}dx$: $I'(\lambda)=-\int_0^\lambda x^2e^{-\lambda x^2}dx+e^{-\lambda^3}$.
- $\int_0^\infty x^ne^{-x}dx=n!$: differentiate $\int_0^\infty e^{-\lambda x}dx=\frac1\lambda$ $n$ times in $\lambda$, then set $\lambda=1$.

## Related

[[Riemann Integration and the Fundamental Theorem of Calculus]] · [[Partial Derivatives and the Multivariate Chain Rule]]
