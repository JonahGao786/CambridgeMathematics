---
title: Complex Exponential and Trigonometric Functions
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices, complex-numbers]
---

# Complex Exponential and Trigonometric Functions

> [!abstract] In one paragraph
> The exponential series converges for every complex $z$ and satisfies $e^ze^w=e^{z+w}$. Defining $\cos$ and $\sin$ from it gives Euler's formula $e^{iz}=\cos z+i\sin z$, so polar form becomes $z=re^{i\theta}$. The exponential has period $2\pi i$.

## Definitions

$$e^z=\sum_{n\ge0}\frac{z^n}{n!},\qquad\cos z=\frac{e^{iz}+e^{-iz}}2,\qquad\sin z=\frac{e^{iz}-e^{-iz}}{2i}.$$

## Key results

- **Properties.** $e^ze^w=e^{z+w}$, $e^0=1$, $e^{-z}=1/e^z$, $(e^z)^n=e^{nz}$; so $e^z\ne0$. *Idea:* multiply the series and use the binomial theorem. → [[Vectors and Matrices - Chapter 1 Complex Numbers#Proposition — Properties of the exponential|proof]]
- **Euler's formula.** $e^{iz}=\cos z+i\sin z$ for all $z\in\mathbb C$; $e^{x+iy}=e^x(\cos y+i\sin y)$, $|e^{x+iy}|=e^x$. → [[Vectors and Matrices - Chapter 1 Complex Numbers#Definition — Complex sine and cosine|lecture]]
- **Lemma.** $e^z=1\iff z=2\pi in$; hence $e^z=e^w\iff z-w\in2\pi i\mathbb Z$. → [[Vectors and Matrices - Chapter 1 Complex Numbers#Lemma — When the exponential equals 1|proof]]

## Pitfalls

- $|e^{i\theta}|=1$ needs $\theta$ **real**: $e^{i\cdot i}=e^{-1}$.
- The exponential is not one-to-one, which is why logarithms are multi-valued.

## Related

[[Complex Numbers]] · [[De Moivre's Theorem]] · [[Complex Logarithms and Powers]] · [[Roots of Unity]]
