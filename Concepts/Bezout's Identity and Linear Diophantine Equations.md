---
title: Bezout's Identity and Linear Diophantine Equations
material_type: source-backed theorem, corollary, proofs and examples
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [11, 12, 13]
---

# Bézout's Identity and Linear Diophantine Equations

**Theorem 7.** For $a,b\in\mathbb N$, there are integers $x,y$ such that
$$xa+yb=\gcd(a,b).$$
The numbers $a,b$ are **coprime** when their gcd is $1$.

## Two proofs

Reversing [[Greatest Common Divisors and Euclid's Algorithm|Euclid's algorithm]] expresses its last positive remainder as an integer linear combination of preceding remainders, eventually reaching the original inputs $a,b$. This also computes the coefficients. The source example gives
$$1=35-2\cdot17=35-2(52-35)=-5\cdot52+3\cdot87.$$

Alternatively, choose the least positive integer linear combination $h=xa+yb$, $x,y\in\mathbb Z$, using well-ordering. Every common divisor of $a,b$ divides $h$. If $h\nmid a$, the positive remainder $r=a-qh<h$ is another such combination, a contradiction. Similarly $h\mid b$. Thus $h$ has the two defining gcd properties. This proof gives existence without a method to find the coefficients.

## Integer linear equations

**Corollary 8.** For $a,b\in\mathbb N$ and $c\in\mathbb Z$, the equation $ax+by=c$ has an integer solution exactly when $\gcd(a,b)\mid c$.

If there is a solution, every common divisor divides $c$. Conversely, if $h=\gcd(a,b)$ divides $c$ and $h=ax_0+by_0$, multiply that identity by the integer $c/h$ to obtain a solution.

The source examples are:

- $160x+72y=33$ has no integer solution, since its left side is even.
- $87x+52y=33$ has a solution obtained by multiplying $3\cdot87-5\cdot52=1$ by $33$.

Source: [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 11–13, which retains both complete proofs and every back-substitution step. The identity is then used to prove [[Divisibility and Prime Numbers|Euclid's lemma]] on page 13.
