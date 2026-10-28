---
title: Groups - Chapter 3 Group Actions
course: Part IA Groups
material_type: lecture notes
chapter: 3
source_file: Ch.3 Group Actions.pdf
drive_file_id: 1werwvz7lKsMJXjP5zBK0gBdekRf8jCdb
source_url: https://drive.google.com/file/d/1werwvz7lKsMJXjP5zBK0gBdekRf8jCdb/view
source_pages: 8
tags: [lecture, groups]
---

# Groups — Chapter 3: Group Actions

> [!abstract] Overview
> A group acts on a set by permuting it. An action is the same thing as a homomorphism $G\to\operatorname{Sym}(X)$; this gives Cayley's theorem. Orbits partition $X$, stabilisers are subgroups, and the orbit–stabiliser theorem relates the two.
> Prerequisites: [[Groups - Chapter 1 Examples and Definitions]] (homomorphisms, $\operatorname{Sym}(X)$, dihedral groups).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition 3.1 — Group action]] | $G\times X\to X$ with $ex=x$, $(gh)x=g(hx)$; examples | 1–2 |
| [[#Theorem 3.2 — Actions are homomorphisms to Sym(X)]] | action $\leftrightarrow$ homomorphism $G\to\operatorname{Sym}(X)$ | 2–3 |
| [[#Theorem 3.3 — Cayley's theorem]] | every group embeds in some $\operatorname{Sym}(X)$ | 4 |
| [[#Definition 3.4 — Orbits and stabilisers]] | $Gx$, $\operatorname{Stab}_G(x)$; transitive, faithful | 5 |
| [[#Proposition 3.5 — Stabilisers are subgroups, orbits partition X]] | $\operatorname{Stab}_G(x)\le G$; orbits partition $X$ | 5–7 |
| [[#Theorem 3.6 — Orbit-stabiliser theorem]] | $G/\operatorname{Stab}_G(x)\to Gx$ is a bijection | 8 |

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

($\Leftarrow$) *A homomorphism determines an action.* Suppose we are given a homomorphism $\varphi:G\to\operatorname{Sym}(X)$. The candidate action is
$$G\times X\to X,\qquad(g,x)\mapsto gx:=\varphi(g)(x).$$
We check the axioms.

1. $ex=\varphi(e)(x)=\mathrm{id}_X(x)=x$.
2. For $g,h\in G$,
$$\begin{aligned}
(g\cdot h)x&=\varphi(g\cdot h)(x)\\
&=(\varphi(g)\cdot\varphi(h))(x)\\
&=\varphi(g)\big(\varphi(h)(x)\big)\\
&=\varphi(g)(hx)\\
&=g(hx).
\end{aligned}$$

### Theorem 3.3 — Cayley's theorem

Every group $G$ is isomorphic to a subgroup of some symmetric group $\operatorname{Sym}(X)$. Furthermore, if $G$ is finite, then $X$ can also be taken finite ($X$ depends on $G$).

**Proof.** Let $X=G$ and consider the regular action $G\curvearrowright X=G$, $g\gamma=g\cdot\gamma$. By Theorem 3.2 this is equivalent to a homomorphism $\varphi:G\to\operatorname{Sym}(X)$. Let $H=\operatorname{Im}\varphi\le\operatorname{Sym}(X)$. Then $\varphi$ restricts to a homomorphism $G\to H$, which is surjective by construction.

*Claim: $\ker\varphi=\{e\}$.* Indeed
$$g\in\ker\varphi\iff\varphi(g)=\mathrm{id}_G\iff g\gamma=\gamma\ \text{ for all }\gamma\in G\ \Rightarrow\ ge=e\ \Rightarrow\ g=e.$$

Thus $\varphi:G\to H$ is an isomorphism. For the last part: since $X=G$, $|X|<\infty$ whenever $|G|<\infty$.

## 3.2 Orbits and stabilisers

### Definition 3.4 — Orbits and stabilisers

Let $G\curvearrowright X$ and $x\in X$.

1. The **orbit** of $x$ is $Gx=\{y\in X:\ y=gx\text{ for some }g\in G\}\subseteq X$.
2. The **stabiliser** of $x$ is $\operatorname{Stab}_G(x)=\{g\in G:\ gx=x\}\subseteq G$.

If $Gx=X$, we say $G$ acts **transitively** on $X$ (the action is transitive). If for every $g\in G$ with $g\ne e$ there exists $x\in X$ with $gx\ne x$, the action $G\curvearrowright X$ is called **faithful**.

**Exercise.** $G\curvearrowright X$ is faithful iff the associated homomorphism $G\to\operatorname{Sym}(X)$ is injective.

### Proposition 3.5 — Stabilisers are subgroups, orbits partition X

Suppose $G\curvearrowright X$.

1. For any $x\in X$, $\operatorname{Stab}_G(x)\le G$.
2. The orbits $\{Gx:x\in X\}$ partition $X$, i.e. $X=\bigcup_{x\in X}Gx$, and $Gx\cap Gy\ne\varnothing\Rightarrow Gx=Gy$.

**Proof.** (i) $e\in\operatorname{Stab}_G(x)$. If $g,h\in\operatorname{Stab}_G(x)$ then
$$(g\cdot h)x=g(hx)=gx=x,$$
using the definition of an action, then $h\in\operatorname{Stab}_G(x)$, then $g\in\operatorname{Stab}_G(x)$. So $g\cdot h\in\operatorname{Stab}_G(x)$. If $g\in\operatorname{Stab}_G(x)$, then
$$g^{-1}x=g^{-1}(gx)=(g^{-1}g)x=ex=x,$$
using $gx=x$. So $g^{-1}\in\operatorname{Stab}_G(x)$. Thus $\operatorname{Stab}_G(x)\le G$.

(ii) As in the proof of Lemma 2.3 ([[Groups - Chapter 2 Lagrange's Theorem#Lemma 2.3 — Cosets partition the group|cosets partition the group]]). Since $x=ex\in Gx$, the orbits cover $X$. Suppose $Gx_1\cap Gx_2\ne\varnothing$ for some $x_1,x_2\in X$. Then $g_1x_1=g_2x_2$ for some $g_1,g_2\in G$, so $x_1=(g_1^{-1}g_2)x_2$. Hence for every $g\in G$,
$$gx_1=(g\cdot g_1^{-1}\cdot g_2)x_2,$$
so $Gx_1\subseteq Gx_2$. By symmetry (swapping $x_1,x_2$), $Gx_2\subseteq Gx_1$. So $Gx_1=Gx_2$.

**Example.** $D_{2n}\curvearrowright X_n$ with $x=1$: $\operatorname{Stab}_{D_{2n}}(x)=\{e,s\}$ (by symmetry, of size $2$), and $Gx=\{e^{2\pi ik/n}:k=0,\dots,n-1\}$, of size $n$.

### Theorem 3.6 — Orbit-stabiliser theorem

Suppose $G\curvearrowright X$ and let $x\in X$. The assignment
$$g\operatorname{Stab}_G(x)\longmapsto gx$$
(where $g\operatorname{Stab}_G(x)$ is a coset of $\operatorname{Stab}_G(x)\le G$) gives a well-defined bijection
$$G/\operatorname{Stab}_G(x)\longrightarrow Gx.$$

> [!todo] Proof of Theorem 3.6 missing (p. 8).
