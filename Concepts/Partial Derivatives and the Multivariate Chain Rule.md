---
title: Partial Derivatives and the Multivariate Chain Rule
material_type: source-backed definitions, examples and theorem statements with supplementary explanation
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: [1, 2, 3, 4]
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

**Corrected proof:** [[Differential Equations - Chapter 3 Partial Differentiation]] now proves total differentiability under continuous first partial derivatives using coordinate increments and the mean value theorem, then proves the chain rule under total differentiability. The incorrect source definition $df=\lim\delta f$ has been replaced by the linear-map definition below. These repairs are labelled supplementary; the contour drawing is unchanged.

Related: [[Differentiation Rules]], [[Taylor Series and Taylor's Theorem]], [[Riemann Integration and the Fundamental Theorem of Calculus]].

## Partial derivatives versus differentiability — supplementary explanation

For $p=(x,y)$ in an open domain, **differentiability** means there is a linear map $L$ such that
$$f(p+h)-f(p)=L(h)+o(\|h\|),\qquad h\to0,$$
where $\|h\|=\sqrt{h_x^2+h_y^2}$. Necessarily
$$L(h)=f_x(p)h_x+f_y(p)h_y.$$
The differential $df_p$ is this map $L$, not the unscaled limit of the change in $f$. Compare the one-variable expansion in [[Limits, Big O and Little o - A First-Year Guide]]. Continuous first partial derivatives in a neighbourhood are a sufficient condition for differentiability.

Having partial derivatives alone is weaker. Define $f(0,0)=0$ and $f(x,y)=xy/(x^2+y^2)$ elsewhere. Both partial derivatives at the origin are zero, since the function vanishes on the axes. But $f(t,t)=1/2$ for $t\ne0$, so $f$ is not even continuous there.

For a differentiable path $p(t)$, its increment is
$$p(t+s)-p(t)=s\,p'(t)+o(s)=O(s).$$
Substituting into the differentiability expansion gives
$$f(p(t+s))-f(p(t))=s\,df_{p(t)}(p'(t))+o(s).$$
The remainder is $o(s)$ because its size relative to the path increment tends to zero and that increment is $O(s)$; a zero increment contributes zero remainder. Divide by $s$ to obtain the chain rule. This is the same remainder argument used in the corrected lecture proof.

For a continuously differentiable implicit relation $F(x,y,z)=0$, a standard sufficient condition for solving locally for one variable is that the partial derivative with respect to that variable is non-zero (the implicit function theorem). Expressions obtained by dividing by $F_x,F_y$ or $F_z$ are only valid where those denominators are non-zero. This qualification matters in questions 11–12 of [[Differential Equations - Examples Sheet 1 2026]].
