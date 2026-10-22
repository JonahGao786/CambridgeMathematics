---
title: Taylor Series and Taylor's Theorem
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Taylor Series and Taylor's Theorem

> [!abstract] In one paragraph
> Near $x_0$, a function is approximated by the polynomial $P_n$ matching its first $n$ derivatives. Taylor's theorem controls the error: $o(h^n)$ in general, and $O(h^{n+1})$ (Lagrange form) if $f^{(n+1)}$ is continuous. The full Taylor series equals $f$ only if the remainders tend to $0$.

## Definitions

- **Taylor series** about $x_0$: $T_f(x)=\sum_{k\ge0}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$ (an infinite series).
- **Taylor polynomial** of degree $n$: $P_n(x)=\sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$.

## Key results

- **Taylor's theorem.** $f$ $n$ times differentiable at $x_0$: $f(x_0+h)=\sum_{k=0}^n\frac{h^k}{k!}f^{(k)}(x_0)+E_n$, $E_n=o(h^n)$.
- **Stronger version.** If $f^{(n+1)}$ exists and is continuous on $(x_0,x_0+h)$: $E_n=\frac{h^{n+1}}{(n+1)!}f^{(n+1)}(x_n)=O(h^{n+1})$ for some $x_0\le x_n\le x_0+h$.
- If $\lim_{n\to\infty}E_n=0$, the Taylor series converges to $f(x)$.

→ [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Theorem — Taylor's theorem|lecture]]

## Example

$e^x$ about $0$, $h>0$: fractional error $\frac{E_n}{e^h}=\frac{h^{n+1}}{(n+1)!}e^{x_n-h}\le\frac{h^{n+1}}{(n+1)!}$ — choose $n$ to meet a target accuracy.

## Pitfalls

- $O(h^{n+1})$ is stronger than $o(h^n)$: $h^{n+1/2}$ is $o(h^n)$ but not $O(h^{n+1})$.
- A good approximation for small $h$ at fixed $n$ says nothing about convergence of the whole series.

## Related

[[Limits, Big O and Little o - A First-Year Guide]] · [[L'Hôpital's Rule]] · [[Complex Exponential and Trigonometric Functions]]
