---
title: Proof by Contradiction and Contraposition
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets, logic]
---

# Proof by Contradiction and Contraposition

> [!abstract] In one paragraph
> To prove "if $A$ then $B$", show that $A$ true and $B$ false cannot happen together. This is the same as proving the contrapositive $\neg B\Rightarrow\neg A$. To disprove it, one counterexample ($A$ true, $B$ false) is enough.

## Key facts

- $A\Rightarrow B\iff\neg B\Rightarrow\neg A$. → [[Numbers and Sets - Chapter 0 Proofs#Truth tables|truth table]]
- Proving the **converse** $B\Rightarrow A$ does not prove $A\Rightarrow B$. → [[Numbers and Sets - Chapter 0 Proofs#Assertion — if n squared is even then n is even|wrong proof]]
- An "if and only if" needs both directions; a chain of equivalences works only if **every** step is $\iff$. → [[Numbers and Sets - Chapter 0 Proofs#Assertion — solutions of a quadratic|example]]
- Every claim must be justified — e.g. assuming a least positive real exists. → [[Numbers and Sets - Chapter 0 Proofs#False claim — every positive real is at least 1|example]]

## Examples

- $n^2$ even $\Rightarrow$ $n$ even: if $n=2k+1$ then $n^2=4(k^2+k)+1$ is odd. → [[Numbers and Sets - Chapter 0 Proofs#Assertion — if n squared is even then n is even|proof]]
- $9\mid n^2\Rightarrow9\mid n$ is false: $n=3$.
- Theorem 3 (infinitely many primes) is a proof by contradiction. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 3 — Infinitely many primes|proof]]

## Related

[[Logical Connectives and Quantifiers]] · [[Natural Numbers and Mathematical Induction]]
