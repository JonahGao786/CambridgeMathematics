---
title: Groups
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Groups

> [!abstract] In one paragraph
> A group is a set with an associative operation, an identity and inverses — the algebra of symmetries. From the (one-sided) axioms one proves that identities and inverses are two-sided and unique, which is what makes cancellation work.

## Definition

$(G,\cdot,e)$ with $\cdot:G\times G\to G$ such that (G1) $(ab)c=a(bc)$; (G2) $ae=a$; (G3) $\forall a\ \exists b:\ ab=e$. **Abelian** if $ab=ba$ for all $a,b$. **Order** $|G|$ = number of elements. → [[Groups - Chapter 1 Examples and Definitions#Definition 1.4 — Group|lecture]]

## Key results

- **Proposition 1.5.** Right inverses are left inverses, $e$ is a left identity, and identity and inverses are unique. → [[Groups - Chapter 1 Examples and Definitions#Proposition 1.5 — Basic properties of groups|proof]]
- **Lemma 1.6 — sock and shoe.** $(ab)^{-1}=b^{-1}a^{-1}$. → [[Groups - Chapter 1 Examples and Definitions#Lemma 1.6 — Sock and shoe lemma|proof]]
- **Powers.** $a^0=e$, $a^n=aa^{n-1}$, $a^{-n}=(a^{-1})^n$; $a^ma^n=a^{m+n}$, $(a^m)^n=a^{mn}$ (exercise).
- **Cancellation.** $ab=ac\Rightarrow b=c$ (multiply on the left by $a^{-1}$); similarly on the right.

## Examples

| Group | Operation | Abelian? |
| --- | --- | --- |
| $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ | $+$ | yes |
| $\mathbb Q^\times,\mathbb R^\times,\mathbb C^\times$ (non-zero) | $\times$ | yes |
| $C_n=\{z:z^n=1\}$ | $\times$ | yes |
| $\mathbb Z_n=\{0,\dots,n-1\}$ | $+_n$ | yes |
| triangle symmetries $\cong D_6$ | composition | no |
| $S_n=\operatorname{Sym}\{1,\dots,n\}$ | composition | no ($n\ge3$) |

Non-examples: $(\mathbb N,+)$; $(\mathbb R,\times)$ ($0$ has no inverse).

## Pitfalls

- Always specify the set **and** the operation. In additive notation $a^{-1}$ is $-a$ and $a^n$ is $na$.
- $ab\ne ba$ in general, so $(ab)^{-1}\ne a^{-1}b^{-1}$ in general.

## Related

[[Subgroups and Generated Subgroups]] · [[Bijections and Permutations]] · [[Homomorphisms and Isomorphisms]] · [[Cyclic Groups and Element Orders]] · [[Isometries and Dihedral Groups]] · [[Latin Squares]] · [[Groups 0 - Handwritten Attempts]]
