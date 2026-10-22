---
title: Complex Numbers
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices, complex-numbers]
---

# Complex Numbers

> [!abstract] In one paragraph
> A complex number $z=x+iy$ is a point of the plane. Addition is vector addition; multiplication multiplies moduli and adds arguments. Conjugation reflects in the real axis, and $z\bar z=|z|^2$ makes division possible.

## Definitions

- $\mathbb C=\{x+iy:x,y\in\mathbb R\}$, $i^2=-1$; $\operatorname{Re}z=x$, $\operatorname{Im}z=y$.
- $\bar z=x-iy$, $|z|=\sqrt{x^2+y^2}$, $z\bar z=|z|^2$, $z^{-1}=\bar z/|z|^2$.
- Polar form $z=r(\cos\theta+i\sin\theta)=re^{i\theta}$, $r=|z|$; principal argument $\arg z\in(-\pi,\pi]$, all arguments $\operatorname{Arg}z=\{\arg z+2\pi n\}$; $\arg0$ undefined.
→ [[Vectors and Matrices - Chapter 1 Complex Numbers#Definition — Argument and polar form|lecture]]

## Key results

- **Conjugation.** $\overline{z_1+z_2}=\bar z_1+\bar z_2$, $\overline{z_1z_2}=\bar z_1\bar z_2$, $\operatorname{Re}z=\frac{z+\bar z}2$, $\operatorname{Im}z=\frac{z-\bar z}{2i}$; $z$ real $\iff z=\bar z$.
- **Modulus.** $|z_1z_2|=|z_1||z_2|$ and the triangle inequalities. → [[Triangle Inequality for Complex Numbers]]
- **Polar multiplication.** Moduli multiply, arguments add (mod $2\pi$). → [[De Moivre's Theorem]]
- **Fundamental theorem of algebra.** → [[Fundamental Theorem of Algebra]]

## Geometry

- $|z_1-z_2|$ is the distance between $z_1$ and $z_2$.
- Line through $z_0$ in direction $w$: $z=z_0+\lambda w$ ($\lambda\in\mathbb R$), i.e. $\bar wz-\bar wz_0=w\bar z-w\bar z_0$.
- Circle: $|z-c|=\rho\iff|z|^2-c\bar z-\bar cz=\rho^2-|c|^2$.
- $z\mapsto z+z_0$ translates, $z\mapsto\lambda z$ ($\lambda>0$) scales, $z\mapsto e^{i\theta}z$ rotates, $z\mapsto\bar z$ reflects.
→ [[Vectors and Matrices - Chapter 1 Complex Numbers#Geometric transformations|lecture]]

## Related

[[Complex Exponential and Trigonometric Functions]] · [[Roots of Unity]] · [[Complex Logarithms and Powers]] · [[Isometries and Dihedral Groups]]
