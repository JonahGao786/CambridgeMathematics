---
title: Implicit Differentiation
material_type: source-backed formulas, derivation and example
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: [5, 6, 7, 8, 9]
---

# Implicit Differentiation

On a level surface $f(x,y,z)=c$, the [[Partial Derivatives and the Multivariate Chain Rule|chain rule]] gives
$$f_x\,dx+f_y\,dy+f_z\,dz=0.$$
Locally, if the indicated implicit function is differentiable and the denominator is non-zero,
$$\left.\frac{\partial z}{\partial x}\right|_y=-\frac{f_x}{f_z}.$$
Here $f_x$ holds $y,z$ fixed, while $f_z$ holds $x,y$ fixed. The derivative of the restricted function $f(x,y,z(x,y))$ is zero, although the ambient partial $f_x$ need not be zero.

For $xy+y^2z+z^5=1$,
$$\left.\frac{\partial z}{\partial x}\right|_y=-\frac{y}{y^2+5z^4}.$$

The cyclic and reciprocal rules, where all ratios are defined, are
$$\left.\frac{\partial x}{\partial y}\right|_z
\left.\frac{\partial y}{\partial z}\right|_x
\left.\frac{\partial z}{\partial x}\right|_y=-1,$$
$$\left.\frac{\partial z}{\partial x}\right|_y
=\frac{1}{\left.\dfrac{\partial x}{\partial z}\right|_y}.$$
Reciprocation requires the same held-fixed variable; replacing it by a different coordinate does not generally preserve the rule.

For the change $x=r\cos\theta$, $y=r\sin\theta$,
$$f_r=f_x\cos\theta+f_y\sin\theta,\qquad
f_\theta=-r\sin\theta\,f_x+r\cos\theta\,f_y,$$
with $\theta$ fixed in $f_r$ and $r$ fixed in $f_\theta$.

Source: [[Differential Equations - Chapter 3 Partial Differentiation]], pages 5–9, which retains all fixed-variable bars, derivations and source geometry as TikZ.
