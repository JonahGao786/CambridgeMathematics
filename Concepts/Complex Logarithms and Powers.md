---
title: Complex Logarithms and Powers
material_type: source-backed definitions with supplementary explanation
course: Part IA Vectors and Matrices
---

# Complex Logarithms and Powers

For $z\ne0$, a logarithm of $z$ is $L\in\mathbb C$ satisfying $e^L=z$. Using the lecture's convention $\arg z\in(-\pi,\pi]$,
$$
\log z=\log|z|+i\arg z,\qquad
\operatorname{Log}z=\{\log z+2\pi in:n\in\mathbb Z\}.
$$
Here $\log z$ is the principal value and $\operatorname{Log}z$ is the **set of all logarithms**. The real $\log|z|$ is the natural logarithm. There is no logarithm of zero because the [[Complex Exponential and Trigonometric Functions|exponential]] never vanishes.

For $\alpha\in\mathbb C$, choosing $L\in\operatorname{Log}z$ gives the value
$$z^\alpha=e^{\alpha L}.$$
Changing $L$ by $2\pi in$ multiplies it by $e^{2\pi in\alpha}$.

- Integer $\alpha$: one value, the usual integer power.
- Rational $\alpha=p/q$ in lowest terms, $q>0$: exactly $q$ values.
- Other $\alpha$: infinitely many values.

The principal value is $e^{\alpha\log z}$.

## Compatible logarithms in power laws

With one fixed $L\in\operatorname{Log}z$,
$$e^{\alpha L}e^{\beta L}=e^{(\alpha+\beta)L}.$$
For $u=e^{\alpha L}$, choose $\alpha L$ as a logarithm of $u$. Then
$$u^\beta=e^{\beta\alpha L}=z^{\alpha\beta}$$
using $L$ on the right. This explains the compatible-value meanings of
$$z^\alpha z^\beta=z^{\alpha+\beta},\qquad
(z^\alpha)^\beta=z^{\alpha\beta}.$$
They are not blanket rules for independently chosen values.

The source examples give
$$
i^i\in\{e^{-(\pi/2+2\pi n)}:n\in\mathbb Z\},\qquad
(1+i)^{1/2}\in\{2^{1/4}e^{i\pi/8},-2^{1/4}e^{i\pi/8}\}.
$$
Their principal values are $e^{-\pi/2}$ and $2^{1/4}e^{i\pi/8}$.

Source and complete worked examples: [[Vectors and Matrices - Chapter 1 Complex Numbers]], pages 16–18.

## Why reduced fractions matter — supplementary explanation

Two choices indexed by $m,n\in\mathbb Z$ give the same value exactly when
$$e^{2\pi i(n-m)\alpha}=1.$$
For $\alpha=p/q$ with $\gcd(p,q)=1$ and $q>0$, this is equivalent to $q\mid n-m$. Thus the values repeat every $q$ choices and there are exactly $q$ distinct ones. Writing $1/2$ as $2/4$ does not create four square roots.

If $\alpha$ is not rational, equality for distinct $m,n$ would imply $(n-m)\alpha\in\mathbb Z$, hence $\alpha\in\mathbb Q$, a contradiction. Thus all indexed choices are distinct.

## A principal-value trap — supplementary example

Let $z=-1$, $\alpha=2$ and $\beta=1/2$. The principal logarithms satisfy $\log(-1)=i\pi$ and $\log1=0$. Therefore
$$
\bigl((-1)^2\bigr)^{1/2}=1^{1/2}=1
\qquad\text{using principal values},
$$
whereas $(-1)^{2(1/2)}=-1$.

To make the nested-power law work, first take $L=i\pi$, obtain $u=e^{2L}=1$, then choose the compatible logarithm $2L=2\pi i$ of $u$, rather than its principal logarithm $0$. That choice gives
$$u^{1/2}=e^{(1/2)(2\pi i)}=-1.$$
This is the mathematical reason for the compatibility condition.

The principal logarithm is also discontinuous across the negative real axis with this argument convention: arguments approaching that axis from above tend to $\pi$, while those from below tend to $-\pi$. Choosing a principal value makes the value unique; it does not make it continuous everywhere.
