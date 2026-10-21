---
title: Differential Equations - Chapter 3 Partial Differentiation
material_type: handwritten lecture notes with labelled mathematical corrections and supplements
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

### Controlled increment derivation — corrected proof (page 3)

The following supplementary proof keeps the source's split into coordinate increments and supplies its missing regularity and remainder control. Assume $f$ has continuous first partial derivatives in an open neighbourhood of $p=(x,y)$; mixed second derivatives are not needed.

For small $h,k$, write
$$\begin{aligned}
f(x+h,y+k)-f(x,y)
&=[f(x+h,y+k)-f(x+h,y)]\\
&\quad+[f(x+h,y)-f(x,y)].
\end{aligned}$$
The one-variable mean value theorem on each coordinate segment gives numbers $\theta,\eta\in(0,1)$ such that
$$f(x+h,y+k)-f(x,y)
=k f_y(x+h,y+\theta k)+h f_x(x+\eta h,y).$$
If an increment is zero, its term is zero and its intermediate point can be chosen arbitrarily on the degenerate segment. Subtract $h f_x(p)+k f_y(p)$ and let $\rho=\sqrt{h^2+k^2}$. Continuity of $f_x,f_y$ at $p$ implies
$$\begin{aligned}
|R(h,k)|
&\le |k|\,|f_y(x+h,y+\theta k)-f_y(p)|\\
&\quad+|h|\,|f_x(x+\eta h,y)-f_x(p)|\\
&=o(\rho).
\end{aligned}$$
Indeed, both derivative differences tend to zero regardless of the intermediate points, and $|h|+|k|\le\sqrt2\rho$. Hence
$$f(x+h,y+k)=f(x,y)+f_x(x,y)h+f_y(x,y)k+o(\rho).$$
This proves total differentiability under the stated $C^1$ hypothesis. The previous source expansion used a mixed derivative and an uncontrolled remainder at a moving base point; the estimate above resolves both issues.

### Differential and chain rule — corrected definition and proof (page 4)

A function is **totally differentiable** at $p$ if there is a linear map $df_p$ with
$$f(p+v)-f(p)=df_p(v)+o(\|v\|).$$
Its differential is that linear map:
$$df_p(h,k)=f_x(p)h+f_y(p)k,$$
or $df=f_x\,dx+f_y\,dy$. Here $dx,dy$ are the coordinate linear maps on an increment: $dx(h,k)=h$ and $dy(h,k)=k$. The source expression $df=\lim_{h,k\to0}(f(x+h,y+k)-f(x,y))$ is not a definition of the differential: for continuous $f$ that limit is just zero.

**Chain rule.** Let $p(t)=(x(t),y(t))$ be differentiable and suppose $f$ is totally differentiable at $p(t)$. For an increment $s$,
$$v(s)=p(t+s)-p(t)=s\,p'(t)+o(s)=O(s).$$
Write the differentiability remainder as $r(v)$, where $r(v)=o(\|v\|)$ and $r(0)=0$. Then $r(v(s))=o(s)$: for each $\varepsilon>0$, sufficiently small $v$ satisfies $|r(v)|\le\varepsilon\|v\|$, while $\|v(s)\|\le C|s|$ for some fixed $C$. Linearity gives
$$\begin{aligned}
f(p(t+s))-f(p(t))
&=df_{p(t)}(v(s))+r(v(s))\\
&=s\,df_{p(t)}(p'(t))+o(s).
\end{aligned}$$
Dividing by $s$ and taking the limit proves
$$\frac d{dt}f(x(t),y(t))
=f_x(x(t),y(t))x'(t)+f_y(x(t),y(t))y'(t).$$
The theorem needs total differentiability at the point; continuous first partial derivatives nearby are a sufficient condition, proved above. The existence of partial derivatives alone is insufficient; see the counterexample in [[Partial Derivatives and the Multivariate Chain Rule]].

If the path is parametrized by $x$, with $y=y(x)$, then
$$\frac d{dx}f(x,y(x))=f_x+f_y\frac{dy}{dx}.$$

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

## Supplementary learning route

[[Partial Derivatives and the Multivariate Chain Rule#Partial derivatives versus differentiability — supplementary explanation]] defines total differentiability, shows why partial derivatives alone are insufficient, and derives the chain rule from a controlled first-order remainder. It complements the corrected proofs above; the added regularity assumptions and proofs are not attributed to the original PDF.
