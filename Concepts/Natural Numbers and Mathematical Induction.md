---
title: Natural Numbers and Mathematical Induction
material_type: concept note
course: Part IA Numbers and Sets
---

# Natural Numbers and Mathematical Induction

The convention in these notes is $\mathbb N=\{1,2,3,\ldots\}$. Write $S(n)=n+1$ for the successor map. The axioms are:

- $1$ is not a successor: $\forall n\in\mathbb N,\ S(n)\ne1$.
- Successor is injective: $\forall m,n\in\mathbb N,\ S(m)=S(n)\Rightarrow m=n$.
- If $P(1)$ and $\forall n\in\mathbb N,\ P(n)\Rightarrow P(S(n))$, then $\forall n\in\mathbb N,\ P(n)$.

Equivalently, injectivity has the contrapositive form $m\ne n\Rightarrow S(m)\ne S(n)$; see [[Proof by Contradiction and Contraposition]].

See [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 1–4.

## Why all three matter

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

## Strong induction

The induction axiom above is **weak induction**. **Strong induction** replaces the step hypothesis $P(n)$ by all earlier cases:
$$P(1),\qquad
\forall n\in\mathbb N:\quad
\bigl(\forall m\le n,\ P(m)\bigr)\Rightarrow P(n+1)
\quad\Longrightarrow\quad\forall n\in\mathbb N,\ P(n).$$
The quantified $m$ are natural numbers.

The two principles are equivalent. Strong induction implies weak induction because it supplies $P(n)$. Conversely, apply weak induction to
$$Q(n):\quad\forall m\le n,\ P(m).$$
Its base case is $P(1)$; its step uses the strong-step hypothesis to add $P(n+1)$ to the preceding cases.

## Well-ordering and least counterexamples

Every non-empty subset of $\mathbb N$ has a least element: the **well-ordering principle**.

Strong induction implies this principle. Suppose a non-empty set has no least element and let $Q(n)$ mean $n$ is not in the set. Then $Q(1)$ holds, or $1$ would be least. If all smaller natural numbers lie outside the set, $n$ must also lie outside it, or $n$ would be least. Strong induction gives $Q(n)$ for every $n$, contradicting non-emptiness.

Thus, when a universal assertion is false, its counterexamples have a least element. A proof can begin with that least counterexample and seek a contradiction.

## Arithmetic and order

Addition and multiplication are commutative and associative, and multiplication distributes over addition. The order relation is defined by
$$a<b\quad\Longleftrightarrow\quad a+c=b\text{ for some }c\in\mathbb N.$$
It asks that these laws be checked rather than supplying their proofs. For the integer extension, $a<b\Rightarrow ac<bc$ requires $c>0$.

For integers, rationals and [[Divisibility and Prime Numbers]], see [[Numbers and Sets - Chapter 1 Elementary Number Theory]].
