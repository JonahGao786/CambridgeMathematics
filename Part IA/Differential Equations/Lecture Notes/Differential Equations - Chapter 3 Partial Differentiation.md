---
title: Differential Equations - Chapter 3 Partial Differentiation
material_type: source-backed notes with course-level explanations
course: Part IA Differential Equations
date: null
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
reference_handout: topic1.pdf
reference_handout_pages: "20–29"
source_pages: 11
---

# Differential Equations — Chapter 3: Partial Differentiation

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view). No date is supplied.

## 3.1 Functions of several variables (page 1)

Differentiation generalizes to functions of more than one independent variable: **multivariate functions**. Examples are terrain height $h(x,y)$, temperature in a room $T(x,y,z,t)$, and gas pressure as a function of volume and temperature.

A contour plot shows curves $f(x,y)=\text{constant}$. The slope at a point $A$ depends on direction. First consider the coordinate directions. The nested contours and the red point $A$ below are qualitative, with no numerical levels specified.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.1,0)--(5.4,0) node[right] {$x$};
  \draw[->] (0,-0.1)--(0,3.8) node[above] {$y$};
  \draw[thick] (0.65,1.2)
    .. controls (0.5,1.9) and (0.65,2.9) .. (1.25,3.1)
    .. controls (1.9,3.25) and (2.45,3.45) .. (2.95,3.1)
    .. controls (3.5,2.7) and (4.6,2.45) .. (4.65,1.8)
    .. controls (4.75,1.1) and (3.45,0.6) .. (2.6,0.65)
    .. controls (1.8,0.6) and (1.2,0.85) .. (0.65,1.2)--cycle;
  \draw (1.05,1.5)
    .. controls (0.95,2.05) and (1.15,2.65) .. (1.65,2.7)
    .. controls (2.25,2.78) and (2.75,2.8) .. (3.15,2.52)
    .. controls (3.6,2.25) and (4.08,1.95) .. (3.87,1.55)
    .. controls (3.4,1.05) and (2.8,0.8) .. (2.25,1.1)
    .. controls (1.8,1.4) and (1.35,1.25) .. (1.05,1.5)--cycle;
  \draw (1.55,1.9)
    .. controls (1.42,2.25) and (1.85,2.4) .. (2.3,2.4)
    .. controls (2.72,2.4) and (3.35,2.55) .. (3.2,2.15)
    .. controls (3,1.75) and (1.8,1.55) .. (1.55,1.9)--cycle;
  \draw (2.08,2.05)
    .. controls (2.3,2.22) and (2.65,2.25) .. (2.7,2.15)
    .. controls (2.65,1.99) and (2.15,1.92) .. (2.08,2.05)--cycle;
  \fill[red] (4.03,1.25) circle (1.5pt) node[above right] {$A$};
  \node at (6.25,3.45) {$f(x,y)$};
  \node[right] (level) at (5.65,2.6) {$f(x,y)=\mathrm{constant}$};
  \draw[->] (level.west)--(4.55,2.2);
\end{tikzpicture}
\end{document}
```

## 3.2 Partial derivatives (pages 1–3)

A **partial derivative** differentiates with respect to one variable while holding the others fixed. For $f(x,y)$,
$$\left.\frac{\partial f}{\partial x}\right|_y
=\lim_{\delta x\to0}\frac{f(x+\delta x,y)-f(x,y)}{\delta x},$$
when the limit exists. This is the slope in the positive $x$-direction, with $y$ held fixed. Similarly,
$$\left.\frac{\partial f}{\partial y}\right|_x
=\lim_{\delta y\to0}\frac{f(x,y+\delta y)-f(x,y)}{\delta y}.$$

### Example and higher derivatives (page 2)

Let
$$f(x,y)=x^2+y^3+e^{xy^2}.$$
Then
$$\left.\frac{\partial f}{\partial x}\right|_y=2x+y^2e^{xy^2},\qquad
\left.\frac{\partial f}{\partial y}\right|_x=3y^2+2xye^{xy^2},$$
and
$$\left.\frac{\partial^2f}{\partial x^2}\right|_y=2+y^4e^{xy^2}.$$
The mixed derivatives in this example agree:
$$\begin{aligned}
\left.\frac{\partial}{\partial x}\left(\left.\frac{\partial f}{\partial y}\right|_x\right)\right|_y
&=2ye^{xy^2}+2xy^3e^{xy^2},\\
\left.\frac{\partial}{\partial y}\left(\left.\frac{\partial f}{\partial x}\right|_y\right)\right|_x
&=2ye^{xy^2}+2xy^3e^{xy^2}.
\end{aligned}$$

### Notation and Schwarz's theorem (pages 2–3)

Usually the fixed-variable bars are omitted: $\partial/\partial x$ implies that **all other independent variables are held fixed**. Write
$$f_x=\frac{\partial f}{\partial x},\qquad
f_{xy}=(f_x)_y=\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
=\frac{\partial^2f}{\partial y\,\partial x}.$$
Following `topic1.pdf`, page 22, the subscript $xy$ means **first $x$, then $y$**. In the fraction notation, the differentiation on the right acts first.

**Schwarz's theorem (statement only).** If the second partial derivatives are continuous in a neighbourhood, then
$$\frac{\partial^2f}{\partial x\,\partial y}
=\frac{\partial^2f}{\partial y\,\partial x}.$$
No proof is supplied.

For $f(x,y,z)$, $\partial f/\partial x$ means $\left.\partial f/\partial x\right|_{y,z}$. Holding only $y$ fixed need not specify the same derivative if $z$ is allowed to vary with $x$.

## 3.3 Multivariate chain rule (pages 3–4)

For a path $x(t),y(t)$ and a function $f(x,y)$, the question is how to find $df/dt$ along the path.

### Small changes and the differential (pages 3–4)

The idea is to add the change caused by $x$ to the change caused by $y$. Following `topic1.pdf`, page 23, split the actual change into two coordinate steps:
$$\begin{aligned}
\delta f
&=f(x+\delta x,y+\delta y)-f(x,y)\\
&=[f(x+\delta x,y+\delta y)-f(x+\delta x,y)]
+[f(x+\delta x,y)-f(x,y)].
\end{aligned}$$
For this Taylor derivation, assume the second partial derivatives are continuous nearby. Applying first-order Taylor expansions to the two steps gives
$$\delta f=f_x\,\delta x+f_y\,\delta y
+O\!\left((|\delta x|+|\delta y|)^2\right).$$
The second derivatives are bounded in a small neighbourhood, so the omitted terms are of second order in the small changes.

The **differential** names the first-order part:
$$df=f_x\,dx+f_y\,dy.$$
In words, change in $f$ ≈ slope in the $x$-direction × change in $x$ + slope in the $y$-direction × change in $y$. The symbol $df$ is not the ordinary limit of $\delta f$; that limit would simply be zero.

### Chain rule along a path (page 4)

If $x=x(t)$ and $y=y(t)$, then
$$\delta x=x'(t)\delta t+o(\delta t),\qquad
\delta y=y'(t)\delta t+o(\delta t).$$
Substitute into the small-change formula, divide by $\delta t$ and let $\delta t\to0$. The first-order terms give
$$\frac{df}{dt}=f_x\frac{dx}{dt}+f_y\frac{dy}{dt},$$
and the remaining terms tend to zero after division. The Taylor assumptions above are enough for this derivation; continuous first partial derivatives already suffice for the chain rule itself.

If the path is parametrized by $x$, with $y=y(x)$, then
$$\frac d{dx}f(x,y(x))=f_x+f_y\frac{dy}{dx}.$$
There are two contributions because $f$ changes both directly with $x$ and through $y(x)$.

### Integral form (page 4)

Along a specified path from $t_0$ to $t_1$,
$$\Delta f=\int df=\int\left(\frac{\partial f}{\partial x}\,dx+
\frac{\partial f}{\partial y}\,dy\right),$$
where $\Delta f$ is the change in $f$ between the endpoints. In parametrized form,
$$\begin{aligned}
\Delta f
&=f(x(t_1),y(t_1))-f(x(t_0),y(t_0))\\
&=\int_{t_0}^{t_1}\left(
\frac{\partial f}{\partial x}\frac{dx}{dt}
+\frac{\partial f}{\partial y}\frac{dy}{dt}
\right)dt.
\end{aligned}$$
The integral is taken along the given path, with sufficient regularity to apply the one-variable fundamental theorem (for example, $f$ and the path continuously differentiable).

Related: [[Partial Derivatives and the Multivariate Chain Rule]], [[Differentiation Rules]], [[Taylor Series and Taylor's Theorem]], [[Limits, Big O and Little o - A First-Year Guide]], [[Riemann Integration and the Fundamental Theorem of Calculus]].


## 3.4 Applications of the multivariate chain rule (pages 5–9)

### Change of variables: Cartesian and polar coordinates (page 5)

It can help to rewrite a differential equation in another coordinate system before solving it. In polar coordinates,
$$x=r\cos\theta,\qquad y=r\sin\theta,$$
and $f(x,y)$ is viewed as $f(x(r,\theta),y(r,\theta))$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.15,0)--(4,0) node[right] {$x$};
  \draw[->] (0,-0.15)--(0,2.8) node[above] {$y$};
  \draw[red,thick] (0,0)--(2.5,1.4) node[midway,above] {$r$};
  \fill (2.5,1.4) circle (1.2pt) node[above right] {$(x,y)$};
  \draw (0.6,0) arc (0:29.25:0.6);
  \node at (0.9,0.23) {$\theta$};
\end{tikzpicture}
\end{document}
```

The chain rule, with the fixed variables shown, gives
$$\begin{aligned}
\left.\frac{\partial f}{\partial r}\right|_\theta
&=\left.\frac{\partial f}{\partial x}\right|_y
\left.\frac{\partial x}{\partial r}\right|_\theta
+\left.\frac{\partial f}{\partial y}\right|_x
\left.\frac{\partial y}{\partial r}\right|_\theta\\
&=f_x\cos\theta+f_y\sin\theta,\\
\left.\frac{\partial f}{\partial\theta}\right|_r
&=\left.\frac{\partial f}{\partial x}\right|_y
\left.\frac{\partial x}{\partial\theta}\right|_r
+\left.\frac{\partial f}{\partial y}\right|_x
\left.\frac{\partial y}{\partial\theta}\right|_r\\
&=-r\sin\theta\,f_x+r\cos\theta\,f_y.
\end{aligned}$$

### Implicit differentiation (pages 6–8)

For a function of three independent variables,
$$df=\left.\frac{\partial f}{\partial x}\right|_{y,z}dx
+\left.\frac{\partial f}{\partial y}\right|_{x,z}dy
+\left.\frac{\partial f}{\partial z}\right|_{x,y}dz.$$
A level equation $f(x,y,z)=c$ describes a surface in the depicted setting. Locally, where the corresponding implicit function is well-defined and differentiable, one variable can be treated as a function of the other two. An explicit formula may not be available. The spherical outline below is a qualitative level-surface sketch, without a specified equation or numerical radius.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (0,0)--(0,3.2) node[above] {$z$};
  \draw[->] (0,0)--(3,-0.9) node[right] {$x$};
  \draw[->] (0,0)--(2.9,1.4) node[right] {$y$};
  \draw[blue,thick] (1.5,1.4) ellipse (0.85 and 1);
  \draw[blue] (0.72,1.78) .. controls (1.1,1.5) and (1.9,1.5) .. (2.28,1.78);
  \draw[blue] (0.65,1.4) .. controls (1.05,1.05) and (1.95,1.05) .. (2.35,1.4);
  \draw[blue] (0.8,0.85) .. controls (1.2,0.65) and (1.9,0.65) .. (2.2,0.85);
  \draw[blue] (1.18,2.33) .. controls (0.92,1.7) and (0.92,1) .. (1.18,0.47);
  \draw[blue] (1.82,2.33) .. controls (2.08,1.7) and (2.08,1) .. (1.82,0.47);
  \node[blue,right] (level) at (3.3,2.7) {$f(x,y,z)=\mathrm{constant}$};
  \draw[blue,->] (level.west)--(2.05,2.13);
\end{tikzpicture}
\end{document}
```

**Example (pages 6–7).** The equation
$$xy+y^2z+z^5=1\tag{*}$$
is treated implicitly, with $z=z(x,y)$. Differentiate with respect to $x$ while holding $y$ fixed:
$$y+y^2\left.\frac{\partial z}{\partial x}\right|_y
+5z^4\left.\frac{\partial z}{\partial x}\right|_y=0.$$
Hence
$$\left.\frac{\partial z}{\partial x}\right|_y=-\frac{y}{y^2+5z^4}.$$
This derivative on the constraint differs from taking the derivative of the ambient expression while holding both $y$ and $z$ fixed.

Along the level surface, $df=0$:
$$0=\left.\frac{\partial f}{\partial x}\right|_{y,z}dx
+\left.\frac{\partial f}{\partial y}\right|_{x,z}dy
+\left.\frac{\partial f}{\partial z}\right|_{x,y}dz.$$
The coordinates cannot all vary independently while staying on the surface. Page 8 contrasts a curve on $f=c$ with an ambient change holding both $y,z$ fixed; the red, blue and green curves are schematic.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (0,0)--(0,3.2) node[above] {$z$};
  \draw[->] (0,0)--(3.5,-1.2) node[right] {$x$};
  \draw[->] (0,0)--(3.5,1.55) node[above right] {$y$};
  \draw[red,thick] (0.6,1.4)
    .. controls (1.5,2.35) and (2.5,2.35) .. (3.2,1.7)
    .. controls (2.65,1.5) and (2.2,0.9) .. (2.2,0.3)
    .. controls (1.7,1.35) and (1,1.5) .. (0.6,1.4);
  \draw[blue,thick] (1.05,1.58)
    .. controls (1.5,1.62) and (1.85,1.45) .. (2,1.18);
  \draw[green!60!black,thick] (1.05,1.58)--(2,1.18);
  \draw[blue,dotted] (1.05,1.58)--(1.05,0.4)--(2,0)--(2,1.18);
  \node[red] (level) at (2.2,3) {$f=c$};
  \draw[red,->] (level.south) .. controls (1.9,2.7) and (1.9,2.4) .. (1.8,2.1);
  \node[blue,right] (on) at (4,1.25) {on surface: $\left.\frac{\partial f}{\partial x}\right|_y=0$};
  \draw[blue,->] (on.west) .. controls (3.5,1.9) and (2.7,1.8) .. (2.15,1.55);
  \node[green!60!black,right] (off) at (3.8,-0.35) {ambient: $\left.\frac{\partial f}{\partial x}\right|_{y,z}\ne0$};
  \draw[green!60!black,->] (3.05,-0.3)
    .. controls (2.15,0.05) and (1.65,0.6) .. (1.65,1.2);
\end{tikzpicture}
\end{document}
```

With $y$ fixed and $z=z(x,y)$, the chain rule reads
$$\begin{aligned}
0&=\left.\frac{\partial}{\partial x}f(x,y,z(x,y))\right|_y\\
&=\left.\frac{\partial f}{\partial x}\right|_{y,z}
  \left.\frac{\partial x}{\partial x}\right|_y
 +\left.\frac{\partial f}{\partial y}\right|_{x,z}
  \left.\frac{\partial y}{\partial x}\right|_y
 +\left.\frac{\partial f}{\partial z}\right|_{x,y}
  \left.\frac{\partial z}{\partial x}\right|_y\\
&=\left.\frac{\partial f}{\partial x}\right|_{y,z}
 +\left.\frac{\partial f}{\partial z}\right|_{x,y}
  \left.\frac{\partial z}{\partial x}\right|_y,
\end{aligned}$$
since the two coordinate derivatives in the middle line are $1$ and $0$. Thus, where the denominator is non-zero,
$$\left.\frac{\partial z}{\partial x}\right|_y
=-\frac{\left.\dfrac{\partial f}{\partial x}\right|_{y,z}}
{\left.\dfrac{\partial f}{\partial z}\right|_{x,y}}.$$
Similarly, the corresponding formulas for $\left.\partial x/\partial y\right|_z$ and $\left.\partial y/\partial z\right|_x$ give the **cyclic rule**, wherever all three ratios are defined:
$$\left.\frac{\partial x}{\partial y}\right|_z
\left.\frac{\partial y}{\partial z}\right|_x
\left.\frac{\partial z}{\partial x}\right|_y=-1.$$

### Reciprocal rule (page 9)

When the same variable is held fixed, and the derivatives exist and are non-zero,
$$\left.\frac{\partial z}{\partial x}\right|_y
=\frac{1}{\left.\dfrac{\partial x}{\partial z}\right|_y}.$$
The indicated proof first obtains
$$\left.\frac{\partial x}{\partial z}\right|_y
=-\frac{\left.\dfrac{\partial f}{\partial z}\right|_{x,y}}
{\left.\dfrac{\partial f}{\partial x}\right|_{y,z}},$$
which is reciprocal to the preceding ratio.

The fixed-variable condition matters. For $(r,\theta)\mapsto(x,y)$,
$$\left.\frac{\partial r}{\partial x}\right|_y
=\frac{1}{\left.\dfrac{\partial x}{\partial r}\right|_y},$$
but this need not equal $1/(\left.\partial x/\partial r\right|_\theta)$, since a different variable is being held fixed. See [[Implicit Differentiation]].

## 3.5 Differentiating an integral with respect to a parameter (pages 9–11)

For a family $f(x;c)$ depending on a parameter $c$, define
$$I(c)=\int_{a(c)}^{b(c)}f(x;c)\,dx.$$
The source states [[Differentiation Under the Integral Sign|Leibniz's integral rule]]:
$$\frac{dI}{dc}
=\int_{a(c)}^{b(c)}\frac{\partial f}{\partial c}(x;c)\,dx
+f(b(c);c)b'(c)-f(a(c);c)a'(c).$$
A sufficient regularity setting is that $a,b$ are continuously differentiable and $f,f_c$ are continuous on a neighbourhood of the relevant integration intervals.

**Source proof calculation (page 10).** Write $h=\delta c$. The difference quotient is
$$\frac{1}{h}\left[
\int_{a(c+h)}^{b(c+h)}f(x;c+h)\,dx
-\int_{a(c)}^{b(c)}f(x;c)\,dx\right].$$
Split its first integral at the old endpoints, giving three contributions:
$$\begin{aligned}
A_h&=\frac1h\int_{a(c)}^{b(c)}[f(x;c+h)-f(x;c)]\,dx,\\
B_h&=\frac1h\int_{b(c)}^{b(c+h)}f(x;c+h)\,dx,\\
C_h&=-\frac1h\int_{a(c)}^{a(c+h)}f(x;c+h)\,dx.
\end{aligned}$$
The source writes
$$\lim_{h\to0}A_h
=\int_{a(c)}^{b(c)}\frac{\partial f}{\partial c}(x;c)\,dx.$$
For the upper-endpoint term, the mean value theorem gives an intermediate $\xi_h$ between $b(c)$ and $b(c+h)$ with
$$B_h=\frac{b(c+h)-b(c)}h\,f(\xi_h;c+h)
\longrightarrow b'(c)f(b(c);c).$$
The source says to use the same argument for the lower-endpoint term, yielding $-a'(c)f(a(c);c)$.

**Why the first term has this limit.** On the fixed finite interval, continuous $f_c$ makes the parameter difference quotient approach $f_c$ uniformly: its error can be made small by the same amount across the interval. The integral error is at most the interval length times that amount, so it tends to zero too. Together with the two endpoint terms, this proves the formula in the smooth setting used here. If an endpoint does not move, its term is zero.

### Example with a moving endpoint (page 11)

Let
$$I(\lambda)=\int_0^\lambda e^{-\lambda x^2}\,dx.$$
Leibniz's rule gives
$$\begin{aligned}
I'(\lambda)
&=\int_0^\lambda -x^2e^{-\lambda x^2}\,dx
+e^{-\lambda^3}\frac{d\lambda}{d\lambda}\\
&=-\int_0^\lambda x^2e^{-\lambda x^2}\,dx+e^{-\lambda^3}.
\end{aligned}$$
The endpoint contribution evaluates the integrand at $x=\lambda$ and uses $d\lambda/d\lambda=1$.

### Factorial integrals (page 11)

To evaluate
$$J_n=\int_0^\infty x^n e^{-x}\,dx,\qquad n\in\mathbb Z_{\ge0},$$
introduce the parameter integral
$$I(\lambda)=\int_0^\infty e^{-\lambda x}\,dx
=\frac1\lambda,\qquad\lambda>0.$$
The source differentiates $n$ times:
$$\frac{d^nI}{d\lambda^n}
=\int_0^\infty(-x)^n e^{-\lambda x}\,dx,$$
while differentiation of the explicit expression gives
$$\frac{d^n}{d\lambda^n}\frac1\lambda
=(-1)^n\frac{n!}{\lambda^{n+1}}.$$
Equating them and setting $\lambda=1$ yields
$$(-1)^nJ_n=(-1)^nn!,\qquad J_n=n!.$$

**Scope of this example.** For $\lambda>0$, the exponential decay controls every polynomial factor $x^n$ arising from differentiation, so the differentiated integrals converge and the interchange is valid locally in $\lambda$. This is an additional condition for the infinite interval; it does not follow from the finite-interval formula alone. The detailed convergence proof is beyond this course-level calculation.

## Related notes

[[Partial Derivatives and the Multivariate Chain Rule]] summarizes the small-change idea and formulas. [[Implicit Differentiation]] and [[Differentiation Under the Integral Sign]] collect their applications.
