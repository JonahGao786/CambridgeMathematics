---
title: Greatest Common Divisors and Euclid's Algorithm
material_type: concept note
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [8, 9, 10, 11, 12, 13, 15, 16]
---

# Greatest Common Divisors and Euclid's Algorithm

For $a,b\in\mathbb N$, their **greatest common divisor** is the positive integer $c$ such that:

- $c\mid a$ and $c\mid b$.
- Every common divisor of $a,b$ divides $c$.

It is also called the **highest common factor**, with notation $\gcd(a,b)=\operatorname{hcf}(a,b)=(a,b)$. For example, the common positive divisors of $12,18$ are $1,2,3,6$, so $\gcd(12,18)=6$.

## Division algorithm

For $n,k\in\mathbb N$, there are unique integers $q,r$ such that
$$n=qk+r,\qquad0\le r<k.$$

Proposition 5 proves existence by induction on $n$. The step increments the remainder if it is below $k-1$, and otherwise increases the quotient and resets the remainder to zero. The base case chooses $1=1\cdot1+0$ when $k=1$, or $1=0\cdot k+1$ when $k>1$.

For uniqueness, if $n=qk+r=q'k+r'$, then $(q-q')k=r'-r$. Both remainders lie between $0$ and $k-1$, so $-k<r'-r<k$. Thus both sides are zero, giving $q=q'$ and $r=r'$.

## Euclid's algorithm

Starting with $a,b>0$, divide $a$ by $b$, then divide $b$ by the remainder, and continue with consecutive remainders. Stop at the first zero remainder and return the preceding non-zero value. If $b$ divides $a$ at the first step, return $b$.

The positive remainders strictly decrease:
$$b>r_1>r_2>\cdots>r_n>0.$$
There are fewer than $b$ positive remainders, followed by the final zero remainder, so the algorithm terminates.

**Theorem 6 — Correctness.** The output is $\gcd(a,b)$.

The last positive remainder divides its predecessor, since the next remainder is zero. Substitution backwards through the divisions shows that it divides all preceding remainders, and then $b$ and $a$.

Conversely, any common divisor of $a,b$ divides the first remainder, then the second, and every following remainder, including the output. This proves the two defining gcd properties. The immediate-termination case has output $b$ and satisfies the same properties.

## Worked examples

$$\begin{aligned}
372&=2\cdot162+48, &162&=3\cdot48+18,\\
48&=2\cdot18+12, &18&=1\cdot12+6,\\
12&=2\cdot6+0.
\end{aligned}$$
Hence $\gcd(372,162)=6$.

$$\begin{aligned}
87&=1\cdot52+35, &52&=1\cdot35+17,\\
35&=2\cdot17+1, &17&=17\cdot1+0.
\end{aligned}$$
Hence $\gcd(87,52)=1$.

## Coprimality and integer linear combinations

Numbers $a,b$ are **coprime** when $\gcd(a,b)=1$. Reversing the second example gives
$$1=35-2\cdot17=-5\cdot52+3\cdot87.$$
More generally, Theorem 7 gives $\gcd(a,b)=xa+yb$ for integers $x,y$. [[Bezout's Identity and Linear Diophantine Equations]] records both proofs, the coefficient-finding method, and the criterion $\gcd(a,b)\mid c$ for solvability of $ax+by=c$.

## Prime-exponent formulas and least common multiples

For positive integers $x,y$, use the same list of distinct primes, allowing exponent zero:
$$x=\prod_{i=1}^k p_i^{a_i},\qquad
y=\prod_{i=1}^k p_i^{b_i},\qquad a_i,b_i\ge0.$$
A common divisor can use at most $\min(a_i,b_i)$ copies of each prime. A common positive multiple needs at least $\max(a_i,b_i)$ copies. Consequently,
$$\gcd(x,y)=\prod_{i=1}^k p_i^{\min(a_i,b_i)},$$
$$\operatorname{lcm}(x,y)=\prod_{i=1}^k p_i^{\max(a_i,b_i)}.$$
The **least common multiple** is positive, and every common integer multiple is an integer multiple of it.

For example,
$$x=2^3\,3^7\,5\,11^3,\qquad y=2^4\,3^2\,11\,13,$$
$$\gcd(x,y)=2^3\,3^2\,11,\qquad
\operatorname{lcm}(x,y)=2^4\,3^7\,5\,11^3\,13.$$
The exponent identity $\min(a_i,b_i)+\max(a_i,b_i)=a_i+b_i$ gives
$$\gcd(x,y)\operatorname{lcm}(x,y)=xy.$$

See [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 8–13 and 15–16. Related: [[Divisibility and Prime Numbers]], [[Modular Arithmetic]] and [[Natural Numbers and Mathematical Induction]].

## From the algorithm to Euclid's lemma

Each remainder in Euclid's algorithm is an integer linear combination of $a,b$: this holds for $r_1=a-q_1b$, and is preserved when subtracting an integer multiple of one remainder from another. The last non-zero remainder therefore gives **Bézout's identity**
$$\gcd(a,b)=ua+vb\qquad\text{for some }u,v\in\mathbb Z.$$
If the algorithm stops immediately, $b=0a+1b$ supplies the same statement. For example, back-substitution in the second worked example gives
$$1=35-2\cdot17=3\cdot35-2\cdot52=3\cdot87-5\cdot52.$$

For prime $p$ and positive $a$ with $p\nmid a$, the only positive common divisor is $1$. Choose $u,v\in\mathbb Z$ with $up+va=1$. If $p\mid ab$, multiplying by $b$ gives
$$b=upb+vab,$$
so $p\mid b$. If instead $p\mid a$, the other alternative already holds. For arbitrary integer $a,b$, zero cases are immediate and signs can be removed using absolute values. This proves [[Divisibility and Prime Numbers|Euclid's lemma]]. See [[Bezout's Identity and Linear Diophantine Equations]].
