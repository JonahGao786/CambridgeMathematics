---
title: Complex Logarithms and Powers
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices, complex-numbers]
---

# Complex Logarithms and Powers

> [!abstract] In one paragraph
> Because $e^w$ has period $2\pi i$, a non-zero $z$ has infinitely many logarithms, differing by multiples of $2\pi i$. Powers $z^\alpha=e^{\alpha L}$ inherit this: one value for integer $\alpha$, $q$ values for $\alpha=p/q$, infinitely many otherwise.

## Definitions

- A **logarithm** of $z\ne0$ is any $w$ with $e^w=z$; they are $\log|z|+i\theta$, $\theta\in\operatorname{Arg}z$.
- Principal logarithm $\log z=\log|z|+i\arg z$ ($\arg z\in(-\pi,\pi]$); all logarithms $\operatorname{Log}z=\{\log z+2\pi ni:n\in\mathbb Z\}$ (a **set**).
- $z^\alpha=e^{\alpha L}$ for a chosen $L\in\operatorname{Log}z$; principal value $e^{\alpha\log z}$.

→ [[Vectors and Matrices - Chapter 1 Complex Numbers#Definition — Logarithm|lecture]]

## Key results

- **Number of values.** $L\mapsto L+2\pi ni$ multiplies $z^\alpha$ by $e^{2\pi in\alpha}$: unique if $\alpha\in\mathbb Z$; exactly $q$ values if $\alpha=p/q$ in lowest terms; infinitely many otherwise.
- **Power laws** $z^\alpha z^\beta=z^{\alpha+\beta}$, $(z^\alpha)^\beta=z^{\alpha\beta}$ hold for **compatible** choices of logarithm. → [[Vectors and Matrices - Chapter 1 Complex Numbers#Definition — Complex powers|lecture]]

## Examples

- $i^i=e^{-(\pi/2+2\pi n)}$, $n\in\mathbb Z$ — all positive reals; principal value $e^{-\pi/2}$.
- $(1+i)^{1/2}=\pm2^{1/4}e^{i\pi/8}$; principal value $2^{1/4}e^{i\pi/8}$.

## Pitfalls

- Principal values alone can break the power laws: $\big((-1)^2\big)^{1/2}=1^{1/2}=1$ (principal), but $(-1)^{2\cdot\frac12}=-1$.

## Related

[[Complex Exponential and Trigonometric Functions]] · [[Roots of Unity]]
