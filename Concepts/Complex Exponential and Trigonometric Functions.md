---
title: Complex Exponential and Trigonometric Functions
material_type: source-backed definitions and proofs with supplementary explanation
course: Part IA Vectors and Matrices
---

# Complex Exponential and Trigonometric Functions

For $z\in\mathbb C$,
$$e^z=\sum_{n=0}^{\infty}\frac{z^n}{n!}.$$
The series is absolutely convergent: for $z\ne0$, the ratio of successive absolute terms is $|z|/(n+1)\to0$; at $z=0$ the result is $1$.

For $z,w\in\mathbb C$ and $n\in\mathbb Z$,
$$e^ze^w=e^{z+w},\qquad e^0=1,\qquad
e^{-z}=1/e^z,\qquad(e^z)^n=e^{nz}.$$
In particular, the exponential never vanishes. The full series-product and induction proofs are in [[Vectors and Matrices - Chapter 1 Complex Numbers]], pages 11–13.

## Euler's formula

Define
$$
\cos z=\frac{e^{iz}+e^{-iz}}2,\qquad
\sin z=\frac{e^{iz}-e^{-iz}}{2i}.
$$
Their series are
$$
\cos z=\sum_{n=0}^{\infty}(-1)^n\frac{z^{2n}}{(2n)!},\qquad
\sin z=\sum_{n=0}^{\infty}(-1)^n\frac{z^{2n+1}}{(2n+1)!}.
$$
Adding the defining expressions gives
$$e^{iz}=\cos z+i\sin z\qquad(z\in\mathbb C).$$

For $\theta\in\mathbb R$, $|e^{i\theta}|=1$, so [[Complex Numbers|polar form]] becomes $z=re^{i\theta}$. More generally, for $x,y\in\mathbb R$,
$$e^{x+iy}=e^x(\cos y+i\sin y),\qquad |e^{x+iy}|=e^x.$$

## Periodicity

Writing $z=x+iy$ shows
$$e^z=1\Longleftrightarrow z=2\pi in
\quad\text{for some }n\in\mathbb Z.$$
Thus
$$e^z=e^w\Longleftrightarrow z-w=2\pi in
\quad\text{for some }n\in\mathbb Z.$$
This explains the multiple values in [[Complex Logarithms and Powers]] and the construction of [[Roots of Unity]].

## What absolute convergence permits — supplementary explanation

A series $\sum a_n$ converges absolutely when the real series $\sum|a_n|$ converges. For the exponential, once $n$ is large enough that $|z|/(n+1)\le1/2$, each successive absolute term is at most half the previous one. The remaining tail is bounded by a convergent geometric series.

For the product of two exponential series, the sum of absolute values of all pairwise terms is finite:
$$
\sum_{j,k\ge0}
\left|\frac{z^jw^k}{j!k!}\right|
=
\left(\sum_{j\ge0}\frac{|z|^j}{j!}\right)
\left(\sum_{k\ge0}\frac{|w|^k}{k!}\right)<\infty.
$$
Consequently those terms can be regrouped by $j+k$ in the product proof. Absolute convergence supplies the justification for the rearrangement.

Euler's formula holds for complex inputs, but the unit-modulus conclusion requires a **real** angle. For example, $e^{i(i)}=e^{-1}$ has modulus $e^{-1}$, not $1$.

Source: [[Vectors and Matrices - Chapter 1 Complex Numbers]], pages 11–14. The explanations in this final section are additional teaching detail.
