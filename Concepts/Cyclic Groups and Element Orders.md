---
title: Cyclic Groups and Element Orders
material_type: concept note
course: Part IA Groups
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: [30, 31, 32]
---

# Cyclic Groups and Element Orders

A group $G$ is **cyclic** if a single element $g$ generates it:
$$G=\langle g\rangle=\{g^k:k\in\mathbb Z\}.$$
Different exponents need not give different elements.

Examples are $C_n$ with generator $e^{2\pi i/n}$, the additive group $\mathbb Z_n$ with generator $1$ modulo $n$, the trivial group, and the additive group $\mathbb Z$ with generator $1$.

## Classification of cyclic groups

**Theorem 1.38.** Every cyclic group is isomorphic to $C_n$ for some $n\in\mathbb N$, or to $\mathbb Z$.

Let $g$ generate $G$ and consider
$$S=\{k\in\mathbb N:g^k=e_G\}.$$

If $S$ is empty, the map
$$\varphi:\mathbb Z\to G,\qquad k\mapsto g^k$$
is a homomorphism by the power law and is surjective by generation. A non-zero kernel element can be replaced by its negative to give a positive $k$ with $g^k=e_G$, a contradiction. The kernel is therefore $\{0\}$, and the [[Homomorphisms and Isomorphisms|kernel criterion]] makes $\varphi$ an isomorphism.

If $S$ is non-empty, let $n=\min S$. Define
$$\varphi:\mathbb Z_n\to G,\qquad k\mapsto g^k.$$
Writing $k+\ell=qn+(k+_n\ell)$ and using $g^n=e_G$ proves preservation of the operation. Every integer exponent can be divided as $k=nq+r$, $0\le r<n$, giving $g^k=g^r$ and hence surjectivity. A kernel element $0\le k<n$ must be $0$ by minimality of $n$, so the map is injective. Thus $G\cong\mathbb Z_n\cong C_n$.

## Order of an element

For any $g$ in any group $G$, its [[Subgroups and Generated Subgroups|generated subgroup]]
$$\langle g\rangle=\{g^k:k\in\mathbb Z\}\le G$$
is cyclic. The **order** of $g$ is
$$o(g)=|\langle g\rangle|.$$
If finite, it is the least positive integer $n$ with $g^n=e_G$, and $\langle g\rangle\cong C_n$. If no positive power is the identity, $o(g)=\infty$ and $\langle g\rangle\cong\mathbb Z$.

See [[Groups - Chapter 1 Examples and Definitions]], pages 30–32. Related: [[Groups]], [[Roots of Unity]], [[Modular Arithmetic]].
