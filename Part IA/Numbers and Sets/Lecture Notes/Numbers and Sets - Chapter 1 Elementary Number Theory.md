---
title: Numbers and Sets - Chapter 1 Elementary Number Theory
material_type: handwritten lecture notes
course: Part IA Numbers and Sets
date: null
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: 2
---

# Numbers and Sets — Chapter 1: Elementary Number Theory

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view). These two pages introduce the natural numbers and addition; further number-theoretic material is not present in this version.

## The natural numbers and Peano axioms (page 1)

Intuitively, the natural numbers consist of
$$1,\quad 1+1,\quad 1+1+1,\quad 1+1+1+1,\quad\ldots.$$
How do we know that this captures every natural number, and that its entries are distinct?

Assume that $\mathbb N$ is a set containing a distinguished element $1$ and equipped with a successor operation $n\mapsto n+1$ satisfying:

1. For every $n\in\mathbb N$, $n+1\ne1$.
2. For every $m,n\in\mathbb N$, if $m\ne n$, then $m+1\ne n+1$.
3. For any property $P(n)$, if $P(1)$ is true and
   $$\forall n\in\mathbb N,\qquad P(n)\Rightarrow P(n+1),$$
   then $P(n)$ is true for every $n\in\mathbb N$.

These are the **Peano axioms** in the lecture's convention $\mathbb N=\{1,2,3,\ldots\}$. The third is the **induction axiom**.

The first two capture the distinctness of the successive entries. The induction axiom captures completeness of the list: take $P(n)$ to mean that $n$ is on the list.

See [[Natural Numbers and Mathematical Induction]] for the role of each axiom and the order of the quantifiers.

## Defining addition recursively (page 2)

Write $2$ for $1+1$, $3$ for $1+1+1$, and so on. For each natural number $k$, define addition by $k$ for every $n\in\mathbb N$ using
$$n+(k+1)=(n+k)+1.$$
The starting operation $n+1$ is the successor operation. The induction is on $k$, taking $P(k)$ to mean that addition by $k$ is defined.

**Explanation of the recursion.** Once the operation $n\mapsto n+k$ has been defined for every $n$, applying successor defines $n\mapsto n+(k+1)$. This defines addition by each natural number. The equation is a definition; associativity and commutativity of addition have not been proved on these pages.
