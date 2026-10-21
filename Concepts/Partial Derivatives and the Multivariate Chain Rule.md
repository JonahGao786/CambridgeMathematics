---
title: Partial Derivatives and the Multivariate Chain Rule
material_type: concept note
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
reference_handout: topic1.pdf
reference_handout_pages: "20–27"
---

# Partial Derivatives and the Multivariate Chain Rule

## Hold the other variables fixed

A partial derivative differentiates with respect to one variable while holding the other independent variables fixed:
$$f_x(x,y)=\lim_{h\to0}\frac{f(x+h,y)-f(x,y)}h.$$
For $f(x,y,z)$, differentiating with respect to $x$ holds both $y$ and $z$ fixed. A contour $f(x,y)=\text{constant}$ helps visualize why the slope depends on direction.

For $f=x^2+y^3+e^{xy^2}$,
$$f_x=2x+y^2e^{xy^2},\qquad f_y=3y^2+2xye^{xy^2},$$
$$f_{xx}=2+y^4e^{xy^2},\qquad
f_{xy}=f_{yx}=2ye^{xy^2}+2xy^3e^{xy^2}.$$
$f_{xy}=(f_x)_y$: differentiate first with respect to $x$, then $y$. **Schwarz's theorem** says that continuous second partial derivatives nearby guarantee equality of the mixed derivatives; its proof is not needed here.

## Small changes and the differential

For a smooth function, the first-order change is
$$\delta f\approx f_x\,\delta x+f_y\,\delta y.$$
Each contribution is a slope multiplied by the corresponding change. We write this first-order part as
$$df=f_x\,dx+f_y\,dy.$$
The actual change $\delta f$ also contains smaller terms. The differential is this first-order expression, not the ordinary limit of $\delta f$.

## Chain rule along a path

If $x=x(t)$ and $y=y(t)$, both variables contribute to the rate of change:
$$\frac{df}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt}.$$
The lecture derives this by substituting the small changes in $x,y$, dividing by the small time interval and taking the limit. Continuous first partial derivatives of $f$ nearby and a differentiable path are sufficient conditions.

If instead $y=y(x)$,
$$\frac{d}{dx}f(x,y(x))=f_x+f_y\frac{dy}{dx}.$$
For a continuously differentiable path and function, integration gives
$$f(x(t_1),y(t_1))-f(x(t_0),y(t_0))
=\int_{t_0}^{t_1}(f_x\,x'(t)+f_y\,y'(t))\,dt.$$
Thus integrating $df$ gives the change between the endpoints.

Applications: [[Implicit Differentiation]] and [[Differentiation Under the Integral Sign]]. For implicit derivatives, keep track of which variable is fixed and only divide by a non-zero partial derivative.

See [[Differential Equations - Chapter 3 Partial Differentiation]], sections 3.1–3.4.
