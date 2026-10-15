---
title: Divisibility and Prime Numbers
material_type: source-backed definitions, propositions and proofs
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [7, 8]
---

# Divisibility and Prime Numbers

For $a,b\in\mathbb Z$,
$$a\mid b\quad\Longleftrightarrow\quad\exists c\in\mathbb Z:\ b=ac.$$
The equivalent words are **divisor**, **factor**, and **multiple**: $a$ is a divisor or factor of $b$, and $b$ is a multiple of $a$.

The factors $\pm1$ and $\pm b$ are the trivial factors of $b$. Other factors are **proper** or **non-trivial**.

A natural number $n\ge2$ is **prime** if its only integer factors are $\pm1$ and $\pm n$. An $n\ge2$ that is not prime is **composite**.

## Existence of prime factorizations

**Proposition 2:** every natural number $n\ge2$ is a product of primes.

The proof uses [[Natural Numbers and Mathematical Induction|strong induction]]. The base case is $2$. For $n>2$, either $n$ itself is prime or $n=ab$ with $1<a,b<n$. The induction hypothesis factors both $a$ and $b$ into primes; multiplying the two factorizations gives one for $n$.

## Infinitely many primes

**Theorem 3:** there are infinitely many primes.

Suppose $p_1,\ldots,p_k$ list all primes, and let $N=p_1\cdots p_k+1$. No $p_i$ divides $N$, since otherwise $p_i$ would divide $1$. But $N\ge2$ has a prime factor by Proposition 2, contradicting completeness of the list.

The proof does not claim that $N$ itself is prime.

## Uniqueness and Euclid's lemma

Existence of a prime factorization does not establish uniqueness. The source illustrates the uniqueness question with $21=3\cdot7$ and $295869=3\cdot7\cdot73\cdot193$; it does not yet give a uniqueness proof.

**Proposition 4 — Euclid's lemma:** if $p$ is prime and $p\mid ab$, then $p\mid a$ or $p\mid b$. The current source states this proposition without proof.

[[Greatest Common Divisors and Euclid's Algorithm]] records the subsequent gcd definition, division theorem and algorithm, without adding an unprovided proof of Euclid's lemma.

Source: [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 7–8, with gcd material on pages 8–11. The natural-number convention and induction principles appear in [[Natural Numbers and Mathematical Induction]]. Related factorial and Fibonacci arguments are retained in [[Numbers and Sets 0 - Handwritten Attempts]].
