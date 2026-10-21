---
title: Bijections and Permutations
material_type: source-backed definitions, lemmas and proofs with supplementary explanation
course: Part IA Groups
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: [13, 14, 15]
---

# Bijections and Permutations

For sets $X,Y$, a **bijection** is a function $f:X\to Y$ with a function $g:Y\to X$ satisfying
$$f\circ g=\operatorname{id}_Y,\qquad g\circ f=\operatorname{id}_X.$$
The function $g$ is the set-theoretic inverse of $f$. Here $\operatorname{id}_Y$ denotes the identity function on $Y$, and
$$(f\circ g)(y)=f(g(y)).$$

A bijection $X\to X$ is a **permutation**.

## Composition and the symmetric group

For a set $X$, $\operatorname{Sym}(X)$ is the set of permutations of $X$ (Definition 1.10).

Composition is associative: for $f:W\to X$, $g:X\to Y$ and $h:Y\to Z$,
$$(h\circ g)\circ f=h\circ(g\circ f),$$
because both sides send $w$ to $h(g(f(w)))$ (Lemma 1.11).

If $f,f'\in\operatorname{Sym}(X)$ have inverses $g,g'$, then
$$(f\circ f')^{-1}=g'\circ g.$$
Both compositions of $f\circ f'$ with $g'\circ g$ equal $\operatorname{id}_X$. Thus composition stays inside $\operatorname{Sym}(X)$ (Lemma 1.12).

Consequently, $(\operatorname{Sym}(X),\circ,\operatorname{id}_X)$ is a [[Groups|group]]: composition is a binary operation, it is associative, and the identity and inverses are supplied by the definitions (Proposition 1.13).

For $X=\{1,\ldots,n\}$, write $S_n=\operatorname{Sym}(X)$ (Definition 1.14). The lecture asks to calculate $|S_n|$; no answer is supplied.

Source: [[Groups - Chapter 1 Examples and Definitions]], pages 13–15, including the map diagram and full proofs. See [[Groups]] for inverses with respect to a group operation.

## Injectivity and surjectivity — supplementary explanation

A function $f:X\to Y$ is **injective** if $f(x)=f(x')$ implies $x=x'$. It is **surjective** if every $y\in Y$ equals $f(x)$ for some $x\in X$. A bijection is equivalently both.

Indeed, an inverse $g$ makes $f(x)=f(x')$ imply $g(f(x))=g(f(x'))$, hence $x=x'$, while $f(g(y))=y$ proves surjectivity. Conversely, if $f$ is injective and surjective, each $y$ has exactly one preimage; defining $g(y)$ to be that preimage gives the two inverse identities.

Composition is read right to left: $f\circ g$ applies $g$ first. The notation $f^{-1}$ for an inverse function requires bijectivity and is not the reciprocal $1/f$. For a general function, $f^{-1}(A)$ may instead denote the **preimage set** $\{x\in X:f(x)\in A\}$, which does not require an inverse function.
