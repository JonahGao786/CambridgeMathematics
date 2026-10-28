---
title: Homomorphisms and Isomorphisms
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Homomorphisms and Isomorphisms

> [!abstract] In one paragraph
> A homomorphism is a map that respects the group operation; an isomorphism is a bijective one, meaning the two groups have the same structure. The kernel measures failure of injectivity: a homomorphism is injective iff its kernel is trivial.

## Definitions

- **Homomorphism** $\varphi:G\to H$: $\varphi(gg')=\varphi(g)\varphi(g')$. **Isomorphism**: bijective homomorphism; $G\cong H$. → [[Groups - Chapter 1 Examples and Definitions#Definition 1.28 — Homomorphism|lecture]]
- $\operatorname{Im}\varphi=\{\varphi(g)\}$, $\ker\varphi=\{g:\varphi(g)=e_H\}$. → [[Groups - Chapter 1 Examples and Definitions#Definition 1.32 — Image and kernel|lecture]]
- **Direct product** $G\times H$ with componentwise operation.

## Key results

- **Lemma 1.29.** $\varphi(e_G)=e_H$, $\varphi(g^{-1})=\varphi(g)^{-1}$.
- **Lemma 1.31.** Composites of homomorphisms are homomorphisms; inverses of isomorphisms are isomorphisms; $\cong$ is an equivalence relation (exercise).
- **Proposition 1.33.** $\operatorname{Im}\varphi\le H$, $\ker\varphi\le G$. → [[Groups - Chapter 1 Examples and Definitions#Proposition 1.33 — Image and kernel are subgroups|proof]]
- **Lemma 1.35.** $\varphi$ injective $\iff\ker\varphi=\{e_G\}$. *Idea:* $\varphi(g_1)=\varphi(g_2)\Rightarrow g_1g_2^{-1}\in\ker\varphi$. → [[Groups - Chapter 1 Examples and Definitions#Lemma 1.35 — Injective iff trivial kernel|proof]]
- **Corollary 1.36.** Isomorphism $\iff$ $\operatorname{Im}\varphi=H$ and $\ker\varphi=\{e_G\}$.

## Examples

- Trivial homomorphism $g\mapsto e_H$; inclusion $H\hookrightarrow G$; $C_m\to C_n$, $z\mapsto z^{m/n}$ ($n\mid m$).
- $\mathbb Z_n\cong C_n$ via $k\mapsto e^{2\pi ik/n}$.
- $(\mathbb R,+)\cong(\mathbb R_{>0},\times)$ via $\exp$.

## Related

[[Groups]] · [[Cyclic Groups and Element Orders]] · [[Subgroups and Generated Subgroups]] · [[Bijections and Permutations]]
