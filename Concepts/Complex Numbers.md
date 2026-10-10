---
title: Complex Numbers
material_type: source-backed definitions and properties
course: Part IA Vectors and Matrices
---

# Complex Numbers

$$\mathbb C=\{x+iy:x,y\in\mathbb R\},\qquad i^2=-1.$$
The representation is unique; $\operatorname{Re}(x+iy)=x$ and $\operatorname{Im}(x+iy)=y$. Real numbers are identified with $x+i0$; numbers $iy$ with $y\ne0$ are purely imaginary.

For $z=x+iy$,
$$\overline z=x-iy,\qquad |z|=\sqrt{x^2+y^2},\qquad z\overline z=|z|^2.$$
For $z\ne0$,
$$z^{-1}=\frac{\overline z}{|z|^2}=\frac{x-iy}{x^2+y^2}.$$
Conjugation respects addition and multiplication, $\overline{\overline z}=z$, and $|\overline z|=|z|$.

For $z\ne0$, polar form is
$$z=r(\cos\theta+i\sin\theta),\qquad r=|z|,$$
with $x=r\cos\theta$ and $y=r\sin\theta$. The principal argument is in $(-\pi,\pi]$; all arguments differ from it by an integer multiple of $2\pi$. The argument of $0$ is undefined.

Moduli multiply and, for non-zero numbers, arguments add modulo $2\pi$. See [[De Moivre's Theorem]] for integer powers and [[Triangle Inequality for Complex Numbers]] for modulus bounds.

Source: [[Vectors and Matrices - Chapter 1 Complex Numbers]], pages 2–9, including arithmetic, conjugation properties, their geometric diagrams and proofs of modulus properties.

The later lecture material develops [[Complex Exponential and Trigonometric Functions]], [[Roots of Unity]] and [[Complex Logarithms and Powers]]. Lines, circles and geometric transformations are in the same lecture note, pages 19–21.
