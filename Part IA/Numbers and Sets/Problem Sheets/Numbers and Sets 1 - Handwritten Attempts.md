---
title: Numbers and Sets 1 - Handwritten Attempts
material_type: handwritten worked solutions and incomplete attempts
course: Part IA Numbers and Sets
date: null
source_file: Numbers - Sets 1.pdf
drive_file_id: 1cAxWubfgZfijKE33WolS74BS9m1Sccpn
source_url: https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view
source_pages: 15
---

# Numbers and Sets 1 — Handwritten Attempts

This PDF contains handwritten answers without supplied question statements. The numbering and expressions match [[Numbers and Sets - Introductory Sheet 2026]], a separately inspected source. Consult that sheet for the questions. The date is not written here. Original claims, omitted steps and superseded work are preserved. Editorial TODOs flag issues without repairing the solutions.

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
The lower-half variable glyphs are not consistently distinguishable as $n$ or $r$ even in an enlarged crop. Ambiguous glyphs are explicitly marked below:
$$2\sum_{k=1}^{r+1}k^2+\sum_{k=1}^{\text{TODO: }n\text{ or }r}k^2+\sum_{k=1}^{\text{TODO: }n\text{ or }r}k-(r+1)^2-1=(r+1)^3-1,$$
$$3\sum_{k=1}^{\text{TODO: }n\text{ or }r}k^2+\frac12r(r+1)+(r+1)^2-1=(r+1)^3-1,$$
$$3\sum_{k=1}^{\text{TODO: }n\text{ or }r}k^2=(r+1)^3-(r+1)^2-\frac12r(r+1),$$
$$6\sum_{k=1}^{\text{TODO: }n\text{ or }r}k^2=(r+1)(2(r+1)^2-2(r+1)-\text{TODO: }n\text{ or }r),$$
$$\sum_{k=1}^{r}k^2=\frac16(r+1)(2r^2+4r+2-3r-2),$$
$$\sum_{k=1}^{\text{TODO: }n\text{ or }r}k^2=\frac16r(r+1)(2r+1).$$

> [!todo] Ambiguous handwriting — page 1, lower half
> After viewing the full page and a enlarged crop, the bounds of the sums and the variable after the final minus sign in the factorised expression cannot all be confidently distinguished as $n$ or $r$. These are marked in the formulas. Confirm from the original PDF before using this derivation; do not assume a consistent variable substitution.

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
&=\sum_{r=1}^{2n}r^2-\sum_{r=1}^{n}(2r)\\
&=\frac16\cdot2n(2n+1)(4n+1)-4\cdot\frac16n(n+1)(2n+1)\\
&=\frac13n(2n+1)(4n+1-2n-2)\\
&=\frac13(2n^2+n)(2n-1)\\
&=\frac13(4n^3-n).
\end{aligned}$$

> [!todo] Manual review — page 5, question 3(i), first line
> The subtracted sum is visibly $\sum(2r)$, with no square, while the next line uses four times a sum of squares. The missing exponent is not silently inserted.

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
The last line writes
$$7\mid8^n-1\quad\Longleftrightarrow\quad7\mid2^{n+2}+3^{2n+1}.$$

> [!todo] Manual review — page 5, question 3(iii), last line
> The written equivalence omits the preceding divisibility statement as a premise. Preserve the chain without supplying a missing argument.

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

“If $F_n$ is prime, then $\gcd(F_n,F_{n-k})=1$ for all $k\le n-1$. So using previous part, $n$ should be a prime. $F_4=2$, also a prime, so $n$ is prime or $n=4$.”

> [!todo] Manual review — page 7, middle
> The source writes $F_4=2$; this conflicts with the supplied recurrence. The gcd claim and deduction of the prime-index condition lack a complete justification. They remain original claims, not established results.

### (b) Last-digit periodicity (page 7, lower half)

The pair $(f_n,f_{n+1})$ has a finite amount of possibilities. Eventually there will be a pair
$$ (f_k,f_{k+1})=(f_n,f_{n+1}).$$
Since $f_{n+2}=f_{n+1}+f_n\pmod{10}$, therefore $f_n$ is periodic.

> [!todo] Incomplete reasoning — page 7, bottom
> Repetition and the forward recurrence establish eventual repetition. No backward argument or justification of periodicity from the beginning is written. No missing proof has been added.

## 6. Factorials (pages 8–9)

### (a) Difference of squares (page 8, upper half)

$$n!=a^2-b^2=(a+b)(a-b).$$
“$n=1$ doesn't work.” $n!$ is even for $n\ge2$, so $a+b$ or $a-b$ must be even. Since $a,b\in\mathbb Z$, $a+b$ and $a-b$ must both be even. Therefore $n!$ must have more than one factor of $2$. The written conclusion is $n!=a^2-b^2$ for $n\ge4$.

> [!todo] Manual review — page 8, question 6(a)
> The claim that $n=1$ does not work needs checking against the allowed squares. Sufficiency for every $n\ge4$ is asserted without a construction or proof.

### (b) Divisibility of the preceding factorial (page 8, lower half)

$$n=p_1^{a_1}p_2^{a_2}p_3^{a_3}\cdots,$$
where $p_n$ is prime and $a_n\in\mathbb Z$, $a_n\ge0$.

The source writes a product over exponent tuples with $i\le a_1$, $j\le a_2$, … and $(i,j,\ldots)\ne(a_1,a_2,\ldots)$:
$$\prod_{\substack{i\le a_1,\ j\le a_2,\ldots\\(i,j,\ldots)\ne(a_1,a_2,\ldots)}}p_1^ip_2^j\cdots\ \mid\ (n-1)!,$$
$$n\mid\prod_{\substack{i\le a_1,\ j\le a_2,\ldots\\(i,j,\ldots)\ne(a_1,a_2,\ldots)}}p_1^ip_2^j\cdots\quad\Longleftrightarrow\quad n\mid(n-1)!.$$
“Therefore $n\mid(n-1)!$ for non-prime $n$.”

> [!todo] Manual review — page 8, question 6(b)
> Lower bounds for the exponents are not written. The product equivalence and blanket conclusion for non-prime $n$ require review; the argument does not justify all exceptional cases. Preserve the claim rather than supplying a classification.

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
$$\log_3 4=\frac pq,\qquad4=3^{p/q},\qquad4^q=3^p.$$
$\gcd(4,3)=1$, so both equal is impossible for $p,q\in\mathbb Z$. Therefore $\log_3 4$ irrational.

> [!todo] Manual review — page 9, question 7(a), right column
> The logarithm argument does not state positivity of $p,q$ or $q\ne0$ and asserts impossibility for integers in general. Preserve its abbreviated reasoning.

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

- $r+\alpha$ irrational. $\alpha$ cannot be written as $\frac pq$, $p,q\in\mathbb N$, so $r+\alpha$ cannot be written as $\frac mn$, $m,n\in\mathbb N$; hence irrational.
- $r\alpha$ can be rational: let $r=0$.
- $\alpha+\beta$ can be rational: let $\alpha=-\beta$.
- $\alpha\beta$ can be rational: let $\alpha=\beta=\sqrt2$.
- $r^\alpha$ can be rational: let $r=3$, $\alpha=\log_3 4$.
- $\alpha^r$ can be rational: let $r=0$.
- $\alpha^\beta$ can be rational: let $\alpha=e$, $\beta=\ln3$.

> [!todo] Manual review — page 11, first and last bullets
> The first argument asserts the conclusion without showing how rationality of $r+\alpha$ would imply rationality of $\alpha$, and uses natural-number fractions despite the real domain. The last example does not prove irrationality of $e$ or $\ln3$, as requested in the sheet. No external proof has been supplied.

## 8. Pigeonhole attempts (page 12)

(i) Consider pairs $(1,2),(3,4),\ldots,(2n-1,2n)$. Two consecutive integers are coprime. Statement proved by pigeonhole principle.

(ii) Consider pairs $(1,2n),(2,2n-1),\ldots,(n,n+1)$; then use pigeonhole principle.

(iii) Consider different sets of numbers in the form $2^n$, $3\cdot2^n$, $5\cdot2^n$, $7\cdot2^n$, … . There are $n$ sets of these; then use pigeonhole principle.

(iv) For a set with $n+1$ elements, it produces $n$ distinct differences. Then use pigeonhole principle: first $n$ elements could not be in $\{\text{diff}\}$, but the $(n+1)$th element must be in $\{\text{diff}\}$.

Counterexamples written:

- (i) $n$ even numbers.
- (ii) $n$ odd numbers.
- (iii) $\{1,2,3,4\}$, $S=\{2,3\}$.
- (iv) $n$ odd numbers.

“No such example where all four fails.”

> [!todo] Incomplete reasoning — page 12, questions 8(iii)–(iv) and final sentence
> The ranges of the powers and the construction of the distinct differences are unspecified. The final simultaneous-counterexample claim is unproved. No missing reasoning is supplied.

## 9. Towns and coloured edges (pages 13–15)

### Superseded attempt (page 13)

The source lists:
$$A:B\text{ through }F\ (5),\quad B:C\text{ through }F\ (4),\quad C:D\text{ through }F\ (3),\quad D:E\text{ through }F\ (2),\quad E:F\ (1).$$
$15$ edges. At least $8$ edges are the same transport. Try to place the $8$ edges without forming a triangle. Assume $AB,CD,EF$ are edges that don't meet each other. Then list $AC,AD,AE,AF$.

A line separates this from the annotation **“IGNORE ABOVE”**. This work is superseded and incomplete, not an established proof.

### Six-town diagrams (page 14)

The coloured edges and labels are transcribed below. The source does not identify which colour denotes train or bus. Arrow-shaped ends appear in the source; no directed-graph interpretation is added. Consult the original PDF for the drawn layout.

[Original diagrams in Google Drive](https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view) — page 14.

From top to bottom:

1. Red edges drawn: $AB,AC,AD,AE,AF$. Blue edges drawn: $BC,CD,DE,EF$. Annotation: “$FD,EC,BD$ can be any colour.”
2. Red: $AC,AD,AE,AF$. Blue: $AB,CD,DE,EF$. Annotation: “$FD,EC$ can be any colour.”
3. Red: $AD,AE,AF$. Blue: $AB,AC,BC,CD,DE,EF$. Annotation: “$FD$ can be any colour.”

> [!todo] Incomplete attempt — page 14
> These are partial diagrams, not complete edge colourings of all pairs. No complete written case argument establishes the six-town conclusion. Undrawn edges must not be reconstructed.

### Five-town diagrams (page 15)

[Original diagrams in Google Drive](https://drive.google.com/file/d/1cAxWubfgZfijKE33WolS74BS9m1Sccpn/view) — page 15.

Upper-left diagram: red $AB,AC,AD,AE$; blue $BC,CD,DE$.

Upper-right diagram: red $AC,AD,AE$; blue $AB,CD,DE$.

Lower-left completed diagram: red $AE,AD,BE,BC,CD$; blue $AB,AC,BD,CE,DE$.

Written conclusion: “Not true if only $5$ towns.” No further prose argument is supplied. No attempts at questions 10–12 appear in this PDF.
