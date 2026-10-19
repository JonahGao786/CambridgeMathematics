---
title: Differentiation Under the Integral Sign
material_type: source-backed theorem and proof-scope note
course: Part IA Differential Equations
source_file: Ch.3 Partial Differentiation.pdf
drive_file_id: 1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E
source_url: https://drive.google.com/file/d/1phlBx3t9Z1WBrEaiYl2z-Ly9wsGhzA4E/view
source_pages: [9, 10]
---

# Differentiation Under the Integral Sign

For
$$I(c)=\int_{a(c)}^{b(c)}f(x;c)\,dx,$$
**Leibniz's integral rule** is
$$I'(c)=\int_{a(c)}^{b(c)}f_c(x;c)\,dx
+f(b(c);c)b'(c)-f(a(c);c)a'(c).$$
A sufficient regularity setting is continuously differentiable endpoints and continuity of $f,f_c$ on a neighbourhood of the integration intervals.

The source splits the difference quotient into the change of the integrand over the old fixed interval, the upper-endpoint interval, and the negative lower-endpoint interval. The mean value theorem gives the two endpoint terms. It moves the limit inside the fixed-interval integral without justification; this remains a localized TODO on page 10 of [[Differential Equations - Chapter 3 Partial Differentiation]], which retains the complete calculation. No missing interchange proof is supplied.

Related: [[Partial Derivatives and the Multivariate Chain Rule]], [[Riemann Integration and the Fundamental Theorem of Calculus]].
