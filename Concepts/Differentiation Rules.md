---
title: Differentiation Rules
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Differentiation Rules

> [!abstract] In one paragraph
> The derivative is the limit of the difference quotient. Derivatives of composites, products and quotients follow from three rules; Leibniz's rule gives the $n$th derivative of a product with binomial coefficients.

## Definition

$$f'(x)=\frac{df}{dx}=\lim_{h\to0}\frac{f(x+h)-f(x)}h,$$
which requires the left- and right-hand limits to exist and agree ($|x|$ fails at $0$). Notation: $f'=\dot f$, $f''=\ddot f$, $f^{(n)}=\frac{d^nf}{dx^n}$. → [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Definition — Derivative|lecture]]

## Key results

| Rule | Formula |
| --- | --- |
| Chain | $\frac d{dx}F(g(x))=F'(g(x))\,g'(x)$ |
| Product | $(uv)'=u'v+uv'$ |
| Quotient | $\big(\frac uv\big)'=\frac{vu'-uv'}{v^2}$ |
| Leibniz | $(uv)^{(n)}=\sum_{r=0}^n\binom nru^{(n-r)}v^{(r)}$ |
| Exponential base $a$ | $\frac d{dx}a^x=a^x\ln a$ |

→ [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Theorem — Chain rule|chain]] · [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Theorem — Leibniz's rule|Leibniz]]

## Examples

- $\frac d{dx}\sin(x^2-x+2)=(2x-1)\cos(x^2-x+2)$.
- $(uv)'''=u'''v+3u''v'+3u'v''+uv'''$ — coefficients from Pascal's triangle.

## Related

[[Taylor Series and Taylor's Theorem]] · [[Partial Derivatives and the Multivariate Chain Rule]] · [[Limits, Big O and Little o - A First-Year Guide]]
