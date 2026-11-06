---
title: Direct Products of Groups
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Direct Products of Groups

> [!abstract] In one paragraph
> $G\times H$ is the set of pairs with componentwise multiplication, of order $|G||H|$. It builds new groups from old, e.g. the Klein four-group $C_2\times C_2$, which is not cyclic. Conversely, the direct product theorem recognises $G\cong H_1\times H_2$ from two commuting subgroups that meet only in $e$ and together give all of $G$.

## Definitions

- **Direct product** $G\times H$: $(g_1,h_1)(g_2,h_2)=(g_1g_2,h_1h_2)$, identity $(e_G,e_H)$, inverse $(g^{-1},h^{-1})$. → [[Groups - Chapter 5 Finite Groups#Definition — Direct product|lecture]]
- **Klein four-group** $K_4=C_2\times C_2$: every element has order dividing $2$, so $K_4\not\cong C_4$. → [[Groups - Chapter 5 Finite Groups#Example — Klein four-group|lecture]]

## Key results

- **Theorem 5.1 — Direct product theorem.** If $H_1\cap H_2=\{e\}$, elements of $H_1$ and $H_2$ commute, and $G=H_1H_2$, then $G\cong H_1\times H_2$. *Idea:* $(h_1,h_2)\mapsto h_1h_2$ is a homomorphism (commuting), onto ($G=H_1H_2$), with trivial kernel ($H_1\cap H_2=\{e\}$). → [[Groups - Chapter 5 Finite Groups#Theorem 5.1 — Direct product theorem|proof]]
- Groups of order $1$, $2$, $3$ are $\{e\}$, $C_2$, $C_3$ (prime order ⇒ cyclic). → [[Cosets and Lagrange's Theorem]]

## Related

[[Groups]] · [[Cyclic Groups and Element Orders]] · [[Homomorphisms and Isomorphisms]] · [[Subgroups and Generated Subgroups]]
