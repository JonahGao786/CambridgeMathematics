---
title: Differentiation Under the Integral Sign
material_type: source-backed theorem, examples and proof-scope notes with supplementary corrected proofs
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: [9, 10, 11]
---

# Differentiation Under the Integral Sign

For
$$I(c)=\int_{a(c)}^{b(c)}f(x;c)\,dx,$$
**Leibniz's integral rule** is
$$I'(c)=\int_{a(c)}^{b(c)}f_c(x;c)\,dx
+f(b(c);c)b'(c)-f(a(c);c)a'(c).$$
A sufficient regularity setting is continuously differentiable endpoints and continuity of $f,f_c$ on a neighbourhood of the integration intervals.

The source splits the difference quotient into the change of the integrand over the old fixed interval, the upper-endpoint interval, and the negative lower-endpoint interval. The mean value theorem gives the two endpoint terms. The original calculation moves the limit inside the fixed-interval integral without justification. [[Differential Equations - Chapter 3 Partial Differentiation]] now supplies a labelled supplementary proof: continuity of $f_c$ on a compact rectangle gives uniform convergence of the parameter difference quotients, so their integral errors tend to zero.

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
The source differentiates $n$ times, for $n\in\mathbb Z_{\ge0}$, to obtain
$$\int_0^\infty(-x)^ne^{-\lambda x}\,dx
=(-1)^n\frac{n!}{\lambda^{n+1}}.$$
Setting $\lambda=1$ gives
$$\int_0^\infty x^ne^{-x}\,dx=n!.$$
The source omitted the improper-integral justification. The supplementary lecture proof now bounds each derivative locally in $\lambda$ by $x^m e^{-\lambda_0x/2}$ and then by an integrable exponential. Uniform convergence on finite intervals together with uniformly small tails justifies each differentiation, without assuming the factorial-integral result itself.

Related: [[Partial Derivatives and the Multivariate Chain Rule]], [[Riemann Integration and the Fundamental Theorem of Calculus]].
