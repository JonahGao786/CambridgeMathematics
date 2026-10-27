---
title: Group Actions
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Group Actions

> [!abstract] In one paragraph
> A group $G$ acts on a set $X$ when each $g$ moves the points of $X$ compatibly with the group operation. Equivalently, each $g$ gives a permutation of $X$ and $g\mapsto$ (that permutation) is a homomorphism $G\to\operatorname{Sym}(X)$.

## Definitions

- **Action** $G\curvearrowright X$: a map $(g,x)\mapsto gx$ with $ex=x$ and $(gh)x=g(hx)$. → [[Groups - Chapter 3 Group Actions#Definition 3.1 — Group action|lecture]]

## Key results

- **Theorem 3.2.** An action of $G$ on $X$ is the same as a homomorphism $\varphi:G\to\operatorname{Sym}(X)$, $\varphi(g)=t_g:x\mapsto gx$. *Idea:* $t_{g^{-1}}$ is inverse to $t_g$, and $t_g\circ t_h=t_{gh}$ by axiom (ii). → [[Groups - Chapter 3 Group Actions#Theorem 3.2 — Actions are homomorphisms to Sym(X)|proof]]

## Examples

- Trivial action; $\operatorname{Sym}(X)$ and its subgroups act on $X$; $\operatorname{Isom}(X)$ acts on $X\subseteq\mathbb C$; $D_{2n}$ acts on the regular $n$-gon and on its vertices $\{z:z^n=1\}$.
- **Regular action:** $G$ acts on itself by $g\gamma=g\cdot\gamma$.

## Related

[[Homomorphisms and Isomorphisms]] · [[Bijections and Permutations]] · [[Isometries and Dihedral Groups]] · [[Groups]]
