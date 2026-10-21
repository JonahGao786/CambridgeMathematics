---
title: L'Hôpital's Rule
material_type: course-level definitions, formulas and explanations
course: Part IA Differential Equations
source_file: Ch.1 Differentiation.pdf
drive_file_id: 1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr
source_url: https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view
source_pages: [12, 13]
reference_handout: topic1.pdf
reference_handout_pages: "12–13"
---

# L'Hôpital's Rule

The form $0/0$ does not determine a limit. The course handout explains L'Hôpital's rule through Taylor expansions.

## Course version

Suppose $f,g$ are differentiable near $x_0$, their first derivatives are continuous at $x_0$, and
$$f(x_0)=g(x_0)=0,\qquad g'(x_0)\ne0.$$
Then
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}
=\frac{f'(x_0)}{g'(x_0)}
=\lim_{x\to x_0}\frac{f'(x)}{g'(x)}.$$

**Why it works.** Put $h=x-x_0$. First-order Taylor expansions give
$$\frac{f(x_0+h)}{g(x_0+h)}
=\frac{hf'(x_0)+o(h)}{hg'(x_0)+o(h)}
=\frac{f'(x_0)+o(h)/h}{g'(x_0)+o(h)/h}.$$
Since $o(h)/h\to0$ and $g'(x_0)\ne0$, the result follows. This is the special case proved in `topic1.pdf`, pages 12–13; more general versions are outside this proof.

## When several derivatives vanish

Compare the first non-zero Taylor terms. If derivatives of $f,g$ through order $n$ exist near $x_0$, the derivatives of orders $0,\ldots,n-1$ vanish at $x_0$, and $g^{(n)}(x_0)\ne0$, then
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}
=\frac{f^{(n)}(x_0)}{g^{(n)}(x_0)}.$$
Both Taylor expansions contain the same factor $(x-x_0)^n/n!$, which cancels. Vanishing derivatives alone are not a reason to differentiate indefinitely: the remaining denominator and required derivatives still need checking.

For
$$f(x)=3\sin x-\sin(3x),\qquad g(x)=2x-\sin(2x),$$
the functions and their first two derivatives vanish at $0$, while $f^{(3)}(0)=24$ and $g^{(3)}(0)=8$. Therefore
$$\lim_{x\to0}\frac{3\sin x-\sin(3x)}{2x-\sin(2x)}=\frac{24}{8}=3.$$

See [[Differential Equations - Chapter 1 Introduction and Basic Calculus]], section 1.4, and [[Taylor Series and Taylor's Theorem]].
