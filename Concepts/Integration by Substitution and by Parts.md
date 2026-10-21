---
title: Integration by Substitution and by Parts
material_type: concept note
course: Part IA Differential Equations
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: [5, 6, 7]
---

# Integration by Substitution and by Parts

## Substitution

A function of a function may suggest substituting for its inner function. For example, use $u=x-x^2$:
$$\int\frac{1-2x}{\sqrt{x-x^2}}\,dx
=\int\frac{du}{\sqrt u}=2\sqrt{x-x^2}+C,$$
on the real domain $0<x<1$.

Useful substitutions:

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

For example, take $u=x$ and $v=-e^{-x}$:
$$\begin{aligned}
\int_0^\infty xe^{-x}\,dx
&=[-xe^{-x}]_0^\infty+\int_0^\infty e^{-x}\,dx\\
&=[-e^{-x}]_0^\infty=1.
\end{aligned}$$
The boundary terms use $xe^{-x}\to0$ and $e^{-x}\to0$ as $x\to\infty$.

For $x>0$, the other worked example uses $u=\log x$, $dv=dx$, hence $du=dx/x$ and $v=x$:
$$\int\log x\,dx=x\log x-\int dx=x(\log x-1)+C.$$
Integration by parts also applies to inverse trigonometric and hyperbolic functions.

See [[Differential Equations - Chapter 2 Integration]], pages 5–7. Related: [[Riemann Integration and the Fundamental Theorem of Calculus]].

## Domains and the fundamental theorem

These techniques reverse [[Differentiation Rules]] using [[Riemann Integration and the Fundamental Theorem of Calculus]]. For continuous $f$ and continuously differentiable $g$,
$$\int_a^b f(g(x))g'(x)\,dx=\int_{g(a)}^{g(b)}f(u)\,du.$$
This formula does not require $g$ to be one-to-one. Solving a substitution backwards, however, requires a suitable branch and the transformed limits. Similarly,
$$\int_a^b u(x)v'(x)\,dx=[uv]_a^b-\int_a^b u'(x)v(x)\,dx$$
for continuously differentiable $u,v$.

The substitution table gives suggestions, not formulas valid on every real domain. For $x=\sin\theta$, choose $-\pi/2\le\theta\le\pi/2$ so $\sqrt{1-x^2}=\cos\theta$. For $x=\cosh u$, choose $u\ge0$ to cover $x\ge1$ and obtain $\sqrt{x^2-1}=\sinh u$; the branch $x\le-1$ needs $x=-\cosh u$. The choice $x=\tanh u$ covers only $|x|<1$. Always use $\sqrt{v^2}=|v|$ before fixing a sign.

An improper integral such as $\int_0^\infty xe^{-x}\,dx$ means $\lim_{R\to\infty}\int_0^R xe^{-x}\,dx$. Apply integration by parts on $[0,R]$ first, then check that each required limit exists.
