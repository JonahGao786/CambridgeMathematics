---
title: De Moivre's Theorem
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices, complex-numbers]
---

# De Moivre's Theorem

> [!abstract] In one paragraph
> Multiplying complex numbers in polar form multiplies the moduli and adds the angles. Repeating this gives integer powers: raising to the $n$th power multiplies the angle by $n$.

## Key results

- **Lemma — polar multiplication.** $r_1(\cos\theta_1+i\sin\theta_1)\cdot r_2(\cos\theta_2+i\sin\theta_2)=r_1r_2(\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2))$. *Idea:* expand and use the angle addition formulae. → [[Vectors and Matrices - Chapter 1 Complex Numbers#Lemma — Multiplying in polar form|proof]]
- **Theorem — De Moivre.** For $\theta\in\mathbb R$, $n\in\mathbb Z$: $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$. *Idea:* induction for $n\ge0$; for $n=-m$ take the reciprocal of a unit-modulus number. → [[Vectors and Matrices - Chapter 1 Complex Numbers#Theorem — De Moivre's theorem|proof]]
- **Consequence.** $z=r(\cos\theta+i\sin\theta)\ne0\Rightarrow z^n=r^n(\cos n\theta+i\sin n\theta)$.

## Example

$(1+i)^4=(\sqrt2)^4(\cos\pi+i\sin\pi)=-4$.

## Related

[[Complex Numbers]] · [[Complex Exponential and Trigonometric Functions]] · [[Roots of Unity]]
