---
title: Proof by Contradiction and Contraposition
material_type: source-backed proof methods
course: Part IA Numbers and Sets
---

# Proof by Contradiction and Contraposition

To establish $A\Rightarrow B$, show that $A$ true and $B$ false cannot occur together. The equivalent contrapositive is
$$A\Rightarrow B\quad\Longleftrightarrow\quad\neg B\Rightarrow\neg A.$$
The converse $B\Rightarrow A$ is a different assertion and does not establish $A\Rightarrow B$.

For example, suppose $n\in\mathbb Z_{>0}$, $n^2$ is even and $n$ is odd. Writing $n=2k+1$, $k\in\mathbb Z$, gives
$$n^2=4(k^2+k)+1,$$
which is odd, a contradiction. Hence $n^2$ even implies $n$ even.

One counterexample with $A$ true and $B$ false disproves a proposed implication. For instance, $n=3$ disproves $9\mid n^2\Rightarrow9\mid n$.

Source: [[Numbers and Sets - Chapter 0 Proofs]], pages 4–5. The invalid converse attempt is preserved there.

An “if and only if” assertion requires both directions; the quadratic example on page 6 illustrates this. Pages 8–9 derive contraposition using truth tables and explain negation of quantifiers; see [[Logical Connectives and Quantifiers]].
