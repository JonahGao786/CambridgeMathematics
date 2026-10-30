---
title: Groups - Chapter 2 Lagrange's Theorem
course: Part IA Groups
material_type: lecture notes
chapter: 2
source_file: Ch.2 Lagrange’s Theorem.pdf
drive_file_id: 1VUBm08n3ryqByd9GOlYwR6emoDA8Y0uv
source_url: https://drive.google.com/file/d/1VUBm08n3ryqByd9GOlYwR6emoDA8Y0uv/view
source_pages: 6
tags: [lecture, groups]
---

# Groups — Chapter 2: Lagrange's Theorem

> [!abstract] Overview
> Cosets cut a group $G$ into disjoint "copies" of a subgroup $H$, all the same size. Counting them gives Lagrange's theorem $|G|=|G:H|\cdot|H|$, and hence that the order of every element divides $|G|$. Consequences: $g^{|G|}=e$, groups of prime order are cyclic, and the Fermat–Euler theorem via the group of units $\mathbb Z_n^\times$.
> Prerequisites: [[Groups - Chapter 1 Examples and Definitions]] (subgroups, order of an element).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Theorem 2.1 — Lagrange (version 1)]] | $\lvert H\rvert$ divides $\lvert G\rvert$ | 1 |
| [[#Definition 2.2 — Left coset]] | $gH=\{gh:h\in H\}$; $G/H$ | 1 |
| [[#Lemma 2.3 — Cosets partition the group]] | every element lies in exactly one left coset | 2 |
| [[#Lemma 2.4 — Cosets have the size of H]] | bijection $H\to gH$ | 3 |
| [[#Definition 2.5 — Index]] | $\lvert G:H\rvert=\lvert G/H\rvert$ | 3 |
| [[#Theorem 2.6 — Lagrange (version 2)]] | $\lvert G\rvert=\lvert G:H\rvert\cdot\lvert H\rvert$ | 3–4 |
| [[#Corollary 2.7 — Order of an element divides the order of the group]] | $\operatorname{ord}(g)\mid\lvert G\rvert$ | 4 |
| [[#Corollary 2.8 — g to the order of G is e]] | $g^{\lvert G\rvert}=e$ | 4 |
| [[#Corollary 2.9 — Groups of prime order]] | prime order $\Rightarrow$ cyclic, every $g\ne e$ generates | 4–5 |
| [[#Definition 2.10 — Euler totient function]] | $\varphi(n)=\lvert\mathbb Z_n^\times\rvert$; $\mathbb Z_n^\times$ is a group | 5 |
| [[#Theorem 2.11 — Fermat–Euler]] | $x^{\varphi(n)}\equiv1\pmod n$ for $\gcd(x,n)=1$ | 6 |

## 2.1 Statement and idea

### Theorem 2.1 — Lagrange (version 1)

If $H\le G$ and $|G|<\infty$, then $|H|$ divides $|G|$.

A slightly stronger version is proved below (Theorem 2.6). **Slogan:** cut $G$ up into "copies" of $H$ called **cosets**.

## 2.2 Cosets

### Definition 2.2 — Left coset

Let $H\le G$ and $g\in G$. The **left coset** of $H$ containing $g$ is the **subset**
$$gH=\{g\cdot h:\ h\in H\}\subseteq G.$$
The set of all left cosets is $G/H=\{gH:g\in G\}$; each element of $G/H$ is itself a set.

Unless $H=\{e_G\}$, we can have $g_1H=g_2H$ with $g_1\ne g_2$. E.g. $eH=hH$ for every $h\in H$.

> [!note] Explanation
> Take $G=\mathbb Z_6$ (under $+_6$) and $H=\{0,2,4\}$. The left cosets are $0+H=H=\{0,2,4\}$ and $1+H=\{1,3,5\}$; also $2+H=H$ and $3+H=1+H$, so different $g$ can give the same coset. The two cosets cut $\mathbb Z_6$ into two pieces of size $3=|H|$, which is why $|H|$ divides $|G|=6$.

**Remark.** There are also **right cosets** $Hg=\{h\cdot g:h\in H\}$; the set of right cosets is $H\backslash G$.

### Lemma 2.3 — Cosets partition the group

If $H\le G$, the left cosets partition $G$:

1. $G=\bigcup_{gH\in G/H}gH$;
2. for all $g_1H,g_2H\in G/H$: $g_1H\cap g_2H\ne\varnothing\Rightarrow g_1H=g_2H$.

Every element of $G$ is in one and only one coset.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (0,0) ellipse (3.2 and 1.8);
  \draw (-1.7,1.35) .. controls (-1.4,0.4) and (-1.1,-0.5) .. (-0.9,-1.7);
  \draw (-1.7,1.35) .. controls (-0.7,0.9) and (0,0.5) .. (0.1,0.2);
  \draw (0.1,1.78) .. controls (0.2,0.9) and (0.2,0.4) .. (0.1,0.2);
  \draw (0.1,0.2) .. controls (0.4,-0.1) and (1.6,-0.7) .. (2.5,-1.1);
  \draw (-0.9,-1.7) .. controls (-0.4,-1) and (-0.2,-0.3) .. (0.1,0.2);
  \node at (-2.1,-0.3) {$H$};
  \node at (-0.9,0.9) {$g_1H$};
  \node at (1.4,1.0) {$g_2H$};
  \node at (0.7,-0.35) {$g_3H$};
  \node at (-0.4,-1.05) {$g_4H$};
  \node at (3.7,1.4) {$G$};
\end{tikzpicture}
\end{document}
```
*Schematic: $G$ cut into disjoint cosets.*

**Proof.** (i) For $g\in G$, $g=g\cdot e\in gH$, so $\bigcup gH=G$.

(ii) Suppose $g_1H\cap g_2H\ne\varnothing$: $g_1h_1=g_2h_2$ for some $h_1,h_2\in H$, so $g_1=g_2h_2h_1^{-1}$. For any $h\in H$,
$$g_1h=g_2\underbrace{h_2h_1^{-1}h}_{\in H}\in g_2H,$$
so $g_1H\subseteq g_2H$. Symmetrically $g_2H\subseteq g_1H$, hence $g_1H=g_2H$.

### Lemma 2.4 — Cosets have the size of H

Let $H\le G$. For every $g\in G$ there is a bijection $H\to gH$.

**Proof.** The function $H\to gH$, $h\mapsto g\cdot h$ has inverse $gH\to H$, $gh\mapsto g^{-1}gh=h$.

Updated picture: all cosets have the same size as $H$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (0,0) ellipse (3 and 1.6);
  \draw (0.1,0.05)--(0.1,1.6);
  \draw (0.1,0.05)--(2.9,0.45);
  \draw (0.1,0.05)--(-0.7,-1.5);
  \draw (0.1,0.05)--(1.9,-1.2);
  \node at (-1.6,-0.1) {$H$};
  \node at (-0.9,1.0) {$g_1H$};
  \node at (1.3,0.9) {$g_2H$};
  \node at (1.9,-0.5) {$g_3H$};
  \node at (0.5,-1.0) {$g_4H$};
\end{tikzpicture}
\end{document}
```
*Schematic: five cosets of equal size; the number of cosets is the index.*

### Definition 2.5 — Index

The **index** of a subgroup $H\le G$ is $|G:H|=|G/H|\in\mathbb N\cup\{\infty\}$.

**Exercise.** Do you get the same number (or $\infty$) if you use right cosets?

## 2.3 Lagrange's theorem

### Theorem 2.6 — Lagrange (version 2)

If $H\le G$ and $|G|<\infty$, then $|G|=|G:H|\cdot|H|$.

**Proof.**
$$|G|=\sum_{gH\in G/H}|gH|\quad\text{(Lemma 2.3: cosets partition }G)\ =\sum_{gH\in G/H}|H|\quad\text{(Lemma 2.4)}\ =|G:H|\cdot|H|.$$

### Corollary 2.7 — Order of an element divides the order of the group

If $|G|<\infty$ and $g\in G$, then $\operatorname{ord}(g)\mid|G|$.

**Proof.** $\operatorname{ord}(g)=|\langle g\rangle|$, where $\langle g\rangle$ is the subgroup generated by $g$. By Lagrange, $\operatorname{ord}(g)\mid|G|$.

### Corollary 2.8 — g to the order of G is e

If $|G|<\infty$ and $g\in G$, then $g^{|G|}=e$.

**Proof.** By Corollary 2.7, $|G|=\operatorname{ord}(g)\cdot k$ for some $k\in\mathbb N$, so
$$g^{|G|}=g^{\operatorname{ord}(g)\cdot k}=e^k=e.$$

> [!note] Explanation
> Powers of $g$ return to $e$ every $\operatorname{ord}(g)$ steps, and Lagrange says $|G|$ is a whole number of such steps. In $S_3$ ($|G|=6$): a transposition has order $2$ and $2\cdot3=6$; a $3$-cycle has order $3$ and $3\cdot2=6$; both satisfy $g^6=e$.

### Corollary 2.9 — Groups of prime order

If $|G|$ is prime, then $G$ is cyclic, and every element $g\ne e$ is a generator.

**Proof.** Pick $g\ne e$. By Corollary 2.7, $\operatorname{ord}(g)\mid|G|$, and $|G|$ is prime, so $\operatorname{ord}(g)=1$ or $\operatorname{ord}(g)=|G|$. If $\operatorname{ord}(g)=1$ then $g=e$, a contradiction. So $\operatorname{ord}(g)=|G|$. Since $\langle g\rangle\le G$ and $|\langle g\rangle|=|G|$, we get $\langle g\rangle=G$, so $g$ generates $G$.

> [!note] Explanation
> A prime $p$ has only the divisors $1$ and $p$, so every non-identity element, whose order divides $|G|=p$, must have order exactly $p$ and therefore already produces the whole group. For example every group with $5$ elements is cyclic, hence isomorphic to $C_5$ (Theorem 1.38).

## 2.4 Applications to number theory

### Definition 2.10 — Euler totient function

$$\varphi(n)=\#\{x\in\mathbb Z_n:\ \gcd(x,n)=1\}.$$

To interpret this, use multiplication on $\mathbb Z_n$, $\times_n:\mathbb Z_n\times\mathbb Z_n\to\mathbb Z_n$, $(x,y)\mapsto xy\pmod n$. It is a binary operation, associative, with identity $1$, but elements do not always have inverses. By the Euclidean algorithm, $x\in\mathbb Z_n$ has a multiplicative inverse modulo $n$
$$\iff\ \exists y,m\in\mathbb Z:\ xy+nm=1\ \iff\ \gcd(x,n)=1.$$
Upshot: $\mathbb Z_n^\times:=\{x\in\mathbb Z_n:\gcd(x,n)=1\}$ is a group with binary operation $\times_n$ and identity $1$, and $|\mathbb Z_n^\times|=\varphi(n)$.

> [!note] Explanation
> $\mathbb Z_n$ is not a group under multiplication, because some elements have no inverse; $\mathbb Z_n^\times$ keeps exactly the invertible ones, those sharing no factor with $n$. For $n=10$: $\mathbb Z_{10}^\times=\{1,3,7,9\}$, so $\varphi(10)=4$. Here $3\cdot7=21\equiv1$, so $3$ and $7$ are inverse to each other, while $2,4,5,6,8$ have no inverse (each shares a factor with $10$) and $0$ is never invertible.

### Theorem 2.11 — Fermat–Euler

Let $x,n\in\mathbb N$. If $\gcd(x,n)=1$ then $x^{\varphi(n)}\equiv1\pmod n$.

**Proof.** By Corollary 2.8 in $\mathbb Z_n^\times$, $x^{|\mathbb Z_n^\times|}=1$. Since $|\mathbb Z_n^\times|=\varphi(n)$ (Definition 2.10), the result follows.

> [!note] Explanation
> Apply "$g^{|G|}=e$" to the group $G=\mathbb Z_n^\times$, which has $\varphi(n)$ elements, and $g=x$. Example: $n=10$, $x=3$: $\varphi(10)=4$ and $3^4=81\equiv1\pmod{10}$. For $n=p$ prime, $\varphi(p)=p-1$ and this is Fermat's little theorem ([[Numbers and Sets - Chapter 1 Elementary Number Theory#Theorem 13 — Fermat's little theorem|Theorem 13]]); the number-theoretic proof there is the same argument written without group language.
