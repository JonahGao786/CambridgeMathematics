---
title: Limits, Big O and Little o - A First-Year Guide
course: Part IA Differential Equations
material_type: concept note
tags: [concept, differential-equations, limits]
---

# Limits, Big O and Little o

> [!abstract] In one paragraph
> $\lim_{x\to x_0}f(x)=A$ says $f(x)$ gets as close to $A$ as you like once $x$ is close enough to $x_0$ (but $x\ne x_0$). Big $O$ says "bounded by a multiple of"; little $o$ says "much smaller than". They let us write Taylor remainders as $o(h^n)$ or $O(h^{n+1})$.

## Definitions

| Statement | Meaning |
| --- | --- |
| $\lim_{x\to x_0}f(x)=A$ | $\forall\varepsilon>0\ \exists\delta>0:\ 0<\lvert x-x_0\rvert<\delta\Rightarrow\lvert f(x)-A\rvert<\varepsilon$ |
| right-hand limit | same with $0<x-x_0<\delta$ |
| $\lim_{x\to\infty}f(x)=A$ | $\forall\varepsilon>0\ \exists X:\ x>X\Rightarrow\lvert f(x)-A\rvert<\varepsilon$ |
| $f=O(g)$ as $x\to x_0$ | $\exists\delta,\mu>0:\ 0<\lvert x-x_0\rvert<\delta\Rightarrow\lvert f\rvert\le\mu\lvert g\rvert$ |
| $f=O(g)$ as $x\to\infty$ | $\exists x_1,\mu>0:\ x>x_1\Rightarrow\lvert f\rvert\le\mu\lvert g\rvert$ |
| $f=o(g)$ as $x\to x_0$ | $\forall\varepsilon>0\ \exists\delta>0:\ 0<\lvert x-x_0\rvert<\delta\Rightarrow\lvert f\rvert\le\varepsilon\lvert g\rvert$ |

→ [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Aside — Limits|lecture]]

## Reading the $\varepsilon$–$\delta$ definition

1. **For every** tolerance $\varepsilon>0$ (however small),
2. **there exists** a $\delta>0$ — which may depend on $\varepsilon$,
3. such that **every** $x$ with $0<|x-x_0|<\delta$ has $|f(x)-A|<\varepsilon$.

The value $f(x_0)$ plays no role: $\frac{x^2-1}{x-1}\to2$ as $x\to1$ although it is undefined at $1$.

**Worked example.** $\lim_{x\to2}x^2=4$. Since $|x^2-4|=|x-2||x+2|$ and $|x-2|<1\Rightarrow|x+2|<5$, take $\delta=\min\{1,\varepsilon/5\}$: then $|x^2-4|<5\delta\le\varepsilon$.

## Key facts

- Limits are unique; limits of sums, products and quotients (denominator limit $\ne0$) are the sums, products and quotients of limits. (Proved in Analysis I.)
- If $g\ne0$ near $x_0$: $f=O(g)\iff f/g$ bounded near $x_0$; $f=o(g)\iff f/g\to0$.
- $o(g)\Rightarrow O(g)$, not conversely ($2x=O(x)$ but not $o(x)$ as $x\to0$).
- Non-zero constants don't matter: $f=O(g)\Rightarrow af=O(g)$ and $f=O(ag)$.
- Differentiability means $f(x_0+h)=f(x_0)+hf'(x_0)+o(h)$. → [[Differential Equations - Chapter 1 Introduction and Basic Calculus#Remainder of the first-order approximation|lecture]]

## Examples

- As $x\to0$: $x^2=O(x)$, $x\ne O(x^2)$, $x^2=o(x)$, $\sin2x=O(x)$ (since $|\sin x|\le|x|$).
- As $x\to0^+$: $x=O(\sqrt x)$.
- As $x\to\infty$: $2x^3+4x=O(x^3)$; $\sqrt x=o(x)$.
- As $h\to0$: $h^{n+1/2}=o(h^n)$ but not $O(h^{n+1})$.

## Pitfalls

- $\delta$ may depend on $\varepsilon$ but not on the particular $x$ being tested.
- "$O$" and "$o$" always refer to a limiting point ($x\to0$, $x\to\infty$, …); $x^2=O(x)$ is true as $x\to0$ and false as $x\to\infty$.

## Related

[[Taylor Series and Taylor's Theorem]] · [[Logical Connectives and Quantifiers]] · [[L'Hôpital's Rule]]
