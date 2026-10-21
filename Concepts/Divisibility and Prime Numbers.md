---
title: Divisibility and Prime Numbers
material_type: concept note
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [7, 8, 13, 14, 15, 17]
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

Iterating the lemma shows that if $p\mid a_1\cdots a_m$, then $p$ divides some factor. Primality is essential.

## Fundamental theorem of arithmetic

Existence of a prime factorization alone does not establish uniqueness. Examples include $21=3\cdot7$ and $295869=3\cdot7\cdot73\cdot193$.

**Theorem 9 (page 14):** every integer $n\ge2$ is a product of primes, uniquely up to reordering.

Existence follows from Proposition 2. For uniqueness, induct on $n$. If
$$n=p_1\cdots p_k=q_1\cdots q_\ell,$$
Euclid's lemma makes $p_1$ divide some $q_i$. Since $q_i$ is prime, $p_1=q_i$. Relabel that factor as $q_1$ and cancel it. The quotient is smaller than $n$, so induction matches the remaining factors; if it is $1$, both remaining products are empty. Thus $k=\ell$ and the factors agree after reordering.

## Positive divisors from prime exponents

If $n=p_1^{a_1}\cdots p_k^{a_k}$ with distinct primes and positive exponents, its positive divisors are exactly
$$p_1^{b_1}\cdots p_k^{b_k},\qquad0\le b_i\le a_i.$$
For example, $2^3\,3^7\,11$ has precisely the positive divisors $2^a3^b11^c$ with $0\le a\le3$, $0\le b\le7$, $0\le c\le1$. An extra prime factor would contradict unique factorization.

The page-15 example $4=2\cdot2=(1+\sqrt{-3})(1-\sqrt{-3})$ concerns the different system $\mathbb Z[\sqrt{-3}]$. The factors $2$ and $1\pm\sqrt{-3}$ are irreducible but not prime, and no two are associates. The norm $x^2+3y^2$ proves irreducibility; see the lecture for the argument. The integer form of Euclid's lemma cannot be transferred to that example without qualification.

## Erdős's counting proof of infinitely many primes

Suppose $p_1,\ldots,p_k$ list all primes. Splitting prime exponents into even parts and remainders writes each positive integer as
$$m^2p_1^{i_1}\cdots p_k^{i_k},\qquad i_\nu\in\{0,1\}.$$
Among numbers at most $N$, there are at most $\sqrt N$ choices of $m$ and $2^k$ choices of the binary exponents. If $N>4^k$, this accounts for fewer than $N$ integers, a contradiction. The lecture attributes this proof to Erdős (1930).

Further results, stated without proof, are the bounds $p_k<2^{2^k}$ and $p_k<4^k$ for the $k$th prime, and the prime number theorem $p_k\sim k\log k$.

See [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 7–8, 13–15 and 17. [[Greatest Common Divisors and Euclid's Algorithm]] supplies the gcd/lcm material; [[Modular Arithmetic]] introduces congruences. The natural-number convention appears in [[Natural Numbers and Mathematical Induction]]. For factorial and Fibonacci exercises, see [[Numbers and Sets 0 - Handwritten Attempts]].

## How uniqueness follows

The bridge from existence to uniqueness is [[Greatest Common Divisors and Euclid's Algorithm#From the algorithm to Euclid's lemma|Bézout's identity and Euclid's lemma]]. If
$$p_1\cdots p_r=q_1\cdots q_s$$
are prime factorizations of the same positive integer, repeated application of Euclid's lemma shows that $p_1$ divides some $q_j$. Since $q_j$ is prime, $p_1=q_j$. Reorder the right-hand factors and cancel this common positive factor. Repeat with the remaining products. One side cannot run out of factors first, because a non-empty product of primes is at least $2$, whereas the empty product is $1$. Thus $r=s$ and the factors agree up to order.

The logical chain is: strong induction gives existence; Euclid's algorithm gives Bézout's identity; Euclid's lemma gives uniqueness. The infinitude-of-primes proof above needs only existence, not uniqueness.

**Terminology:** “proper divisor” in other texts often includes $1$ and excludes only the number itself among positive divisors. Here it means non-trivial factors, excluding both $\pm1$ and $\pm n$.
