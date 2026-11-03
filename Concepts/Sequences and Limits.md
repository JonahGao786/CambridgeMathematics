---
title: Sequences and Limits
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Sequences and Limits

> [!abstract] In one paragraph
> $a_n\to\ell$ means the terms **get and stay** within any $\varepsilon$ of $\ell$: for every $\varepsilon>0$ there is $N$ with $|a_n-\ell|<\varepsilon$ for all $n\ge N$. To prove a limit, pick $N$ from $\varepsilon$ (usually via Archimedes, $N>\frac1\varepsilon$); to disprove one, find a single $\varepsilon$ that infinitely many terms miss. The triangle inequality shows limits are unique.

## Definitions

- **Sequence** $(a_n)_{n=1}^\infty$: order matters, repetition allowed. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Sequence|lecture]]
- **Limit:** $\forall\varepsilon>0\ \exists N\ \forall n\ge N,\ |a_n-\ell|<\varepsilon$. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Limit of a sequence|lecture]]
- **Absolute value** and the triangle inequality $|a-c|\le|a-b|+|b-c|$. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Absolute value|lecture]]
- **Convergent / divergent;** $a_n\not\to\ell$ means $\exists\varepsilon>0\ \forall N\ \exists n\ge N,\ |a_n-\ell|\ge\varepsilon$. → [[Numbers and Sets - Chapter 2 The Reals#Definition — Convergence and divergence|lecture]]

## Key results

- **Uniqueness of limits.** If $a_n\to\ell$ and $a_n\to k\ne\ell$, take $\varepsilon=\frac12|\ell-k|$; then $|\ell-k|<2\varepsilon$, a contradiction. → [[Numbers and Sets - Chapter 2 The Reals#Proposition — Uniqueness of limits|proof]]

## Examples

- $1-\frac1n\to1$, $\ 0,\frac12,0,\frac14,\dots\to0$, $\ 1-\frac1{2^n}\to1$ (all with $N>\frac1\varepsilon$). → [[Numbers and Sets - Chapter 2 The Reals#Examples of limits|lecture]]
- $(-1)^n$ diverges: $\varepsilon=1$ would need $|1-\ell|<1$ and $|-1-\ell|<1$, giving $2<2$.

## Related

[[Real Numbers and the Least Upper Bound Axiom]] · [[Logical Connectives and Quantifiers]] · [[Limits, Big O and Little o - A First-Year Guide]]
