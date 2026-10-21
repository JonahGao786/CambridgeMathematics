---
title: Differential Equations - Chapter 2 Integration
material_type: source-backed notes with course-level explanations
course: Part IA Differential Equations
date: null
source_file: Ch.2 Integration.pdf
drive_file_id: 1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N
source_url: https://drive.google.com/file/d/1nJYhFVmMI7O9dls3BfHoF7do6W0uNg9N/view
reference_handout: topic1.pdf
reference_handout_pages: "13–19"
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

### Why the rectangle sums give the area (pages 2–3)

Follow the strip argument in `topic1.pdf`, pages 14–15. For this error estimate, assume $f$ is continuous on $[a,b]$, differentiable inside it, and $|f'|\le M$ for one fixed constant $M$ throughout the interval.

Since $A_n=\Delta x\,f(c_n)$ and $|c_n-x_n|\le\Delta x$, the mean value theorem gives
$$|A_n-f(x_n)\Delta x|
=\Delta x\,|f(c_n)-f(x_n)|\le M(\Delta x)^2.$$
Adding the $N$ strip errors,
$$\left|A-\sum_{n=0}^{N-1}f(x_n)\Delta x\right|
\le NM(\Delta x)^2=\frac{M(b-a)^2}{N}\longrightarrow0.$$
Thus the limiting rectangle sum agrees with the area. In the lecture's notation, each error is $O((\Delta x)^2)$ and their sum is $O(1/N)$; using the same bound $M$ for every strip makes this step valid.

Continuous functions are Riemann integrable even without a bounded derivative; the general proof belongs to Analysis I. The integral represents signed area if $f$ takes negative values.

## 2.2 Fundamental theorem of calculus (page 3)

The [[Riemann Integration and the Fundamental Theorem of Calculus|fundamental theorem of calculus]] expresses integration as the inverse of differentiation. For continuous $f$ on the interval, let
$$F(x)=\int_a^x f(t)\,dt.$$
Then, at interior points,
$$F'(x)=\frac{d}{dx}\int_a^x f(t)\,dt=f(x).$$

**Proof using the mean value theorem for integrals.** For small $h\ne0$, there is a point $c_h$ between $x$ and $x+h$ such that
$$\frac{F(x+h)-F(x)}h
=\frac1h\int_x^{x+h}f(t)\,dt=f(c_h).$$
As $h\to0$, also $c_h\to x$, so continuity gives $F'(x)=f(x)$. This works for either sign of $h$.

This is the mean-value idea used in `topic1.pdf`, pages 15–16. Its $f(x)h+O(h^2)$ estimate is also valid when $f$ is differentiable at $x$; continuity alone suffices for the argument above.

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

If $A'=f$, the definite integral can be evaluated as
$$\int_a^b f(t)\,dt=A(b)-A(a).$$
Here $A$ is continuous on $[a,b]$ and differentiable inside it. Indeed, $(A-F)'=0$, so $A-F$ is constant.

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

## Related notes

[[Riemann Integration and the Fundamental Theorem of Calculus]] summarizes the area and antiderivative viewpoints. [[Integration by Substitution and by Parts]] collects the techniques and examples.
