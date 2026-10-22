---
title: Bijections and Permutations
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Bijections and Permutations

> [!abstract] In one paragraph
> A bijection is a function with a two-sided inverse; a permutation is a bijection from a set to itself. Under composition, the permutations of $X$ form the symmetric group $\operatorname{Sym}(X)$; for $X=\{1,\dots,n\}$ this is $S_n$.

## Definitions

- **Bijection** $f:X\to Y$: there is $g:Y\to X$ with $f\circ g=\operatorname{id}_Y$, $g\circ f=\operatorname{id}_X$. Equivalently $f$ is **injective** and **surjective**.
- **Permutation**: a bijection $X\to X$; $\operatorname{Sym}(X)$ = all permutations of $X$; $S_n=\operatorname{Sym}\{1,\dots,n\}$.

→ [[Groups - Chapter 1 Examples and Definitions#Definition 1.9 — Bijection and permutation|lecture]]

## Key results

- **Lemma 1.11.** Composition of functions is associative. → [[Groups - Chapter 1 Examples and Definitions#Lemma 1.11 — Composition is associative|proof]]
- **Lemma 1.12.** $f,f'\in\operatorname{Sym}(X)\Rightarrow f\circ f'\in\operatorname{Sym}(X)$, with inverse $g'\circ g$. → [[Groups - Chapter 1 Examples and Definitions#Lemma 1.12 — Composites of permutations|proof]]
- **Proposition 1.13.** $(\operatorname{Sym}(X),\circ,\operatorname{id}_X)$ is a group.
- **Finite sets.** If $|X|=|Y|<\infty$: bijective $\iff$ injective $\iff$ surjective.

## Pitfalls

- $f\circ g$ means "first $g$, then $f$".
- $f^{-1}$ (inverse function) needs $f$ bijective; it is not $1/f$.

## Related

[[Groups]] · [[Isometries and Dihedral Groups]] · [[Homomorphisms and Isomorphisms]]
