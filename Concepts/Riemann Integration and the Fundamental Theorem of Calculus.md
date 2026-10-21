---
title: Riemann Integration and the Fundamental Theorem of Calculus
material_type: source-backed definitions, theorem and proof with explicit proof scope and supplementary explanation
course: Part IA Differential Equations
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: [1, 2, 3, 4]
---

# Riemann Integration and the Fundamental Theorem of Calculus

With $\Delta x=(b-a)/N$ and $x_n=a+n\Delta x$, a uniform left-endpoint Riemann sum is
$$\sum_{n=0}^{N-1}f(x_n)\,\Delta x.$$
For a Riemann-integrable function, its limit is $\int_a^b f(x)\,dx$. More generally, the limit is independent of non-uniform interval widths and sample points when the largest interval width tends to zero.

For the positive continuous curve in the source, the integral mean value theorem gives a strip area
$$A_n=\Delta x\,f(c_n),\qquad x_n<c_n<x_{n+1}.$$

**Corrected uniform estimate.** If $f$ is continuous on $[a,b]$, differentiable on $(a,b)$ and $|f'|\le M$ throughout, the mean value theorem and an integral bound give
$$|A_n-\Delta x\,f(x_n)|\le\frac M2(\Delta x)^2,$$
so the total error is at most $M(b-a)^2/(2N)$. The constant is independent of the strip and of $N$. Continuity alone still gives convergence by uniform continuity, but not this rate. [[Differential Equations - Chapter 2 Integration]] now contains both complete arguments, explicitly supplementing the source's previously unjustified summation of pointwise $O$ terms.

## Fundamental theorem of calculus

For continuous $f$, define
$$F(x)=\int_a^x f(t)\,dt.$$
At interior points,
$$F'(x)=f(x),\qquad F(a)=0.$$

**Proof under continuity — supplementary correction.** For $h\ne0$, let $I_h$ be the segment from $x$ to $x+h$. Then
$$\left|\frac{F(x+h)-F(x)}h-f(x)\right|
\le\sup_{t\in I_h}|f(t)-f(x)|\longrightarrow0.$$
Continuity at $x$ proves the limit from both sides. The source used the stronger estimate $\int_x^{x+h}f(t)\,dt=f(x)h+O(h^2)$, valid when $f$ is differentiable at $x$. The proof above covers the stated continuous case with an $o(h)$ remainder.

The corollaries, using the [[Differentiation Rules|chain rule]], are
$$\frac{d}{dx}\int_x^b f(t)\,dt=-f(x),$$
$$\frac{d}{dx}\int_a^{g(x)}f(t)\,dt=f(g(x))g'(x)$$
for differentiable $g$ with values in the interval.

An indefinite integral $\int f(x)\,dx$ denotes an antiderivative with an arbitrary integration constant.

Source: [[Differential Equations - Chapter 2 Integration]], pages 1–4, including both area diagrams. Related: [[Limits, Big O and Little o - A First-Year Guide]] and [[Integration by Substitution and by Parts]].

## Completing the learning bridge — supplementary proofs

These arguments are additional explanations, not proofs attributed to the lecture.

The corrected proof above shows that continuity supplies the first-order integral estimate $F(x+h)-F(x)=hf(x)+o(h)$. No derivative of $f$ is needed.

**Evaluating a definite integral.** If $A$ is continuous on $[a,b]$, differentiable on $(a,b)$ and $A'=f$ there for continuous $f$, then $(A-F)'=0$ on $(a,b)$. The mean value theorem implies $A-F$ is constant, so
$$\int_a^b f(t)\,dt=A(b)-A(a).$$
This connects the integral definition with the antiderivatives used in [[Integration by Substitution and by Parts]].

**Uniform control for Riemann sums.** A continuous function on $[a,b]$ is uniformly continuous. Put
$$\omega_f(\delta)=\sup\{|f(s)-f(t)|:s,t\in[a,b],\ |s-t|\le\delta\}.$$
Then $\omega_f(\delta)\to0$. Upper and lower sums differ by at most $(b-a)\omega_f(\delta)$, proving integrability. The error of a tagged sum with largest interval width $\delta$ is at most the same bound. This establishes convergence without claiming the lecture's stronger $O(1/N)$ rate. A bounded derivative supplies that stronger rate by the mean value theorem. A single convergent sequence of left-endpoint sums alone is not the definition of Riemann integrability.
