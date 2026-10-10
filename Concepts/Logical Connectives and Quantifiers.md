---
title: Logical Connectives and Quantifiers
material_type: source-backed definitions with supplementary explanation
course: Part IA Numbers and Sets
---

# Logical Connectives and Quantifiers

For assertions $A,B$:

- $A\land B$ means both are true.
- $A\lor B$ means at least one is true, including the case when both are true.
- $\neg A$ means $A$ is false.
- $A\Rightarrow B$ fails exactly when $A$ is true and $B$ is false.
- $A\Longleftrightarrow B$ means $(A\Rightarrow B)\land(B\Rightarrow A)$.

The lecture writes $A\cup B$ for logical “or”. These notes use the conventional $\lor$ to distinguish it from set union.

$$A\Rightarrow B\quad\Longleftrightarrow\quad(\neg A)\lor B
\quad\Longleftrightarrow\quad\neg B\Rightarrow\neg A.$$
See [[Proof by Contradiction and Contraposition]].

For a fixed domain $D$,
$$
\begin{aligned}
\neg\bigl(\forall x\in D,\ A(x)\bigr)
&\Longleftrightarrow\exists x\in D,\ \neg A(x),\\
\neg\bigl(\exists x\in D,\ B(x)\bigr)
&\Longleftrightarrow\forall x\in D,\ \neg B(x).
\end{aligned}
$$
Also, $\neg(A\land B)\Longleftrightarrow(\neg A)\lor(\neg B)$.

Source: [[Numbers and Sets - Chapter 0 Proofs]], pages 6 and 8–9.

## Quantifier order — supplementary explanation

In $\forall x\,\exists y\,P(x,y)$, the choice of $y$ may depend on $x$. In $\exists y\,\forall x\,P(x,y)$, one $y$ must work for every $x$.

For example, over $\mathbb R$,
$$\forall x\in\mathbb R\ \exists y\in\mathbb R:\ y>x$$
is true: choose $y=x+1$. But
$$\exists y\in\mathbb R\ \forall x\in\mathbb R:\ y>x$$
is false: for any proposed $y$, take $x=y+1$.

When negating a sequence of quantifiers, reverse each $\forall$ and $\exists$, keep their order and domains, and negate the final condition:
$$
\neg\bigl(\forall x\in D\ \exists y\in E:\ P(x,y)\bigr)
\Longleftrightarrow
\exists x\in D\ \forall y\in E:\ \neg P(x,y).
$$
This is the same rule used to negate the definition of a limit in [[Limits, Big O and Little o - A First-Year Guide]]. It also explains why a single counterexample disproves a universally quantified assertion.
