---
title: Groups 1 - Handwritten Attempts
material_type: handwritten worked solutions and incomplete attempts
course: Part IA Groups
date: null
source_file: Groups 1.pdf
drive_file_id: 17C8KN1XdaZj4KDVAvQ5tdxptR4KTmPHY
source_url: https://drive.google.com/file/d/17C8KN1XdaZj4KDVAvQ5tdxptR4KTmPHY/view
source_pages: 9
---

# Groups 1 — Handwritten Attempts

The PDF contains handwritten answers without the question statements. Their numbering and examples match [[Groups - Introductory Sheet 2026]], a separate Drive source. Consult that sheet for the supplied questions. The transcription below preserves the original claims, including errors and omitted reasoning; review callouts are editorial, not supplied solutions. The date is not written in this PDF.

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/17C8KN1XdaZj4KDVAvQ5tdxptR4KTmPHY/view).

## 1. Axioms (page 1, top)

- There exists one identity element in the group, $a\cdot e=a$.
- Each element has its own inverse, $a\cdot a^{-1}=e$.
- Associativity: $(a\cdot b)\cdot c=a\cdot(b\cdot c)$.
- Closure.

Abelian groups are commutative: $a\cdot b=b\cdot a$.

> [!todo] Manual review — page 1, question 1
> The written identity and inverse formulas are one-sided, and “closure” has no accompanying formula. Preserve these as the student's abbreviated answer; they are not a complete quantified axiom statement.

## 2. Examples (pages 1–3)

The check marks and crosses below reproduce the handwritten assessments. Unwritten commutativity answers remain unwritten.

### (i) Integers under subtraction (page 1, left)

- Identity: ✓, $0$.
- Inverse: ✓, self-inverse.
- Associativity: ✗, $(a-b)-c\ne a-(b-c)$.
- Closure: ✓, $-:\mathbb Z\times\mathbb Z\to\mathbb Z$.

> [!todo] Manual review — page 1, question 2(i), identity
> The claimed identity is not two-sided for subtraction. The original check mark is retained.

### (ii) Rationals under addition (page 1, lower left)

- Identity: ✓, $0$.
- Inverse: ✓, $a^{-1}=-a$.
- Associativity: ✓, $(a+b)+c=a+(b+c)$.
- Closure: ✓, $+:\mathbb Q\times\mathbb Q\to\mathbb Q$.

Subgroups written: $(\mathbb Z,+)$, $(\mathbb Z_{\mathrm{even}},+)$.

### (iii) Reals under multiplication (page 1, upper right)

- Identity: ✓, $1$.
- Inverse: ✗, no inverse for $0$.
- Associativity: ✓, $abc=a(bc)$.
- Closure: ✓, $\times:\mathbb R\times\mathbb R\to\mathbb R$.

### (iv) Complex operation (page 1, lower right)

- Identity: ✓, $-i$.
- Inverse: ✓, $a^{-1}=a-2i$.
- Associativity: ✓.
- Closure: ✓.

Subgroup conditions written: $\operatorname{Im}(a),\operatorname{Re}(a)\in\mathbb Z$; $\operatorname{Im}(a),\operatorname{Re}(a)\in\mathbb Q$.

> [!todo] Manual review — page 1, question 2(iv), inverse
> The formula $a^{-1}=a-2i$ is written without a minus sign before $a$ and appears inconsistent with the supplied operation. It has not been repaired.

### (v) Cross product (page 2, top)

- Identity: ✗.
- Inverse: ✗, $\mathbf b\times\mathbf b^{-1}=e$, but identity doesn't exist.
- Associativity: ✗. Let $\mathbf b\parallel\mathbf c$; the written comparison is $\mathbf a\times\mathbf b\times\mathbf c\ne\mathbf a\times(\mathbf b\times\mathbf c)$.
- Closure: ✗. $\mathbf b\parallel\mathbf c$, $\mathbf b\times\mathbf c=0$, not in set.

> [!todo] Manual review — page 2, question 2(v), associativity
> The left-hand cross product has no parentheses. Its intended grouping is not specified; do not silently insert one.

### (vi) Invertible real matrices (page 2, upper middle)

- Identity: ✓, $e=I$.
- Inverse: ✓, $\det(A)\ne0$.
- Associativity: ✓.
- Closure: ✓, $\det(AB)=\det(A)\det(B)\ne0$.

Subgroups written: $(nI,\times)$, $n\in\mathbb R$; “(rational matrices, $\times$)”.

> [!todo] Manual review — page 2, question 2(vi), subgroup examples
> The scalar-matrix example explicitly allows $n=0$, and the rational-matrix example omits an invertibility condition. Preserve the original abbreviated examples.

### (vii) Absolute-difference operation (page 2, middle)

- Identity: ✓, $e=0$.
- Inverse: ✓, self-inverse.
- Associativity: ✗, $(1*2)*3=2\ne1*(2*3)$.
- Closure: ✓.

### (viii) Multiplication modulo six (page 2, bottom)

- Identity: ✗, $2\times_6 1=2$, $2\times_6 4=2$, “multiple identities”.
- Inverse: ✗, $2^{-1}$ doesn't exist.
- Associativity: ✓.
- Closure: ✗, $2\times_6 3=0$.

> [!todo] Manual review — page 2, question 2(viii), identity reasoning
> The two displayed products concern a single element and do not establish multiple identities for the whole set. The original assessment is retained.

### (ix) Multiplication modulo seven (page 3, top)

- Identity: ✓, $e=1$.
- Inverse: ✓, $2^{-1}=4$, $3^{-1}=5$, $4^{-1}=2$, $5^{-1}=3$, $6^{-1}=6$.
- Associativity: ✓.
- Closure: ✓.

Subgroups: $(\{1,2,4\},\times_7)$, $(\{1,6\},\times_7)$.

## 3. Bracketing (page 3)

The common target is $(ab)(cd)$. The four displayed transformations are:
$$\begin{aligned}
a((bc)d)&=a(b(cd))=(ab)(cd),\\
a(b(cd))&=(ab)(cd),\\
((ab)c)d&=(ab)(cd),\\
(a(bc))d&=((ab)c)d=(ab)(cd).
\end{aligned}$$

For $a,b,c,d,e$:

“Two groups of two”:
$$((ab)(cd))e,\qquad (ab)((cd)e),\qquad ((ab)c)(de),\qquad (ab)(c(de)).$$
A brace counts the first pair as $2$. “By symmetry, $6$ ways.”

“One group of two”:
$$(((ab)c)d)e,\qquad ((a(bc))d)e,\qquad (a((bc)d))e,\qquad a(((bc)d)e).$$
A brace counts these as $4$. “By symmetry, $8$ ways.”

“$14$ ways in total.” This is the written counting argument; no missing enumeration is supplied.

## 4. Matrix products and commutation (pages 4–5)

### (a) Page 4

$$\begin{aligned}
AB&=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix}=\begin{pmatrix}2&1\\0&1\end{pmatrix},\\
BA&=\begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}2&2\\0&1\end{pmatrix},\\
(AB)^2&=\begin{pmatrix}2&1\\0&1\end{pmatrix}\begin{pmatrix}2&1\\0&1\end{pmatrix}=\begin{pmatrix}4&3\\0&1\end{pmatrix},\\
A^2B^2&=\left(\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}\right)\left(\begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix}\right)\\
&=\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}4&0\\0&1\end{pmatrix}=\begin{pmatrix}4&2\\0&1\end{pmatrix}.
\end{aligned}$$

### (b) Page 5, upper half

Base case $n=1$: true. Assume true for $n=k$, $k\in\mathbb N$; consider $n=k+1$.
$$\begin{aligned}
(ab)^{k+1}&=(ab)^k(ab)\\
&=a^kb^kab\\
&=a^{k+1}b^{k+1}\quad\text{by commutativity}.
\end{aligned}$$
By induction, true for all $n\in\mathbb N$.

Converse calculation:
$$abab=aabb,\qquad aba=aab,\qquad a^{-1}aba=a^{-1}aab,\qquad ba=ab.$$
The final written equivalence is
$$ (ab)^n=a^nb^n,\ n\in\mathbb N\quad\Longleftrightarrow\quad a,b\text{ commute}.$$
The universal condition is supplied by the linked question; the source calculation uses the case $n=2$.

### (c) Page 5, lower half

Matrices written:
$$C=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad D=\begin{pmatrix}0&0\\1&1\end{pmatrix}.$$
$$CD=\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&0\\1&1\end{pmatrix}=0,\qquad DC=\begin{pmatrix}0&0\\1&1\end{pmatrix}\begin{pmatrix}1&0\\0&0\end{pmatrix}=\begin{pmatrix}0&0\\1&0\end{pmatrix}.$$
“The set of $2\times2$ matrices does not form a group.”

> [!todo] Incomplete reasoning — page 5, question 4(c)
> No calculation of $(CD)^n=C^nD^n$ for every $n\in\mathbb N$ is written. The missing argument has not been supplied.

## 5. Singular-matrix group (page 6)

$$\begin{pmatrix}a&0\\0&0\end{pmatrix}\begin{pmatrix}b&0\\0&0\end{pmatrix}=\begin{pmatrix}ab&0\\0&0\end{pmatrix}.$$
“This is isomorphic to $(\{0\}\setminus\mathbb R,\times)$.”

> [!todo] Manual review — page 6, first paragraph
> The set difference is visibly written in the order $\{0\}\setminus\mathbb R$. It appears reversed; the transcription preserves it. Conditions $a,b\ne0$ and the isomorphism map are not written here.

Let $A,B,C$ be $2\times2$ matrices such that $AB=C$.
$$\det(A)\det(B)=\det(C).$$
If $\det(A)\ne0$, $\det(B)=0$, then $\det(C)=0$. Assume $B$ has an inverse $B^{-1}$ such that $A=CB^{-1}$.
$$\det(A)=\det(C)\det(B^{-1}),\qquad \det(A)=0,$$
a contradiction. So to form a group under multiplication, all matrices in the set have non-zero determinant or zero determinant.

> [!todo] Manual review — page 6, determinant argument
> The reasoning assumes $A=CB^{-1}$ without discussing the identity of a group of singular matrices, and only explicitly treats $2\times2$ matrices although the supplied general question has no such restriction. Preserve the argument without extending it.

## 6. Integer subgroups (page 7)

$$\{nk:k\in\mathbb Z\}\subset\mathbb Z,\qquad n\in\mathbb Z^+.$$
$$e=0,\qquad (nk)^{-1}=-nk,$$
$$nk_1+nk_2=n(k_1+k_2)\in\{nk:k\in\mathbb Z\}.$$
$$ (\{nk:k\in\mathbb Z\},+)\le(\mathbb Z,+).$$

The source then writes
$$k\in m\mathbb Z,n\mathbb Z\quad\Longleftrightarrow\quad k\mid m,n,$$
$$\Longleftrightarrow\quad (m\mathbb Z\cap n\mathbb Z,+)=(\operatorname{lcm}(m,n)\mathbb Z,+).$$
$$ (m\mathbb Z\cup n\mathbb Z,+)\le(\mathbb Z,+)\quad\Longleftrightarrow\quad m\mid n\text{ or }n\mid m.$$

> [!todo] Manual review — page 7, middle and scope
> The divisibility relation $k\mid m,n$ is written in that direction and appears reversed. The union criterion has no proof. The answer initially assumes $n>0$ and does not discuss the zero cases included in the question.

## 7. Associativity (page 8)

### (a) Matrix multiplication

Consider $(ABC)_{ij}$, with $A$ of size $m\times n$, $B$ of size $n\times p$, and $C$ of size $p\times q$.
$$\begin{aligned}
((AB)C)_{ij}&=\sum_{k=1}^{p}(AB)_{ik}C_{kj}\\
&=\sum_{k=1}^{p}\left(\sum_{m=1}^{n}A_{im}B_{mk}\right)C_{kj}\\
&=\sum_{k=1}^{p}\sum_{m=1}^{n}A_{im}B_{mk}C_{kj},\\
(A(BC))_{ij}&=\sum_{m=1}^{n}A_{im}(BC)_{mj}\\
&=\sum_{m=1}^{n}A_{im}\sum_{k=1}^{p}B_{mk}C_{kj}\\
&=\sum_{k=1}^{p}\sum_{m=1}^{n}A_{im}B_{mk}C_{kj}.
\end{aligned}$$
$$ ((AB)C)_{ij}=(A(BC))_{ij}\quad\Longleftrightarrow\quad (AB)C=A(BC).$$
The source reuses $m$ as both a dimension and a summation index; this notation is preserved.

### (b) Function composition

The written expressions (with evaluation notation left as supplied) are
$$\begin{aligned}
(f\circ g)\circ h&=f(g(x))\circ h=f(g(h(x))),\\
f\circ(g\circ h)&=f\circ g(h(x))=f(g(h(x))).
\end{aligned}$$
Counterexample written: $\sin(\arcsin x)\ne\arcsin(\sin x)$.

> [!todo] Manual review — page 8, question 7(b), bottom
> No common set $S$ or admissible value of $x$ is specified for the sine/arcsine example. The written inequality should not be treated as an unconditional identity of functions $S\to S$.

## 8. Unfinished (page 9)

The page contains only the heading “8)”; the rest is blank. No answer to question 8 is present. Questions 9–12 have no written attempts in this PDF.
