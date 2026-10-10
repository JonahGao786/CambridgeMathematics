---
title: Numbers and Sets 1 - Handwritten Attempts
material_type: handwritten worked solutions and incomplete attempts
course: Part IA Numbers and Sets
date: null
source_file: Numbers - Sets 0.pdf
drive_file_id: 1cAxWubfgZfijKE33WolS74BS9m1Sccpn
source_url: https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view
source_pages: 18
---

# Numbers and Sets 1 — Handwritten Attempts

This PDF contains handwritten answers without supplied question statements. The numbering and expressions match [[Numbers and Sets - Introductory Sheet 2026]], a separately inspected source. Consult that sheet for the questions. The date is not written here. Obvious typos and notation are normalized, with routine algebra made explicit where helpful. Substantive errors and unfinished arguments remain marked; superseded work is preserved.

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view).

## 1. Sum of squares (page 1)

$$\begin{aligned}
(r+1)^3-r^3&=(r+1-r)((r+1)^2+r(r+1)+r^2)\\
&=(r+1)^2+r(r+1)+r^2.
\end{aligned}$$
$$\begin{aligned}
&(r+1)^3-r^3+r^3-(r-1)^3+\cdots-1\\
&=(r+1)^2+r(r+1)+r^2+r^2+r(r-1)+(r-1)^2\\
&\qquad +(r-1)^2+(r-1)(r-2)+(r-2)^2+\cdots\\
&=2\sum_{k=1}^{r+1}k^2-(r+1)^2-1+\sum_{k=1}^{r}k(k+1)=(r+1)^3-1.
\end{aligned}$$
$$2\sum_{k=1}^{r+1}k^2+\sum_{k=1}^{r}k^2+\sum_{k=1}^{r}k-(r+1)^2-1=(r+1)^3-1,$$
$$3\sum_{k=1}^{r}k^2+\frac12r(r+1)+(r+1)^2-1=(r+1)^3-1,$$
$$3\sum_{k=1}^{r}k^2=(r+1)^3-(r+1)^2-\frac12r(r+1),$$
$$6\sum_{k=1}^{r}k^2=(r+1)(2(r+1)^2-2(r+1)-r),$$
$$\sum_{k=1}^{r}k^2=\frac16(r+1)(2r^2+4r+2-3r-2),$$
$$\sum_{k=1}^{r}k^2=\frac16r(r+1)(2r+1).$$

## 2. Induction (pages 2–4)

### (i) Odd squares (page 2)

Base case $n=1$: $\frac13(4-1)=1$, true. Assume true for some $n=k$, $k\in\mathbb Z^+$; consider $n=k+1$.
$$\begin{aligned}
\sum_{i=1}^{k+1}(2i-1)^2
&=\frac13(4k^3-k)+(2k+1)^2\\
&=\frac13(4k^3-k)+(4k^2+4k+1)\\
&=\frac13(4k^3+12k^2+12k-k+3)\\
&=\frac13(4(k+1)^3-(k+1)),\quad\text{true}.
\end{aligned}$$
By induction, this is true for all $n\in\mathbb Z^+$.

### (ii) Divisibility by six (page 3)

Base case $n=1$: $1^3+5=6$, true. Assume true for $n=k$, $k\in\mathbb Z^+$; consider $n=k+1$.
$$\begin{aligned}
(k+1)^3+5(k+1)&=k^3+3k^2+3k+1+5k+5\\
&=k^3+5k+3(k^2+k+2).
\end{aligned}$$
$6\mid k^3+5k$. Consider $3(k^2+k+2)$.
$$2\mid k^2+k\text{ for even and odd }k\quad\Longleftrightarrow\quad6\mid3(k^2+k+2).$$
By induction, $6\mid n^3+5n$ for all $n\in\mathbb Z^+$.

### (iii) Divisibility by seven (page 4)

Base case $n=1$: $2^3+3^3=35$, true. Assume true for $n=k$, $k\in\mathbb Z^+$; consider $n=k+1$.
$$\begin{aligned}
2^{k+3}+3^{2k+3}&=2\cdot2^{k+2}+9\cdot3^{2k+1}\\
&=2(2^{k+2}+3^{2k+1})+7\cdot3^{2k+1}.
\end{aligned}$$
$$7\mid2^{k+2}+3^{2k+1},\quad7\mid7\cdot3^{2k+1}\quad\Longleftrightarrow\quad7\mid2^{k+3}+3^{2k+3}.$$
By induction, $7\mid2^{n+2}+3^{2n+1}$ for all $n\in\mathbb Z^+$.

## 3. Alternative arguments (page 5)

### (i)

$$\begin{aligned}
\sum_{r=1}^{n}(2r-1)^2
&=\sum_{r=1}^{2n}r^2-\sum_{r=1}^{n}(2r)^2\\
&=\frac16\cdot2n(2n+1)(4n+1)-4\cdot\frac16n(n+1)(2n+1)\\
&=\frac13n(2n+1)(4n+1-2n-2)\\
&=\frac13(2n^2+n)(2n-1)\\
&=\frac13(4n^3-n).
\end{aligned}$$

### (ii)

Consider
$$\begin{aligned}
n^3+5n+6&=(n+1)(n^2-n+6)\\
&=(n+1)(n(n-1)+6)\\
&=6(n+1)+(n-1)n(n+1).
\end{aligned}$$
$6\mid6(n+1)$, and $n-1,n,n+1$ are consecutive integers, so $6\mid(n-1)n(n+1)$.
$$6\mid n^3+5n+6\quad\Longleftrightarrow\quad6\mid n^3+5n.$$

### (iii)

$$7\mid4^k-(-3)^k,\qquad k=2n+1.$$
The displayed chain is
$$\begin{aligned}
&7\mid4^{2n+1}+3^{2n+1}\\
\Longleftrightarrow\quad&7\mid2^{4n+2}+3^{2n+1}\\
\Longleftrightarrow\quad&7\mid2^{3n}\cdot2^{n+2}+3^{2n+1}\\
\Longleftrightarrow\quad&7\mid8^n\cdot2^{n+2}+3^{2n+1}.
\end{aligned}$$
Since $7\mid8^n-1$, the preceding divisibility statement gives
$$7\mid2^{n+2}+3^{2n+1}.$$

## 4. Horses (page 6, top)

Induction step fails when $n=1$: no overlap between $h_1$ and $h_2$, so cannot deduce $h_1$ and $h_2$ have the same colour.

## 5. Fibonacci numbers (pages 6–7)

The sequence written is $1,1,2,3,5,\ldots$; see [[Fibonacci Numbers]] for the supplied definition.

### (a) Addition formula (page 6)

$$F_{n+k}=F_kF_{n+1}+F_{k-1}F_n.$$
Base case $k=2$: trivial. Base case $k=3$:
$$F_{n+3}=F_{n+2}+F_{n+1}=2F_{n+1}+F_n,\quad\text{true}.$$
Assume this is true for $k=r$ and $k=r+1$, $r\in\mathbb Z$, $r\ge2$. Consider $k=r+2$:
$$\begin{aligned}
F_{n+r+2}&=F_{n+r+1}+F_{n+r}\\
&=F_{r+1}F_{n+1}+F_rF_n+F_rF_{n+1}+F_{r-1}F_n\\
&=F_{r+2}F_{n+1}+F_{r+1}F_n,\quad\text{true}.
\end{aligned}$$
By induction, true for all $k\in\mathbb Z$, $k\ge2$.

Let $k=n+1$:
$$F_{2n+1}=F_{n+1}^2+F_n^2.$$
$$\begin{aligned}
F_{n+2}^2-F_n^2&=(F_{n+2}+F_n)(F_{n+2}-F_n)\\
&=F_{n+1}F_{n+2}+F_{n+1}F_n\\
&=F_{2n+2}.
\end{aligned}$$

### (a) Divisibility and prime indices (page 7, upper half)

Base case $k=1$: trivial. Assume true for $k=r$, $r\in\mathbb N$; consider $k=r+1$:
$$F_{(r+1)n}=F_{rn}F_{n+1}+F_{rn-1}F_n,$$
which is a multiple of $F_n$. By induction, this is true for all $k\in\mathbb N$.

“If $F_n$ is prime, then $\gcd(F_n,F_{n-k})=1$ for all $1\le k\le n-1$. So using previous part, $n$ should be a prime. $F_4=3$, also a prime, so $n$ is prime or $n=4$.”

### (b) Last-digit periodicity (page 7, lower half)

The pair $(f_n,f_{n+1})$ has a finite amount of possibilities. Eventually there will be a pair
$$ (f_k,f_{k+1})=(f_n,f_{n+1}).$$
The recurrence is $f_{n+2}\equiv f_{n+1}+f_n\pmod{10}$. Its pair transition is reversible, since $f_n\equiv f_{n+2}-f_{n+1}\pmod{10}$. Thus a repeated pair can also be traced backwards to the first pair, so the sequence is periodic from the beginning.

## 6. Factorials (pages 8–9)

### (a) Difference of squares (page 8, upper half)

$$n!=a^2-b^2=(a+b)(a-b).$$
The case $n=1$ works: $1!=1^2-0^2$. For $n\ge2$, $n!$ is even, so $a+b$ or $a-b$ must be even. Since $a,b\in\mathbb Z$, $a+b$ and $a-b$ must both be even. Therefore $n!$ must have more than one factor of $2$. For $n\ge4$, $4\mid n!$. Writing $n!=4t$,
$$n!=(t+1)^2-(t-1)^2.$$
Thus the answer is $n=1$ or $n\ge4$; $n=2,3$ each give a factorial with only one factor of $2$.

### (b) Divisibility of the preceding factorial (page 8, lower half)

If $n$ is prime, then $n\nmid(n-1)!$: none of the factors $1,\ldots,n-1$ is divisible by $n$.

For a composite $n$ with a factorization
$$n=ab,\qquad1<a,b<n,\qquad a\ne b,$$
both $a$ and $b$ appear as **distinct factors** of $(n-1)!$. Hence their product $ab=n$ divides $(n-1)!$.

**Explanation of the case split.** Choose a prime divisor $p$ of $n$ and take $a=p$, $b=n/p$. These are distinct unless $n=p^2$. The product argument uses two distinct entries in the factorial; knowing only that $a$ and $b$ separately divide the factorial would not suffice in general.

If $n=p^2$ for a prime $p$, consider the two factors $p$ and $2p$. When $p>2$,
$$1<p<2p<p^2=n.$$
Thus $p(2p)=2p^2$ divides $(n-1)!$, and in particular $n=p^2$ divides $(n-1)!$.

For $n=4$, $p=2$ and $2p=n$, so this argument fails; indeed $4\nmid3!=6$.

Therefore $n\mid(n-1)!$ for every composite $n\ne4$. The boundary case $n=1$ also works, since $0!=1$. The positive integers satisfying the condition are exactly
$$n=1\quad\text{or}\quad n\text{ composite with }n\ne4.$$

#### Superseded, incorrect attempt (previous version, page 8)

The earlier processed version used a product of proper divisors:
$$n=p_1^{a_1}p_2^{a_2}p_3^{a_3}\cdots,$$
where $p_n$ is prime and $a_n\in\mathbb Z$, $a_n\ge0$.

The source writes a product over exponent tuples with $i\le a_1$, $j\le a_2$, … and $(i,j,\ldots)\ne(a_1,a_2,\ldots)$:
$$\prod_{\substack{i\le a_1,\ j\le a_2,\ldots\\(i,j,\ldots)\ne(a_1,a_2,\ldots)}}p_1^ip_2^j\cdots\ \mid\ (n-1)!,$$
$$n\mid\prod_{\substack{i\le a_1,\ j\le a_2,\ldots\\(i,j,\ldots)\ne(a_1,a_2,\ldots)}}p_1^ip_2^j\cdots\quad\Longleftrightarrow\quad n\mid(n-1)!.$$
“Therefore $n\mid(n-1)!$ for non-prime $n$.”

This blanket conclusion fails at $n=4$. The revised proof above handles the exception; the earlier argument is retained as superseded, rather than as a current proof.

### (c) Trailing zeroes (page 9, top)

Need $2026$ factors of $10$. More factors of $2$ than $5$, so count factors of $5$:
$$\left\lfloor\frac n5\right\rfloor+\left\lfloor\frac n{25}\right\rfloor+\left\lfloor\frac n{125}\right\rfloor+\left\lfloor\frac n{625}\right\rfloor+\cdots.$$
“I wrote a Python script and gets $n=8120$.” The script is not present in the source.

## 7. Irrationality (pages 9–11)

### (a) Page 9

Assume $\sqrt[3]{4}$ is rational:
$$\sqrt[3]{4}=\frac pq,\qquad p,q\in\mathbb N,\quad p,q\text{ coprime}.$$
$$4=\frac{p^3}{q^3},\quad p^3=4q^3.$$
$p^3$ is even. Let $p=2m$. Then
$$8m^3=4q^3,\qquad2m^3=q^3.$$
$q^3$ is even. $p,q$ even contradicts coprimality. Therefore $\sqrt[3]{4}$ is irrational.

Assume $\log_3 4$ rational:
$$\log_3 4=\frac pq,\qquad p,q\in\mathbb Z_{>0},\qquad4=3^{p/q},\qquad4^q=3^p.$$
$\gcd(4,3)=1$, so $4^q=3^p$ is impossible for positive integers $p,q$. Therefore $\log_3 4$ irrational.

### (b) Descent (page 10)

$$\begin{aligned}
11n-3m&=\sqrt{11}\,m-3\sqrt{11}\,n\\
\Longleftrightarrow\quad(11+3\sqrt{11})n&=(\sqrt{11}+3)m\\
\Longleftrightarrow\quad\frac mn&=\sqrt{11}.
\end{aligned}$$
$$3<\sqrt{11}<4\quad\Longrightarrow\quad3n<m<4n.$$
$$m-3n<n,\qquad11n-3m<m.$$
Let $m-3n=p$, $11n-3m=q$, $p,q\in\mathbb N$. Then $\frac qp=\sqrt{11}$. This process can be infinitely repeated; it contradicts $m,n,p,q\in\mathbb N$, so $\sqrt{11}$ irrational.

For $\sqrt{111}$, $10<\sqrt{111}<11$:
$$\text{if }\frac mn=\sqrt{111},\qquad\frac{111n-10m}{m-10n}=\sqrt{111}.$$
For $\sqrt{121}$, $10<\sqrt{121}<12$. We cannot deduce the new denominator is smaller than the original denominator; therefore method fails.

### (c) Page 11

- $r+\alpha$ is irrational: otherwise $\alpha=(r+\alpha)-r$ would be rational, a contradiction.
- $r\alpha$ can be rational: let $r=0$.
- $\alpha+\beta$ can be rational: let $\alpha=-\beta$.
- $\alpha\beta$ can be rational: let $\alpha=\beta=\sqrt2$.
- $r^\alpha$ can be rational: let $r=3$, $\alpha=\log_3 4$.
- $\alpha^r$ can be rational: let $r=0$.
- $\alpha^\beta$ can be rational: let $\alpha=e$, $\beta=\ln3$.

> [!todo] Substantive gap — page 11, last bullet
> The counterexample requires $e$ and $\ln3$ to be irrational; the source supplies no justification. The irrationality of $\ln3$ is not an elementary consequence of the earlier arguments, so this prerequisite remains unresolved here.

## 8. Pigeonhole attempts (page 12)

(i) Consider pairs $(1,2),(3,4),\ldots,(2n-1,2n)$. Two consecutive integers are coprime. Statement proved by pigeonhole principle.

(ii) Consider pairs $(1,2n),(2,2n-1),\ldots,(n,n+1)$; then use pigeonhole principle.

(iii) Partition $\{1,\ldots,2n\}$ into chains with a fixed odd part $u$:
$$\{u2^k:k\ge0,\ u2^k\le2n\},\qquad u=1,3,5,\ldots,2n-1.$$
There are $n$ chains; use the pigeonhole principle. Two members of one chain have the same odd part, so one divides the other.

(iv) Let $M=\max S$. The $n$ differences $M-s$, for $s\in S\setminus\{M\}$, are distinct and belong to $\{1,\ldots,2n\}$. Together with the $n+1$ elements of $S$, this gives $2n+1$ entries in a set of size $2n$. By the pigeonhole principle, one difference is in $S$: $M-s=t$ for some $s,t\in S$.

Counterexamples written:

- (i) $n$ even numbers.
- (ii) $n$ odd numbers.
- (iii) $\{1,2,3,4\}$, $S=\{2,3\}$.
- (iv) $n$ odd numbers.

“No such example where all four fails.”

## 9. Towns and coloured edges (pages 13–15)

### Superseded, incomplete attempt (page 13)

$$A:B\text{ through }F\ (5),\quad B:C\text{ through }F\ (4),\quad C:D\text{ through }F\ (3),\quad D:E\text{ through }F\ (2),\quad E:F\ (1).$$
$15$ edges. At least $8$ edges are the same transport. Try to place the $8$ edges without forming a triangle. Assume $AB,CD,EF$ are edges that don't meet each other. Then list $AC,AD,AE,AF$.

This incomplete attempt does not establish the claim.

### Six-town diagrams (page 14)

The three six-town diagrams below and the three five-town diagrams on page 15 are drawn in TikZ for TikZJax, preserving the original circular arrangements of labelled towns and the red/blue edges. Positions carry no metric information; crossings of edges are not additional vertices. The source does not identify which colour denotes train or bus. Occasional arrow-shaped pen strokes are not interpreted as directed transport routes. Only edges actually drawn are included; annotations about undrawn edges remain annotations.

[Original diagrams in Google Drive](https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view) — page 14.

From top to bottom:

1. Red edges drawn: $AB,AC,AD,AE,AF$. Blue edges drawn: $BC,CD,DE,EF$. Annotation: “$FD,EC,BD$ can be any colour to form a monochrome triangle.”
2. Red: $AC,AD,AE,AF$. Blue: $AB,CD,DE,EF$. Annotation: “$FD,EC$ can be any colour to form a monochrome triangle.”
3. Red: $AD,AE,AF$. Blue: $AB,AC,DE,EF$. Annotation: “$FD$ can be any colour to form a monochrome triangle.”

#### Page 14 — top: partial six-town graph

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9,vertex/.style={circle,fill=white,inner sep=3pt}]
  \coordinate (A) at (-1.35,1.8);
  \coordinate (B) at (1.35,1.8);
  \coordinate (C) at (2.4,0);
  \coordinate (D) at (1.35,-1.8);
  \coordinate (E) at (-1.35,-1.8);
  \coordinate (F) at (-2.4,0);
  \draw[red,thick] (A) -- (B);
  \draw[red,thick] (A) -- (C);
  \draw[red,thick] (A) -- (D);
  \draw[red,thick] (A) -- (E);
  \draw[red,thick] (A) -- (F);
  \draw[blue,thick] (B) -- (C);
  \draw[blue,thick] (C) -- (D);
  \draw[blue,thick] (D) -- (E);
  \draw[blue,thick] (E) -- (F);
  \node[vertex] at (A) {$A$};
  \node[vertex] at (B) {$B$};
  \node[vertex] at (C) {$C$};
  \node[vertex] at (D) {$D$};
  \node[vertex] at (E) {$E$};
  \node[vertex] at (F) {$F$};
  \node[anchor=north west,text width=3cm,align=left] at (2.85,1.8) {$FD,EC,BD$ can be any colour.};
\end{tikzpicture}
\end{document}
```

#### Page 14 — middle: partial six-town graph

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9,vertex/.style={circle,fill=white,inner sep=3pt}]
  \coordinate (A) at (-1.35,1.8);
  \coordinate (B) at (1.35,1.8);
  \coordinate (C) at (2.4,0);
  \coordinate (D) at (1.35,-1.8);
  \coordinate (E) at (-1.35,-1.8);
  \coordinate (F) at (-2.4,0);
  \draw[red,thick] (A) -- (C);
  \draw[red,thick] (A) -- (D);
  \draw[red,thick] (A) -- (E);
  \draw[red,thick] (A) -- (F);
  \draw[blue,thick] (A) -- (B);
  \draw[blue,thick] (C) -- (D);
  \draw[blue,thick] (D) -- (E);
  \draw[blue,thick] (E) -- (F);
  \node[vertex] at (A) {$A$};
  \node[vertex] at (B) {$B$};
  \node[vertex] at (C) {$C$};
  \node[vertex] at (D) {$D$};
  \node[vertex] at (E) {$E$};
  \node[vertex] at (F) {$F$};
  \node[anchor=north west,text width=3cm,align=left] at (2.85,1.8) {$FD,EC$ can be any colour.};
\end{tikzpicture}
\end{document}
```

#### Page 14 — bottom: partial six-town graph

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9,vertex/.style={circle,fill=white,inner sep=3pt}]
  \coordinate (A) at (-1.35,1.8);
  \coordinate (B) at (1.35,1.8);
  \coordinate (C) at (2.4,0);
  \coordinate (D) at (1.35,-1.8);
  \coordinate (E) at (-1.35,-1.8);
  \coordinate (F) at (-2.4,0);
  \draw[red,thick] (A) -- (D);
  \draw[red,thick] (A) -- (E);
  \draw[red,thick] (A) -- (F);
  \draw[blue,thick] (A) -- (B);
  \draw[blue,thick] (A) -- (C);
  \draw[blue,thick] (D) -- (E);
  \draw[blue,thick] (E) -- (F);
  \node[vertex] at (A) {$A$};
  \node[vertex] at (B) {$B$};
  \node[vertex] at (C) {$C$};
  \node[vertex] at (D) {$D$};
  \node[vertex] at (E) {$E$};
  \node[vertex] at (F) {$F$};
  \node[anchor=north west,text width=3cm,align=left] at (2.85,1.8) {$FD$ can be any colour.};
\end{tikzpicture}
\end{document}
```

> [!todo] Incomplete attempt — page 14
> The annotations claim that the listed remaining edges can have any colour and still give a monochrome triangle. The missing step is explaining why an arbitrary two-colouring can be reduced to one of these three patterns. Partial diagrams can suffice for a proof; a complete edge colouring is not required. Undrawn edges remain undrawn.

### Five-town diagrams (page 15)

[Original diagrams in Google Drive](https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view) — page 15.

Upper-left diagram: red $AB,AC,AD,AE$; blue $BC,CD,DE$.

Upper-right diagram: red $AC,AD,AE$; blue $AB,CD,DE$.

Lower-left completed diagram: red $AE,AD,BE,BC,CD$; blue $AB,AC,BD,CE,DE$.

#### Page 15 — upper left: partial five-town graph

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9,vertex/.style={circle,fill=white,inner sep=3pt}]
  \coordinate (A) at (-1.2,1.7);
  \coordinate (B) at (1.2,1.7);
  \coordinate (C) at (2,-0.3);
  \coordinate (D) at (0,-1.9);
  \coordinate (E) at (-2,-0.3);
  \draw[red,thick] (A) -- (B);
  \draw[red,thick] (A) -- (C);
  \draw[red,thick] (A) -- (D);
  \draw[red,thick] (A) -- (E);
  \draw[blue,thick] (B) -- (C);
  \draw[blue,thick] (C) -- (D);
  \draw[blue,thick] (D) -- (E);
  \node[vertex] at (A) {$A$};
  \node[vertex] at (B) {$B$};
  \node[vertex] at (C) {$C$};
  \node[vertex] at (D) {$D$};
  \node[vertex] at (E) {$E$};
\end{tikzpicture}
\end{document}
```

#### Page 15 — upper right: partial five-town graph

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9,vertex/.style={circle,fill=white,inner sep=3pt}]
  \coordinate (A) at (-1.2,1.7);
  \coordinate (B) at (1.2,1.7);
  \coordinate (C) at (2,-0.3);
  \coordinate (D) at (0,-1.9);
  \coordinate (E) at (-2,-0.3);
  \draw[red,thick] (A) -- (C);
  \draw[red,thick] (A) -- (D);
  \draw[red,thick] (A) -- (E);
  \draw[blue,thick] (A) -- (B);
  \draw[blue,thick] (C) -- (D);
  \draw[blue,thick] (D) -- (E);
  \node[vertex] at (A) {$A$};
  \node[vertex] at (B) {$B$};
  \node[vertex] at (C) {$C$};
  \node[vertex] at (D) {$D$};
  \node[vertex] at (E) {$E$};
\end{tikzpicture}
\end{document}
```

#### Page 15 — lower left: completed five-town graph

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=0.9,vertex/.style={circle,fill=white,inner sep=3pt}]
  \coordinate (A) at (-1.2,1.7);
  \coordinate (B) at (1.2,1.7);
  \coordinate (C) at (2,-0.3);
  \coordinate (D) at (0,-1.9);
  \coordinate (E) at (-2,-0.3);
  \draw[red,thick] (A) -- (E);
  \draw[red,thick] (A) -- (D);
  \draw[red,thick] (B) -- (E);
  \draw[red,thick] (B) -- (C);
  \draw[red,thick] (C) -- (D);
  \draw[blue,thick] (A) -- (B);
  \draw[blue,thick] (A) -- (C);
  \draw[blue,thick] (B) -- (D);
  \draw[blue,thick] (C) -- (E);
  \draw[blue,thick] (D) -- (E);
  \node[vertex] at (A) {$A$};
  \node[vertex] at (B) {$B$};
  \node[vertex] at (C) {$C$};
  \node[vertex] at (D) {$D$};
  \node[vertex] at (E) {$E$};
\end{tikzpicture}
\end{document}
```

Written conclusions: “No monochrome triangle in this case” and “Not true if only $5$ towns.” No further prose argument is supplied.

## 10. Lunar-rover fuel depots (page 16)

The question in [[Numbers and Sets - Introductory Sheet 2026]] asks for a starting depot from which the rover can complete one circuit, collecting fuel along the way. Total fuel permits exactly one circuit.

The source diagram marks a starting depot $A$, a later depot $B$, and two possible new depots along the arc between them. Their positions are schematic; the circle represents the moon.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}
  \draw[thick] (0,0) circle (1.8);
  \foreach \ang/\lab in {90/{A\;\mathrm{(start)}},60/{\mathrm{new}_2},30/{\mathrm{new}_1},-10/B} {
    \draw (\ang:1.68)--(\ang:1.92);
    \node at (\ang:2.5) {$\lab$};
  }
\end{tikzpicture}
\end{document}
```

**Incomplete proof:** Let $n\in\mathbb Z^+$ be the number of depots. The case $n=1$ is trivial.

For $n=2$, let the shortest distance between depots be $d$, total fuel be $F$, and fuel in one depot be $f$. Fuel is measured by the distance it permits the rover to travel. If $f\le d$, then $F-f\ge d$. The claimed conclusion is that there is always one depot that can be the starting depot.

Assume the result for $n=k$, with $k\ge2$, and consider $n=k+1$. Let the starting depot in the $k$-depot configuration be $A$, with fuel $f_A$, and let the next depot be $B$, with
$$f_A\ge d_{AB}.$$
Place a new depot $C$ between $A$ and $B$, and move fuel $f_C$ from $A$ to $C$.

- If $f_A-f_C\ge d_{AC}$, the proposed starting depot is still $A$.
- Otherwise, if $f_A-f_C<d_{AC}$, then $f_C>d_{CB}$, and the proposed starting depot is $C$.

**Claimed conclusion:** By induction, there is always a starting depot for any number of depots.

> [!todo] Essential gap — page 16, question 10, induction step
> The construction inserts the new depot after a starting depot already chosen in the smaller configuration. It does not establish that every arbitrary configuration of $k+1$ depots arises in this way. A reduction to a suitable $k$-depot configuration, with a justified relation between its starting depot and the removed depot, is missing. Reaching the next depot alone also does not justify completing the whole circuit from the proposed new start.

## 11–12. Unfinished (pages 17–18)

Page 17 contains only “11)”, and page 18 only “12)”; neither has a written answer.
