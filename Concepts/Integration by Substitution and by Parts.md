---
title: Integration by Substitution and by Parts
material_type: source-backed techniques and worked examples
course: Part IA Differential Equations
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: [5, 6, 7]
---

# Integration by Substitution and by Parts

## Substitution

A function of a function may suggest substituting for its inner function. The source example uses $u=x-x^2$:
$$\int\frac{1-2x}{\sqrt{x-x^2}}\,dx
=\int\frac{du}{\sqrt u}=2\sqrt{x-x^2}+C,$$
on the real domain $0<x<1$.

The source lists:

| Integrand contains | Substitution |
| --- | --- |
| $\sqrt{1-x^2}$ | $x=\sin\theta$ |
| $1+x^2$ | $x=\tan\theta$ |
| $\sqrt{x^2-1}$ | $x=\cosh u$ |
| $\sqrt{x^2+1}$ | $x=\sinh u$ |
| $1-x^2$ | $x=\tanh u$ |

For the second worked example, $x-1=\sin\theta$ with $\theta\in[-\pi/2,\pi/2]$ ensures $\cos\theta\ge0$. Thus
$$\begin{aligned}
\int\sqrt{2x-x^2}\,dx
&=\int\cos^2\theta\,d\theta\\
&=\frac14\sin2\theta+\frac12\theta+C\\
&=\frac12\arcsin(x-1)+\frac12(x-1)\sqrt{1-(x-1)^2}+C.
\end{aligned}$$
The original real domain is $0\le x\le2$, with the antiderivative calculation on its interior.

## Integration by parts

Integrating the [[Differentiation Rules|product rule]] gives
$$\int uv'\,dx=uv-\int u'v\,dx.$$

For the supplied example, take $u=x$ and $v=-e^{-x}$:
$$\begin{aligned}
\int_0^\infty xe^{-x}\,dx
&=[-xe^{-x}]_0^\infty+\int_0^\infty e^{-x}\,dx\\
&=[-e^{-x}]_0^\infty=1.
\end{aligned}$$
The boundary terms use $xe^{-x}\to0$ and $e^{-x}\to0$ as $x\to\infty$.

Source: [[Differential Equations - Chapter 2 Integration]], pages 5–7, which retains all substitution steps, the inverse-sine branch and the trigonometric/hyperbolic identities. Related: [[Riemann Integration and the Fundamental Theorem of Calculus]].
