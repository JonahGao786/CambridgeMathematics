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

> [!note] Explanation
> Think of each element $g$ as a move that shuffles the points of $X$: the point $x$ is sent to $gx$. Axiom (i) says the identity move does nothing. Axiom (ii) says doing $h$ first and then $g$ is the same as doing the single move $g\cdot h$. Example: the rotation $r$ of a triangle acts on the vertices $1,2,3$ by sending each vertex to the next one; $r\cdot r$ then sends each vertex two steps on.

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

> [!note] Explanation
> $t_g$ is "the shuffle of $X$ performed by $g$". It is a permutation because the move $g$ can be undone by $g^{-1}$. Axiom (ii) says exactly that performing $h$ then $g$ equals performing $g\cdot h$, i.e. $t_g\circ t_h=t_{gh}$, which is the condition for $g\mapsto t_g$ to be a homomorphism. Conversely a homomorphism $G\to\operatorname{Sym}(X)$ assigns a shuffle to each $g$, and that is an action. So an action and a homomorphism to $\operatorname{Sym}(X)$ are two descriptions of the same thing.

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

> [!note] Explanation
> Cayley's theorem says every abstract group is secretly a group of permutations. The permutations come from letting $G$ act on itself: $g$ shuffles the elements of $G$ by $\gamma\mapsto g\gamma$. Different $g$ give different shuffles (if $g\gamma=\gamma$ for one $\gamma$ then $g=e$), so nothing is lost and $G$ appears as a subgroup of $\operatorname{Sym}(G)$. Example: $C_3=\{1,\omega,\omega^2\}$ with $\omega=e^{2\pi i/3}$. The element $\omega$ acts by $1\mapsto\omega\mapsto\omega^2\mapsto1$, a $3$-cycle, and $\omega^2$ by the inverse $3$-cycle, so $C_3$ is the subgroup of $S_3$ generated by a $3$-cycle.

## 3.2 Orbits and stabilisers

### Definition 3.4 — Orbits and stabilisers

Let $G\curvearrowright X$ and $x\in X$.

1. The **orbit** of $x$ is $Gx=\{y\in X:\ y=gx\text{ for some }g\in G\}\subseteq X$.
2. The **stabiliser** of $x$ is $\operatorname{Stab}_G(x)=\{g\in G:\ gx=x\}\subseteq G$.

If $Gx=X$, we say $G$ acts **transitively** on $X$ (the action is transitive). If for every $g\in G$ with $g\ne e$ there exists $x\in X$ with $gx\ne x$, the action $G\curvearrowright X$ is called **faithful**.

> [!note] Explanation
> The orbit $Gx$ is the set of all places the point $x$ can be moved to. The stabiliser $\operatorname{Stab}_G(x)$ is the set of moves that leave $x$ where it is. The action is *transitive* if every point can be moved to every other point, and *faithful* if every $g\ne e$ really moves some point (no non-trivial element acts as "do nothing"). Example: $D_{12}$ acting on the $6$ vertices of a hexagon is transitive (rotations carry one vertex to any other) and faithful (a non-trivial symmetry of a hexagon cannot fix all vertices).

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

> [!note] Explanation
> (i) Moves that fix $x$ can be combined (do one fixing $x$, then another: $x$ stays put) and undone (the inverse of a move fixing $x$ also fixes $x$), so they form a subgroup. (ii) "Lying in the same orbit" is like "lying in the same coset": it splits $X$ into disjoint pieces. For the trivial action every point is its own orbit; for a transitive action there is a single orbit, $X$ itself.

(ii) As in the proof of Lemma 2.3 ([[Groups - Chapter 2 Lagrange's Theorem#Lemma 2.3 — Cosets partition the group|cosets partition the group]]). Since $x=ex\in Gx$, the orbits cover $X$. Suppose $Gx_1\cap Gx_2\ne\varnothing$ for some $x_1,x_2\in X$. Then $g_1x_1=g_2x_2$ for some $g_1,g_2\in G$, so $x_1=(g_1^{-1}g_2)x_2$. Hence for every $g\in G$,
$$gx_1=(g\cdot g_1^{-1}\cdot g_2)x_2,$$
so $Gx_1\subseteq Gx_2$. By symmetry (swapping $x_1,x_2$), $Gx_2\subseteq Gx_1$. So $Gx_1=Gx_2$.

**Example.** $D_{2n}\curvearrowright X_n$ with $x=1$: $\operatorname{Stab}_{D_{2n}}(x)=\{e,s\}$ (by symmetry, of size $2$), and $Gx=\{e^{2\pi ik/n}:k=0,\dots,n-1\}$, of size $n$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \foreach \k in {0,...,5} {
    \coordinate (v\k) at ({60*\k+90}:1.4);
  }
  \draw[thick] (v0) -- (v1) -- (v2) -- (v3) -- (v4) -- (v5) -- cycle;
  \draw[red,dashed] (0,1.8) -- (0,-1.8);
  \fill[red] (v0) circle (2.5pt) node[above right] {$x=1$};
  \node[red,below] at (0,-1.8) {axis of $s$};
\end{tikzpicture}
\end{document}
```
*$D_{12}$ acting on the vertices of the hexagon $X_6$: the vertex $x=1$ is fixed by $e$ and the reflection $s$ in the dashed axis (stabiliser of size $2$), and moved to every vertex by the rotations (orbit of size $6$). The picture is rotated so that $x$ is at the top.*

### Theorem 3.6 — Orbit-stabiliser theorem

Suppose $G\curvearrowright X$ and let $x\in X$. The assignment
$$g\operatorname{Stab}_G(x)\longmapsto gx$$
(where $g\operatorname{Stab}_G(x)$ is a coset of $\operatorname{Stab}_G(x)\le G$) gives a well-defined bijection
$$G/\operatorname{Stab}_G(x)\longrightarrow Gx,$$
where $G/\operatorname{Stab}_G(x)$ is the set of all cosets. *Well-defined* means that the rule assigns a unique image to each element: the value $gx$ must not depend on the choice of representative $g$ of the coset.

> [!note] Explanation
> Two moves $g,g'$ send $x$ to the same point exactly when $g^{-1}g'$ fixes $x$, that is, when $g'=gh$ for some $h\in\operatorname{Stab}_G(x)$, so $g$ and $g'$ lie in the same coset of $\operatorname{Stab}_G(x)$. So each point of the orbit $Gx$ corresponds to exactly one coset of $\operatorname{Stab}_G(x)$. For finite $G$, counting with Lagrange gives $|Gx|\cdot|\operatorname{Stab}_G(x)|=|G|$. Check on the hexagon: orbit of size $6$, stabiliser of size $2$, and $6\cdot2=12=|D_{12}|$.

> [!todo] Proof of Theorem 3.6 missing (p. 8).
