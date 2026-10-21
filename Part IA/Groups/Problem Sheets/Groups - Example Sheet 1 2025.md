---
title: Groups - Example Sheet 1 2025
material_type: printed example sheet, questions only
course: Part IA Groups
date: Michaelmas 2025
source_file: Groups 1 Q.pdf
drive_file_id: 1Vp2N13TFa7SxBgqgdt30Mww17EvcjzE-
source_url: https://drive.google.com/file/d/1Vp2N13TFa7SxBgqgdt30Mww17EvcjzE-/view
source_pages: 2
source_contact: hjrw2@cam.ac.uk
---

# IA Groups — Example Sheet 1

**Michaelmas 2025.** Contact printed on the sheet: `hjrw2@cam.ac.uk`.

Questions marked \* are more challenging. Questions 1–11 are on page 1; questions 12–14 are on page 2.

## 1. Idempotent elements (page 1)

Let $G$ be any group. Show that the identity $e$ is the only element $g\in G$ satisfying
$$g^2=g.$$

## 2. Intersections and unions of subgroups (page 1)

Let $H$ and $K$ be two subgroups of a group $G$. Show that $H\cap K$ is a subgroup of $G$.

Show that $H\cup K$ is a subgroup of $G$ if and only if either $H\subseteq K$ or $K\subseteq H$.

## 3. A binary operation on real numbers (page 1)

Let $G=\mathbb R\setminus\{-1\}$ and define
$$x*y=x+y+xy,$$
where $xy$ denotes the usual product of two real numbers. Show that $(G,*,0)$ is a group.

What is the inverse of $2$ in this group? Solve
$$2*x*5=6.$$

## 4. Powers in a finite group (page 1)

Let $G$ be a finite group.

**(a)** Let $g\in G$. Show from first principles that there is a positive integer $n$ such that $g^n=e$. The least such $n$ is called the **order of $g$**.

**(b)** Show from first principles that there is a positive integer $N$ such that $g^N=e$ for every $g\in G$.

## 5. A finite multiplicatively closed set (page 1)

Let $S$ be a finite, non-empty set of non-zero complex numbers which is closed under multiplication. Show that
$$S\subseteq\{z\in\mathbb C:|z|=1\}.$$

Show that $S$ is a group with respect to multiplication, and deduce that $S$ is the set of $n$th roots of unity for some $n\in\mathbb N$; that is,
$$S=\{e^{2\pi i k/n}:k=0,1,\ldots,n-1\}.$$

## 6. An infinite group with finite-order elements (page 1)

Show that
$$G=\{e^{\pi i t}:t\in\mathbb Q\}$$
is a group under multiplication. Show that $G$ is infinite, but that every element of $G$ has finite order.

**Challenging part (\*):** Does $G$ have an infinite, proper subgroup?

## 7. Orders under a homomorphism (page 1)

Let $f:G\to H$ be a group homomorphism, and let $g\in G$ have finite order. Show that the order of $f(g)$ is finite and divides the order of $g$.

## 8. Subgroups of cyclic groups (page 1)

Show that any subgroup of a cyclic group is cyclic.

## 9. Generators and homomorphisms (page 1)

Let $G$ be a group and $X\subseteq G$.

**(a)** Prove that
$$\langle X\rangle=
\{x_1^{\varepsilon_1}x_2^{\varepsilon_2}\cdots x_n^{\varepsilon_n}:
n\ge0,\ x_1,\ldots,x_n\in X,\ \varepsilon_1,\ldots,\varepsilon_n\in\{-1,1\}\}.$$
The product of $0$ elements of $G$ is interpreted as the identity element.

**(b)** Now suppose $G=\langle X\rangle$ and $\phi,\psi:G\to K$ are both homomorphisms. Prove that, if $\phi(x)=\psi(x)$ for every $x\in X$, then $\phi=\psi$.

## 10. Homomorphisms involving cyclic and dihedral groups (page 1)

Let $C_n$ be the cyclic group with $n$ elements and $D_{2n}$ the group of symmetries of the regular $n$-gon.

If $n$ is odd and $\theta:D_{2n}\to C_n$ is a homomorphism, show that $\theta(g)=e$ for every $g\in D_{2n}$.

Can you find all homomorphisms $D_{2n}\to C_n$ if $n$ is even?

Prove that the homomorphisms $C_n\to C_m$ correspond to the elements $x\in C_m$ satisfying $x^n=e$.

## 11. Groups whose non-identity elements have order two (page 1)

Let $G$ be a group in which every element other than the identity has order two. Show that $G$ is abelian.

Show also that, if $G$ is finite, then $|G|$ is a power of $2$.

**Hint:** Consider a minimal generating set for $G$.

## 12. Elements of order two (page 2)

Let $G$ be a finite group of even order. Show from first principles that $G$ contains an element of order two.

Can a group have exactly two elements of order two?

## 13. Isometries of the complex plane (page 2)

Show that every isometry of $\mathbb C$ is either of the form $z\mapsto az+b$ or of the form $z\mapsto a\overline z+b$, with $a,b\in\mathbb C$ and $|a|=1$ in either case.

**Challenging part (\*):** Describe the finite subgroups of the group of isometries of $\mathbb C$.

**Hint:** First show that every finite subgroup of $\operatorname{Isom}(\mathbb C)$ fixes a point in $\mathbb C$.

## 14. Isometries of a quadrilateral (page 2)

Suppose $Q$ is a quadrilateral in $\mathbb C$. Show that its group of isometries $\operatorname{Isom}(Q)$ has order at most $8$.

For which $n$ is there an $\operatorname{Isom}(Q)$ of order $n$?

**Challenging part (\*):** Which groups can arise as $\operatorname{Isom}(Q)$, up to isomorphism?

Related notes: [[Groups]], [[Bijections and Permutations]], [[Subgroups and Generated Subgroups]], [[Roots of Unity]] and [[Groups - Chapter 1 Examples and Definitions]].

## Prerequisite vocabulary

The current lecture ends before several terms used in this sheet are defined. The following definitions supply reading context, without solving the exercises.

- The **order of an element** $g$ is the least positive $n$ with $g^n=e$, if such an $n$ exists; otherwise its order is infinite. This differs from the **order of a group**, $|G|$.
- A group is **cyclic** if $G=\langle\{g\}\rangle=\{g^k:k\in\mathbb Z\}$ for some $g$. The concrete roots-of-unity group $C_n$ in [[Groups]] is a model of the finite cyclic group used here.
- A **homomorphism** $\phi:G\to H$ satisfies $\phi(ab)=\phi(a)\phi(b)$ for all $a,b\in G$, with each side using its own group's operation.
- An **isomorphism** is a bijective homomorphism. “Up to isomorphism” means identifying groups whose elements can be bijectively relabelled while preserving multiplication.

Questions 1–3 use the group axioms and subgroup definitions; questions 4–12 also use powers, element order or the vocabulary above. Questions 13–14 use [[Isometries and Dihedral Groups]] and [[Complex Numbers|complex-plane geometry]]. In this repository $D_{2n}$ denotes the symmetries of an $n$-gon; some other texts call it $D_n$.
