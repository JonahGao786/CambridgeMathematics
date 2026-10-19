---
title: Partial Derivatives and the Multivariate Chain Rule
material_type: source-backed definitions, examples and theorem statements
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
---

# Partial Derivatives and the Multivariate Chain Rule

A partial derivative holds every other independent variable fixed:
$$f_x(x,y)=\lim_{h\to0}\frac{f(x+h,y)-f(x,y)}h.$$
For $f(x,y,z)$, differentiating with respect to $x$ holds both $y$ and $z$ fixed. A contour is a level curve $f(x,y)=\text{constant}$; slopes can depend on direction.

For $f=x^2+y^3+e^{xy^2}$,
$$f_x=2x+y^2e^{xy^2},\qquad f_y=3y^2+2xye^{xy^2},$$
$$f_{xx}=2+y^4e^{xy^2},\qquad
\frac{\partial}{\partial x}\frac{\partial f}{\partial y}
=\frac{\partial}{\partial y}\frac{\partial f}{\partial x}
=2ye^{xy^2}+2xy^3e^{xy^2}.$$

**Schwarz's theorem (statement only):** continuous second partial derivatives in a neighbourhood imply equality of the mixed partial derivatives. The source writes $f_{xy}=\partial^2 f/(\partial x\,\partial y)$ with the rightmost differentiation performed first; check this convention when using subscripts.

For differentiable $f$ and a differentiable path $x(t),y(t)$, the **chain rule** is
$$\frac d{dt}f(x(t),y(t))=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}.$$
Equivalently, $df=f_x\,dx+f_y\,dy$ is the linear first-order differential. If $y=y(x)$,
$$\frac d{dx}f(x,y(x))=f_x+f_y\frac{dy}{dx}.$$
Under sufficient regularity for integration, such as continuously differentiable $f$ and path,
$$f(x(t_1),y(t_1))-f(x(t_0),y(t_0))
=\int_{t_0}^{t_1}(f_x\,x'(t)+f_y\,y'(t))\,dt.$$

**Proof status:** [[Differential Equations - Chapter 3 Partial Differentiation]], pages 3–4, retains the increment derivation with a localized TODO for regularity/uniform remainder control, and flags the incorrect definition $df=\lim\delta f$. These gaps are not a proof of the general theorem. The source note contains the contour drawing and all differentiation steps.

Applications in [[Differential Equations - Chapter 3 Partial Differentiation]], pages 5–10, now include the polar-coordinate chain rule, [[Implicit Differentiation|implicit differentiation with fixed-variable, cyclic and reciprocal rules]], and [[Differentiation Under the Integral Sign|Leibniz's integral rule]]. The earlier derivation flags on pages 3–4 remain.

Related: [[Differentiation Rules]], [[Taylor Series and Taylor's Theorem]], [[Riemann Integration and the Fundamental Theorem of Calculus]].
