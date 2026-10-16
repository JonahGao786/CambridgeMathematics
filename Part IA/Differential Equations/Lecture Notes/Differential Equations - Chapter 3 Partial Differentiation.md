---
title: Differential Equations - Chapter 3 Partial Differentiation
material_type: handwritten lecture notes
course: Part IA Differential Equations
date: null
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: 4
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
f_{xy}=\frac{\partial^2f}{\partial x\,\partial y}
=\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right).$$
Here the displayed source convention reads $xy$ as “differentiate in $y$ first, then $x$”; the rightmost differentiation is first. The convention matters when reading the derivation below.

**Schwarz's theorem (statement only).** If the second partial derivatives are continuous in a neighbourhood, then
$$\frac{\partial^2f}{\partial x\,\partial y}
=\frac{\partial^2f}{\partial y\,\partial x}.$$
No proof is supplied.

For $f(x,y,z)$, $\partial f/\partial x$ means $\left.\partial f/\partial x\right|_{y,z}$. Holding only $y$ fixed need not specify the same derivative if $z$ is allowed to vary with $x$.

## 3.3 Multivariate chain rule (pages 3–4)

For a path $x(t),y(t)$ and a function $f(x,y)$, the question is how to find $df/dt$ along the path.

### Source derivation (page 3)

Under $(x,y)\mapsto(x+\delta x,y+\delta y)$, split the increment as
$$\begin{aligned}
\delta f
&=f(x+\delta x,y+\delta y)-f(x,y)\\
&=\bigl[f(x+\delta x,y+\delta y)-f(x+\delta x,y)\bigr]
+\bigl[f(x+\delta x,y)-f(x,y)\bigr].
\end{aligned}$$
Using one-variable Taylor/differentiability expansions, the source writes
$$f(x+\delta x,y)-f(x,y)=f_x(x,y)\,\delta x+o(\delta x),$$
$$f(x+\delta x,y+\delta y)-f(x+\delta x,y)
=f_y(x+\delta x,y)\,\delta y+o(\delta y),$$
and expands
$$f_y(x+\delta x,y)=f_y(x,y)+f_{xy}(x,y)\,\delta x+o(\delta x).$$
Consequently,
$$\begin{aligned}
\delta f={}&[f_y(x,y)+f_{xy}(x,y)\,\delta x+o(\delta x)]\delta y
+o(\delta y)+f_x(x,y)\delta x+o(\delta x)\\
={}&f_y(x,y)\delta y+f_x(x,y)\delta x
+f_{xy}(x,y)\delta x\delta y
+\delta y\,o(\delta x)+o(\delta y)+o(\delta x).
\end{aligned}$$

> [!todo] Incomplete two-variable derivation — page 3
> The expansion uses a mixed derivative and treats a remainder from a base point depending on $\delta x$ as though it were controlled uniformly as both increments tend to zero. The necessary regularity and remainder control are not established in the source. The displayed calculation is retained, with its mixed derivative written consistently with the source's rightmost-first convention.

### Differential and chain rule (page 4)

> [!warning] Incorrect definition of the differential — page 4
> The source writes $df=\lim_{\delta x,\delta y\to0}\delta f$. For continuous $f$ that unscaled limit is zero, so it does not define the differential. The first-order differential formula stated below is retained separately from that incorrect definition.

The source states the **differential form** of the chain rule:
$$df=\frac{\partial f}{\partial x}\,dx+\frac{\partial f}{\partial y}\,dy.$$
This is the linear first-order change when $f$ is differentiable. For a differentiable path and $f$ differentiable along it,
$$\begin{aligned}
\frac d{dt}f(x(t),y(t))
&=\lim_{\delta t\to0}\left(
\frac{\partial f}{\partial x}\frac{\delta x}{\delta t}
+\frac{\partial f}{\partial y}\frac{\delta y}{\delta t}\right)\\
&=\frac{\partial f}{\partial x}\frac{dx}{dt}
+\frac{\partial f}{\partial y}\frac{dy}{dt}.
\end{aligned}$$
The partial derivatives are evaluated on the path. The displayed limit describes the first-order differential expression; the source does not supply a rigorous passage from the increment expansion to this limit under general hypotheses.

If the path is parametrized by $x$, with $y=y(x)$, then
$$\begin{aligned}
\frac d{dx}f(x,y(x))
&=\frac{\partial f}{\partial x}\frac{dx}{dx}
+\frac{\partial f}{\partial y}\frac{dy}{dx}\\
&=f_x+f_y\frac{dy}{dx}.
\end{aligned}$$

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
