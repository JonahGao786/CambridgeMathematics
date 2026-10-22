---
title: Numbers and Sets - Chapter 0 Proofs
course: Part IA Numbers and Sets
material_type: lecture notes
chapter: 0
source_file: Ch.0 Proofs.pdf
drive_file_id: 1eCbmGml6mnoT9KYo8YHBIBmp8iPB_l_F
source_url: https://drive.google.com/file/d/1eCbmGml6mnoT9KYo8YHBIBmp8iPB_l_F/view
source_pages: 9
tags: [lecture, numbers-and-sets]
---

# Numbers and Sets — Chapter 0: Proofs

> [!abstract] Overview
> What a proof is, and the common ways proofs go right or wrong: direct proof, proving the converse by mistake, counterexamples, contradiction/contrapositive, two-directional ("iff") proofs, and unjustified assumptions. Ends with truth tables and negating quantifiers.
> Course chapters: I Elementary Number Theory · II The Reals · III Sets and Functions · IV Countability (4 example sheets).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Assertion — n cubed minus n is a multiple of 3]] | direct proof by factorizing | 4 |
| [[#Assertion — if n squared is even then n is even]] | wrong proof (converse), then proof by contradiction | 4–5 |
| [[#False assertion — multiples of 9]] | one counterexample disproves | 4 |
| [[#Assertion — solutions of a quadratic]] | an "iff" needs both directions | 6 |
| [[#False claim — every positive real is at least 1]] | unjustified existence assumption | 7 |
| [[#Truth tables]] | $\land,\lor,\neg$; contrapositive | 8 |
| [[#Negating quantifiers]] | $\neg\forall=\exists\neg$, $\neg\exists=\forall\neg$ | 9 |

## 0.1 What a proof is

A **proof** is a sequence of true statements, without logical gaps, establishing some conclusion. We have to start somewhere, with agreed assumptions (**axioms**).

We prove things because we want to know **that** they are true, we hope to gain insight into **why** they are true, and sometimes the proof is beautiful.

**Examples of statements.**

| | Statement | Status |
| --- | --- | --- |
| 1 | There are infinitely many primes $p$ such that $2p+1$ is also prime. | No-one knows if it is true. |
| 2 | There are infinitely many primes $p$ such that one of $p+2,p+4,\dots,p+240$ is also prime. | Proved in August 2026. |
| 3 | For every integer $n\ge 2$ there is a prime $p\in(n,2n)$. | Not obvious, but true. |
| 4 | No computer algorithm factors an $n$-digit integer in at most $n^3$ steps. | Would be a disaster if false. |
| 5 | Every non-constant polynomial with complex coefficients has a complex root. | [[Fundamental Theorem of Algebra]] |
| 6 | For all $m,n\in\mathbb Z$, $mn=nm$. | Worth thinking about. |
| 7 | $1+1=2$. | Does it need proving? |

## 0.2 Proofs and non-proofs

### Assertion — n cubed minus n is a multiple of 3

For every positive integer $n$, $n^3-n$ is a multiple of $3$.

**Proof.** $n^3-n=n(n^2-1)=(n-1)n(n+1)$. One of the three consecutive integers $n-1,n,n+1$ is a multiple of $3$, hence so is their product.

### Assertion — if n squared is even then n is even

For any $n\in\mathbb Z^+$, if $n^2$ is even then $n$ is even.

> [!warning] Wrong proof
> Given an even integer $n$, write $n=2k$ with $k\in\mathbb Z^+$. Then $n^2=(2k)^2=2(2k^2)$, which is even.
>
> This proves the **converse**. We want "if $A$ then $B$" but have shown "if $B$ then $A$".

**Proof (by contradiction).** Suppose on the contrary that $n^2$ is even but $n$ is odd. Write $n=2k+1$ with $k\in\mathbb Z$. Then
$$n^2=(2k+1)^2=4k^2+4k+1=4(k^2+k)+1,$$
which is odd, contradicting the assumption that $n^2$ is even.

To show "if $A$ then $B$" we showed there is no case where $A$ is true and $B$ is false. In other words, showing $A\Rightarrow B$ ("if $A$ then $B$", "$A$ implies $B$") is the same as showing the **contrapositive** $\neg B\Rightarrow\neg A$. See [[Proof by Contradiction and Contraposition]].

### False assertion — multiples of 9

"For any $n\in\mathbb Z^+$, if $n^2$ is a multiple of $9$, then so is $n$." This is simply false: take $n=3$.

To show "if $A$ then $B$" is false, it is enough to exhibit one instance where $A$ is true and $B$ is false. **One counterexample is enough.**

### Assertion — solutions of a quadratic

The solutions of $x^2-5x+6=0$ are $x=2$ or $x=3$.

This is really two assertions: (i) $x=2$ and $x=3$ are solutions; (ii) there are no other solutions.

**Proof.** (i) If $x=2$ or $x=3$, then $x-2=0$ or $x-3=0$, so $(x-2)(x-3)=0$, so $x^2-5x+6=0$.

(ii) If $x^2-5x+6=0$, then $(x-2)(x-3)=0$, so $x-2=0$ or $x-3=0$, so $x=2$ or $x=3$.

Alternatively, in one chain:
$$x=2\text{ or }x=3\iff x-2=0\text{ or }x-3=0\iff(x-2)(x-3)=0\iff x^2-5x+6=0.$$
Here $\iff$ means "if and only if", i.e. "$A\Rightarrow B$ and $B\Rightarrow A$", i.e. "is equivalent to". **It is vital that every step is $\iff$.**

### False claim — every positive real is at least 1

> [!warning] Wrong proof
> Let $r$ be the least positive real. Either $r=1$, $r<1$ or $r>1$. If $r<1$ then $0<r^2<r$, contradicting minimality of $r$. If $r>1$ then $0<1<r$, again a contradiction. Hence $r=1$.
>
> Nonsense: we do not know that there **is** a least positive real (indeed $r/2$ is always smaller).

**Moral.** Every claim must be justified.

## 0.3 Combining claims

### Truth tables

For assertions $A,B$ write $A\land B$ for "$A$ and $B$", $A\lor B$ for "$A$ or $B$" (inclusive), and $\neg A$ for "not $A$".

| $A$ | $B$ | $A\land B$ | $A\lor B$ | $\neg A$ | $\neg B$ |
| --- | --- | --- | --- | --- | --- |
| F | F | F | F | T | T |
| T | F | F | T | F | T |
| F | T | F | T | T | F |
| T | T | T | T | F | F |

Comparing truth tables:

- $\neg(A\land B)$ is equivalent to $(\neg A)\lor(\neg B)$.
- $A\Rightarrow B$ is equivalent to $(\neg A)\lor B$, hence to $B\lor(\neg A)$, hence to $(\neg B)\Rightarrow(\neg A)$.

Assertions may involve **quantifiers**: $\forall a$ ("for all $a$") and $\exists b$ ("there exists $b$").

### Negating quantifiers

$$\neg\big(\forall x\ A(x)\big)\ \text{ means }\ \exists x\ \neg A(x),\qquad
\neg\big(\exists x\ B(x)\big)\ \text{ means }\ \forall x\ \neg B(x).$$

See [[Logical Connectives and Quantifiers]].
