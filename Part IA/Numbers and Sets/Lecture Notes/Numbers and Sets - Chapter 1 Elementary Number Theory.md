---
title: Numbers and Sets - Chapter 1 Elementary Number Theory
material_type: handwritten lecture notes
course: Part IA Numbers and Sets
date: null
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: 7
---

# Numbers and Sets — Chapter 1: Elementary Number Theory

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view), seven pages. No date is supplied.

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

**Explanation of the recursion.** Once the operation $n\mapsto n+k$ has been defined for every $n$, applying successor defines $n\mapsto n+(k+1)$. This defines addition by each natural number. The equation is a definition; the arithmetic laws below are stated for checking, without proofs.

Multiplication and powers can similarly be defined recursively. The source does not give those recursions explicitly.

## Arithmetic and order on the natural numbers (pages 2–3)

The usual arithmetic rules can be checked. For all $a,b,c\in\mathbb N$:

1. **(i) Commutativity of addition:** $a+b=b+a$.
2. **(ii) Commutativity of multiplication:** $ab=ba$.
3. **(iii) Associativity of addition:** $a+(b+c)=(a+b)+c$.
4. **(iv) Associativity of multiplication:** $a(bc)=(ab)c$.
5. **(v) Distributivity:** $a(b+c)=ab+ac$.

Define $a<b$ if $a+c=b$ for some $c\in\mathbb N$. The source lists:

6. **(vi)** $a<b\Rightarrow a+c<b+c$.
7. **(vii)** $a<b\Rightarrow ac<bc$.
8. **(viii)** $a<b$ and $b<c\Rightarrow a<c$.
9. **(ix)** $\neg(a<a)$.

Here $c\in\mathbb N$ is positive, as required in (vii). No proofs of (i)–(ix) are supplied.

## Weak and strong induction (page 3)

The induction axiom is also called the **weak principle of induction (WPI)**.

The **strong principle of induction (SPI)** states that if

1. $P(1)$ holds; and
2. for every $n\in\mathbb N$,
   $$\bigl(\forall m\in\mathbb N,\ m\le n\Rightarrow P(m)\bigr)\Rightarrow P(n+1),$$

then $P(n)$ holds for every $n\in\mathbb N$.

WPI and SPI are equivalent. SPI implies WPI because the strong hypothesis includes $P(n)$. To see that WPI implies SPI, apply WPI to
$$Q(n):\quad P(m)\text{ holds for every }m\le n.$$
The base case is $Q(1)=P(1)$. If $Q(n)$ holds, the strong step gives $P(n+1)$, so $Q(n+1)$ holds. This makes the source's indicated argument explicit.

## Well-ordering and least counterexamples (pages 3–4)

The **well-ordering principle (WOP)** says that if $P(n)$ holds for some $n\in\mathbb N$, there is a least $n\in\mathbb N$ for which it holds. Equivalently, every non-empty subset of $\mathbb N$ has a minimal element.

**Theorem 1 — SPI implies WOP (page 4).**

**Proof.** Suppose that $P(n)$ holds for at least one natural number but has no least such number. Set
$$Q(n):\quad\neg P(n).$$
Certainly $Q(1)$ holds: otherwise $1$ would be a least number satisfying $P$.

For $n>1$, suppose $Q(k)$ holds for every $k<n$. Then $P(k)$ is false for every $k<n$. If $P(n)$ were true, $n$ would be the least number satisfying it, contradicting the assumption. Hence $Q(n)$ holds.

By SPI, $Q(n)$ holds for every $n\in\mathbb N$. This contradicts the assumed existence of an $n$ satisfying $P$, proving WOP.

WOP gives a method of proof: if a universal claim were false, there would be a least counterexample, from which one may try to derive a contradiction. See [[Natural Numbers and Mathematical Induction]].

## The integers (page 5)

The integers $\mathbb Z$ consist of the symbols $n,-n$, where $n\in\mathbb N\cup\{0\}$. Addition and multiplication extend those on $\mathbb N$, and rules (i)–(v) continue to hold. In addition:

10. **(x) Additive identity:** for all $a\in\mathbb Z$, $a+0=a$.
11. **(xi) Additive inverses:** for every $a\in\mathbb Z$, there is a $b\in\mathbb Z$ with $a+b=0$.

Again define $a<b$ if $a+c=b$ for some $c\in\mathbb N$. Rules (vi), (viii) and (ix) continue to hold, but multiplication requires the positive-factor condition:
$$\text{(vii')}\qquad a<b\text{ and }c>0\Rightarrow ac<bc\qquad(a,b,c\in\mathbb Z).$$

## The rationals (page 6)

The rationals $\mathbb Q$ consist of expressions $a/b$, where $a,b\in\mathbb Z$ and $b\ne0$. The expressions $a/b$ and $c/d$ represent the same rational number if
$$ad=bc\qquad(b,d\ne0).$$

Define addition by
$$\frac ab+\frac cd=\frac{ad+bc}{bd}.$$
Check that this is independent of the chosen representations of the two fractions. Multiplication can be defined similarly; no multiplication formula or proof of well-definedness is supplied here.

For positive denominators $b,d>0$, define
$$\frac ab<\frac cd\quad\Longleftrightarrow\quad ad<bc.$$
The preceding arithmetic and applicable order rules can be checked. The inclusions are
$$\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q.$$

## Divisibility, primes and composites (page 7)

For $a,b\in\mathbb Z$, **$a$ divides $b$** if there is a $c\in\mathbb Z$ with $b=ac$. Write $a\mid b$. Equivalent descriptions are that $a$ is a divisor or factor of $b$, or that $b$ is a multiple of $a$.

For any $b\in\mathbb Z$, $\pm1$ and $\pm b$ are factors. All other factors are called **proper** or **non-trivial** factors.

A natural number $n\ge2$ is **prime** if its only integer factors are $\pm1$ and $\pm n$. If $n\ge2$ is not prime, it is **composite**. See [[Divisibility and Prime Numbers]].
