---
title: Greatest Common Divisors and Euclid's Algorithm
course: Part IA Numbers and Sets
material_type: concept note
tags: [concept, numbers-and-sets]
---

# Greatest Common Divisors and Euclid's Algorithm

> [!abstract] In one paragraph
> The gcd of $a,b$ is the common divisor that every other common divisor divides. Euclid's algorithm finds it by repeated division with remainder; running the algorithm backwards writes the gcd as $xa+yb$.

## Definition

For $a,b\in\mathbb N$, $c=\gcd(a,b)=\operatorname{hcf}(a,b)=(a,b)$ if (i) $c\mid a$ and $c\mid b$, and (ii) $d\mid a,\ d\mid b\Rightarrow d\mid c$. $a,b$ are **coprime** if $\gcd(a,b)=1$.

## Key results

- **Proposition 5 — Division algorithm.** For $n,k\in\mathbb N$ there are unique $q,r$ with $n=qk+r$, $0\le r\le k-1$. *Idea:* induction on $n$; uniqueness since $|r'-r|<k$. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Proposition 5 — Division algorithm|proof]]
- **Theorem 6 — Euclid's algorithm.** Divide $a$ by $b$, then $b$ by $r_1$, $r_1$ by $r_2$, …; the last non-zero remainder is $\gcd(a,b)$. *Idea:* $r_n$ divides every earlier remainder, and every common divisor divides every remainder. → [[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 6 — Euclid's algorithm computes the gcd|proof]]

## Worked example

$$372=2\cdot162+48,\quad162=3\cdot48+18,\quad48=2\cdot18+12,\quad18=1\cdot12+6,\quad12=2\cdot6,$$
so $\gcd(372,162)=6$.

## gcd and lcm from prime factorizations

With $x=\prod p_i^{a_i}$, $y=\prod p_i^{b_i}$ ($a_i,b_i\ge0$):
$$\gcd(x,y)=\prod p_i^{\min(a_i,b_i)},\qquad\operatorname{lcm}(x,y)=\prod p_i^{\max(a_i,b_i)},\qquad\gcd(x,y)\operatorname{lcm}(x,y)=xy.$$
→ [[Numbers and Sets - Chapter 1 Elementary Number Theory#Applications of Theorem 9|applications of Theorem 9]]

## Related

[[Bezout's Identity and Linear Diophantine Equations]] · [[Divisibility and Prime Numbers]] · [[Modular Arithmetic]]
