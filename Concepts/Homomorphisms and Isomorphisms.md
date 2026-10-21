---
title: Homomorphisms and Isomorphisms
material_type: concept note
course: Part IA Groups
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: [25, 26, 27, 28, 29, 30]
---

# Homomorphisms and Isomorphisms

A **homomorphism** $\varphi:G\to H$ satisfies
$$\varphi(gg')=\varphi(g)\varphi(g')\qquad(g,g'\in G).$$
Examples are the trivial map $g\mapsto e_H$ and a subgroup inclusion. The map $C_m\to C_n$, $z\mapsto z^{m/n}$ for $n\mid m$ is an assigned exercise.

Lemma 1.29 gives $\varphi(e_G)=e_H$ and $\varphi(g^{-1})=\varphi(g)^{-1}$. The first follows by cancelling in $\varphi(e_G)^2=\varphi(e_G)$; the second follows from $\varphi(g)\varphi(g^{-1})=\varphi(e_G)=e_H$.

A bijective homomorphism is an **isomorphism**; write $G\cong H$. Examples are
$$\mathbb Z_n\cong C_n,\qquad k\mapsto e^{2\pi ik/n},$$
and
$$(\mathbb R,+,0)\cong(\mathbb R_{>0},\times,1),\qquad x\mapsto e^x.$$
In the first example, each residue corresponds to exactly one $n$th root of unity, and addition modulo $n$ corresponds to multiplication. In the second, $e^{x+y}=e^xe^y$ and $\log$ is the inverse.

Lemma 1.31 states that homomorphisms compose, the inverse of an isomorphism is an isomorphism, and $\cong$ is an equivalence relation. The proofs are assigned as an exercise.

## Image and kernel

For $\varphi:G\to H$,
$$\operatorname{Im}(\varphi)=\{\varphi(g):g\in G\},\qquad
\ker(\varphi)=\{g\in G:\varphi(g)=e_H\}.$$
Proposition 1.33 proves $\operatorname{Im}(\varphi)\le H$ and $\ker(\varphi)\le G$ on page 29. The image contains $e_H=\varphi(e_G)$ and is closed under products and inverses because
$$\varphi(g_1)\varphi(g_2)=\varphi(g_1g_2),\qquad
\varphi(g)^{-1}=\varphi(g^{-1}).$$
The kernel contains $e_G$; if $g_1,g_2$ are in it, their product maps to $e_He_H=e_H$, and the inverse of a kernel element maps to $e_H^{-1}=e_H$.

## Injectivity, surjectivity and the kernel

A function $f:X\to Y$ is **injective** when $f(x_1)=f(x_2)$ implies $x_1=x_2$, and **surjective** when every $y\in Y$ equals $f(x)$ for some $x\in X$. For finite sets of equal size, injectivity, surjectivity and bijectivity are equivalent; see [[Bijections and Permutations]].

**Lemma 1.35.** A group homomorphism is injective if and only if $\ker(\varphi)=\{e_G\}$.

If injective, its kernel has only $e_G$, which maps to $e_H$. Conversely, if the kernel is trivial and $\varphi(g_1)=\varphi(g_2)$, then
$$\varphi(g_1g_2^{-1})=\varphi(g_1)\varphi(g_2)^{-1}=e_H.$$
Thus $g_1g_2^{-1}=e_G$ and $g_1=g_2$.

**Corollary 1.36.** A homomorphism is an isomorphism exactly when its image is the whole target and its kernel is trivial. These criteria are used in [[Cyclic Groups and Element Orders]].

See [[Groups - Chapter 1 Examples and Definitions]], pages 25–30. Related: [[Groups]], [[Subgroups and Generated Subgroups]], [[Bijections and Permutations]], [[Roots of Unity]].
