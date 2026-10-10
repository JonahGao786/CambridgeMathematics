---
title: Roots of Unity
material_type: source-backed theorem and proof with supplementary explanation
course: Part IA Vectors and Matrices
---

# Roots of Unity

For an integer $N\ge1$, the solutions of $z^N=1$ are
$$z_k=e^{2\pi ik/N}=\omega^k,\qquad
k=0,\ldots,N-1,\qquad\omega=e^{2\pi i/N}.$$
There are $N$ distinct roots on the unit circle, equally spaced by angle $2\pi/N$. For $N\ge3$, they are the vertices of a regular $N$-gon.

**Proof.** Write $z=re^{i\theta}$. The equation $r^Ne^{iN\theta}=1$ requires $r^N=1$ and $N\theta=2\pi n$ for some $n\in\mathbb Z$. Since $r>0$, $r=1$. The angles with $n=0,\ldots,N-1$ give distinct points, and increasing $n$ by $N$ repeats a point.

## Roots of a non-zero complex number

For $a=Re^{i\theta}\ne0$ and $N\ge1$, the solutions of $z^N=a$ are
$$z_n=R^{1/N}e^{i(\theta+2\pi n)/N},\qquad n=0,\ldots,N-1.$$
Here $R^{1/N}$ is the positive real root. The roots are equally spaced on a circle of radius $R^{1/N}$.

If $a=0$, only $z=0$ is a root, with multiplicity $N$.

**Supplementary explanation.** Replacing the chosen argument $\theta$ by $\theta+2\pi m$ just relabels these $N$ roots. It does not change their set. The factor $e^{2\pi in/N}$ makes every root a rotation of any one chosen root.

Source: [[Vectors and Matrices - Chapter 1 Complex Numbers]], page 15. Related: [[De Moivre's Theorem]], [[Complex Exponential and Trigonometric Functions]], [[Complex Logarithms and Powers]].
