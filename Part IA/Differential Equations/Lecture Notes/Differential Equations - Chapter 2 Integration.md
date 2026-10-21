---
title: Differential Equations - Chapter 2 Integration
material_type: handwritten lecture notes with labelled mathematical corrections and supplements
course: Part IA Differential Equations
date: null
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
source_pages: 7
---

# Differential Equations — Chapter 2: Integration

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view). No date is supplied.

The chapter reviews integration as “area under a curve” and as the “inverse of differentiation”. See [[Riemann Integration and the Fundamental Theorem of Calculus]] and [[Integration by Substitution and by Parts]].

## 2.1 Integrals as Riemann sums (page 1)

For a suitably regular function $f$, a definite integral is the limit of a sum. For example, with a uniform partition and left endpoints,
$$\int_a^b f(x)\,dx
=\lim_{N\to\infty}\sum_{n=0}^{N-1}f(x_n)\,\Delta x,$$
where
$$\Delta x=\frac{b-a}{N},\qquad x_n=a+n\Delta x.$$

The source sketch shows an increasing curve and left-endpoint rectangles. Red is the curve; blue marks an interval width and a partition point. The geometry is schematic; no formula or numerical scale for $f$ is supplied.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.2,0)--(5.8,0);
  \draw[->] (0,-0.2)--(0,3.5);
  \foreach \x/\h in {1/0.5500,1.5/0.5952,2/0.6972,2.5/0.8701,3/1.1278,3.5/1.4844,4/1.9538} {
    \draw (\x,0) rectangle (\x+0.5,\h);
  }
  \draw (4.5,0)--(4.5,2.55);
  \draw[red,thick] (0.55,0.50)
    .. controls (0.70,0.51) and (0.86,0.536) .. (1,0.55)
    .. controls (2.166667,0.60) and (3.333333,1.00) .. (4.5,2.55)
    .. controls (4.65,2.76) and (4.78,2.99) .. (4.9,3.2);
  \node[below] at (1,0) {$a$};
  \node[below] at (4.5,0) {$b$};
  \draw[blue,<->] (2.5,1.4)--(3,1.4) node[midway,above] {$\Delta x$};
  \node[blue] at (3.25,-0.85) {$x_n$};
  \draw[blue,->] (3.05,-0.75) .. controls (2.65,-0.6) and (2.55,-0.35) .. (2.5,-0.08);
\end{tikzpicture}
\end{document}
```

The function is **Riemann integrable** if generalized Riemann sums have the same limit regardless of the chosen rectangles: interval widths may be non-uniform, and sample points need not be left endpoints. The largest interval width tends to zero.

## Relation to area under the curve (pages 2–3)

For a continuous $f$, the mean value theorem for integrals, referenced to Analysis I, gives
$$A_n=(x_{n+1}-x_n)f(c_n),\qquad x_n<c_n<x_{n+1},$$
where $A_n$ is the area under the positive curve between $x_n$ and $x_{n+1}$ in the sketch.

Blue hatching indicates this area; the black horizontal edge is the left-endpoint rectangle. The curve is qualitative.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \begin{scope}
    \clip (1.3,0)--(1.3,0.7)
      .. controls (2,0.88) and (2.55,1.15) .. (3.3,1.65)
      --(3.3,0)--cycle;
    \foreach \x in {0.4,0.7,...,3.4} {
      \draw[blue] (\x,0)--(\x+0.9,1.9);
    }
  \end{scope}
  \draw[->] (-0.15,0)--(5,0);
  \draw[->] (0,0)--(0,3.3);
  \draw (1.3,0)--(1.3,0.7)--(3.3,0.7);
  \draw (3.3,0)--(3.3,1.65);
  \draw[red,thick] (0.7,0.59)
    .. controls (1,0.62) and (1.11,0.65) .. (1.3,0.7)
    .. controls (2,0.88) and (2.55,1.15) .. (3.3,1.65)
    .. controls (3.8,2.03) and (4.1,2.55) .. (4.6,3.15);
  \node[red,right] at (4.6,3.15) {$f(x)$};
  \node[below] at (1.3,0) {$x_n$};
  \node[below] at (3.3,0) {$x_{n+1}$};
  \draw[<->] (1.3,2.05)--(3.3,2.05) node[midway,above] {$\Delta x$};
\end{tikzpicture}
\end{document}
```

### Uniform error control — corrected proof (pages 2–3)

The source estimates each strip by $A_n=\Delta x\,f(x_n)+O((\Delta x)^2)$ and then sums the errors. The following supplementary argument supplies the missing uniform bound.

Assume $f$ is continuous on $[a,b]$, differentiable on $(a,b)$, and $|f'(t)|\le M$ there, for one constant $M$ (for example, $f\in C^1([a,b])$). The mean value theorem gives
$$|f(t)-f(x_n)|\le M|t-x_n|.$$
Consequently, with $A_n=\int_{x_n}^{x_{n+1}}f(t)\,dt$,
$$\begin{aligned}
|A_n-f(x_n)\Delta x|
&\le\int_{x_n}^{x_{n+1}}|f(t)-f(x_n)|\,dt\\
&\le\frac M2(\Delta x)^2.
\end{aligned}$$
Since $A=\sum_{n=0}^{N-1}A_n$, the total error is bounded by
$$\left|A-\sum_{n=0}^{N-1}f(x_n)\Delta x\right|
\le\frac{M(b-a)^2}{2N}\longrightarrow0.$$
The same $M$ works for every strip and every $N$, so the claimed $O(1/N)$ rate is now justified. For a non-negative $f$, $A$ is ordinary area; in general the integral is signed area.

**With continuity alone.** Continuous $f$ on $[a,b]$ is uniformly continuous. Define
$$\omega_f(\delta)=\sup_{\substack{s,t\in[a,b]\\|s-t|\le\delta}}|f(s)-f(t)|.$$
Then $\omega_f(\delta)\to0$. Upper and lower Riemann sums for a partition of mesh at most $\delta$ differ by at most $(b-a)\omega_f(\delta)$, so $f$ is Riemann integrable. Each tagged sum differs from its integral by at most the same bound. This proves convergence for continuous functions without asserting an $O(1/N)$ rate. Pointwise differentiability alone did not justify the source's uniform error estimate.

## 2.2 Fundamental theorem of calculus (page 3)

The [[Riemann Integration and the Fundamental Theorem of Calculus|fundamental theorem of calculus]] expresses integration as the inverse of differentiation. For continuous $f$ on the interval, let
$$F(x)=\int_a^x f(t)\,dt.$$
Then, at interior points,
$$F'(x)=\frac{d}{dx}\int_a^x f(t)\,dt=f(x).$$

**Corrected proof under the stated continuity hypothesis — supplementary.** For $h\ne0$ small enough that $x+h\in[a,b]$, put $I_h=[\min(x,x+h),\max(x,x+h)]$. Additivity and orientation of the integral give
$$\frac{F(x+h)-F(x)}h-f(x)
=\frac1h\int_x^{x+h}(f(t)-f(x))\,dt.$$
Therefore
$$\left|\frac{F(x+h)-F(x)}h-f(x)\right|
\le\sup_{t\in I_h}|f(t)-f(x)|\longrightarrow0$$
by continuity at $x$. This works for positive and negative $h$, proving $F'(x)=f(x)$.

The source's estimate $\int_x^{x+h}f(t)\,dt=f(x)h+O(h^2)$ is valid if $f$ is also differentiable at $x$, but is unnecessary here. Under continuity, the correct general remainder is $o(h)$, exactly what differentiation requires.

### Corollaries and indefinite-integral notation (page 4)

The function $F$ solves
$$F'(x)=f(x),\qquad F(a)=0.$$

The corollaries are
$$\frac{d}{dx}\int_x^b f(t)\,dt=-f(x)$$
and, for differentiable $g$ with values in the interval,
$$\begin{aligned}
\frac{d}{dx}\int_a^{g(x)}f(t)\,dt
&=\frac{d}{dx}F(g(x))\\
&=F'(g(x))g'(x)=f(g(x))g'(x).
\end{aligned}$$

**Evaluation by an antiderivative — supplementary consequence.** If $A$ is continuous on $[a,b]$, differentiable on $(a,b)$ and $A'=f$ there, then $(A-F)'=0$. The mean value theorem shows that $A-F$ is constant, giving
$$\int_a^b f(t)\,dt=A(b)-A(a).$$
This is the bridge from Riemann sums to the substitution and integration-by-parts calculations below.

An **indefinite integral** is written $\int f(x)\,dx$ or $\int^x f(t)\,dt$. An unspecified lower limit leaves an integration constant.

## 2.3 Integration techniques (pages 5–7)

### Substitution (page 5)

When the integrand contains a function of a function, substituting for the inner function may help.

**Example.** On $0<x<1$, consider
$$I=\int\frac{1-2x}{\sqrt{x-x^2}}\,dx.$$
Let $u=x-x^2$, so $du/dx=1-2x$. Then
$$I=\int\frac{du}{\sqrt u}=2\sqrt u+C=2\sqrt{x-x^2}+C.$$

### Trigonometric and hyperbolic substitutions (pages 5–6)

Recall
$$\cos^2\theta+\sin^2\theta=1,\qquad 1+\tan^2\theta=\sec^2\theta,$$
$$\cosh^2u-\sinh^2u=1,\qquad 1-\tanh^2u=\operatorname{sech}^2u.$$

The source lists these useful substitutions:

| Integrand contains | Substitution |
| --- | --- |
| $\sqrt{1-x^2}$ | $x=\sin\theta$ |
| $1+x^2$ | $x=\tan\theta$ |
| $\sqrt{x^2-1}$ | $x=\cosh u$ |
| $\sqrt{x^2+1}$ | $x=\sinh u$ |
| $1-x^2$ | $x=\tanh u$ |

**Example (page 6).**
$$I=\int\sqrt{2x-x^2}\,dx=\int\sqrt{1-(x-1)^2}\,dx.$$
Take $x-1=\sin\theta$, so $dx=\cos\theta\,d\theta$, with
$$-\frac\pi2\le\theta\le\frac\pi2$$
to give a unique choice for $0\le x\le2$. On this branch $\cos\theta\ge0$, so
$$\begin{aligned}
I&=\int\sqrt{\cos^2\theta}\,\cos\theta\,d\theta\\
&=\int\cos^2\theta\,d\theta\\
&=\int\left(\frac12\cos2\theta+\frac12\right)d\theta\\
&=\frac14\sin2\theta+\frac12\theta+C\\
&=\frac12\arcsin(x-1)
+\frac12(x-1)\sqrt{1-(x-1)^2}+C.
\end{aligned}$$
The inverse sine uses its branch $[-\pi/2,\pi/2]$.

### Integration by parts (page 7)

From the product rule $(uv)'=u'v+uv'$,
$$\int uv'\,dx=uv-\int u'v\,dx.$$

**Example.** With $u=x$ and $v'=e^{-x}$, hence $u'=1$ and $v=-e^{-x}$,
$$\begin{aligned}
I=\int_0^\infty xe^{-x}\,dx
&=[-xe^{-x}]_0^\infty-\int_0^\infty(-e^{-x})\,dx\\
&=[-e^{-x}]_0^\infty=1.
\end{aligned}$$
The improper upper endpoints are limits; $xe^{-x}\to0$ and $e^{-x}\to0$ as $x\to\infty$.


**Example.** For $x>0$, let $u=\log x$ and $dv=dx$, so $du=dx/x$ and $v=x$. Then
$$\begin{aligned}
I=\int\log x\,dx
&=x\log x-\int dx\\
&=x(\log x-1)+C.
\end{aligned}$$
The source notes that integration by parts also works for inverse trigonometric and inverse hyperbolic functions; no further examples are supplied.

## Supplementary learning route

[[Riemann Integration and the Fundamental Theorem of Calculus#Completing the learning bridge — supplementary proofs]] summarizes the corrected continuity-based proof and the antiderivative evaluation formula above. [[Integration by Substitution and by Parts#Domains and the fundamental theorem — supplementary explanation]] explains branch restrictions and improper endpoints used above.
