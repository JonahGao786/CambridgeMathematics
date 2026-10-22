---
title: L'Hôpital's Rule
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# L'Hôpital's Rule

> [!abstract] In one paragraph
> For a $0/0$ limit, replace $f/g$ by $f'/g'$. The lecture proves it, under extra assumptions, by first-order Taylor expansion: near $x_0$ both functions are approximately linear, so their ratio is the ratio of slopes.

## Statement

$f,g$ differentiable on an open interval containing $x_0$, $g'(x)\ne0$ for $x\ne x_0$, and $f(x_0)=g(x_0)=0$ (as limits). Then
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}=\lim_{x\to x_0}\frac{f'(x)}{g'(x)},$$
provided the right-hand limit exists. → [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Theorem — L'Hopital's rule|lecture]]

*Proof idea (when $g'(x_0)\ne0$ and $f',g'$ continuous):* $\frac{f(x)}{g(x)}=\frac{f'(x_0)+o(x-x_0)/(x-x_0)}{g'(x_0)+o(x-x_0)/(x-x_0)}\to\frac{f'(x_0)}{g'(x_0)}$.

**Generalisation.** If also $f'(x_0)=g'(x_0)=0$, use $f''/g''$, and so on.

## Example

$$\lim_{x\to0}\frac{3\sin x-\sin3x}{2x-\sin2x}=\frac{f'''(0)}{g'''(0)}=\frac{-3+27}{8}=3.$$

## Pitfalls

- Check that the form really is $0/0$ before differentiating.
- Differentiate numerator and denominator **separately** — not the quotient.

## Related

[[Taylor Series and Taylor's Theorem]] · [[Limits, Big O and Little o - A First-Year Guide]]
