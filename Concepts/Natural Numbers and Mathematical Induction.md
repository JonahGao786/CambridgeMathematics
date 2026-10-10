---
title: Natural Numbers and Mathematical Induction
material_type: source-backed axioms with supplementary explanation
course: Part IA Numbers and Sets
---

# Natural Numbers and Mathematical Induction

The convention in these notes is $\mathbb N=\{1,2,3,\ldots\}$. Write $S(n)=n+1$ for the successor map. The axioms are:

- $1$ is not a successor: $\forall n\in\mathbb N,\ S(n)\ne1$.
- Successor is injective: $\forall m,n\in\mathbb N,\ S(m)=S(n)\Rightarrow m=n$.
- If $P(1)$ and $\forall n\in\mathbb N,\ P(n)\Rightarrow P(S(n))$, then $\forall n\in\mathbb N,\ P(n)$.

The source states injectivity in the equivalent contrapositive form $m\ne n\Rightarrow S(m)\ne S(n)$; see [[Proof by Contradiction and Contraposition]].

Source: [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 1–2.

## Why all three matter — supplementary explanation

The first axiom prevents the successor chain from returning to $1$. Injectivity prevents two earlier entries from merging: any proposed repetition can be reduced, by repeatedly using injectivity, to the impossible assertion that $1$ is a successor.

Those two conditions alone do not rule out extra elements outside the chain beginning at $1$. Induction does: the elements reachable from $1$ contain $1$ and are closed under successor, so they must be all of $\mathbb N$.

In an induction proof:

1. Establish the base case $P(1)$.
2. Fix an **arbitrary** $n\in\mathbb N$ and, assuming $P(n)$, prove $P(n+1)$.
3. Apply the axiom to conclude $\forall n\in\mathbb N,\ P(n)$.

The induction hypothesis is local to the step. It does not assume the final universal conclusion. The step must work for every permitted $n$, including the first step.

## Recursive addition

For each fixed $n\in\mathbb N$, define
$$n+1=S(n),\qquad n+(k+1)=S(n+k)\quad(k\in\mathbb N).$$
Induction on $k$ makes addition by every natural number available. This does not itself assert that arbitrary regroupings of sums are valid; algebraic laws require their own proofs.
