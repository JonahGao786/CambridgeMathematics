---
title: Riemann Integration and the Fundamental Theorem of Calculus
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations]
---

# Riemann Integration and the Fundamental Theorem of Calculus

> [!abstract] In one paragraph
> The integral is a limit of rectangle sums, and it equals the area under the curve. The fundamental theorem of calculus says integration undoes differentiation: $\frac d{dx}\int_a^xf=f(x)$.

## Definitions

- $\int_a^bf(x)\,dx=\lim_{N\to\infty}\sum_{n=0}^{N-1}f(x_n)\Delta x$, $\Delta x=\frac{b-a}N$, $x_n=a+n\Delta x$.
- **Riemann integrable**: the limit does not depend on how the rectangles are chosen, as all widths $\to0$.
- **Indefinite integral** $\int f(x)\,dx$ or $\int^xf(t)\,dt$ — defined up to a constant.

→ [[Differential Equations - Chapter 2 Integration#Definition — Integral as a Riemann sum|lecture]]

## Key results

- **Area.** Each strip has area $A_n=\Delta x\,f(x_n)+O((\Delta x)^2)$ (MVT), and the $N$ errors add to $O(1/N)\to0$, so area $=\int_a^bf\,dx$. → [[Differential Equations - Chapter 2 Integration#Relation to area under the curve|lecture]]
- **FTC.** $F(x)=\int_a^xf(t)\,dt\Rightarrow F'(x)=f(x)$; $F$ solves $F'=f$, $F(a)=0$. *Idea:* $\frac1h\int_x^{x+h}f=f(x)+O(h)$. → [[Differential Equations - Chapter 2 Integration#Theorem — Fundamental theorem of calculus|proof]]
- **Corollaries.** $\frac d{dx}\int_x^bf=-f(x)$; $\frac d{dx}\int_a^{g(x)}f=f(g(x))\,g'(x)$.

## Related

[[Integration by Substitution and by Parts]] · [[Differentiation Under the Integral Sign]] · [[Taylor Series and Taylor's Theorem]]
