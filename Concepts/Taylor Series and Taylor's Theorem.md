---
title: Taylor Series and Taylor's Theorem
material_type: source-backed definitions, theorem statements and example
course: Part IA Differential Equations
source_file: Ch.1 Differentiation.pdf
drive_file_id: 1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr
source_url: https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view
source_pages: [10, 11]
---

# Taylor Series and Taylor's Theorem

For $f$ infinitely differentiable near $x_0$, its **Taylor series** is
$$\sum_{k=0}^{\infty}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k.$$
The **Taylor polynomial** through degree $n$ is
$$P_n(x)=\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k.$$
It matches $f(x_0)$ and the first $n$ derivatives there. A Taylor series is not automatically equal to its function.

With $x=x_0+h$, Taylor's theorem gives
$$f(x_0+h)=P_n(x_0+h)+E_n(h).$$
If $f$ is $n$ times differentiable at $x_0$, with the lower derivatives defined nearby, the **Peano remainder** satisfies
$$E_n(h)=o(h^n)\qquad(h\to0).$$

If $f^{(n+1)}$ is continuous near the segment between $x_0$ and $x_0+h$, the **Lagrange remainder** is
$$E_n(h)=\frac{f^{(n+1)}(\xi_n)}{(n+1)!}h^{n+1}$$
for some $\xi_n$ on that segment. For fixed $n$, local boundedness of $f^{(n+1)}$ gives $E_n(h)=O(h^{n+1})$.

The latter error estimate is stronger: $|h|^{n+1/2}$ is $o(h^n)$ but not $O(h^{n+1})$. See [[Limits, Big O and Little o - A First-Year Guide]].

For a fixed $x$, the Taylor series converges to $f(x)$ if $E_n(x-x_0)\to0$ as $n\to\infty$. This is a different limit from $h\to0$ with $n$ fixed.

For $f(x)=e^x$, $x_0=0$ and $h>0$, the source gives
$$E_n(h)=\frac{h^{n+1}}{(n+1)!}e^{\xi_n},\qquad0\le\xi_n\le h,$$
so the fractional error satisfies
$$0\le\frac{E_n(h)}{e^h}\le\frac{h^{n+1}}{(n+1)!}.$$
This determines a sufficient polynomial degree for a target accuracy at the chosen $h$.

Source: [[Differential Equations - Chapter 1 Introduction and Basic Calculus]], expanded differentiation PDF, pages 10–11. The theorem is stated without proof. Its first-order form is used in the special-case proof of [[L'Hôpital's Rule]].
