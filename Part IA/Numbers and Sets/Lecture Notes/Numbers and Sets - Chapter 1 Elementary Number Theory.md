---
title: Numbers and Sets - Chapter 1 Elementary Number Theory
material_type: handwritten lecture notes
course: Part IA Numbers and Sets
date: null
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: 11
---

# Numbers and Sets — Chapter 1: Elementary Number Theory

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view), eleven pages. No date is supplied.

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

## Proposition 2 — Existence of prime factorizations (page 7)

Every natural number $n\ge2$ can be written as a product of primes.

**Proof by strong induction on $n$.** The claim holds for $n=2$. Let $n>2$ and suppose it holds for every integer from $2$ through $n-1$.

If $n$ is prime, it is already a product consisting of one prime. Otherwise $n=ab$ for integers satisfying $1<a,b<n$. By the induction hypothesis,
$$a=p_1p_2\cdots p_k,\qquad b=q_1q_2\cdots q_\ell$$
for primes $p_1,\ldots,p_k,q_1,\ldots,q_\ell$. Hence
$$n=ab=p_1p_2\cdots p_kq_1q_2\cdots q_\ell$$
is a product of primes.

## Theorem 3 — Infinitely many primes (page 8)

**Proof.** Suppose there are only finitely many primes, say $p_1,\ldots,p_k$. Put
$$N=p_1p_2\cdots p_k+1.$$
If $p_1\mid N$, then $p_1\mid N-p_1p_2\cdots p_k=1$, which is impossible. The same argument applies to every $p_i$.

Thus none of the primes on the list divides $N$. But Proposition 2 says that $N\ge2$ is a product of primes, so it must have a prime divisor. This contradicts the supposed complete list.

### The uniqueness question and Proposition 4 (page 8)

The existence proof does not establish uniqueness of a prime factorization. The source asks about
$$21=3\cdot7,\qquad 295869=3\cdot7\cdot73\cdot193,$$
and asks why
$$9049\cdot40099\ne6701\cdot54151.$$
No proof of uniqueness or answer to this comparison question is supplied.

**Proposition 4 — Euclid's lemma.** If $p$ is prime and $p\mid ab$, then $p\mid a$ or $p\mid b$.

**Statement only:** this version of the lecture supplies no proof of Proposition 4.

## Highest common factors (pages 8–9)

For $a,b\in\mathbb N$, a natural number $c$ is their **highest common factor** or **greatest common divisor** if:

1. $c\mid a$ and $c\mid b$.
2. Every common divisor $d$ of $a$ and $b$ divides $c$.

Write
$$c=\operatorname{hcf}(a,b)=\gcd(a,b)=(a,b).$$

For example, the positive factors of $12$ are $1,2,3,4,6,12$, and those of $18$ are $1,2,3,6,9,18$. Their common positive factors are $1,2,3,6$, so $\gcd(12,18)=6$.

The source next establishes that the gcd always exists by [[Greatest Common Divisors and Euclid's Algorithm|Euclid's algorithm]].

## Proposition 5 — Division algorithm (page 9)

Let $n,k\in\mathbb N$. There are integers $q,r$ such that
$$n=qk+r,\qquad 0\le r\le k-1.$$

**Proof by induction on $n$.** For $n=1$, take $q=1,r=0$ if $k=1$, and $q=0,r=1$ if $k>1$.

Suppose $n\ge2$ and the result holds for $n-1$:
$$n-1=qk+r,\qquad 0\le r\le k-1.$$
If $r<k-1$, then
$$n=qk+(r+1),$$
with an admissible remainder. If $r=k-1$, then
$$n=qk+(k-1+1)=(q+1)k,$$
with remainder $0$.

**Uniqueness.** If $n=qk+r=q'k+r'$ with both remainders between $0$ and $k-1$, then
$$(q-q')k=r'-r,\qquad -k<r'-r<k.$$
The only multiple of $k$ strictly between $-k$ and $k$ is $0$. Thus $q=q'$ and $r=r'$.

## Euclid's algorithm (page 10)

Input $a,b\in\mathbb N$. Repeatedly apply the division algorithm:

| Stage | Division | Remainder condition |
| --- | --- | --- |
| 1 | $a=q_1b+r_1$ | $0\le r_1<b$ |
| 2 | $b=q_2r_1+r_2$ | $0\le r_2<r_1$ |
| 3 | $r_1=q_3r_2+r_3$ | $0\le r_3<r_2$ |
| $n$ | $r_{n-2}=q_nr_{n-1}+r_n$ | $0<r_n<r_{n-1}$ |
| $n+1$ | $r_{n-1}=q_{n+1}r_n+0$ | first zero remainder |

The output is the last non-zero remainder $r_n$. If the first remainder is already zero, the output is $b$.

The positive remainders satisfy
$$b>r_1>r_2>\cdots>r_n>0,$$
so there are fewer than $b$ positive remainders. In the source's indexing $n<b$; one final division produces the zero remainder.

The worked example is
$$\begin{aligned}
372&=2\cdot162+48,\\
162&=3\cdot48+18,\\
48&=2\cdot18+12,\\
18&=1\cdot12+6,\\
12&=2\cdot6+0.
\end{aligned}$$
The output is $6$.

## Theorem 6 — Correctness of Euclid's algorithm (page 10)

The output of Euclid's algorithm with input $a,b$ is $\gcd(a,b)$.

**Proof.** Let $r_n$ be the last positive remainder.

1. Since the next remainder is zero, $r_n\mid r_{n-1}$. The preceding division then gives $r_n\mid r_{n-2}$. Continuing backwards shows that $r_n$ divides all earlier remainders, then $b$ and $a$.
2. If $\alpha\mid a$ and $\alpha\mid b$, the first division gives $\alpha\mid r_1$. The second gives $\alpha\mid r_2$, and induction through the divisions gives $\alpha\mid r_n$.

These are exactly the two defining gcd properties. If the first remainder is zero, $b\mid a$, so the output $b$ satisfies them immediately.

### Another worked example (page 11)

$$\begin{aligned}
87&=1\cdot52+35,\\
52&=1\cdot35+17,\\
35&=2\cdot17+1,\\
17&=17\cdot1+0.
\end{aligned}$$
The last non-zero remainder is $1$, so $\gcd(87,52)=1$.
