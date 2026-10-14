---
title: Riemann Integration and the Fundamental Theorem of Calculus
material_type: source-backed definitions, theorem and proof with explicit proof scope
course: Part IA Differential Equations
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: [1, 2, 3, 4]
---

# Riemann Integration and the Fundamental Theorem of Calculus

With $\Delta x=(b-a)/N$ and $x_n=a+n\Delta x$, a uniform left-endpoint Riemann sum is
$$\sum_{n=0}^{N-1}f(x_n)\,\Delta x.$$
For a Riemann-integrable function, its limit is $\int_a^b f(x)\,dx$. More generally, the limit is independent of non-uniform interval widths and sample points when the largest interval width tends to zero.

For the positive continuous curve in the source, the integral mean value theorem gives the area of one strip as
$$A_n=\Delta x\,f(c_n),\qquad x_n<c_n<x_{n+1}.$$
The source then uses differentiability to write
$$A_n=\Delta x\,f(x_n)+O((\Delta x)^2).$$

> [!todo] Uniform error estimate — source pages 2–3
> The sum of these errors is $O(1/N)$ only if the $O$-constant is uniform across the partition. Pointwise differentiability alone does not establish this. The complete source calculation and its review note are retained in [[Differential Equations - Chapter 2 Integration]].

## Fundamental theorem of calculus

For continuous $f$, define
$$F(x)=\int_a^x f(t)\,dt.$$
At interior points,
$$F'(x)=f(x),\qquad F(a)=0.$$

**Source proof under stronger hypotheses:** differentiability of $f$ at $x$ yields the displayed mean-value/Taylor estimate
$$\int_x^{x+h}f(t)\,dt=f(x)h+O(h^2),$$
so
$$\frac{F(x+h)-F(x)}h=f(x)+O(h)\longrightarrow f(x).$$
This proof covers the stronger differentiable case. The source does not supply the general continuous-case proof.

The corollaries, using the [[Differentiation Rules|chain rule]], are
$$\frac{d}{dx}\int_x^b f(t)\,dt=-f(x),$$
$$\frac{d}{dx}\int_a^{g(x)}f(t)\,dt=f(g(x))g'(x)$$
for differentiable $g$ with values in the interval.

An indefinite integral $\int f(x)\,dx$ denotes an antiderivative with an arbitrary integration constant.

Source: [[Differential Equations - Chapter 2 Integration]], pages 1–4, including both area diagrams. Related: [[Limits, Big O and Little o - A First-Year Guide]] and [[Integration by Substitution and by Parts]].
