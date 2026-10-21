---
title: Differential Equations - Examples Sheet 1 2026
material_type: problem sheet
course: Part IA Differential Equations
date: Michaelmas Term 2026
author: Prof. Christopher Thomas
source_file: Examples Sheet 1 Q.pdf
drive_file_id: 1op-x1O8r0hY-y1C9QzaadcH6PGKOP6Zv
source_url: https://drive.google.com/file/d/1op-x1O8r0hY-y1C9QzaadcH6PGKOP6Zv/view
source_pages: 4
additional_sources:
  - source_file: A3a.pdf
    drive_file_id: 1IwSWbNNhS66lST2EnZ3epL2xixPzYxMG
    source_url: https://drive.google.com/file/d/1IwSWbNNhS66lST2EnZ3epL2xixPzYxMG/view
    source_pages: 4
---

# Differential Equations — Examples Sheet 1

Mathematical Tripos Part IA, Michaelmas Term 2026. Prof. Christopher Thomas.

Sources: [Examples Sheet 1 Q.pdf](https://drive.google.com/file/d/1op-x1O8r0hY-y1C9QzaadcH6PGKOP6Zv/view) and [A3a.pdf](https://drive.google.com/file/d/1IwSWbNNhS66lST2EnZ3epL2xixPzYxMG/view). Every page was visually read; the two four-page PDFs have identical rendered pages, though their file bytes differ. This note contains the supplied questions. Handwritten answers are separate in [[Differential Equations - Examples Sheet 1 Handwritten Proofs]].

## Instructions (page 1)

The starred questions are intended as extras: do them if you have time, but not at the expense of unstarred questions on later sheets.

The source notice is: “Copyright © 2025 University of Cambridge. Not to be quoted or reproduced without permission.”

## 1. Power rule (page 1)

Show, from first principles, that, for a non-negative integer $n$,
$$\frac{d}{dx}x^n=nx^{n-1}.$$

## 2. Product rule (page 1)

Let $f(x)=u(x)v(x)$. Use the definition of the derivative of a function to show that
$$\frac{df}{dx}=u\frac{dv}{dx}+\frac{du}{dx}v.$$

## 3. Repeated derivatives (page 1)

Calculate:

- (i) $d^n(xe^x)/dx^n$ using (a) the Leibniz rule and (b) application of the product rule.
- (ii) $d^3(\ln x)^2/dx^3$.

## 4. Taylor series and an exponential limit (page 1)

- (i) Write down or determine the Taylor series for $f(x)=e^{ax}$ about $x=1$.
- (ii) Write down or determine the Taylor series for $\ln(1+x)$ about $x=0$. Then show that
  $$\lim_{k\to\infty}k\ln\left(1+\frac{x}{k}\right)=x$$
  and deduce that
  $$\lim_{k\to\infty}\left(1+\frac{x}{k}\right)^k=e^x.$$

## 5. First three non-zero Taylor terms (page 1)

Determine by any method the first three non-zero terms of the Taylor expansions about $x=0$ of:

- (i) $(x^2+a)^{-3/2}$;
- (ii) $\ln(\cos x)$;
- (iii) $\exp[-(x-a)^{-2}]$, where $a$ is a constant.

## 6. Factorial bounds (page 2)

By considering the area under the curves $y=\ln x$ and $y=\ln(x-1)$, show that
$$N\ln N-N<\ln(N!)<(N+1)\ln(N+1)-N.$$
Hence show that
$$\frac{N!}{N+1}<\left(\frac{N+1}{e}\right)^N.$$

## 7. An integral solving a differential equation (page 2)

Show that
$$y(x)=\int_x^\infty e^{-t^2}\,dt$$
satisfies the differential equation $y''+2xy'=0$.

## ★8. An integral recurrence (page 2)

Let $J_n$ be the indefinite integral
$$J_n=\int\frac{x^{-n}}{(ax^2+2bx+c)^{1/2}}\,dx.$$
By integrating $\int x^{-(n+1)}(ax^2+2bx+c)^{1/2}\,dx$ by parts, show that, for $n\ne0$,
$$ncJ_{n+1}+(2n-1)bJ_n+(n-1)aJ_{n-1}
=-x^{-n}(ax^2+2bx+c)^{1/2}.$$
Hence evaluate
$$\int_1^2\frac{1}{x^{5/2}(x+2)^{1/2}}\,dx.$$

## ★9. Income distribution and the Gini index (pages 2–3)

In a large population, the proportion with income between $x$ and $x+dx$ is $f(x)\,dx$. Express the mean income $\mu$ as an integral, assuming that any positive income is possible.

Let $p=F(x)$ be the proportion of the population with income less than $x$, and let $G(x)$ be the mean income earned by people with income less than $x$. Further, let $\theta(p)$ be the proportion of total income earned by people with income less than $x$, as a function of the proportion $p$ of the population with income less than $x$.

Express $F(x)$ and $G(x)$ as integrals and derive an expression for $\theta(p)$, showing that
$$\theta(0)=0,\qquad\theta(1)=1,$$
$$\theta'(p)=\frac{F^{-1}(p)}{\mu},\qquad
\theta''(p)=\frac{1}{\mu f(F^{-1}(p))}>0.$$
You may assume that $F(x)$ is strictly increasing.

Sketch the graph of a function $\theta(p)$ with these properties. Deduce that, if there is any variation in income, the bottom proportion $p$ of the population, ordered by income, receives less than $p$ of the total income, for all positive values of $p$.

> [!todo] Endpoint qualification — page 2, question 9
> The printed strict inequality includes “all positive values of $p$”, but $p=1$ has $\theta(1)=1$. The strict comparison requires the interior range $0<p<1$; the printed wording is retained above.

The “Gini index” is twice the area between $\theta(p)$ and the diagonal joining $(0,0)$ and $(1,1)$.

A particular population has the exponential income distribution
$$f(x)=\lambda e^{-\lambda x}\qquad(x>0),\qquad\lambda>0.$$
Using the expression for $\theta(p)$, compute the Gini index in this case.

**Food for thought:** To what extent does the Gini index capture the degree of income inequality for this distribution?

## 10. Partial derivatives and polar coordinates (page 3)

For $f(x,y)=\exp(-xy)$, find $(\partial f/\partial x)|_y$ and $(\partial f/\partial y)|_x$. Check that
$$\frac{\partial^2f}{\partial x\partial y}
=\frac{\partial^2f}{\partial y\partial x}.$$

Now express $x,y$ in polar coordinates, $x=r\cos\theta$ and $y=r\sin\theta$. Find $(\partial f/\partial r)|_\theta$ and $(\partial f/\partial\theta)|_r$ using (a) the chain rule and (b) first expressing $f$ in terms of $r,\theta$. Check that the two methods give the same results.

## 11. Implicit differentiation (page 3)

If $xyz+x^3+y^4+z^5=0$, an implicit equation for any of $x,y,z$ in terms of the other two, find
$$\left.\frac{\partial x}{\partial y}\right|_z,\qquad
\left.\frac{\partial y}{\partial z}\right|_x,\qquad
\left.\frac{\partial z}{\partial x}\right|_y,$$
and show that their product is $-1$.

Does this result hold for an arbitrary relation $f(x,y,z)=0$? What about $f(x_1,x_2,\ldots,x_n)=0$?

## 12. Thermodynamic derivatives (page 3)

The pressure $p$ of a system can be considered as a function of volume $V$ and temperature $T$, or as a function of $V$ and entropy $S$.

(i) By expressing $p(V,S)$ in the form $p(V,S(V,T))$, evaluate
$$\left.\frac{\partial p}{\partial V}\right|_T
-\left.\frac{\partial p}{\partial V}\right|_S$$
in terms of $\left.\partial S/\partial V\right|_T$ and $\left.\partial S/\partial p\right|_V$.

(ii) Hence, using $T\,dS=dU+p\,dV$, conservation of energy with internal energy $U$, show that
$$\left.\frac{\partial\ln p}{\partial\ln V}\right|_T
-\left.\frac{\partial\ln p}{\partial\ln V}\right|_S
=\left.\frac{\partial(pV)}{\partial T}\right|_V
\left[\frac{p^{-1}\left.(\partial U/\partial V)\right|_T+1}
{\left.(\partial U/\partial T)\right|_V}\right].$$

**Hint:** $\left.(\partial\ln p/\partial\ln V)\right|_T
=(V/p)\left.(\partial p/\partial V)\right|_T$.

## 13. Differentiation under an integral (page 4)

By differentiating $I$ with respect to $\lambda$, show that
$$I(\lambda,\alpha)=\int_0^\infty\frac{\sin(\lambda x)}{x}e^{-\alpha x}\,dx
=\tan^{-1}\left(\frac\lambda\alpha\right)+c(\alpha).$$
Show that $c(\alpha)$ is independent of $\alpha$ and hence, by considering $\alpha\to\infty$ and $\alpha\to0^+$, show that, for $\lambda>0$,
$$\int_0^\infty\frac{\sin(\lambda x)}{x}\,dx=\frac\pi2.$$
What is the integral when $\lambda<0$?

## 14. Gaussian integral (page 4)

Let
$$f(x)=\left(\int_0^x e^{-t^2}\,dt\right)^2,\qquad
g(x)=\int_0^1\frac{e^{-x^2(t^2+1)}}{1+t^2}\,dt.$$
Show that $f'(x)+g'(x)=0$. Deduce that $f(x)+g(x)=\pi/4$, and hence that
$$\int_0^\infty e^{-t^2}\,dt=\frac{\sqrt\pi}{2}.$$

Comments and corrections may be sent to the source author at c.e.thomas@damtp.cam.ac.uk.

## Conditions to check while solving — supplementary review

The question statements above are preserved. The following qualifications prevent using formulas outside their domains.

- **Question 1:** the constant case $n=0$ has derivative zero; at $x=0$ do not interpret this by separately evaluating the undefined factor $x^{-1}$ in $0x^{-1}$.
- **Question 5:** for a real expansion in (i), use $a>0$. Part (iii) needs $a\ne0$ as written; even then a coefficient can vanish for special $a$, so “three non-zero terms” requires checking the parameter. See the localized note in [[Differential Equations - Examples Sheet 1 Handwritten Proofs]].
- **Question 8:** indefinite integrals represent families of antiderivatives. The displayed recurrence is understood up to an additive constant, or with compatible choices of those constants.
- **Question 9:** a finite positive mean $0<\mu<\infty$ is needed to normalize income shares. Strict increase of $F$ alone does not ensure $f(F^{-1}(p))>0$ at every point: the displayed second-derivative formula requires that positivity and enough regularity for differentiating the inverse. Endpoint values are interpreted by limits.
- **Questions 11–12:** implicit derivatives and reciprocal derivative expressions require the relevant local solvability and non-zero denominators. See [[Partial Derivatives and the Multivariate Chain Rule]].
- **Question 13:** begin with $\alpha>0$; taking $\alpha\to0^+$ through an improper integral needs justification, as does differentiating under the integral. A pointwise limit of integrands alone is insufficient.
