---
title: Greatest Common Divisors and Euclid's Algorithm
material_type: source-backed definition, algorithm, theorems and proofs
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [8, 9, 10, 11, 12, 13]
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

Source: [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 8–13, including the full algorithm table and proofs. Related: [[Divisibility and Prime Numbers]] and [[Natural Numbers and Mathematical Induction]].
