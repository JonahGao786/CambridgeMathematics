---
title: Vectors and Matrices - Chapter 1 Complex Numbers
material_type: handwritten lecture notes
course: Part IA Vectors and Matrices
date: null
source_file: Ch.1 Complex Numbers.pdf
drive_file_id: 1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh
source_url: https://drive.google.com/file/d/1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh/view
source_pages: 21
---

# Vectors and Matrices — Chapter 1: Complex Numbers

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh/view). The handwritten date is not supplied.

## Course contents (page 1)

1. Complex Numbers.
2. Vectors.
3. Matrices.
4. Eigenvalues and Eigenvectors.

## 1.1 Real numbers (page 2)

The number systems satisfy
$$\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R\subset\mathbb C.$$

- Natural numbers: $\mathbb N=\{1,2,3,\ldots\}$.
- Integers: $\mathbb Z=\{\ldots,-1,0,1,2,\ldots\}$.
- Rational numbers: $\mathbb Q=\{p/q:p,q\in\mathbb Z,\ q\ne0\}$.
- Real numbers: rational and irrational numbers together. Examples of irrational numbers given: $\sqrt2,\pi,e$.

## 1.2 Complex numbers (page 2)

$$\mathbb C=\{x+iy:x,y\in\mathbb R\},\qquad i^2=-1.$$
For $z=x+iy$, the real part is $\operatorname{Re}(z)=x$ and the imaginary part is $\operatorname{Im}(z)=y$.

1. Representation is unique:
   $$x+iy=u+iv\quad\Longleftrightarrow\quad x=u,\ y=v.$$
2. Identify $x\in\mathbb R$ with $x+i0\in\mathbb C$.
3. Numbers $iy$ with $y\ne0$ are **purely imaginary**.

See [[Complex Numbers]].

### 1.2.1 Arithmetic (page 3)

Let $z_1=x_1+iy_1$ and $z_2=x_2+iy_2$.

Addition, and similarly subtraction, is componentwise:
$$z_1+z_2=(x_1+x_2)+i(y_1+y_2).$$
Multiplication:
$$z_1z_2=(x_1x_2-y_1y_2)+i(x_1y_2+x_2y_1).$$

Properties:

1. Addition and multiplication are associative and commutative.
2. The additive identity is $0$; the additive inverse of $z$ is $-z$.
3. The multiplicative identity is $1$. For $z=x+iy\ne0$,
   $$z^{-1}=\frac{x-iy}{x^2+y^2},\qquad zz^{-1}=1.$$
4. Distributivity:
   $$z_1(z_2+z_3)=z_1z_2+z_1z_3.$$

### 1.2.2 Conjugate and modulus (page 4)

For $z=x+iy$, define
$$\overline z=x-iy,\qquad |z|=\sqrt{x^2+y^2}.$$
The modulus is a non-negative real number, with
$$|z|=0\quad\Longleftrightarrow\quad z=0,$$
and
$$z\overline z=|z|^2=x^2+y^2.$$

For $z_1,z_2,z_3\in\mathbb C$:
$$
\begin{aligned}
\overline{\overline z}&=z,\\
\overline{z_1+z_2}&=\overline{z_1}+\overline{z_2},\\
\overline{z_1z_2}&=\overline{z_1}\,\overline{z_2},\\
|\overline z|&=|z|,\\
\operatorname{Re}(z)&=\frac{z+\overline z}{2},\qquad
\operatorname{Im}(z)=\frac{z-\overline z}{2i}.
\end{aligned}
$$
In particular, $z$ is real exactly when $z=\overline z$.

**Division.** For $z_2\ne0$,
$$\frac{z_1}{z_2}=\frac{z_1\overline{z_2}}{|z_2|^2}.$$
For example,
$$\frac{1+2i}{3-i}=\frac{(1+2i)(3+i)}{(3-i)(3+i)}=\frac{1+7i}{10}.$$

### 1.2.3 Argument and polar form (page 5, upper part)

For $z=x+iy\ne0$, an argument of $z$ is an angle $\theta\in\mathbb R$ such that
$$z=r(\cos\theta+i\sin\theta),\qquad r=|z|.$$
This is the **polar form** of $z$; see [[Complex Numbers]].
$$x=r\cos\theta,\qquad y=r\sin\theta,$$
so
$$\cos\theta=\frac{x}{r}=\frac{x}{\sqrt{x^2+y^2}},\qquad
\sin\theta=\frac{y}{r}=\frac{y}{\sqrt{x^2+y^2}}.$$

The principal argument satisfies $\arg(z)\in(-\pi,\pi]$. The set of all arguments is
$$\operatorname{Arg}(z)=\{\arg(z)+2\pi n:n\in\mathbb Z\}.$$
The argument of $0$ is undefined.

### 1.2.4 Further properties (pages 5–7)

**[[Fundamental Theorem of Algebra]]** (page 5, lower part). Every polynomial of degree $n\ge1$ with complex coefficients factors as
$$p(z)=c_nz^n+\cdots+c_0=c_n(z-\alpha_1)\cdots(z-\alpha_n),$$
where $c_n\ne0$ and $\alpha_1,\ldots,\alpha_n\in\mathbb C$. It has exactly $n$ roots counted with multiplicity. No proof of this theorem is supplied in the source.

**Modulus properties** (page 6). For $z_1,z_2\in\mathbb C$:
$$
\begin{aligned}
|z_1z_2|&=|z_1|\,|z_2|,\\
\left|\frac{z_1}{z_2}\right|&=\frac{|z_1|}{|z_2|}\quad(z_2\ne0),\\
|z_1+z_2|&\le |z_1|+|z_2|,\\
\bigl||z_1|-|z_2|\bigr|&\le |z_1-z_2|.
\end{aligned}
$$
The last two are the [[Triangle Inequality for Complex Numbers|triangle and reverse triangle inequalities]].

**Proof of multiplicativity.** Square both sides:
$$|z_1z_2|^2=z_1z_2\overline{z_1}\,\overline{z_2}=|z_1|^2|z_2|^2.$$
Taking non-negative square roots gives the first property. Apply it to $z_1/z_2$ and $z_2$:
$$\left|\frac{z_1}{z_2}\,z_2\right|^2=
\left|\frac{z_1}{z_2}\right|^2|z_2|^2=|z_1|^2,$$
and divide by $|z_2|^2>0$ to obtain the quotient property.

**Proof of the triangle inequality** (page 7). Write $z_j=x_j+iy_j$ with $x_j,y_j\in\mathbb R$. Use $\operatorname{Re}(z)\le |z|$. Then
$$
\begin{aligned}
|z_1+z_2|^2
&=(x_1+x_2)^2+(y_1+y_2)^2\\
&=x_1^2+y_1^2+x_2^2+y_2^2+2x_1x_2+2y_1y_2\\
&=|z_1|^2+|z_2|^2+2\operatorname{Re}(z_1\overline{z_2})\\
&\le |z_1|^2+|z_2|^2+2|z_1|\,|\overline{z_2}|\\
&=|z_1|^2+|z_2|^2+2|z_1|\,|z_2|\\
&=(|z_1|+|z_2|)^2.
\end{aligned}
$$
Take non-negative square roots. For the reverse inequality,
$$|z_1|=|(z_1-z_2)+z_2|\le |z_1-z_2|+|z_2|.$$
Rearrange and interchange $z_1,z_2$ to obtain both bounds and hence the reverse triangle inequality.

## 1.3 Argand diagram (page 8)

Represent $z=x+iy$ by the point $(x,y)$, or by its position vector from the origin. Horizontal axis: $\operatorname{Re}$; vertical axis: $\operatorname{Im}$.

The diagrams are drawn directly in TikZ for the installed TikZJax plugin. Their coordinates set the layout of the qualitative source sketches, without asserting numerical values for the labelled variables.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.1,>=latex]
  \coordinate (O) at (0,0);
  \coordinate (Z) at (3,1.8);
  \draw[->] (-0.35,0) -- (4.1,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-0.35) -- (0,2.7) node[above] {$\mathrm{Im}$};
  \draw[densely dotted] (0,1.8) node[left] {$y$} -- (Z) -- (3,0) node[below] {$x$};
  \draw[->,red,thick] (O) -- (Z) node[midway,above,sloped,text=black] {$r=|z|$};
  \fill (Z) circle (1.3pt);
  \node[above right] at (Z) {$z=x+iy$};
  \node[below left] at (O) {$0$};
\end{tikzpicture}
\end{document}
```

### 1.3.1 Addition and subtraction (page 8, lower part)

- $z_1+z_2$: the parallelogram rule, shown in blue with dashed translated sides.
- $z_1-z_2$: the displacement from $z_2$ to $z_1$, shown in red and also translated to start at the origin.
- $|z_1-z_2|$: the distance between the two points, equal to the length of either red arrow.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.1,>=latex]
  \coordinate (O) at (0,0);
  \coordinate (Z1) at (1.2,2.1);
  \coordinate (Z2) at (2.25,0.8);
  \coordinate (Sum) at (3.45,2.9);
  \coordinate (Difference) at (-1.05,1.3);
  \draw[->] (-1.7,0) -- (4.2,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-0.35) -- (0,3.5) node[above] {$\mathrm{Im}$};
  \draw[->,thick] (O) -- (Z1);
  \draw[->,thick] (O) -- (Z2);
  \draw[->,blue,thick] (O) -- (Sum);
  \draw[->,blue,dashed] (Z1) -- (Sum);
  \draw[->,blue,dashed] (Z2) -- (Sum);
  \draw[->,red,thick] (Z2) -- (Z1);
  \draw[->,red,thick] (O) -- (Difference);
  \node[above left] at (Z1) {$z_1$};
  \node[below right] at (Z2) {$z_2$};
  \node[above right,blue] at (Sum) {$z_1+z_2$};
  \node[above left,red] at (Difference) {$z_1-z_2$};
  \node[below left] at (O) {$0$};
\end{tikzpicture}
\end{document}
```

### 1.3.2 Complex conjugation (page 9, top)

Conjugation reflects $x+iy$ across the real axis to $x-iy$. The dotted vertical line joins the two reflected points.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.1,>=latex]
  \coordinate (O) at (0,0);
  \coordinate (Z) at (2.4,1.3);
  \coordinate (Conjugate) at (2.4,-1.3);
  \draw[->] (-0.35,0) -- (3.7,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-1.8) -- (0,2) node[above] {$\mathrm{Im}$};
  \draw[densely dotted] (Z) -- (Conjugate);
  \draw[->,red,thick] (O) -- (Z);
  \draw[->,blue,thick] (O) -- (Conjugate);
  \node[above right,red] at (Z) {$x+iy$};
  \node[below right,blue] at (Conjugate) {$x-iy$};
  \node[below left] at (O) {$0$};
\end{tikzpicture}
\end{document}
```

## 1.4 De Moivre's theorem (pages 9–10)

**Lemma** (page 9). For
$$z_j=r_j(\cos\theta_j+i\sin\theta_j),\qquad j=1,2,$$
we have
$$z_1z_2=r_1r_2\bigl(\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\bigr).$$

**Proof.** Expand the product:
$$
z_1z_2=r_1r_2\bigl(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2
+i(\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2)\bigr).
$$
Use the angle addition formulae
$$
\begin{aligned}
\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2&=\cos(\theta_1+\theta_2),\\
\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2&=\sin(\theta_1+\theta_2).
\end{aligned}
$$

**Remarks.** Moduli multiply and arguments add modulo $2\pi$:
$$\arg(z_1z_2)\equiv\arg(z_1)+\arg(z_2)\pmod{2\pi}\qquad(z_1,z_2\ne0).$$
For division, moduli divide and arguments subtract.

**[[De Moivre's Theorem]]** (page 10). For $\theta\in\mathbb R$ and $n\in\mathbb Z$,
$$ (\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta).$$

**Proof.** For $n\ge0$, use induction. At $n=0$, both sides equal $1$. For the step from $n$ to $n+1$, multiply the inductive expression by $\cos\theta+i\sin\theta$ and apply the preceding lemma.

For $n=-m<0$, use the positive-power case and $|\cos\theta+i\sin\theta|=1$:
$$
\begin{aligned}
(\cos\theta+i\sin\theta)^{-m}
&=\frac{1}{\cos(m\theta)+i\sin(m\theta)}\\
&=\cos(m\theta)-i\sin(m\theta)\\
&=\cos(-m\theta)+i\sin(-m\theta).
\end{aligned}
$$
This proves the integer-power statement.

**Consequence.** For $z=r(\cos\theta+i\sin\theta)\ne0$ and $n\in\mathbb Z$,
$$z^n=r^n\bigl(\cos(n\theta)+i\sin(n\theta)\bigr).$$
For example,
$$ (1+i)^4=(\sqrt2)^4(\cos\pi+i\sin\pi)=-4.$$

## 1.5 Exponential and trigonometric functions (pages 11–15)

### 1.5.1 The complex exponential (pages 11–13)

For $z\in\mathbb C$, define
$$\exp(z)=e^z=\sum_{n=0}^{\infty}\frac{z^n}{n!}
=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots.$$
This converges absolutely for every $z$. For $z\ne0$, the ratio of successive absolute terms is
$$\frac{|z|^{n+1}}{(n+1)!}\frac{n!}{|z|^n}
=\frac{|z|}{n+1}\longrightarrow0.$$
For $z=0$ the series is simply $1$.

For $z,w\in\mathbb C$ and $n\in\mathbb Z$:
$$
e^ze^w=e^{z+w},\qquad e^0=1,\qquad
e^{-z}=\frac1{e^z},\qquad (e^z)^n=e^{nz}.
$$
In particular $e^z\ne0$ for every $z\in\mathbb C$.

**Proof of the product rule for exponentials** (page 12). Expand and multiply:
$$
\begin{aligned}
\left(\sum_{j=0}^{\infty}\frac{z^j}{j!}\right)
\left(\sum_{k=0}^{\infty}\frac{w^k}{k!}\right)
&=\sum_{m=0}^{\infty}\sum_{k=0}^m
\frac{z^kw^{m-k}}{k!(m-k)!}\\
&=\sum_{m=0}^{\infty}\frac1{m!}
\sum_{k=0}^m\binom mkz^kw^{m-k}\\
&=\sum_{m=0}^{\infty}\frac{(z+w)^m}{m!}
=e^{z+w}.
\end{aligned}
$$
**Explanation.** Absolute convergence permits grouping the product terms by their total degree $m=j+k$. The inner sum is finite and the binomial theorem applies. This grouping is not justified for arbitrary conditionally convergent series.

Substitution gives $e^0=1$. The product rule then gives $e^ze^{-z}=1$, so $e^z$ is non-zero and $e^{-z}=1/e^z$.

**Proof of the integer-power rule** (page 13). The case $n=0$ is immediate. Assuming $(e^z)^n=e^{nz}$ for $n\ge0$, the product rule gives
$$(e^z)^{n+1}=(e^z)^ne^z=e^{nz}e^z=e^{(n+1)z}.$$
For $n=-m<0$, the positive-power result and reciprocal identity give
$$(e^z)^n=(e^z)^{-m}=\frac1{(e^z)^m}
=\frac1{e^{mz}}=e^{-mz}=e^{nz}.$$

### 1.5.2 Trigonometric functions and Euler's formula (pages 13–14)

For $z\in\mathbb C$, define
$$
\begin{aligned}
\cos z&=\frac{e^{iz}+e^{-iz}}2
=\sum_{n=0}^{\infty}(-1)^n\frac{z^{2n}}{(2n)!},\\
\sin z&=\frac{e^{iz}-e^{-iz}}{2i}
=\sum_{n=0}^{\infty}(-1)^n\frac{z^{2n+1}}{(2n+1)!}.
\end{aligned}
$$
For real inputs, these reduce to the usual trigonometric functions.

Adding the defining expressions gives **Euler's formula**:
$$
\cos z+i\sin z
=\frac{e^{iz}+e^{-iz}}2+\frac{e^{iz}-e^{-iz}}2
=e^{iz}.
$$
Thus $e^{iz}=\cos z+i\sin z$ for every $z\in\mathbb C$.

For a **real** angle $\theta$,
$$\operatorname{Re}(e^{i\theta})=\cos\theta,\qquad
\operatorname{Im}(e^{i\theta})=\sin\theta,\qquad |e^{i\theta}|=1.$$
More generally, for $x,y\in\mathbb R$,
$$e^{x+iy}=e^x(\cos y+i\sin y),\qquad |e^{x+iy}|=e^x.$$
The latter formula also appears at the end of page 12.

**Lemma** (page 14). For $z\in\mathbb C$,
$$e^z=1\quad\Longleftrightarrow\quad z=2\pi in
\quad\text{for some }n\in\mathbb Z.$$
**Proof.** Write $z=x+iy$. If $e^z=1$, its modulus gives $e^x=1$, hence $x=0$. Its real and imaginary parts give $\cos y=1$ and $\sin y=0$, so $y=2\pi n$. The converse follows by substitution.

Consequently,
$$e^z=e^w\quad\Longleftrightarrow\quad
z-w=2\pi in\quad\text{for some }n\in\mathbb Z.$$
Indeed, divide by the non-zero $e^w$ and use the lemma. The complex exponential is periodic with period $2\pi i$ and is not one-to-one.

**Exponential polar form.** For $z\ne0$,
$$z=re^{i\theta},\qquad r=|z|>0,\quad\theta\in\operatorname{Arg}(z).$$
Then
$$z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)},\qquad
z^n=r^ne^{in\theta}\quad(n\in\mathbb Z).$$
See [[Complex Exponential and Trigonometric Functions]].

### 1.5.3 Roots of unity (page 15)

Fix an integer $N\ge1$ and solve $z^N=1$. Write $z=re^{i\theta}$. Then
$$r^Ne^{iN\theta}=1
\quad\Longleftrightarrow\quad
r=1,\quad N\theta=2\pi n\quad(n\in\mathbb Z).$$
The $N$ distinct roots are
$$z_k=e^{2\pi ik/N}=\omega^k,\qquad
k=0,\ldots,N-1,\quad\omega=e^{2\pi i/N}.$$
They lie on the unit circle, equally spaced by angle $2\pi/N$. For $N\ge3$, they are the vertices of a regular $N$-gon. See [[Roots of Unity]].

For a non-zero complex number $a=Re^{i\theta}$, $R>0$,
$$z^N=a\quad\Longleftrightarrow\quad
z=R^{1/N}e^{i(\theta+2\pi n)/N},\qquad n=0,\ldots,N-1.$$
Here $R^{1/N}$ is the positive real root. The roots lie equally spaced on the circle of radius $R^{1/N}$. If $a=0$, the only root is $z=0$, with multiplicity $N$.

## 1.6 Logarithms and complex powers (pages 16–18)

### 1.6.1 Logarithms and principal values (page 16)

For $z\ne0$, a **logarithm** of $z$ is $w\in\mathbb C$ satisfying $e^w=z$.

The exponential is many-to-one. If $w$ is a logarithm, then $w+2\pi in$ is also a logarithm for every $n\in\mathbb Z$.

Write $z=re^{i\theta}$. Since
$$z=e^{\log r}e^{i\theta}=e^{\log r+i\theta},$$
all its logarithms are $\log r+i\theta$ for $\theta\in\operatorname{Arg}(z)$. Here $\log r$ is the real natural logarithm.

Following the source's notation and argument interval $(-\pi,\pi]$, define
$$
\begin{aligned}
\log z&=\log|z|+i\arg(z)
&&\text{(principal logarithm)},\\
\operatorname{Log}z
&=\{\log z+2\pi in:n\in\mathbb Z\}
&&\text{(all logarithms)}.
\end{aligned}
$$
The capitalized $\operatorname{Log}z$ denotes a **set** here; conventions in other texts may differ. See [[Complex Logarithms and Powers]].

### 1.6.2 Complex powers (page 17)

For $z\ne0$ and $\alpha\in\mathbb C$, choose $L\in\operatorname{Log}z$ and define the corresponding value
$$z^\alpha=e^{\alpha L}.$$
Changing $L$ to $L+2\pi in$ multiplies this value by $e^{2\pi in\alpha}$. The principal value is $e^{\alpha\log z}$.

1. If $\alpha=p\in\mathbb Z$, then $e^{2\pi inp}=1$. There is one value, agreeing with the integer power.
2. If $\alpha=p/q\in\mathbb Q$ in lowest terms with $q>0$, the multipliers $e^{2\pi inp/q}$ have exactly $q$ distinct values. Thus $z^{p/q}$ has exactly $q$ values.
3. Otherwise there are infinitely many values.

**Power laws with compatible choices.** Using the same fixed $L\in\operatorname{Log}z$,
$$z^\alpha z^\beta=e^{\alpha L}e^{\beta L}
=e^{(\alpha+\beta)L}=z^{\alpha+\beta}.$$
For the nested power, choose $u=e^{\alpha L}$ as the value of $z^\alpha$, then choose $\alpha L$ as a logarithm of $u$. This is legitimate because $e^{\alpha L}=u$. With these choices,
$$(z^\alpha)^\beta=u^\beta=e^{\beta(\alpha L)}
=e^{(\alpha\beta)L}=z^{\alpha\beta}.$$
The equalities require these compatible logarithms; independently taking principal values need not preserve them.

### 1.6.3 Examples (page 18)

**1. Logarithms of $i$ and the power $i^i$.** Since $i=e^{i\pi/2}$ and $|i|=1$,
$$
\operatorname{Arg}(i)=\{\pi/2+2\pi n:n\in\mathbb Z\},\qquad
\log i=i\pi/2,\qquad
\operatorname{Log}i=\{i(\pi/2+2\pi n):n\in\mathbb Z\}.
$$
The values of $i^i$ are therefore
$$e^{i(\log i+2\pi in)}
=e^{-(\pi/2+2\pi n)},\qquad n\in\mathbb Z.$$
There are infinitely many values, all positive real. The principal value, at $n=0$, is $e^{-\pi/2}$.

**2. Logarithms and square roots of $1+i$.** Since $1+i=\sqrt2e^{i\pi/4}$,
$$
\log(1+i)=\frac12\log2+\frac{i\pi}4,\qquad
\operatorname{Log}(1+i)
=\left\{\frac12\log2+i\left(\frac\pi4+2\pi n\right):n\in\mathbb Z\right\}.
$$
Its square roots are
$$
\begin{aligned}
(1+i)^{1/2}
&=e^{\frac12(\log(1+i)+2\pi in)}\\
&=e^{\frac14\log2+i(\pi/8+\pi n)}
=2^{1/4}e^{i(\pi/8+\pi n)}\\
&=
\begin{cases}
2^{1/4}e^{i\pi/8},&n\text{ even},\\
-2^{1/4}e^{i\pi/8},&n\text{ odd}.
\end{cases}
\end{aligned}
$$
There are exactly two roots, of modulus $2^{1/4}$ and opposite directions. The principal square root is $2^{1/4}e^{i\pi/8}$.

## 1.7 Lines and circles (pages 19–21)

### 1.7.1 Lines (page 19)

A line through $z_0\in\mathbb C$ in a non-zero direction $w\in\mathbb C$ is
$$z=z_0+\lambda w,\qquad\lambda\in\mathbb R.$$
Since $\lambda$ is real, conjugating gives $\overline z=\overline{z_0}+\lambda\overline w$. Eliminate $\lambda$:
$$
\frac{z-z_0}{w}
=\frac{\overline z-\overline{z_0}}{\overline w}.
$$
Cross-multiplying,
$$\overline w\,z-\overline w\,z_0
=w\overline z-w\overline{z_0}.$$

The example has $z_0=1+i$ and $w=1-i$, so $x=1+\lambda$, $y=1-\lambda$, and $x+y=2$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=1.1]
  \draw[->] (-0.8,0)--(3.6,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-0.8)--(0,3.6) node[above] {$\mathrm{Im}$};
  \foreach \t in {1,2,3} {
    \draw (\t,0.05)--(\t,-0.05) node[below] {$\t$};
    \draw (0.05,\t)--(-0.05,\t) node[left] {$\t$};
  }
  \draw[<->,blue,thick] (-0.7,2.7)--(2.7,-0.7);
  \draw[densely dashed] (0,1)--(1,1)--(1,0);
  \fill (1,1) circle (1.4pt);
  \node[above right] at (1,1) {$z_0=1+i$};
  \draw[->,red,thick] (1,1)--(2,0)
    node[midway,above right] {$w=1-i$};
  \node[blue,below right] at (2.65,-0.7) {$x+y=2$};
\end{tikzpicture}
\end{document}
```

### 1.7.2 Circles (page 20)

For centre $c\in\mathbb C$ and radius $\rho>0$, equivalent descriptions of the circle are:

1. $z=c+\rho e^{i\theta}$ for $\theta\in\mathbb R$ (parametric form).
2. $|z-c|=\rho$ (distance from centre).
3. $|z|^2-c\overline z-\overline c z=\rho^2-|c|^2$ (expanded equation).

To obtain the last form,
$$
\begin{aligned}
|z-c|^2&=\rho^2,\\
(z-c)(\overline z-\overline c)&=\rho^2,\\
|z|^2-c\overline z-\overline c z&=\rho^2-|c|^2.
\end{aligned}
$$

### 1.7.3 Geometric transformations (page 21)

| Transformation | Map | Conditions |
| --- | --- | --- |
| Translation | $z\mapsto z+z_0$ | $z_0\in\mathbb C$ |
| Positive scaling | $z\mapsto\lambda z$ | $\lambda>0$ |
| Rotation about the origin | $z\mapsto ze^{i\theta}$ | $\theta\in\mathbb R$ |
| Reflection in the real axis | $z\mapsto\overline z$ | |
| Complex inversion | $z\mapsto1/z$ | $z\ne0$ |

The examples use $z_1=1+i$. Their images are
$$
\begin{aligned}
z_1+(1-i)&=2,&2z_1&=2+2i,&iz_1&=-1+i,\\
\overline{z_1}&=1-i,&-z_1&=-1-i,&1/z_1&=(1-i)/2.
\end{aligned}
$$
Blue arrows show $z_1$ and red arrows its image, as in the source. The translation panel also shows the displacement $1-i$; the rotation arc and reflection guide preserve their geometric information.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=0.85,every node/.style={font=\small}]
  \fill[gray!15] (0,0)--(1,1)--(2,0)--cycle;
  \foreach \x/\y in {0/0,5.5/0,11/0,0/-5.7,5.5/-5.7,11/-5.7} {
    \begin{scope}[shift={(\x,\y)}]
      \draw[->] (-1.7,0)--(2.6,0) node[right] {$\mathrm{Re}$};
      \draw[->] (0,-1.7)--(0,2.6) node[above] {$\mathrm{Im}$};
      \draw[->,blue,thick] (0,0)--(1,1);
    \end{scope}
  }
  \foreach \x/\y in {0/0,11/0,0/-5.7,5.5/-5.7,11/-5.7} {
    \begin{scope}[shift={(\x,\y)}]
      \node[blue,above right] at (1,1) {$1+i$};
    \end{scope}
  }
  \node[blue,above left] at (6.5,1) {$1+i$};
  \begin{scope}
    \node[anchor=south] at (0.5,3.15) {Translation: $z\mapsto z+1-i$};
    \draw[->] (1,1)--(2,0) node[midway,above right] {$1-i$};
    \draw[->,red,thick] (0,0)--(2,0) node[below right] {$2$};
  \end{scope}
  \begin{scope}[shift={(5.5,0)}]
    \node[anchor=south] at (0.5,3.15) {Scaling: $z\mapsto2z$};
    \draw[->,red,thick] (0,0)--(2,2) node[above right] {$2+2i$};
  \end{scope}
  \begin{scope}[shift={(11,0)}]
    \node[anchor=south] at (0.5,3.15) {Rotation: $z\mapsto iz$};
    \draw[->,red,thick] (0,0)--(-1,1) node[above left] {$-1+i$};
    \draw[->,densely dashed] (1,1) arc[start angle=45,end angle=135,radius=1.4142];
  \end{scope}
  \begin{scope}[shift={(0,-5.7)}]
    \node[anchor=south] at (0.5,3.15) {Reflection: $z\mapsto\overline z$};
    \draw[densely dashed] (1,1)--(1,-1);
    \draw[->,red,thick] (0,0)--(1,-1) node[below right] {$1-i$};
  \end{scope}
  \begin{scope}[shift={(5.5,-5.7)}]
    \node[anchor=south] at (0.5,3.15) {Negative scaling: $z\mapsto-z$};
    \draw[->,red,thick] (0,0)--(-1,-1) node[below left] {$-1-i$};
  \end{scope}
  \begin{scope}[shift={(11,-5.7)}]
    \node[anchor=south] at (0.5,3.15) {Reciprocal: $z\mapsto1/z$};
    \draw[->,red,thick] (0,0)--(0.5,-0.5) node[below right] {$(1-i)/2$};
  \end{scope}
\end{tikzpicture}
\end{document}
```

**Explanation.** For $z=re^{i\phi}\ne0$, inversion gives $1/z=r^{-1}e^{-i\phi}$: it reciprocates the modulus and reverses the angle. Positive scaling preserves the angle, whereas multiplication by $-1$ rotates it by $\pi$.
