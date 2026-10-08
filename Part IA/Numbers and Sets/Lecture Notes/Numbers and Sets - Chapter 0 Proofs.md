---
title: Numbers and Sets - Chapter 0 Proofs
material_type: handwritten lecture notes
course: Part IA Numbers and Sets
date: 2026–27
source_file: Ch.0 Proofs.pdf
drive_file_id: 1eCbmGml6mnoT9KYo8YHBIBmp8iPB_l_F
source_url: https://drive.google.com/file/d/1eCbmGml6mnoT9KYo8YHBIBmp8iPB_l_F/view
duplicate_source_file: Untitled Notebook.pdf
duplicate_drive_file_id: 1uBB2lbhifeSfjmU7LYXEj-ldQJdKCzdn
source_pages: 5
---

# Numbers and Sets — Chapter 0: Proofs

Sources: [Ch.0 Proofs.pdf](https://drive.google.com/file/d/1eCbmGml6mnoT9KYo8YHBIBmp8iPB_l_F/view) and [Untitled Notebook.pdf](https://drive.google.com/file/d/1uBB2lbhifeSfjmU7LYXEj-ldQJdKCzdn/view). Both documents were visually read in full and compared page by page: all five rendered pages are identical. Their Drive records remain separate in the sync manifest.

## Course outline (page 1)

Numbers and Sets, academic year 2026–27:

1. Elementary Number Theory.
2. The Reals.
3. Sets and Functions.
4. Countability.

There will be four examples sheets.

## What a proof does (page 2)

A proof is a sequence of true statements, without logical gaps, establishing a conclusion. We have to start somewhere, with agreed assumptions: axioms.

We want to prove things because:

- We want to know **that** they are true.
- We hope to gain insight into **why** they are true.
- We might be lucky, and the proof is beautiful.

## Examples of statements (page 3)

The accompanying remarks below are remarks recorded in the lecture, rather than proofs supplied by these notes.

| No. | Statement | Recorded remark |
| --- | --- | --- |
| 1 | There are infinitely many primes $p$ such that $2p+1$ is also prime. | “No-one knows if it's true.” |
| 2 | There are infinitely many primes $p$ such that at least one of $p+2,p+4,p+6,\ldots,p+240$ is also prime. | “Was proved in Aug. 2026.” No reference or proof is supplied. |
| 3 | For every integer $n\ge2$, there is a prime $p\in(n,2n)$. | “Not obvious but true.” |
| 4 | There is no computer algorithm that will factor an $n$-digit integer in at most $n^3$ steps. | “Would be a disaster if false.” |
| 5 | Every non-constant polynomial with complex coefficients has a root in the complex numbers. | The [[Fundamental Theorem of Algebra]]. |
| 6 | For all $m,n\in\mathbb Z$, $mn=nm$. | “Worth thinking about…” |
| 7 | $1+1=2$. | “Does it need proving?” |

These statements and historical remarks are retained as examples from the lecture, without an independent claim of verification.

## A direct proof (page 4, top)

**Assertion.** For every positive integer $n$, $n^3-n$ is a multiple of $3$.

**Proof.** For $n\in\mathbb Z_{>0}$,
$$
n^3-n=n(n^2-1)=(n-1)n(n+1).
$$
One of the three consecutive integers $n-1,n,n+1$ is a multiple of $3$, so their product is a multiple of $3$. $\square$

## A non-proof: proving the converse (page 4, middle)

**Assertion.** For $n\in\mathbb Z_{>0}$, if $n^2$ is even, then $n$ is even.

The source crosses out the label “Proof” and its end-of-proof square on the following attempt:

> Given an even integer $n$, write $n=2k$, where $k\in\mathbb Z_{>0}$. Then
> $$n^2=(2k)^2=2(2k^2),$$
> so $n^2$ is even.

This proves the converse. We want to show “if $A$, then $B$”, but have shown “if $B$, then $A$”. It does not establish the assertion. See [[Proof by Contradiction and Contraposition]] for the valid argument on the next page.

## Disproving an assertion (page 4, bottom)

**False assertion.** For $n\in\mathbb Z_{>0}$, if $n^2$ is a multiple of $9$, then $n$ is a multiple of $9$.

Take $n=3$: $n^2=9$ is a multiple of $9$, but $n=3$ is not. To disprove “if $A$, then $B$”, one instance with $A$ true and $B$ false is enough.

“One counterexample is enough.”

## Proof by contradiction (page 5)

Return to the assertion: if $n^2$ is even, then $n$ is even.

**Proof.** Suppose, on the contrary, that $n^2$ is even but $n$ is odd. Write $n=2k+1$, where $k\in\mathbb Z$. Then
$$
\begin{aligned}
n^2&=(2k+1)^2\\
&=4k^2+4k+1\\
&=4(k^2+k)+1,
\end{aligned}
$$
which is odd, contradicting the assumption that $n^2$ is even. $\square$

To show “if $A$, then $B$”, this argument shows that there is no case in which $A$ is true and $B$ is false. Equivalently,
$$
\underbrace{A\Rightarrow B}_{\text{“if A then B”, or “A implies B”}}
\quad\Longleftrightarrow\quad
\neg B\Rightarrow\neg A.
$$
