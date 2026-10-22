---
title: Logical Connectives and Quantifiers
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets, logic]
---

# Logical Connectives and Quantifiers

> [!abstract] In one paragraph
> Assertions are combined with "and", "or", "not" and "implies"; their truth is decided by truth tables. Quantifiers $\forall$ ("for all") and $\exists$ ("there exists") are negated by swapping them and negating what follows.

## Definitions

| Symbol | Meaning | False exactly when |
| --- | --- | --- |
| $A\land B$ | $A$ and $B$ | at least one is false |
| $A\lor B$ | $A$ or $B$ (inclusive) | both are false |
| $\neg A$ | not $A$ | $A$ is true |
| $A\Rightarrow B$ | if $A$ then $B$ | $A$ true and $B$ false |
| $A\iff B$ | $(A\Rightarrow B)\land(B\Rightarrow A)$ | $A$, $B$ have different truth values |

## Key results

- **De Morgan.** $\neg(A\land B)\iff(\neg A)\lor(\neg B)$. → [[Numbers and Sets - Chapter 0 Proofs#Truth tables|truth table]]
- **Implication.** $A\Rightarrow B\iff(\neg A)\lor B\iff(\neg B)\Rightarrow(\neg A)$ (the **contrapositive**). → [[Numbers and Sets - Chapter 0 Proofs#Truth tables|truth table]]
- **Negating quantifiers.** $\neg(\forall x\ A(x))\iff\exists x\ \neg A(x)$ and $\neg(\exists x\ B(x))\iff\forall x\ \neg B(x)$, over the same domain. → [[Numbers and Sets - Chapter 0 Proofs#Negating quantifiers|lecture]]

## Quantifier order

In $\forall x\ \exists y\ P(x,y)$ the choice of $y$ may depend on $x$; in $\exists y\ \forall x\ P(x,y)$ one $y$ must work for every $x$. Over $\mathbb R$: $\forall x\ \exists y:\ y>x$ is true (take $y=x+1$), but $\exists y\ \forall x:\ y>x$ is false.

To negate a chain, swap every quantifier, keep the order, negate the end:
$$\neg\big(\forall x\ \exists y\ P(x,y)\big)\iff\exists x\ \forall y\ \neg P(x,y).$$

## Pitfalls

- "Or" is inclusive: $A\lor B$ is true when both hold.
- The converse $B\Rightarrow A$ is a different statement from $A\Rightarrow B$.

## Related

[[Proof by Contradiction and Contraposition]] · [[Numbers and Sets - Chapter 0 Proofs]]
