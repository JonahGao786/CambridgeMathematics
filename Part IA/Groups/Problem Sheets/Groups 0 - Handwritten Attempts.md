---
title: Groups 1 - Handwritten Attempts
material_type: handwritten worked solutions and incomplete attempts
course: Part IA Groups
date: null
source_file: Groups 0.pdf
drive_file_id: 17C8KN1XdaZj4KDVAvQ5tdxptR4KTmPHY
source_url: https://drive.google.com/file/d/17C8KN1XdaZj4KDVAvQ5tdxptR4KTmPHY/view
source_pages: 13
---

# Groups 1 — Handwritten Attempts

The PDF contains handwritten answers without the question statements. Their numbering and examples match [[Groups - Introductory Sheet 2026]], a separate Drive source. Consult that sheet for the supplied questions. Obvious typos and notation are normalized, with routine algebra made explicit where helpful. Substantive errors and unfinished arguments remain marked. The date is not written in this PDF.

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/17C8KN1XdaZj4KDVAvQ5tdxptR4KTmPHY/view).

## 1. Axioms (page 1, top)

- Identity: there is an $e\in G$ such that $a\cdot e=e\cdot a=a$ for every $a\in G$.
- Inverses: every $a\in G$ has an inverse $a^{-1}\in G$ with $a\cdot a^{-1}=a^{-1}\cdot a=e$.
- Associativity: $(a\cdot b)\cdot c=a\cdot(b\cdot c)$.
- Closure: $a\cdot b\in G$ for all $a,b\in G$.

Abelian groups are commutative: $a\cdot b=b\cdot a$.

## 2. Examples (pages 1–3)

The check marks and crosses below reproduce the handwritten assessments. Unwritten commutativity answers remain unwritten.

### (i) Integers under subtraction (page 1, left)

- Identity: ✗, no two-sided identity.
- Inverse assessment: ✓, “self-inverse”, since $a-a=0$. Without a two-sided identity, this is not a group inverse.
- Associativity: ✗, $(a-b)-c\ne a-(b-c)$.
- Closure: ✓, $-:\mathbb Z\times\mathbb Z\to\mathbb Z$.

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
- Inverse: ✓, $a^{-1}=-a-2i$.
- Associativity: ✓.
- Closure: ✓.

Subgroup conditions written: $\operatorname{Im}(a),\operatorname{Re}(a)\in\mathbb Z$; $\operatorname{Im}(a),\operatorname{Re}(a)\in\mathbb Q$.

### (v) Cross product (page 2, top)

- Identity: ✗.
- Inverse: ✗, $\mathbf b\times\mathbf b^{-1}=e$, but identity doesn't exist.
- Associativity: ✗. For suitable $\mathbf a,\mathbf b,\mathbf c$ with $\mathbf b\parallel\mathbf c$, $(\mathbf a\times\mathbf b)\times\mathbf c\ne\mathbf a\times(\mathbf b\times\mathbf c)$.
- Closure: ✗. $\mathbf b\parallel\mathbf c$, $\mathbf b\times\mathbf c=0$, not in set.

### (vi) Invertible real matrices (page 2, upper middle)

- Identity: ✓, $e=I$.
- Inverse: ✓, $\det(A)\ne0$.
- Associativity: ✓.
- Closure: ✓, $\det(AB)=\det(A)\det(B)\ne0$.

Subgroups: the non-zero scalar matrices $\{tI:t\in\mathbb R\setminus\{0\}\}$, and the invertible $2\times2$ rational matrices, both under multiplication.

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
Since $C^2=C$ and $D^2=D$, for every positive integer $n$, $C^nD^n=CD=0=(CD)^n$. This does not contradict (b): the set of all $2\times2$ matrices does not form a group.

## 5. Singular-matrix group (page 6)

$$\begin{pmatrix}a&0\\0&0\end{pmatrix}\begin{pmatrix}b&0\\0&0\end{pmatrix}=\begin{pmatrix}ab&0\\0&0\end{pmatrix}.$$
For $a,b\ne0$, this is isomorphic to $(\mathbb R\setminus\{0\},\times)$ via $t\mapsto\begin{pmatrix}t&0\\0&0\end{pmatrix}$.

For the general statement, let $A,B,C$ belong to a group of square matrices of a common size, with $AB=C$.
$$\det(A)\det(B)=\det(C).$$
If $\det(A)\ne0$, $\det(B)=0$, then $\det(C)=0$. Let $B^{-1}$ be the inverse of $B$ within this group. Then $CB^{-1}=ABB^{-1}=A$.
$$\det(A)=\det(C)\det(B^{-1}),\qquad \det(A)=0,$$
a contradiction. So to form a group under multiplication, all matrices in the set have non-zero determinant or zero determinant.

## 6. Integer subgroups (page 7)

$$\{nk:k\in\mathbb Z\}\subset\mathbb Z,\qquad n\in\mathbb Z^+.$$
$$e=0,\qquad (nk)^{-1}=-nk,$$
$$nk_1+nk_2=n(k_1+k_2)\in\{nk:k\in\mathbb Z\}.$$
$$ (\{nk:k\in\mathbb Z\},+)\le(\mathbb Z,+).$$

For $m,n>0$,
$$k\in m\mathbb Z\cap n\mathbb Z\quad\Longleftrightarrow\quad m\mid k\text{ and }n\mid k,$$
$$\Longleftrightarrow\quad (m\mathbb Z\cap n\mathbb Z,+)=(\operatorname{lcm}(m,n)\mathbb Z,+).$$
$$ (m\mathbb Z\cup n\mathbb Z,+)\le(\mathbb Z,+)\quad\Longleftrightarrow\quad m\mid n\text{ or }n\mid m.$$

The zero case gives $0\mathbb Z=\{0\}$, also a subgroup. If either $m$ or $n$ is zero, the intersection is $\{0\}$ and the union is the other subgroup.

## 7. Associativity (page 8)

### (a) Matrix multiplication

Consider $(ABC)_{ij}$, with $A$ of size $m\times n$, $B$ of size $n\times p$, and $C$ of size $p\times q$.
$$\begin{aligned}
((AB)C)_{ij}&=\sum_{k=1}^{p}(AB)_{ik}C_{kj}\\
&=\sum_{k=1}^{p}\left(\sum_{\ell=1}^{n}A_{i\ell}B_{\ell k}\right)C_{kj}\\
&=\sum_{k=1}^{p}\sum_{\ell=1}^{n}A_{i\ell}B_{\ell k}C_{kj},\\
(A(BC))_{ij}&=\sum_{\ell=1}^{n}A_{i\ell}(BC)_{\ell j}\\
&=\sum_{\ell=1}^{n}A_{i\ell}\sum_{k=1}^{p}B_{\ell k}C_{kj}\\
&=\sum_{k=1}^{p}\sum_{\ell=1}^{n}A_{i\ell}B_{\ell k}C_{kj}.
\end{aligned}$$
$$ ((AB)C)_{ij}=(A(BC))_{ij}\quad\Longleftrightarrow\quad (AB)C=A(BC).$$

### (b) Function composition

For each $x\in S$,
$$\begin{aligned}
((f\circ g)\circ h)(x)&=(f\circ g)(h(x))=f(g(h(x))),\\
(f\circ(g\circ h))(x)&=f((g\circ h)(x))=f(g(h(x))).
\end{aligned}$$
Proposed example: $\sin(\arcsin x)$ and $\arcsin(\sin x)$, with the caveat that the domains of the functions have changed.

> [!todo] Manual review — page 8, question 7(b), bottom
> The domain caveat is acknowledged, but no common set $S$ is supplied on which both sine and the usual real arcsine are functions $S\to S$ giving a non-commuting example. This does not yet answer the counterexample part of the question as stated.

## 8. Cayley tables and Latin squares (pages 9–10)

### (a) A finite group's Cayley table (page 9)

Each row and column is a translate of the group: $aG=G$ and $Ga=G$.

For a fixed $a$, suppose two entries in its row coincide:
$$ab=ac=d\quad\Longrightarrow\quad b=c=a^{-1}d.$$
Thus distinct column labels cannot give a repeated row entry. The analogous cancellation on the right excludes repeated entries within a column. Hence the Cayley table of a finite group forms a [[Latin Squares|Latin square]].

To find the identity, find the row and column that preserve the order of the table's element labels. Two elements whose product gives the identity are inverses of each other.

If the group is abelian, its Cayley table is symmetric about the diagonal from top left to bottom right.

### (b) The supplied five-element Latin square (page 9, bottom)

**Incorrect answer:** “It is; it has an identity, elements are self-inverse, and it's a non-abelian group.”

> [!todo] Manual review — page 9, question 8(b)
> Associativity fails: in the table in [[Groups - Introductory Sheet 2026]], $(a*a)*b=e*b=b$, whereas $a*(a*b)=a*c=d$. Hence this table is not the Cayley table of a group.

### (c) Associative Latin-square operation (page 10)

The separate question supplies a non-empty finite set $S$ with an associative, closed operation $*$ whose table is a Latin square.

For every $a\in S$, the Latin-square property says that $aS$ is a rearrangement of the elements of $S$. Hence there is an $e_a\in S$ such that $a*e_a=a$.

For every $b\in S$,
$$ (a*e_a)*b=a*b,$$
and associativity gives
$$ a*(e_a*b)=a*b.$$
Cancellation in the row labelled $a$ gives $e_a*b=b$ for every $b\in S$.

These left identities are all the same: choose $b_0\in S$. Since $e_a*b_0=b_0=e_{a'}*b_0$, cancellation in column $b_0$ gives $e_a=e_{a'}$. Write this common element as $e$. Then $a*e=a$ and $e*a=a$ for every $a\in S$, so $e$ is a two-sided identity.

Similarly, each row contains $e$, so for every $a\in S$ there is an $a^{-1}\in S$ with $a*a^{-1}=e$. It is also a left inverse, by associativity and column cancellation:
$$ (a^{-1}*a)*a^{-1}=a^{-1}*(a*a^{-1})=a^{-1}*e=a^{-1}=e*a^{-1}.$$
Thus $a^{-1}*a=e$. The group axioms are satisfied, so $(S,*)$ is a [[Groups|group]].

## 9. Two operations and the interchange law (page 11)

The hypotheses in [[Groups - Introductory Sheet 2026]], question 9, give two binary operations $\circ$ and $*$ on $S$, with two-sided identities $e_1$ and $e_2$ respectively, and
$$ (a\circ b)*(c\circ d)=(a*c)\circ(b*d)\qquad(a,b,c,d\in S).$$

### Common identity and operation (page 11, upper half)

$$\begin{aligned}
(a\circ b)*(e_2\circ e_1)&=(a*e_2)\circ(b*e_1),\\
a\circ b&=a\circ(b*e_1).
\end{aligned}$$
Taking $a=e_1$ gives $b=b*e_1$ for every $b\in S$. Taking $b=e_2$ then gives $e_2=e_1$. Write their common value as $e$.

$$\begin{aligned}
(a\circ e)*(e\circ b)&=(a*e)\circ(e*b),\\
a*b&=a\circ b.
\end{aligned}$$
Thus $*=\circ$.

### Associativity (page 11, lower half)

Apply the interchange law with the common operation:
$$ (a\circ b)\circ(e\circ c)=(a\circ e)\circ(b\circ c).$$
Using the common identity,
$$ (a\circ b)\circ c=a\circ(b\circ c),$$
so the operation is associative.

### Commutativity attempt (page 11, bottom)

**Wrong proof:**
$$\begin{aligned}
(a\circ b)\circ(e\circ a)&=a\circ(b\circ a),\\
a\circ(a\circ b)&=a\circ(b\circ a),\\
a\circ b&=b\circ a\quad\text{claimed to show commutativity}.
\end{aligned}$$

> [!todo] Manual review — page 11, question 9, lower half
> The final cancellation of the leading $a$ is unjustified: these hypotheses do not give cancellation. The intermediate rearrangement to $a\circ(a\circ b)$ also uses commutativity before it has been proved. The common identity, common operation and associativity are established above, but this argument does not prove commutativity.

## 10–12. Unfinished

Page 12 contains only the heading “10)”, and page 13 only “11)”; neither has a written answer. No attempt at question 12 is present.
