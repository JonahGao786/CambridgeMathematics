---
title: Homomorphisms and Isomorphisms
material_type: source-backed definitions, lemmas, proofs and examples
course: Part IA Groups
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: [25, 26, 27, 28]
---

# Homomorphisms and Isomorphisms

A **homomorphism** $\varphi:G\to H$ satisfies
$$\varphi(gg')=\varphi(g)\varphi(g')\qquad(g,g'\in G).$$
Examples are the trivial map $g\mapsto e_H$ and a subgroup inclusion. The map $C_m\to C_n$, $z\mapsto z^{m/n}$ for $n\mid m$ is an assigned exercise.

Lemma 1.29 gives $\varphi(e_G)=e_H$ and $\varphi(g^{-1})=\varphi(g)^{-1}$. The first follows by cancelling in $\varphi(e_G)^2=\varphi(e_G)$; the second follows from $\varphi(g)\varphi(g^{-1})=\varphi(e_G)=e_H$.

A bijective homomorphism is an **isomorphism**; write $G\cong H$. Source examples are
$$\mathbb Z_n\cong C_n,\qquad k\mapsto e^{2\pi ik/n},$$
and
$$(\mathbb R,+,0)\cong(\mathbb R_{>0},\times,1),\qquad x\mapsto e^x.$$
The source calculates preservation of addition modulo $n$ in the first example, while well-definedness and bijectivity are asserted. In the second, $e^{x+y}=e^xe^y$ and $\log$ is the inverse.

Lemma 1.31 states that homomorphisms compose, the inverse of an isomorphism is an isomorphism, and $\cong$ is an equivalence relation. The proofs are assigned as an exercise.

## Image and kernel

For $\varphi:G\to H$,
$$\operatorname{Im}(\varphi)=\{\varphi(g):g\in G\},\qquad
\ker(\varphi)=\{g\in G:\varphi(g)=e_H\}.$$
Proposition 1.33 states $\operatorname{Im}(\varphi)\le H$ and $\ker(\varphi)\le G$; no proof is supplied.

Source: [[Groups - Chapter 1 Examples and Definitions]], pages 25–28. Related: [[Groups]], [[Subgroups and Generated Subgroups]], [[Bijections and Permutations]], [[Roots of Unity]].
