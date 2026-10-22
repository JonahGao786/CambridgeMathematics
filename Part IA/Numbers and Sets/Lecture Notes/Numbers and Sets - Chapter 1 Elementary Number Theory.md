---
title: Numbers and Sets - Chapter 1 Elementary Number Theory
course: Part IA Numbers and Sets
material_type: lecture notes
chapter: 1
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: 23
tags: [lecture, numbers-and-sets]
---

# Numbers and Sets — Chapter 1: Elementary Number Theory

> [!abstract] Overview
> Builds $\mathbb N$ from the Peano axioms, gives the induction principles, then develops divisibility: division algorithm → Euclid's algorithm → Bézout → Euclid's lemma → unique prime factorization. Finishes with modular arithmetic, units mod $n$, linear congruences and the Chinese Remainder Theorem.
> Prerequisite: [[Numbers and Sets - Chapter 0 Proofs]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Peano axioms]] | $\mathbb N$, successor, induction axiom | 1 |
| [[#Definition — Strong induction and well-ordering]] | SPI, WOP; WPI $\iff$ SPI | 3 |
| [[#Theorem 1 — Strong induction implies well-ordering]] | SPI $\Rightarrow$ WOP | 4 |
| [[#Definition — Divisibility and primes]] | $a\mid b$, prime, composite | 7 |
| [[#Proposition 2 — Existence of prime factorization]] | every $n\ge2$ is a product of primes | 7 |
| [[#Theorem 3 — Infinitely many primes]] | Euclid's proof | 8 |
| [[#Definition — Highest common factor]] | $\gcd(a,b)$ | 8 |
| [[#Proposition 5 — Division algorithm]] | $n=qk+r$, $0\le r\le k-1$, unique | 9 |
| [[#Theorem 6 — Euclid's algorithm computes the gcd]] | last non-zero remainder $=\gcd(a,b)$ | 10 |
| [[#Theorem 7 — Bezout's identity]] | $xa+yb=\gcd(a,b)$ for some $x,y\in\mathbb Z$ | 11 |
| [[#Corollary 8 — Bezout's theorem]] | $ax+by=c$ solvable $\iff\gcd(a,b)\mid c$ | 13 |
| [[#Proposition 4 — Euclid's lemma]] | $p\mid ab\Rightarrow p\mid a$ or $p\mid b$ | 8, 13 |
| [[#Theorem 9 — Fundamental theorem of arithmetic]] | prime factorization is unique | 14 |
| [[#Applications of Theorem 9]] | divisors, gcd, lcm, Erdős's proof | 15–17 |
| [[#Definition — Integers modulo n]] | $x\equiv y\pmod n\iff n\mid x-y$ | 18 |
| [[#Definition — Units modulo n]] | inverse of $a$ mod $n$ | 19 |
| [[#Proposition 10 — Units modulo a prime]] | $a\not\equiv0\pmod p\Rightarrow a$ is a unit | 20 |
| [[#Proposition 10' — Units modulo n]] | $a$ unit mod $n\iff\operatorname{hcf}(a,n)=1$ | 20 |
| [[#Corollary 11 — Solving linear congruences]] | $ax\equiv b\pmod n$ | 21 |
| [[#Theorem 12 — Chinese Remainder Theorem]] | simultaneous congruences, coprime moduli | 23 |

## 1.1 The natural numbers

Intuitively the natural numbers are $1,\ 1+1,\ 1+1+1,\ \dots$ — but how do we know this captures all of them, and that they are all distinct?

### Definition — Peano axioms

The **natural numbers** $\mathbb N$ form a set containing a special element $1$, with an operation "$+1$", such that

1. $\forall n\in\mathbb N,\ n+1\ne1$;
2. $\forall m,n\in\mathbb N$, if $m\ne n$ then $m+1\ne n+1$;
3. for any property $P(n)$: if $P(1)$ is true and $\forall n\in\mathbb N,\ P(n)\Rightarrow P(n+1)$, then $P(n)$ is true for all $n\in\mathbb N$.

(i)–(iii) are the **Peano axioms**; (iii) is the **induction axiom**. (i) and (ii) say any two of $1,1+1,\dots$ are distinct; (iii) says the list is complete (take $P(n)=$ "$n$ is on the list").

**Arithmetic.** Write $2=1+1$, $3=1+1+1$, etc. Define "$+k$" for every $k$ by
$$n+(k+1)=(n+k)+1\qquad\text{for every }n\in\mathbb N,$$
by induction on $k$ with $P(k)=$ "$+k$ is defined": $+1$ is defined, and if $n+k$ is defined then so is $(n+k)+1$, which defines $n+(k+1)$. Multiplication and powers are defined similarly. One may check, for all $a,b,c$:

| | Rule | | Rule |
| --- | --- | --- | --- |
| (i) | $a+b=b+a$ | (iv) | $a(bc)=(ab)c$ |
| (ii) | $ab=ba$ | (v) | $a(b+c)=ab+ac$ |
| (iii) | $a+(b+c)=(a+b)+c$ | | |

**Order.** Define $a<b$ if $a+c=b$ for some $c\in\mathbb N$. Then for all $a,b,c$:
(vi) $a<b\Rightarrow a+c<b+c$; (vii) $a<b\Rightarrow ac<bc$; (viii) $a<b$ and $b<c\Rightarrow a<c$; (ix) $\neg(a<a)$.

### Definition — Strong induction and well-ordering

The induction axiom is the **weak principle of induction (WPI)**. The **strong principle of induction (SPI)**: if

1. $P(1)$ holds, and
2. $\forall n\in\mathbb N$: $\big(P(m)\ \forall m\le n\big)\Rightarrow P(n+1)$,

then $P(n)$ holds for all $n\in\mathbb N$.

WPI and SPI are equivalent. Clearly SPI $\Rightarrow$ WPI. For WPI $\Rightarrow$ SPI, apply WPI to $Q(n)=$ "$P(m)$ holds $\forall m\le n$".

The **well-ordering principle (WOP)**: if $P(n)$ holds for some $n\in\mathbb N$, there is a least $n\in\mathbb N$ such that $P(n)$ holds. Equivalently, every non-empty subset of $\mathbb N$ has a minimal element.

### Theorem 1 — Strong induction implies well-ordering

SPI $\Rightarrow$ WOP.

**Proof.** Suppose there is no least $n$ with $P(n)$. We show by SPI that $P(n)$ holds for no $n$. Let $Q(n)=\neg P(n)$.

- $Q(1)$ holds: otherwise $1$ would be the minimal element with $P$.
- Given $n$, suppose $Q(k)$ for all $k<n$, i.e. $P(k)$ is false for all $k<n$. Then $P(n)$ is false, otherwise $n$ would be the minimal element with $P$. So $Q(n)$ holds.

By SPI, $Q(n)$ holds for all $n$, i.e. $P(n)$ is false for all $n$.

**Method (least counterexample).** To prove $P(n)$ for all $n$: if not, WOP gives a minimal counterexample, from which we try to derive a contradiction.

## 1.2 The integers and the rationals

**Integers.** $\mathbb Z$ consists of the symbols $n,-n$ for $n\in\mathbb N\cup\{0\}$. Define $+$ and $\cdot$ from $\mathbb N$; rules (i)–(v) hold, and also

- (x) $\forall a\in\mathbb Z,\ a+0=a$ (identity for $+$);
- (xi) $\forall a\in\mathbb Z\ \exists b\in\mathbb Z,\ a+b=0$ (inverse for $+$).

Define $a<b$ if $a+c=b$ for some $c\in\mathbb N$. Rules (vi), (viii), (ix) still hold, but (vii) becomes
$$\text{(vii}'\text{)}\qquad \forall a,b,c\in\mathbb Z:\ a<b\text{ and }c>0\ \Rightarrow\ ac<bc.$$

**Rationals.** $\mathbb Q$ consists of expressions $\frac ab$ with $a,b\in\mathbb Z$, $b\ne0$, where $\frac ab$ and $\frac cd$ are the same if $ad=bc$. Define
$$\frac ab+\frac cd=\frac{ad+bc}{bd},$$
and check this does not depend on how the fractions are written. Multiplication is defined similarly, and for $b,d>0$, $\frac ab<\frac cd$ if $ad<bc$. All preceding rules apply, and $\mathbb N\subseteq\mathbb Z\subseteq\mathbb Q$.

## 1.3 Primes

### Definition — Divisibility and primes

For $a,b\in\mathbb Z$, **$a$ divides $b$**, written $a\mid b$, if $\exists c\in\mathbb Z$ with $b=ac$ ("$a$ is a divisor/factor of $b$", "$b$ is a multiple of $a$"). For any $b$, $\pm1$ and $\pm b$ are factors; all other factors are **proper** (non-trivial).

A natural number $n\ge2$ is **prime** if its only factors are $\pm1,\pm n$; otherwise it is **composite**.

### Proposition 2 — Existence of prime factorization

Every natural number $n\ge2$ can be written as a product of primes.

**Proof.** By (strong) induction on $n$. True for $n=2$. Let $n>2$ and suppose the claim holds for $2,\dots,n-1$. If $n$ is prime, done. If $n$ is composite, $n=ab$ with $1<a,b<n$; by the induction hypothesis $a=p_1\cdots p_k$, $b=q_1\cdots q_\ell$ for primes $p_i,q_j$. Hence $n=p_1\cdots p_kq_1\cdots q_\ell$.

### Theorem 3 — Infinitely many primes

There are infinitely many primes.

**Proof.** Suppose the primes are $p_1,\dots,p_k$. Let $N=p_1p_2\cdots p_k+1$. Then $p_1\nmid N$, else $p_1\mid N-p_1\cdots p_k=1$. Likewise none of $p_2,\dots,p_k$ divides $N$, contradicting that $N$ is a product of primes (Proposition 2).

**Uniqueness?** Proposition 2 does not give uniqueness. $21=3\cdot7$ is clearly unique, but what about $295869=3\cdot7\cdot73\cdot193$? Why is $9049\cdot40099\ne6701\cdot54151$? This is answered by [[#Theorem 9 — Fundamental theorem of arithmetic|Theorem 9]], whose key input is:

**Proposition 4 (Euclid's lemma).** If $p$ is prime and $p\mid ab$, then $p\mid a$ or $p\mid b$. *(Proved below, after Bézout.)*

## 1.4 Highest common factors and Euclid's algorithm

### Definition — Highest common factor

For $a,b\in\mathbb N$, a natural number $c$ is the **highest common factor** (hcf) or **greatest common divisor** (gcd) of $a,b$ if

1. $c\mid a$ and $c\mid b$ ($c$ is a common factor), and
2. $d\mid a$ and $d\mid b$ $\Rightarrow$ $d\mid c$ (every common divisor divides $c$).

Write $c=\operatorname{hcf}(a,b)=\gcd(a,b)=(a,b)$.

**Example.** Factors of $12$: $1,2,3,4,6,12$; of $18$: $1,2,3,6,9,18$. Common factors $1,2,3,6$, so $\gcd(12,18)=6$. We still need to show $\gcd(a,b)$ always exists.

### Proposition 5 — Division algorithm

Let $n,k\in\mathbb N$. Then $n=qk+r$ for integers $q,r$ with $0\le r\le k-1$; moreover $q,r$ are unique.

**Proof.** Induction on $n$. True for $n=1$ ($q=1,r=0$ if $k=1$; $q=0,r=1$ if $k>1$). Suppose $n\ge2$ and $n-1=qk+r$ with $0\le r\le k-1$.

- If $r<k-1$: $n=(n-1)+1=qk+(r+1)$.
- If $r=k-1$: $n=qk+k-1+1=(q+1)k$.

**Uniqueness.** If $n=qk+r=q'k+r'$ then $(q-q')k=r'-r$, and $-k<r'-r<k$. The only multiple of $k$ in that range is $0$, so $q=q'$, $r=r'$.

### Theorem 6 — Euclid's algorithm computes the gcd

**Euclid's algorithm.** Input $a,b\in\mathbb N$; divide repeatedly:

| Step | Division | Remainder | Example $a=372,\ b=162$ |
| --- | --- | --- | --- |
| 1 | $a=q_1b+r_1$ | $0\le r_1\le b-1$ | $372=2\cdot162+48$ |
| 2 | $b=q_2r_1+r_2$ | $0\le r_2\le r_1-1$ | $162=3\cdot48+18$ |
| 3 | $r_1=q_3r_2+r_3$ | $0\le r_3\le r_2-1$ | $48=2\cdot18+12$ |
| $\vdots$ | | | $18=1\cdot12+6$ |
| $n$ | $r_{n-2}=q_nr_{n-1}+r_n$ | $0\le r_n\le r_{n-1}-1$ | $12=2\cdot6$ |
| $n+1$ | $r_{n-1}=q_{n+1}r_n+0$ | $r_{n+1}=0$ | |

**Output:** $r_n$, the last non-zero remainder ($6$ in the example). The algorithm terminates in $n<b$ steps since $b>r_1>r_2>\dots>r_n>0$.

**Theorem 6.** The output of Euclid's algorithm with input $a,b$ is $\gcd(a,b)$.

**Proof.** (i) $r_n\mid r_{n-1}$ (as $r_{n+1}=0$), so $r_n\mid r_{n-2}$, and by induction $r_n\mid r_i$ for all $i$. Hence $r_n\mid b$ (step 2) and $r_n\mid a$ (step 1).

(ii) If $\alpha\mid a$ and $\alpha\mid b$, then $\alpha\mid r_1$ (step 1), $\alpha\mid r_2$ (step 2), and by induction $\alpha\mid r_i$ for all $i\le n$.

So $r_n$ satisfies both conditions of the gcd.

**Example.** $\gcd(87,52)$:
$$87=1\cdot52+35,\quad 52=1\cdot35+17,\quad 35=2\cdot17+1,\quad 17=17\cdot1,$$
so $\gcd(87,52)=1$. When $\gcd(a,b)=1$, $a$ and $b$ are **coprime**.

## 1.5 Bézout's identity

Euclid's algorithm can be **reversed**:
$$\begin{aligned}
1&=35-2\cdot17=35-2(52-35)=-2\cdot52+3\cdot35\\
&=-2\cdot52+3(87-52)=-5\cdot52+3\cdot87.
\end{aligned}$$

### Theorem 7 — Bezout's identity

$\forall a,b\in\mathbb N\ \exists x,y\in\mathbb Z$ such that $xa+yb=\gcd(a,b)$. ("$\gcd(a,b)$ is a linear combination of $a$ and $b$.")

**Proof 1 (reverse Euclid).** Run Euclid's algorithm to get the output $r_n$. Step $n$ gives $r_n=xr_{n-1}+yr_{n-2}$ for some $x,y\in\mathbb Z$. Step $n-1$ expresses $r_{n-1}=xr_{n-2}+yr_{n-3}$, so substituting, $r_n=xr_{n-2}+yr_{n-3}$ for some (new) $x,y\in\mathbb Z$. Continuing inductively, $r_n=xr_i+yr_{i-1}$ for some $x,y\in\mathbb Z$, for each $i=2,\dots,n-1$. Steps 1 and 2 then give $r_n=xa+yb$.

**Remark.** This not only proves existence of $x,y$ but gives a method to find them.

**Proof 2 (least positive combination).** Let $h$ be the least positive integer of the form $xa+yb$ with $x,y\in\mathbb Z$ (it exists by WOP, since $a=1a+0b>0$). We show $h=\gcd(a,b)$.

- (ii): if $d\mid a$ and $d\mid b$ then $d\mid xa+yb$ for all $x,y$, in particular $d\mid h$.
- (i): suppose $h\nmid a$. Write $a=qh+r$ with $0<r<h$. Then $r=a-qh=a-q(xa+yb)$ is also a positive linear combination of $a,b$, strictly smaller than $h$ — contradiction. So $h\mid a$, and by the same argument $h\mid b$.

**Remark.** Proof 2 shows $\gcd(a,b)$ exists and is a linear combination of $a,b$, but gives no way to find $\gcd(a,b)$ or the coefficients.

**Examples.** $160x+72y=33$ has no integer solution (left side even, right side odd). $87x+52y=33$ does: from $87x'+52y'=1$ (with $x'=3$, $y'=-5$), take $x=33x'$, $y=33y'$.

### Corollary 8 — Bezout's theorem

Let $a,b\in\mathbb N$. The equation $ax+by=c$ has an integer solution if and only if $\gcd(a,b)\mid c$.

**Proof.** Let $h=\gcd(a,b)$.
($\Rightarrow$) If $ax+by=c$, then since $h\mid a$ and $h\mid b$, also $h\mid c$.
($\Leftarrow$) If $h\mid c$: by Theorem 7, $h=ax+by$ for some $x,y\in\mathbb Z$, so
$$c=\frac ch\cdot h=\frac ch(ax+by)=a\Big(\frac{cx}h\Big)+b\Big(\frac{cy}h\Big).$$

### Proposition 4 — Euclid's lemma

If $p$ is prime and $p\mid ab$, then $p\mid a$ or $p\mid b$.

**Proof.** Suppose $p\mid ab$ but $p\nmid a$; we show $p\mid b$. Since $p$ is prime and $p\nmid a$, $\gcd(p,a)=1$, so by Theorem 7 there are $x,y\in\mathbb Z$ with $xp+ya=1$. Then
$$xpb+yab=b,$$
and $p$ divides both terms on the left ($p\mid p$ and $p\mid ab$), so $p\mid b$.

**Remarks.**
1. Similarly $p\mid a_1a_2\cdots a_n\Rightarrow p\mid a_i$ for some $i$: Proposition 4 gives $p\mid a_1$ or $p\mid a_2\cdots a_n$, then induct on the number of factors.
2. We do need $p$ prime (e.g. $6\mid 2\cdot3$ but $6\nmid2$, $6\nmid3$).

## 1.6 Unique factorization

### Theorem 9 — Fundamental theorem of arithmetic

Every natural number $n\ge2$ is expressible as a product of primes, uniquely up to reordering.

**Proof.** Existence is Proposition 2. Uniqueness by (strong) induction on $n$; true for $n=2$. Given $n>2$, suppose $n=p_1p_2\cdots p_k=q_1q_2\cdots q_\ell$ with all $p_i,q_j$ prime. We want $k=\ell$ and, after reordering, $p_i=q_i$ for all $i$.

$p_1\mid n=q_1\cdots q_\ell$, so by Proposition 4 (Remark 1) $p_1\mid q_i$ for some $i$; relabelling, $p_1\mid q_1$. Since $q_1$ is prime, $p_1=q_1$. So
$$\frac n{p_1}=p_2\cdots p_k=q_2\cdots q_\ell<n,$$
and by the induction hypothesis $k=\ell$ and, after reordering, $p_2=q_2,\dots,p_k=q_\ell$. (If $n/p_1=1$ both products are empty.)

**Remark — non-unique factorization.** There are "arithmetical systems" with $+$ and $\times$ in which factorization is **not** unique. In $\mathbb Z[\sqrt{-3}]=\{x+y\sqrt{-3}=x+yi\sqrt3:\ x,y\in\mathbb Z\}$, sums and products stay in the set, e.g.
$$(1+\sqrt{-3})+(1-\sqrt{-3})=2,\qquad (1+\sqrt{-3})(1-\sqrt{-3})=4.$$
One can define "prime" in $\mathbb Z[\sqrt{-3}]$, and $1\pm\sqrt{-3}$ are prime in this sense — but also $4=2\cdot2$, so factorization is not unique.

> [!note] Explanation
> "Prime" here means "cannot be split into two factors other than $\pm1$". Using $N(x+y\sqrt{-3})=x^2+3y^2$ (multiplicative): $2$ and $1\pm\sqrt{-3}$ all have $N=4$, and no element has $N=2$, so none of them splits.

### Applications of Theorem 9

**(1) Divisors.** The factors of $n=2^3\cdot3^7\cdot11$ are exactly $2^a3^b11^c$ with $0\le a\le3$, $0\le b\le7$, $0\le c\le1$. There are no others: if e.g. $7\mid n$, we would get a factorization of $n$ involving $7$, contradicting uniqueness. In general the factors of $n=p_1^{a_1}\cdots p_k^{a_k}$ are exactly $p_1^{b_1}\cdots p_k^{b_k}$ with $0\le b_i\le a_i$.

**(2) Common factors and gcd.** The common factors of $2^3\cdot3^7\cdot5\cdot11^3$ and $2^4\cdot3^2\cdot11\cdot13$ are $2^a3^b11^c$ with $0\le a\le3$, $0\le b\le2$, $0\le c\le1$, so the gcd is $2^3\cdot3^2\cdot11$. In general, for $a_i,b_i\ge0$,
$$\gcd\Big(\prod p_i^{a_i},\ \prod p_i^{b_i}\Big)=\prod p_i^{\min(a_i,b_i)}.$$

**(3) Common multiples and lcm.** The common multiples of the two numbers in (2) are $2^a3^b5^c11^d13^e$ times any integer, with $a\ge4,b\ge7,c\ge1,d\ge3,e\ge1$. So $2^4\cdot3^7\cdot5\cdot11^3\cdot13$ is a common multiple and every common multiple is a multiple of it: it is the **least common multiple** (lcm). In general
$$\operatorname{lcm}\Big(\prod p_i^{a_i},\ \prod p_i^{b_i}\Big)=\prod p_i^{\max(a_i,b_i)}.$$
Since $\min(a_i,b_i)+\max(a_i,b_i)=a_i+b_i$, we get $\gcd(x,y)\operatorname{lcm}(x,y)=xy$.

**(4) Another proof of Theorem 3 (Erdős, 1930).** Let $p_1,\dots,p_k$ be all the primes. Every number is uniquely $p_1^{j_1}\cdots p_k^{j_k}$; rewrite this as
$$p_1^{j_1}\cdots p_k^{j_k}=m^2\,p_1^{i_1}\cdots p_k^{i_k},\qquad i_\ell\in\{0,1\}.\tag{$*$}$$
Let $N\in\mathbb N$. A number $\le N$ of the form $(*)$ has $m\le\sqrt N$, so there are at most $\sqrt N\cdot2^k$ such numbers $\le N$. If $N>\sqrt N\cdot2^k$, i.e. $N>4^k$, some number $\le N$ is not of the form $(*)$, so it has a prime factor outside $\{p_1,\dots,p_k\}$ — contradiction.

Proof 1 gives $k$th prime $<2^{2^k}$; proof 2 gives $k$th prime $<4^k$. In fact $k$th prime $\sim k\log k$ (prime number theorem; not proved here).

## 1.7 Modular arithmetic

### Definition — Integers modulo n

Let $n\ge2$. The **integers modulo $n$**, written $\mathbb Z_n$ or $\mathbb Z/n\mathbb Z$, are the integers with two regarded as the same if they differ by a multiple of $n$ (e.g. in $\mathbb Z_7$, $2$ is the same as $16$). Write $x\equiv y\pmod n$, $x\equiv y\ (n)$, or $x=y$ in $\mathbb Z_n$:
$$x\equiv y\pmod n\iff n\mid x-y\iff x=y+kn\text{ for some }k\in\mathbb Z.$$

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (0,0) circle (1.35);
  \foreach \a in {90,50,8,-42,-92,155,120} \draw[thick] (\a:1.27)--(\a:1.43);
  \node[above] at (90:1.48) {$0=n$};
  \node[above right] at (50:1.48) {$1$};
  \node[right] at (8:1.48) {$2$};
  \node[below right] at (-42:1.48) {$3$};
  \node[below] at (-92:1.48) {$4$};
  \node[left] at (155:1.48) {$n-2$};
  \node[above left] at (120:1.48) {$n-1$};
\end{tikzpicture}
\end{document}
```
*$\mathbb Z_n$ viewed as a clock.*

**Arithmetic is well defined.** If $a\equiv a'$ and $b\equiv b'\pmod n$, then
$$n\mid(a-a')+(b-b')=(a+b)-(a'+b'),\qquad n\mid(a-a')b+a'(b-b')=ab-a'b',$$
so $a+b\equiv a'+b'$ and $ab\equiv a'b'\pmod n$. So we can do arithmetic modulo $n$, inheriting the usual rules from $\mathbb Z$.

**Example.** $2a^2+3b^2=1$ has no solution with $a,b\in\mathbb Z$: a solution gives $2a^2\equiv1\pmod3$, but $2\cdot0^2\equiv0$, $2\cdot1^2\equiv2$, $2\cdot2^2\equiv2\pmod 3$.

### Definition — Units modulo n

**Example.** Solve $7x\equiv2\pmod{10}$. Since $3\cdot7\equiv1\pmod{10}$, multiply by $3$: $x\equiv3\cdot2=6\pmod{10}$.

Given $a,b\in\mathbb Z$, **$b$ is an inverse of $a$ modulo $n$** if $ab\equiv1\pmod n$. Then $a$ is **invertible** modulo $n$, or a **unit** modulo $n$. E.g. in $\mathbb Z_{10}$, $3$ is an inverse of $7$ and both are units; $4$ is not a unit, since $4x\not\equiv1\pmod{10}$ for all $x\in\mathbb Z$.

**Remark.** If $a$ is a unit modulo $n$:

1. Its inverse is unique: if $ab\equiv ab'\equiv1$, then $b\equiv bab'\equiv b'\pmod n$.
2. So we may write $a^{-1}$ for it.
3. If $ab\equiv ac\pmod n$ then $b\equiv c\pmod n$ — "we can cancel units", multiplying both sides by $a^{-1}$. This is false in general: $4\cdot3\equiv4\cdot8\pmod{10}$ but $3\not\equiv8$.

### Proposition 10 — Units modulo a prime

Let $p$ be prime. Then every $a\not\equiv0\pmod p$ is a unit modulo $p$.

**Proof.** $\operatorname{hcf}(a,p)=1$, so $ax+py=1$ for some $x,y\in\mathbb Z$ (Theorem 7). Then $ax=1-py$, so $ax\equiv1\pmod p$.

### Proposition 10' — Units modulo n

Let $n\ge2$. Then $a$ is a unit modulo $n$ iff $\operatorname{hcf}(a,n)=1$.

**Proof.**
$$\operatorname{hcf}(a,n)=1\iff ax+ny=1\text{ for some }x,y\in\mathbb Z\iff ax=1-ny\iff ax\equiv1\pmod n\text{ for some }x.$$
(The first $\iff$ is Corollary 8 with $c=1$.)

### Corollary 11 — Solving linear congruences

If $\operatorname{hcf}(a,n)=1$, the congruence $ax\equiv b\pmod n$ has a unique solution modulo $n$. In particular, $a$ has a unique inverse modulo $n$.

> [!note] Explanation
> By Proposition 10′, $a^{-1}$ exists; $x\equiv a^{-1}b$ is a solution, and any solution satisfies $x\equiv a^{-1}ax\equiv a^{-1}b$.

**The case $\operatorname{hcf}(a,n)=\alpha>1$.** If there is a solution, then $n\mid ax-b$, so $\alpha\mid ax-b$; also $\alpha\mid a$, hence $\alpha\mid b$. Conversely, if $\alpha\mid b$, write $n=\alpha n'$, $a=\alpha a'$, $b=\alpha b'$. Then
$$ax\equiv b\ (n)\iff ax-b=kn\iff\alpha a'x-\alpha b'=k\alpha n'\iff a'x-b'=kn'\iff a'x\equiv b'\ (n'),$$
and $\operatorname{hcf}(a',n')=1$, so this has a unique solution mod $n'$.

**Summary.** If $\operatorname{hcf}(a,n)=\alpha>1$, then $ax\equiv b\pmod n$ has no solution unless $\alpha\mid b$, in which case its solutions are exactly those of $\frac a\alpha x\equiv\frac b\alpha\pmod{\frac n\alpha}$.

**Examples.**
1. $7x\equiv4\pmod{30}$. $\operatorname{hcf}(7,30)=1$ and Euclid gives $13\cdot7-3\cdot30=1$, so $13\cdot7\equiv1\pmod{30}$ and $x\equiv13\cdot4\equiv22\pmod{30}$. If $x'$ is another solution, $7x\equiv7x'$, so $x\equiv x'\pmod{30}$ since $7$ is a unit. Short form:
   $$7x\equiv4\ (30)\iff13\cdot7x\equiv13\cdot4\ (30)\iff x\equiv22\ (30).$$
2. $10x\equiv12\pmod{34}$:
   $$10x=12+34y\iff5x=6+17y\iff5x\equiv6\ (17)\iff x\equiv6\cdot7\ (17)\iff x\equiv8\ (17),$$
   using $5\cdot7=35\equiv1\pmod{17}$.

## 1.8 Simultaneous congruences

"How many soldiers in Han Xin's army? In rows of 3, 2 are left; in rows of 4, 1 is left." So $x\equiv1\pmod4$ ($x=1,5,9,\dots$) and $x\equiv2\pmod3$ ($x=2,5,8,\dots$).

What about $x\equiv1\pmod4$ ($1,5,9,13,17,21,\dots$) and $x\equiv2\pmod6$ ($2,8,14,20,26,32,\dots$)?

> [!note] Explanation
> The first list is all odd and the second all even, so there is no common solution: $4$ and $6$ are not coprime, which is why Theorem 12 assumes coprime moduli.

### Theorem 12 — Chinese Remainder Theorem

Let $m,n$ be coprime and $a,b\in\mathbb Z$. Then there is a unique solution modulo $mn$ to the simultaneous congruences
$$x\equiv a\pmod m\quad\text{and}\quad x\equiv b\pmod n.$$

> [!todo] p. 23 — the notebook ends after the statement; add the proof when the next lecture is synced.
