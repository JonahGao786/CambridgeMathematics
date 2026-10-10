---
title: Differential Equations - Examples Sheet 1 Handwritten Proofs
material_type: handwritten worked proofs
course: Part IA Differential Equations
date: null
source_file: Examples Sheet 1.pdf
drive_file_id: 13RHsCyXVE8qyIQtepFN5CYrkA5ObHNSo
source_url: https://drive.google.com/file/d/13RHsCyXVE8qyIQtepFN5CYrkA5ObHNSo/view
source_pages: 1
---

# Differential Equations — Examples Sheet 1: Handwritten Proofs

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/13RHsCyXVE8qyIQtepFN5CYrkA5ObHNSo/view).

> [!todo] Missing question context — page 1
> The document contains answers labelled 1 and 2, but no supplied questions or stated hypotheses. The proofs below identify the necessary assumptions; the original wording and intended scope remain unavailable.

## 1. Differentiating $x^n$ (page 1, upper half)

The supplied calculation uses the finite binomial expansion. For a positive integer $n$,
$$
\begin{aligned}
\frac{d}{dx}(x^n)
&=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}\\
&=\lim_{h\to0}
\frac{\displaystyle\sum_{k=0}^n\binom nkx^{n-k}h^k-x^n}{h}\\
&=\lim_{h\to0}\left(
nx^{n-1}+\sum_{k=2}^n\binom nkx^{n-k}h^{k-1}
\right)\\
&=nx^{n-1}.
\end{aligned}
$$
The sum from $k=2$ to $n$ is empty when $n=1$.

**Explanation.** The $k=0$ term cancels $x^n$, and the $k=1$ term becomes $nx^{n-1}$ after division by $h\ne0$. Every remaining term has a positive power of $h$, so tends to zero. There are only finitely many terms, which permits taking their limits term by term. This calculation does not prove the rule for an arbitrary real exponent.

## 2. Product rule (page 1, lower half)

Assume $u$ and $v$ are differentiable at the real point $x$, and defined in a neighbourhood of $x$. The supplied argument starts with
$$
u(x)v'(x)+v(x)u'(x)
=
\lim_{h\to0}\left(
u(x)\frac{v(x+h)-v(x)}h
+
v(x)\frac{u(x+h)-u(x)}h
\right).
$$
Add and subtract $u(x+h)v(x+h)$ in the numerator. The resulting identity is
$$
\begin{aligned}
&u(x)\bigl(v(x+h)-v(x)\bigr)
+v(x)\bigl(u(x+h)-u(x)\bigr)\\
&\qquad=
u(x+h)v(x+h)-u(x)v(x)\\
&\qquad\quad-
\bigl(v(x+h)-v(x)\bigr)\bigl(u(x+h)-u(x)\bigr).
\end{aligned}
$$
After dividing by $h$ and taking limits, the source writes the last correction as $vu'-vu'$, giving
$$u(x)v'(x)+v(x)u'(x)=(uv)'(x).$$

### Justifying the correction and existence of the derivative

This explains the limiting step implicit in the source. Set
$$D_u(h)=\frac{u(x+h)-u(x)}h,\qquad
D_v(h)=\frac{v(x+h)-v(x)}h\qquad(h\ne0).$$
Both have finite limits. Hence
$$
\frac{u(x+h)v(x+h)-u(x)v(x)}h
=
u(x)D_v(h)+v(x)D_u(h)
+\bigl(v(x+h)-v(x)\bigr)D_u(h).
$$
Differentiability implies continuity: $v(x+h)-v(x)=hD_v(h)\to0$ because $D_v(h)$ has a finite limit and is therefore bounded for sufficiently small non-zero $h$. Meanwhile $D_u(h)\to u'(x)$. The last product tends to zero. Thus the product's difference quotient has a limit, proving both existence of $(uv)'(x)$ and
$$(uv)'(x)=u(x)v'(x)+v(x)u'(x).$$

In the notation of [[Limits, Big O and Little o - A First-Year Guide]],
$$u(x+h)-u(x)=O(h),\qquad v(x+h)-v(x)=O(h),$$
so their product is $O(h^2)$ and division by $h$ leaves $O(h)\to0$.

See [[Differential Equations - Chapter 1 Introduction and Basic Calculus]] for the derivative and limit definitions.
