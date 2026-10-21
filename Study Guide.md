---
title: Study Guide
material_type: study guide
date: 2026-10-21
---

# Study Guide

Use this guide to follow the main ideas in each course and find the relevant lectures, concept notes and exercises.

Use the concept sequence in each course for revision, then return to the linked lectures for full derivations and to the sheets for practice. **Wrong proof**, **Incomplete proof**, and **TODO** labels describe limitations of an argument; they do not by themselves determine whether the conclusion is true or false.

## Numbers and Sets

Start with implication and quantifier order, then induction and well-ordering. Prime factorization existence uses strong induction; uniqueness uses Euclid’s lemma, which follows from Bézout’s identity. Fibonacci identities are exercise material: consult the attempt’s proof-status notes before treating a claim as established.

### Concept sequence

1. [[Logical Connectives and Quantifiers]]
2. [[Proof by Contradiction and Contraposition]]
3. [[Natural Numbers and Mathematical Induction]]
4. [[Divisibility and Prime Numbers]]
5. [[Greatest Common Divisors and Euclid's Algorithm]]
6. [[Bezout's Identity and Linear Diophantine Equations]]
7. [[Modular Arithmetic]]
8. [[Fibonacci Numbers]]

### Lectures and practice

- [[Numbers and Sets - Chapter 0 Proofs]]
- [[Numbers and Sets - Chapter 1 Elementary Number Theory]]
- [[Numbers and Sets - Introductory Sheet 2026]]
- [[Numbers and Sets 0 - Handwritten Attempts]]

## Vectors and Matrices

First learn complex arithmetic and polar form, then exponential notation, roots and logarithm choices. The fundamental theorem of algebra is a stated theorem, not a prerequisite for the explicit roots-of-unity calculation. For vectors, follow span → basis → orthonormal coordinates; the dot product gives length and projection, while the cross product adds orientation in three dimensions.

### Concept sequence

1. [[Complex Numbers]]
2. [[De Moivre's Theorem]]
3. [[Triangle Inequality for Complex Numbers]]
4. [[Fundamental Theorem of Algebra]]
5. [[Complex Exponential and Trigonometric Functions]]
6. [[Roots of Unity]]
7. [[Complex Logarithms and Powers]]
8. [[Vectors and Linear Span]]
9. [[Real Inner Products and Cauchy-Schwarz]]
10. [[Orthonormal Bases and Vector Coordinates]]
11. [[Cross Products and Scalar Triple Products]]
12. [[Lines, Planes and Vector Equations]]
13. [[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]]

### Lectures and practice

- [[Vectors and Matrices - Chapter 1 Complex Numbers]]
- [[Vectors and Matrices - Chapter 2 Vectors]]

## Groups

Start with the set, operation and axioms; then use inverses to justify cancellation. Bijections supply permutation examples, and closure under operations leads to subgroups and generators. Read complex polar form and roots of unity before the geometric isometry examples. The dihedral classification uses preservation of corners and adjacency. The 2025 example sheet includes a guide to its prerequisite vocabulary.

### Concept sequence

1. [[Groups]]
2. [[Bijections and Permutations]]
3. [[Subgroups and Generated Subgroups]]
4. [[Latin Squares]]
5. [[Isometries and Dihedral Groups]]
6. [[Homomorphisms and Isomorphisms]]
7. [[Cyclic Groups and Element Orders]]

### Lectures and practice

- [[Groups - Chapter 1 Examples and Definitions]]
- [[Groups - Example Sheet 1 2025]]
- [[Groups - Introductory Sheet 2026]]
- [[Groups 0 - Handwritten Attempts]]

## Differential Equations

Read limits and error notation before derivative rules. Taylor polynomials approximate locally; equality to an infinite Taylor series needs a separate remainder argument. Integration reverses differentiation under the fundamental theorem. For several variables, start with holding one variable fixed, then add the first-order changes to obtain the differential and chain rule.

### Concept sequence

1. [[Limits, Big O and Little o - A First-Year Guide]]
2. [[Differentiation Rules]]
3. [[Taylor Series and Taylor's Theorem]]
4. [[L'Hôpital's Rule]]
5. [[Riemann Integration and the Fundamental Theorem of Calculus]]
6. [[Integration by Substitution and by Parts]]
7. [[Partial Derivatives and the Multivariate Chain Rule]]
8. [[Implicit Differentiation]]
9. [[Differentiation Under the Integral Sign]]
10. [[First-Order Linear Differential Equations]]
11. [[Forward Euler Method]]

### Lectures and practice

- [[Differential Equations - Chapter 1 Introduction and Basic Calculus]]
- [[Differential Equations - Chapter 2 Integration]]
- [[Differential Equations - Chapter 3 Partial Differentiation]]
- [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]]
- [[Differential Equations - Examples Sheet 1 2026]]
- [[Differential Equations - Examples Sheet 1 Handwritten Proofs]]

## Connections between courses

- **Logic → limits:** the order “for every tolerance, there exists a neighbourhood” uses [[Logical Connectives and Quantifiers]].
- **Number theory → subgroups:** well-ordering and division with remainder underpin the classification of subgroups of the integers. Bézout’s identity uses the same integer-linear-combination idea.
- **Complex numbers → geometry and groups:** multiplication by a unit complex number rotates the plane; conjugation reflects it. These maps connect [[Roots of Unity]] to [[Isometries and Dihedral Groups]].
- **Geometry → multivariate calculus:** the slopes in the coordinate directions give the two contributions $df=f_x\,dx+f_y\,dy$; along a path, both coordinates can change.

## Conventions and coverage

Here $\mathbb N=\{1,2,3,\ldots\}$ and $F_1=F_2=1$; $F_0$ has not been defined in this convention. Function composition is right to left. The complex-number notes use $\log z$ for the principal value and $\operatorname{Log}z$ for the set of logarithms, with $\arg z\in(-\pi,\pi]$. $f_{xy}=(f_x)_y=\partial_y(\partial_x f)$ means first $x$, then $y$; check the convention in other texts.

The lecture’s word “proper” for subgroups excludes both the whole group and the trivial subgroup, whereas standard usage excludes only the whole group. Its “proper factors” likewise means non-trivial factors. Inner-product axioms here are for real vector spaces; the cross product is used in $\mathbb R^3$ with a fixed orientation.

These notes cover the introductory material in each course. General matrix and eigenvalue theory and a full treatment of first-order ODE solution methods are outside their current scope.
