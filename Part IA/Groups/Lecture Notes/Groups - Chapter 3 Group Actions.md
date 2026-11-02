---
title: Groups - Chapter 3 Group Actions
course: Part IA Groups
material_type: lecture notes
chapter: 3
source_file: Ch.3 Group Actions.pdf
drive_file_id: 1werwvz7lKsMJXjP5zBK0gBdekRf8jCdb
source_url: https://drive.google.com/file/d/1werwvz7lKsMJXjP5zBK0gBdekRf8jCdb/view
source_pages: 15
tags: [lecture, groups]
---

# Groups — Chapter 3: Group Actions

> [!abstract] Overview
> A group acts on a set by permuting it. An action is the same thing as a homomorphism $G\to\operatorname{Sym}(X)$; this gives Cayley's theorem. Orbits partition $X$, stabilisers are subgroups, and the orbit–stabiliser theorem relates the two. It is used to compute $|G|$ (the symmetry group of the cube) and to prove Cauchy's theorem. Finally, $G$ acting on itself by conjugation gives conjugacy classes, centralisers and the centre.
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
| [[#Corollary 3.7 — Counting with orbits and stabilisers]] | $\lvert G\rvert=\lvert\operatorname{Stab}_G(x)\rvert\cdot\lvert Gx\rvert$ | 9 |
| [[#Example — Symmetries of the cube]] | $\lvert G\rvert=6\cdot8=48$ | 9–10 |
| [[#Theorem 3.8 — Cauchy's theorem]] | prime $p\mid\lvert G\rvert\Rightarrow$ an element of order $p$ | 10–13 |
| [[#Definition 3.9 — Conjugate]] | $hgh^{-1}$; conjugation action $(g,\gamma)\mapsto g\gamma g^{-1}$ | 13 |
| [[#Definition 3.10 — Conjugacy classes]] | orbits of conjugation, $\operatorname{ccl}(g)$; reflections in $D_{2n}$ | 14 |
| [[#Definition 3.11 — Centraliser]] | $C_G(g)=\{h:hgh^{-1}=g\}$, the elements commuting with $g$ | 14 |
| [[#Definition 3.12 — Centre]] | $Z(G)=\bigcap_gC_G(g)$ | 15 |

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

**Proof.** Write $S$ for $\operatorname{Stab}_G(x)$ and define
$$\varphi:G/S\to Gx,\qquad gS\mapsto gx.$$

- *$\varphi$ is well defined.* Suppose $g_1S=g_2S$. Then $g_1=g_2s$ for some $s\in S$, so
$$g_1x=(g_2s)x=g_2(sx)=g_2x,$$
since $s\in S$ fixes $x$.
- *$\varphi$ is surjective.* $\varphi(gS)=gx$ for any $g\in G$, so every point of $Gx$ is hit.
- *$\varphi$ is injective.* Suppose $g_1x=g_2x$. Then
$$g_2^{-1}(g_1x)=g_2^{-1}(g_2x)\ \Rightarrow\ (g_2^{-1}g_1)x=x\ \Rightarrow\ g_2^{-1}g_1\in S\ \Rightarrow\ g_1S=g_2S.$$

> [!note] Explanation
> Two moves $g,g'$ send $x$ to the same point exactly when $g^{-1}g'$ fixes $x$, that is, when $g'=gh$ for some $h\in\operatorname{Stab}_G(x)$. So the moves split into batches (the cosets of $\operatorname{Stab}_G(x)$), and all moves in one batch send $x$ to the same place. Different batches send $x$ to different places, and every place in the orbit is reached. Hence points of the orbit $Gx$ correspond one-to-one to cosets. "Well defined" is the step checking that the rule $gS\mapsto gx$ does not depend on which representative $g$ of the coset was used.

### Corollary 3.7 — Counting with orbits and stabilisers

If $G$ is a group acting on $X$, $x\in X$, and $|G|<\infty$, then
$$|G|=|\operatorname{Stab}_G(x)|\cdot|Gx|.$$

**Proof.** By the orbit–stabiliser theorem and Lagrange,
$$|Gx|=|G/\operatorname{Stab}_G(x)|=\frac{|G|}{|\operatorname{Stab}_G(x)|}.$$

**Example.** $D_{2n}\curvearrowright X_n$ with $x=1$: $|D_{2n}x|=n$ and $|\operatorname{Stab}_G(x)|=2$, and indeed $|D_{2n}|=2n$.

> [!note] Explanation
> Orbit–stabiliser is a counting tool: to find $|G|$ it is enough to find the size of one orbit and the size of one stabiliser, and multiply. Think of the moves of $G$ grouped into batches of $|\operatorname{Stab}_G(x)|$ moves, one batch for each point $x$ can reach; the total number of moves is then (number of batches) $\times$ (batch size).

### Example — Symmetries of the cube

Let $G$ be the group of symmetries of a cube $C$ (reflections in planes, rotations about axes, point reflection). It acts on the set $\operatorname{Vert}(C)$ of vertices, and two vertices $x,y$ are adjacent if they share an edge. (Later, in the viewpoint of isometries, it will be clear why this is a group.)

**Exercise.** $G\cong H\le\operatorname{Sym}(\operatorname{Vert}(C))$, where $H$ is the subgroup of permutations that respect adjacency of vertices.

What is $|G|$? Use orbit–stabiliser. Let $z$ be the centre of a face.
- The orbit $Gz$ is the set of all face centres, so $|Gz|=6$ (e.g. using rotations).
- $\operatorname{Stab}_G(z)$ is the set of symmetries preserving that face, i.e. the symmetries of the square $X_4$. The rotations and reflections of the top face all extend to the whole cube, so $\operatorname{Stab}_G(z)\cong D_8$.

By orbit–stabiliser, $|G|=6\cdot8=48$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,x={(1.1cm,0cm)},y={(0.6cm,0.5cm)},z={(0cm,1.1cm)}]
  \def\a{2.2}
  % left cube: top face with its symmetries
  \begin{scope}
    \fill[red!12] (0,0,\a) -- (\a,0,\a) -- (\a,\a,\a) -- (0,\a,\a) -- cycle;
    \draw (0,0,0) -- (\a,0,0) -- (\a,0,\a) -- (0,0,\a) -- cycle;
    \draw (\a,0,0) -- (\a,\a,0) -- (\a,\a,\a) -- (\a,0,\a);
    \draw (0,0,\a) -- (0,\a,\a) -- (\a,\a,\a);
    \draw[dashed] (0,\a,0) -- (\a,\a,0); \draw[dashed] (0,\a,0) -- (0,\a,\a); \draw[dashed] (0,0,0) -- (0,\a,0);
    % reflection axes of the top face
    \draw[red,dashed] (0,{\a/2},\a) -- (\a,{\a/2},\a);
    \draw[red,dashed] ({\a/2},0,\a) -- ({\a/2},\a,\a);
    \draw[red,dashed] (0,0,\a) -- (\a,\a,\a);
    \draw[red,dashed] (\a,0,\a) -- (0,\a,\a);
    % rotation about z
    \draw[red,thick,->,domain=30:320,samples=40,variable=\t] plot ({\a/2+0.55*cos(\t)},{\a/2+0.55*sin(\t)},\a);
    \fill[red] ({\a/2},{\a/2},\a) circle (1.8pt);
    \node[red,fill=red!12,inner sep=1pt,above right=1pt] at ({\a/2},{\a/2},\a) {$z$};
  \end{scope}
  % right cube: axis through the face centres
  \begin{scope}[xshift=5.6cm]
    \draw (0,0,0) -- (\a,0,0) -- (\a,0,\a) -- (0,0,\a) -- cycle;
    \draw (\a,0,0) -- (\a,\a,0) -- (\a,\a,\a) -- (\a,0,\a);
    \draw (0,0,\a) -- (0,\a,\a) -- (\a,\a,\a);
    \draw[dashed] (0,\a,0) -- (\a,\a,0); \draw[dashed] (0,\a,0) -- (0,\a,\a); \draw[dashed] (0,0,0) -- (0,\a,0);
    \draw[blue,thick] ({\a/2},{\a/2},-0.5) -- ({\a/2},{\a/2},{\a+0.6});
    \fill[blue] ({\a/2},{\a/2},\a) circle (1.8pt);
    \node[blue,right] at ({\a/2},{\a/2},{\a+0.6}) {axis through $z$};
  \end{scope}
\end{tikzpicture}
\end{document}
```
*Left: the top face, with centre $z$, its four reflection axes (dashed) and a rotation about $z$. Right: the axis through the centres of the top and bottom faces; every rotation and reflection of the top face extends to a symmetry of the whole cube.*

### Theorem 3.8 — Cauchy's theorem

If $|G|<\infty$ and $p$ is a prime dividing $|G|$, then there exists $g\in G$ with $\operatorname{ord}(g)=p$.

**Proof.** *Step 0: setup.* Let $X$ be the set
$$X=\{(g_1,\dots,g_p):\ g_i\in G\text{ for all }i,\ g_1\cdot g_2\cdots g_p=e\}\subseteq\underbrace{G\times G\times\cdots\times G}_{p\text{ times}}.$$
Write $C_p=\{1,t,t^2,\dots,t^{p-1}\}$, where $t$ is the name of our generator. *Idea:* use a well-defined action of $C_p$ on $X$.

*Step 1: candidate action.* Define
$$t^k(g_1,\dots,g_p)=(g_{k+1},g_{k+2},\dots,g_p,g_1,\dots,g_k).$$
*Well defined?* We need $t^k(g_1,\dots,g_p)\in X$. From $g_1g_2\cdots g_p=e$,
$$g_1^{-1}g_1g_2\cdots g_p=g_1^{-1}e\ \Rightarrow\ g_2\cdots g_pg_1=g_1^{-1}g_1\ \Rightarrow\ g_2\cdots g_pg_1=e.$$
So inductively $g_{k+1}g_{k+2}\cdots g_pg_1\cdots g_k=e$.

*Action axioms.* $1\cdot(g_1,\dots,g_p)=(g_1,\dots,g_p)$, and $t^k\cdot t^\ell(g_1,\dots,g_p)=t^{k+\ell}(g_1,\dots,g_p)$. So $C_p\curvearrowright X$.

*Step 2: use this action and orbit–stabiliser.* What is $|X|$? Observe $g_p=g_{p-1}^{-1}g_{p-2}^{-1}\cdots g_1^{-1}$. So $g_1,\dots,g_{p-1}$ can be chosen arbitrarily and $g_p$ is then uniquely determined, so
$$|X|=|G|^{p-1}.$$
The action $C_p\curvearrowright X$ partitions $X$ into orbits
$$X=C_px_1\sqcup C_px_2\sqcup\cdots\sqcup C_px_n\qquad(\text{disjoint union, some }n\in\mathbb N).$$
By orbit–stabiliser, for all $i$, $|C_px_i|$ divides $|C_p|=p$, so $|C_px_i|=1$ or $p$. Say there are $\ell$ orbits of size $1$, which after reordering are $C_px_1,\dots,C_px_\ell$, and $n-\ell$ orbits of size $p$. Then
$$|G|^{p-1}=|X|=\sum_{i=1}^n|C_px_i|=\sum_{i=1}^\ell|C_px_i|+\sum_{i=\ell+1}^n|C_px_i|=\ell+(n-\ell)p.$$
As $p\mid|G|$, we must have $p\mid\ell$, so $\ell\ge p\ge2$, i.e. there are at least two orbits of size $1$, provided $\ell\ne0$.

*Step 3: orbits of size $1$.* Observe that $x=(g_1,\dots,g_p)$ has $C_px=\{x\}$ (an orbit of size $1$) if and only if $g_1=g_2=\dots=g_p$.
- $(e,e,\dots,e)\in X$ has an orbit of size $1$, so $\ell\ne0$.
- So $\ell\ge2$, and hence there is at least one other, say $(g,g,\dots,g)\in X$ with $g\ne e$.

By definition of $X$, $g^p=e$, so $\operatorname{ord}(g)\mid p$. Then $\operatorname{ord}(g)=1$ or $p$. As $g\ne e$, we must have $\operatorname{ord}(g)=p$. $\square$

> [!note] Explanation
> *Goal:* find an element of order $p$. *Trick:* look at all $p$-tuples of elements of $G$ whose product is $e$, and cycle the entries (move the first entry to the end). The product stays $e$ because $g_1(g_2\cdots g_p)=e$ forces $g_2\cdots g_p=g_1^{-1}$, so $(g_2\cdots g_p)g_1=e$. *Counting:* choosing $g_1,\dots,g_{p-1}$ freely fixes $g_p$, so $X$ has $|G|^{p-1}$ elements, a multiple of $p$. Every orbit of the cycling action has size $1$ or $p$. The orbits of size $p$ contribute a multiple of $p$ to $|X|$, so the number $\ell$ of size-$1$ orbits is also a multiple of $p$. Since $(e,\dots,e)$ is one such orbit, there must be at least $p-1\ge1$ more, and a tuple fixed by cycling is just $(g,\dots,g)$ with $g^p=e$.

## 3.3 Conjugation

### Definition 3.9 — Conjugate

Let $G$ be a group and $g\in G$. For any $h\in G$, the element
$$h\cdot g\cdot h^{-1}\in G$$
is called the **conjugate** of $g$ by $h$.

**Example.** Suppose $G$ is an abelian group. Then for any $g,h\in G$,
$$h\cdot g\cdot h^{-1}=h\cdot h^{-1}\cdot g=g,$$
so the only conjugate of $g$ is $g$ itself.

**Exercise.** $G$ acts on itself by **conjugation**:
$$G\times G\to G,\qquad(g,\gamma)\mapsto g\gamma g^{-1}.$$
This action is different from the regular action $(g,\gamma)\mapsto g\gamma$.

### Definition 3.10 — Conjugacy classes

The **conjugacy classes** of $G$ are the orbits under the conjugation action, with
$$\operatorname{ccl}(g)=\{h\cdot g\cdot h^{-1}:h\in G\}$$
for the orbit of $g$.

**Example (Example Sheet 2, Q7).** $D_{2n}$ has
- one conjugacy class of reflections if $n$ is odd;
- two conjugacy classes of reflections if $n$ is even.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.1]
  % triangle, n = 3
  \coordinate (A) at (90:1); \coordinate (B) at (210:1); \coordinate (C) at (330:1);
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[blue] (A) -- (0,-0.5); \draw[blue] (B) -- (0.433,0.25); \draw[blue] (C) -- (-0.433,0.25);
  \node at (0,-1.0) {\small$n=3$: one class};
  % square, edge-midpoint axes
  \begin{scope}[xshift=3cm]
    \draw[thick] (-0.8,-0.8) rectangle (0.8,0.8);
    \draw[blue] (0,-0.8) -- (0,0.8); \draw[blue] (-0.8,0) -- (0.8,0);
    \draw[blue,<->] (-0.25,0.5) -- (0.25,0.5); \draw[blue,<->] (0.5,-0.25) -- (0.5,0.25);
  \end{scope}
  % square, diagonal axes
  \begin{scope}[xshift=5.4cm]
    \draw[thick] (-0.8,-0.8) rectangle (0.8,0.8);
    \draw[red] (-0.8,-0.8) -- (0.8,0.8); \draw[red] (-0.8,0.8) -- (0.8,-0.8);
    \draw[red,<->] (-0.55,0.2) -- (-0.2,0.55); \draw[red,<->] (0.2,0.55) -- (0.55,0.2);
  \end{scope}
  \node at (4.2,-1.0) {\small$n=4$: two classes};
\end{tikzpicture}
\end{document}
```
*For $n$ odd every reflection axis joins a vertex to the midpoint of the opposite edge, and all such reflections are conjugate. For $n$ even there are two kinds of axis: through midpoints of opposite edges (blue) and through opposite vertices (red), giving two classes.*

**Slogan #1.** Two group elements are conjugate if and only if they have the same "shape".

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.2]
  % left: s, reflection in the real axis
  \draw[thick] (0,1) -- (-1,0) -- (0,-1) -- (1,0) -- cycle;
  \node[above] at (0,1) {$i$}; \node[left] at (-1,0) {$-1$};
  \node[right] at (1,0) {$1$}; \node[below] at (0,-1) {$-i$};
  \draw[blue,thick] (-1,0) -- (1,0);
  \draw[blue,<->] (0,0.3) -- (0,-0.3);
  \node[blue] at (-0.2,0.35) {$s$};
  % right: rsr^{-1}
  \begin{scope}[xshift=4cm]
    \draw[thick] (0,1) -- (-1,0) -- (0,-1) -- (1,0) -- cycle;
    \node[above] at (0,1) {$r(1)$}; \node[left] at (-1,0) {$r(i)$};
    \node[right] at (1,0) {$r(-i)$}; \node[below] at (0,-1) {$r(-1)$};
    \draw[blue,thick] (0,1) -- (0,-1);
    \draw[blue,<->] (-0.3,0) -- (0.3,0);
    \node at (1.3,0.8) {$rsr^{-1}$};
  \end{scope}
\end{tikzpicture}
\end{document}
```
*Left: $s$ is the reflection in the axis through $1$ and $-1$. Right: the same square with its vertices relabelled by the rotation $r$; $rsr^{-1}$ is the reflection in the axis through $r(1)$ and $r(-1)$.*

**Slogan #2.** $g\cdot f\cdot g^{-1}$ acts as "$f$ with the space relabelled by $g$".

> [!note] Explanation
> To apply $rsr^{-1}$ to the point $r(x)$: first $r^{-1}$ takes it back to $x$, then $s$ moves $x$ to $s(x)$, then $r$ takes this to $r(s(x))$. So $rsr^{-1}$ sends $r(x)\mapsto r(s(x))$: it does what $s$ does, but to the points renamed by $r$. Since $s$ fixes $1$ and $-1$, $rsr^{-1}$ fixes $r(1)$ and $r(-1)$, so it is the reflection in the axis through them. This is why conjugate elements have the same "shape".

### Definition 3.11 — Centraliser

The **centraliser** of $g$ is the stabiliser of $g$ under the conjugation action:
$$C_G(g)=\{h\in G:h\cdot g\cdot h^{-1}=g\}.$$

**Remark.** $h\cdot g\cdot h^{-1}=g\iff h\cdot g=g\cdot h$. So the centraliser of $g$ is exactly the set of elements that commute with $g$.

### Definition 3.12 — Centre

The **centre** of $G$ is
$$Z(G)=\{h\in G:hg=gh\text{ for all }g\in G\}=\bigcap_{g\in G}C_G(g),$$
i.e. the set of elements of $G$ which commute with everything.
