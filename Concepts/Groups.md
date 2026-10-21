---
title: Groups
material_type: concept note
course: Part IA Groups
---

# Groups

A group is a triple $(G,\cdot,e)$ with a binary operation $\cdot:G\times G\to G$ and $e\in G$ satisfying:

- $(a\cdot b)\cdot c=a\cdot(b\cdot c)$ for all $a,b,c\in G$.
- $a\cdot e=a$ for every $a\in G$.
- For every $a\in G$, there is a $b\in G$ with $a\cdot b=e$.

This is the right-sided definition used in the lecture. Proposition 1.5 proves that $e\cdot a=a$ and $b\cdot a=e$ also hold, and that the identity and inverses are unique. The complete proofs appear in [[Groups - Chapter 1 Examples and Definitions]], pages 7–9.

The six symmetries of an equilateral triangle form a group under composition. The rotation/reflection examples show that a group need not be commutative.

## Inverses and powers

Write $a^{-1}$ for the unique inverse of $a$. The **sock and shoe lemma** is
$$(ab)^{-1}=b^{-1}a^{-1}.$$
Its proof verifies $ab(b^{-1}a^{-1})=e$ by associativity and uses uniqueness of inverses.

Integer powers are defined by
$$a^0=e,\qquad a^n=aa^{n-1}\ (n>0),\qquad
a^n=(a^{-1})^{-n}\ (n<0).$$
The lecture asks as an exercise to prove $a^ma^n=a^{m+n}$ and $(a^m)^n=a^{mn}$ for $m,n\in\mathbb Z$.

## Abelian and finite groups

A group is **abelian** if $ab=ba$ for all $a,b\in G$. The one-element group $\{e\}$ is the **trivial group**. The **order** is $|G|$, and a group is finite if $|G|<\infty$.

The additive groups of $\mathbb Z,\mathbb Q,\mathbb R,\mathbb C$ are abelian, with inverse $-x$. The non-zero elements of $\mathbb Q,\mathbb R,\mathbb C$ form abelian groups under multiplication. All of $\mathbb R$ does not form a multiplicative group, since $0$ has no inverse.

**Exercise.** Verify the group axioms for the multiplicative group $C_n=\{z\in\mathbb C:z^n=1\}$ of [[Roots of Unity|roots of unity]] and addition modulo $n$ on $\mathbb Z_n=\{0,\ldots,n-1\}$. [[Bijections and Permutations]] introduces the set-theoretic inverse of a function.

## Symmetric groups and subgroups

For every set $X$, $(\operatorname{Sym}(X),\circ,\operatorname{id}_X)$ is a group. [[Bijections and Permutations]] records the composition and inverse lemmas used in the proof.

A subset $H\subseteq G$ is a subgroup if it contains $e_G$ and is closed under the operation and inverses. [[Subgroups and Generated Subgroups]] records the examples, the classification $H=n\mathbb Z$ for subgroups of the additive integers, and the intersection definition of $\langle X\rangle$.

## Geometric groups

For $X\subseteq\mathbb C$, distance-preserving bijections form a subgroup $\operatorname{Isom}(X)\le\operatorname{Sym}(X)$. For a regular $n$-gon $X_n$, $D_{2n}=\operatorname{Isom}(X_n)$ is the dihedral group. [[Isometries and Dihedral Groups]] records the rotations and reflections, the kite and three point lemmas, and the classification using preservation of corners and adjacency.

## Products and structure-preserving maps

The direct product $G\times H$ has componentwise operation $(g_1,h_1)(g_2,h_2)=(g_1g_2,h_1h_2)$ and identity $(e_G,e_H)$; verifying the group axioms is an exercise. [[Homomorphisms and Isomorphisms]] records maps preserving the operation, bijective such maps, the examples $\mathbb Z_n\cong C_n$ and $(\mathbb R,+)\cong(\mathbb R_{>0},\times)$, the image/kernel subgroup proofs, and the criterion that injectivity is equivalent to a trivial kernel.

## Cyclic groups and element orders

A group is cyclic if $G=\{g^k:k\in\mathbb Z\}$ for some generator $g$. [[Cyclic Groups and Element Orders]] gives the classification: $G\cong C_n$ for some positive integer $n$, or $G\cong\mathbb Z$. For any element $g$ of any group, $o(g)=|\langle g\rangle|$ is its order; if finite, it is the least positive exponent with $g^n=e_G$.

See [[Groups - Chapter 1 Examples and Definitions]], pages 5–33, with symmetry diagrams on pages 1–4. Related examples and attempts: [[Groups 0 - Handwritten Attempts]]. Finite group tables are [[Latin Squares|Latin squares]].

## Cancellation and the chosen operation

If $ab=ac$, multiply on the left by $a^{-1}$ to obtain $b=c$; if $ba=ca$, multiply on the right. Associativity and inverses justify cancellation. Closure or the existence of an identity alone does not. This is the step used in [[Latin Squares]] and in many subgroup arguments.

Always specify the set and operation. In an additive group, $a^{-1}$ in abstract multiplicative notation corresponds to $-a$, and $a^n$ corresponds to $na$. A collection of singular matrices can be a group with its own identity matrix for that collection; see question 5 of [[Groups 0 - Handwritten Attempts]].
