---
title: Divisibility and Prime Numbers
material_type: source-backed definitions, propositions and proofs
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [7, 8, 13, 14]
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

## Euclid's lemma

**Proposition 4:** if $p$ is prime and $p\mid ab$, then $p\mid a$ or $p\mid b$.

**Proof (page 13).** If $p\nmid a$, primality gives $\gcd(p,a)=1$. By [[Bezout's Identity and Linear Diophantine Equations|Bézout's identity]], choose integers $x,y$ with $xp+ya=1$. Multiplying by $b$ yields
$$b=xpb+yab.$$
Both terms on the right are divisible by $p$, hence $p\mid b$.

Iterating the lemma shows that if $p\mid a_1\cdots a_m$, then $p$ divides some factor. Primality is essential; the source supplies no counterexample for a composite divisor.

## Fundamental theorem of arithmetic

Existence of a prime factorization alone does not establish uniqueness. The earlier source questions use $21=3\cdot7$ and $295869=3\cdot7\cdot73\cdot193$.

**Theorem 9 (page 14):** every integer $n\ge2$ is a product of primes, uniquely up to reordering.

Existence follows from Proposition 2. For uniqueness, induct on $n$. If
$$n=p_1\cdots p_k=q_1\cdots q_\ell,$$
Euclid's lemma makes $p_1$ divide some $q_i$. Since $q_i$ is prime, $p_1=q_i$. Relabel that factor as $q_1$ and cancel it. The quotient is smaller than $n$, so induction matches the remaining factors; if it is $1$, both remaining products are empty. Thus $k=\ell$ and the factors agree after reordering.

Source: [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 7–8 and 13–14. The complete uniqueness proof and unanswered product-comparison question are retained there. [[Greatest Common Divisors and Euclid's Algorithm]] supplies the gcd material on pages 8–13. The natural-number convention appears in [[Natural Numbers and Mathematical Induction]]. Related factorial and Fibonacci arguments are retained in [[Numbers and Sets 0 - Handwritten Attempts]].
