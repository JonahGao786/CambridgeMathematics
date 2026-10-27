---
title: Groups - Chapter 3 Group Actions
course: Part IA Groups
material_type: lecture notes
chapter: 3
source_file: Ch.3 Group Actions.pdf
drive_file_id: 1werwvz7lKsMJXjP5zBK0gBdekRf8jCdb
source_url: https://drive.google.com/file/d/1werwvz7lKsMJXjP5zBK0gBdekRf8jCdb/view
source_pages: 3
tags: [lecture, groups]
---

# Groups — Chapter 3: Group Actions

> [!abstract] Overview
> A group acts on a set by permuting it. An action is the same thing as a homomorphism $G\to\operatorname{Sym}(X)$.
> Prerequisites: [[Groups - Chapter 1 Examples and Definitions]] (homomorphisms, $\operatorname{Sym}(X)$, dihedral groups).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition 3.1 — Group action]] | $G\times X\to X$ with $ex=x$, $(gh)x=g(hx)$; examples | 1–2 |
| [[#Theorem 3.2 — Actions are homomorphisms to Sym(X)]] | action $\leftrightarrow$ homomorphism $G\to\operatorname{Sym}(X)$ | 2–3 |

## 3.1 Actions

### Definition 3.1 — Group action

An **action** of a group $G$ on a set $X$ is a function
$$G\times X\to X,\qquad(g,x)\mapsto gx\in X\quad(\text{no dot}),$$
such that

1. $ex=x$ for all $x\in X$;
2. $(g\cdot h)x=g(hx)$ for all $g,h\in G$, $x\in X$.

We write $G\curvearrowright X$ to indicate that $G$ acts on $X$.

**Examples.**
1. **Trivial action.** For any group $G$ and set $X$, $gx=x$ for all $g\in G$, $x\in X$.
2. $\operatorname{Sym}(X)$ acts on $X$ via $fx=f(x)$ for $f\in\operatorname{Sym}(X)$ (left: group action notation; right: function notation). Any subgroup $H\le\operatorname{Sym}(X)$ also acts on $X$.
3. For $X\subseteq\mathbb C$, $\operatorname{Isom}(X)$ acts on $X$ in the same way.
4. Special case of 3: $D_{2n}$ acts on $X_n$, the regular $n$-gon, and on the vertices of $X_n$, i.e. $\{z\in\mathbb C:z^n=1\}$.
5. **Regular action.** Every group $G$ acts on itself ($X=G$) via $g\gamma=g\cdot\gamma$ for all $g\in G$, $\gamma\in X=G$ (left side: action, right side: the group operation).

### Theorem 3.2 — Actions are homomorphisms to Sym(X)

An action of a group $G$ on a set $X$ is the same as a homomorphism $\varphi:G\to\operatorname{Sym}(X)$: there is a one-to-one way of going between the two.

**Proof.** ($\Rightarrow$) *An action determines a homomorphism.* If $G\curvearrowright X$, consider, for $g\in G$,
$$t_g:X\to X,\qquad x\mapsto gx.$$
Is $t_g$ a permutation? We need a set-theoretic inverse; guess $t_{g^{-1}}$:
$$t_{g^{-1}}(t_gx)=t_{g^{-1}}(gx)=g^{-1}(gx)=(g^{-1}\cdot g)x=ex=x\quad\text{for all }x\in X,$$
using action axioms (ii) and (i). So $t_{g^{-1}}\circ t_g=\mathrm{id}_X$; similarly $t_g\circ t_{g^{-1}}=\mathrm{id}_X$. So $t_g\in\operatorname{Sym}(X)$.

This gives a function $\varphi:G\to\operatorname{Sym}(X)$, $g\mapsto t_g$. It is a homomorphism: for $g,h\in G$, $x\in X$,
$$(t_g\circ t_h)(x)=t_g(hx)=g(hx)=(g\cdot h)x=t_{g\cdot h}(x).$$
As this holds for all $x\in X$, $t_g\circ t_h=t_{g\cdot h}$, so $\varphi(g)\cdot\varphi(h)=\varphi(g\cdot h)$.

> [!todo] Converse direction (a homomorphism $G\to\operatorname{Sym}(X)$ gives an action) missing, p. 3.
