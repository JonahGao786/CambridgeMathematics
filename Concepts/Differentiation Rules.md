---
title: Differentiation Rules
material_type: source-backed theorem statements and examples
course: Part IA Differential Equations
source_file: Ch.1 Differentiation.pdf
drive_file_id: 1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr
source_url: https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view
source_pages: [8, 9]
---

# Differentiation Rules

For $f(x)=F(g(x))$, where $g$ is differentiable at $x$ and $F$ is differentiable at $g(x)$, the **chain rule** is
$$f'(x)=F'(g(x))g'(x).$$
For example,
$$\frac d{dx}\sin(x^2-x+2)=\cos(x^2-x+2)(2x-1).$$

For differentiable $u,v$, the **product rule** and **quotient rule** are
$$(uv)'=u'v+uv',\qquad
\left(\frac uv\right)'=\frac{vu'-uv'}{v^2}\quad(v\ne0).$$
The quotient rule follows by applying the product rule to $u(1/v)$.

If $u,v$ are $n$ times differentiable, **Leibniz's rule** gives
$$(uv)^{(n)}=\sum_{r=0}^{n}\binom nr u^{(n-r)}v^{(r)}.$$
The first coefficient rows are $1,1$; $1,2,1$; and $1,3,3,1$, as in Pascal's triangle.

Source: [[Differential Equations - Chapter 1 Introduction and Basic Calculus]], expanded differentiation PDF, pages 8–9. These are statements and examples; proofs of these rules are not supplied there. A handwritten product-rule proof is separately transcribed in [[Differential Equations - Examples Sheet 1 Handwritten Proofs]]. Repeated derivatives enter [[Taylor Series and Taylor's Theorem]].
