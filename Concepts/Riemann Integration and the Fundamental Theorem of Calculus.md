---
title: Riemann Integration and the Fundamental Theorem of Calculus
material_type: course-level definitions, formulas and explanations
course: Part IA Differential Equations
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: [1, 2, 3, 4]
reference_handout: topic1.pdf
reference_handout_pages: "13–16"
---

# Riemann Integration and the Fundamental Theorem of Calculus

## Integral as a sum of thin rectangles

Divide $[a,b]$ into $N$ intervals of width $\Delta x=(b-a)/N$, with $x_n=a+n\Delta x$. For a continuous function,
$$\int_a^b f(x)\,dx=\lim_{N\to\infty}\sum_{n=0}^{N-1}f(x_n)\Delta x.$$
The rectangles approximate the signed area under the curve. Riemann integrability requires the same limit when the sample points and partition are changed, provided the largest interval width tends to zero.

**The lecture's error estimate.** If $f$ is continuous on $[a,b]$, differentiable inside it and $|f'|\le M$, the mean value theorem bounds each strip error by $M(\Delta x)^2$. Summing gives
$$\text{total error}\le NM(\Delta x)^2=\frac{M(b-a)^2}{N}\longrightarrow0.$$
One fixed bound $M$ must work throughout the interval. Continuity alone still gives integrability, but need not give this $1/N$ error estimate. The general theory is left to Analysis I.

## Fundamental theorem of calculus

For continuous $f$, define
$$F(x)=\int_a^x f(t)\,dt.$$
Then $F(a)=0$ and, at interior points,
$$F'(x)=f(x).$$

**Why it works.** The difference $F(x+h)-F(x)$ is the integral over the short interval from $x$ to $x+h$. The mean value theorem for integrals gives
$$\frac{F(x+h)-F(x)}h=f(c_h)$$
for some $c_h$ between the endpoints. As $h\to0$, continuity gives $f(c_h)\to f(x)$.

If $A$ is an antiderivative, continuous on $[a,b]$ and differentiable inside it, then $(A-F)'=0$. Hence
$$\int_a^b f(t)\,dt=A(b)-A(a).$$
An indefinite integral $\int f(x)\,dx$ denotes an antiderivative plus an arbitrary constant.

## Variable endpoints

The fundamental theorem and the chain rule give
$$\frac{d}{dx}\int_x^b f(t)\,dt=-f(x),$$
$$\frac{d}{dx}\int_a^{g(x)}f(t)\,dt=f(g(x))g'(x).$$
Here $g$ is differentiable and takes values in the integration domain.

See [[Differential Equations - Chapter 2 Integration]], sections 2.1–2.2, and `topic1.pdf`, pages 13–16. [[Integration by Substitution and by Parts]] applies these ideas to evaluating integrals.
