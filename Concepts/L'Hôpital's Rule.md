---
title: L'Hôpital's Rule
material_type: source-backed theorem and example with supplementary full proof
course: Part IA Differential Equations
source_file: Ch.1 Differentiation.pdf
drive_file_id: 1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr
source_url: https://drive.google.com/file/d/1_FQhFkQDZpKx_jw272-80DE9XYHgs-yr/view
source_pages: [12, 13]
---

# L'Hôpital's Rule

The source states the **$0/0$ form**: let $f,g$ be differentiable on an open interval containing $x_0$, with $g'(x)\ne0$ for $x\ne x_0$ in that interval. Suppose
$$\lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=0.$$
Then, provided the right-hand limit exists,
$$\lim_{x\to x_0}\frac{f(x)}{g(x)}
=\lim_{x\to x_0}\frac{f'(x)}{g'(x)}.$$
Differentiability at $x_0$ implies $f(x_0)=g(x_0)=0$.

**Proof supplied for a stronger special case.** Assume also $g'(x_0)\ne0$ and continuity of the first derivatives near $x_0$. The first-order form of [[Taylor Series and Taylor's Theorem]] gives
$$f(x)=(x-x_0)f'(x_0)+o(x-x_0),\qquad
g(x)=(x-x_0)g'(x_0)+o(x-x_0).$$
After cancelling $x-x_0$, the quotient limit is $f'(x_0)/g'(x_0)$. Continuity of $f',g'$ makes this equal to $\lim_{x\to x_0}f'(x)/g'(x)$. The source supplies only that special-case proof. The supplementary argument below covers the theorem's stated hypotheses.

## Proof under the stated hypotheses — supplementary

For $x\ne x_0$ sufficiently near $x_0$, Rolle's theorem and $g'(t)\ne0$ for $t\ne x_0$ imply $g(x)\ne0$. Cauchy's mean value theorem on the segment between $x_0$ and $x$ then gives $\xi_x$ strictly between the endpoints with
$$\frac{f(x)}{g(x)}=\frac{f(x)-f(x_0)}{g(x)-g(x_0)}
=\frac{f'(\xi_x)}{g'(\xi_x)}.$$
Since $0<|\xi_x-x_0|<|x-x_0|$, the assumed limit of the derivative quotient yields the desired limit. This includes infinite limits and does not require continuity of $f',g'$ or $g'(x_0)\ne0$. The lecture note proves the needed Cauchy mean-value identity directly from Rolle's theorem.

## Repeated applications

The rule may be applied again when a derivative quotient is still $0/0$, provided its hypotheses hold at each stage. Vanishing derivatives at the point alone are insufficient to justify repetition.

The example is
$$f(x)=3\sin x-\sin(3x),\qquad g(x)=2x-\sin(2x).$$
The first two derivatives of each vanish at $0$, while
$$f'''(x)=-3\cos x+27\cos(3x),\qquad g'''(x)=8\cos(2x).$$
Three valid applications give
$$\lim_{x\to0}\frac{3\sin x-\sin(3x)}{2x-\sin(2x)}=\frac{24}{8}=3.$$

Source: [[Differential Equations - Chapter 1 Introduction and Basic Calculus]], expanded differentiation PDF, pages 12–13. The original special-case proof and supplementary proof under the stated hypotheses are both included there.
