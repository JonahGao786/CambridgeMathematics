---
title: De Moivre's Theorem
material_type: source-backed theorem and proof
course: Part IA Vectors and Matrices
---

# De Moivre's Theorem

For $\theta\in\mathbb R$ and $n\in\mathbb Z$,
$$ (\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta).$$

The polar multiplication lemma from [[Complex Numbers]] is
$$
r_1(\cos\theta_1+i\sin\theta_1)r_2(\cos\theta_2+i\sin\theta_2)
=r_1r_2\bigl(\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\bigr).
$$
It follows by expanding the product and applying the sine and cosine addition formulae.

For $n\ge0$, induction starts at $n=0$, where both sides are $1$. Multiply the inductive expression by $\cos\theta+i\sin\theta$ and use the lemma for the step from $n$ to $n+1$.

For $n=-m<0$, the positive-power case and unit modulus give
$$
\begin{aligned}
(\cos\theta+i\sin\theta)^{-m}
&=\frac1{\cos(m\theta)+i\sin(m\theta)}\\
&=\cos(m\theta)-i\sin(m\theta)\\
&=\cos(-m\theta)+i\sin(-m\theta).
\end{aligned}
$$

Consequently, if $z=r(\cos\theta+i\sin\theta)\ne0$, then for every $n\in\mathbb Z$,
$$z^n=r^n\bigl(\cos(n\theta)+i\sin(n\theta)\bigr).$$
Example: $(1+i)^4=(\sqrt2)^4(\cos\pi+i\sin\pi)=-4$.

Source: [[Vectors and Matrices - Chapter 1 Complex Numbers]], pages 9–10; the angle addition formulae are written out there.
