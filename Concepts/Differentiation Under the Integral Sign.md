---
title: Differentiation Under the Integral Sign
material_type: concept note
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
reference_handout: topic1.pdf
reference_handout_pages: "28–29"
source_pages: [9, 10, 11]
---

# Differentiation Under the Integral Sign

For
$$I(c)=\int_{a(c)}^{b(c)}f(x;c)\,dx,$$
**Leibniz's integral rule** is
$$I'(c)=\int_{a(c)}^{b(c)}f_c(x;c)\,dx
+f(b(c);c)b'(c)-f(a(c);c)a'(c).$$
A sufficient regularity setting is continuously differentiable endpoints and continuity of $f,f_c$ on a neighbourhood of the integration intervals.

Split the difference quotient into the change of the integrand over the old fixed interval, the upper-endpoint interval, and the negative lower-endpoint interval. The mean value theorem gives the two endpoint terms. For continuous $f_c$, the difference-quotient error becomes small across the fixed interval, so its integral error tends to zero. Thus the formula has three contributions: the integrand changes, the upper endpoint moves, and the lower endpoint moves. The short derivation is in [[Differential Equations - Chapter 3 Partial Differentiation]].

## Moving-endpoint example

For
$$I(\lambda)=\int_0^\lambda e^{-\lambda x^2}\,dx,$$
page 11 calculates
$$I'(\lambda)
=-\int_0^\lambda x^2e^{-\lambda x^2}\,dx+e^{-\lambda^3}.$$
The last term is the upper-endpoint contribution.

## Factorial integrals

For $\lambda>0$,
$$I(\lambda)=\int_0^\infty e^{-\lambda x}\,dx=\frac1\lambda.$$
Differentiate $n$ times, for $n\in\mathbb Z_{\ge0}$, to obtain
$$\int_0^\infty(-x)^ne^{-\lambda x}\,dx
=(-1)^n\frac{n!}{\lambda^{n+1}}.$$
Setting $\lambda=1$ gives
$$\int_0^\infty x^ne^{-x}\,dx=n!.$$
For $\lambda>0$, exponential decay controls the polynomial factors introduced by differentiation and justifies this calculation. The infinite-interval justification needs more than the finite-interval rule; its detailed convergence proof is omitted here.

Related: [[Partial Derivatives and the Multivariate Chain Rule]], [[Riemann Integration and the Fundamental Theorem of Calculus]].
