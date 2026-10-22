---
title: Vectors and Matrices - Chapter 1 Complex Numbers
course: Part IA Vectors and Matrices
material_type: lecture notes
chapter: 1
source_file: Ch.1 Complex Numbers.pdf
drive_file_id: 1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh
source_url: https://drive.google.com/file/d/1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh/view
source_pages: 21
tags: [lecture, vectors-and-matrices]
---

# Vectors and Matrices — Chapter 1: Complex Numbers

> [!abstract] Overview
> Arithmetic, conjugate, modulus and argument of complex numbers; the Argand diagram; De Moivre's theorem; the complex exponential and Euler's formula; roots of unity; multi-valued logarithms and powers; lines, circles and transformations of the plane.
> Course chapters: 1 Complex Numbers · 2 Vectors · 3 Matrices · 4 Eigenvalues and Eigenvectors.

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Complex numbers]] | $\mathbb C=\{x+iy\}$, $i^2=-1$ | 2 |
| [[#Definition — Conjugate and modulus]] | $\bar z$, $\lvert z\rvert$, $z\bar z=\lvert z\rvert^2$ | 4 |
| [[#Definition — Argument and polar form]] | $z=r(\cos\theta+i\sin\theta)$, $\arg z\in(-\pi,\pi]$ | 5 |
| [[#Theorem — Fundamental theorem of algebra]] | degree $n$ polynomial has $n$ roots | 5 |
| [[#Proposition — Properties of the modulus]] | multiplicative; triangle inequalities | 6–7 |
| [[#Lemma — Multiplying in polar form]] | moduli multiply, arguments add | 9 |
| [[#Theorem — De Moivre's theorem]] | $(\cos\theta+i\sin\theta)^n=\cos n\theta+i\sin n\theta$ | 10 |
| [[#Definition — Complex exponential]] | $e^z=\sum z^n/n!$ | 11 |
| [[#Proposition — Properties of the exponential]] | $e^ze^w=e^{z+w}$, $e^0=1$, $e^{-z}=1/e^z$, $(e^z)^n=e^{nz}$ | 11–13 |
| [[#Definition — Complex sine and cosine]] | Euler's formula $e^{iz}=\cos z+i\sin z$ | 13 |
| [[#Lemma — When the exponential equals 1]] | $e^z=1\iff z=2\pi in$; periodicity | 14 |
| [[#Roots of unity]] | $z^N=1\iff z=e^{2\pi ik/N}$ | 15 |
| [[#Definition — Logarithm]] | $\log z$, $\operatorname{Log}z$ | 16 |
| [[#Definition — Complex powers]] | $z^\alpha=e^{\alpha L}$; number of values; power laws | 17 |
| [[#Lines]] | $\bar wz-\bar wz_0=w\bar z-w\bar z_0$ | 19 |
| [[#Circles]] | $\lvert z-c\rvert=\rho$ | 20 |
| [[#Geometric transformations]] | translation, scaling, rotation, reflection, inversion | 21 |

## 1.1 Real numbers

$\mathbb N\subset\mathbb Z\subset\mathbb Q\subset\mathbb R\subset\mathbb C$, where $\mathbb N=\{1,2,3,\dots\}$, $\mathbb Z=\{\dots,-1,0,1,2,\dots\}$, $\mathbb Q=\{p/q:p,q\in\mathbb Z,\ q\ne0\}$, and $\mathbb R$ is the rational and irrational numbers together (irrationals: $\sqrt2,\pi,e$).

## 1.2 Complex numbers

### Definition — Complex numbers

$$\mathbb C=\{x+iy:\ x,y\in\mathbb R\},\qquad i^2=-1.$$
For $z=x+iy$: **real part** $\operatorname{Re}(z)=x$, **imaginary part** $\operatorname{Im}(z)=y$.

**Remarks.** (1) The representation is unique: $x+iy=u+iv\iff x=u,\ y=v$. (2) Identify $x\in\mathbb R$ with $x+i0\in\mathbb C$. (3) Numbers $iy$ with $y\in\mathbb R$ are **purely imaginary**.

**1.2.1 Arithmetic.** For $z_1=x_1+iy_1$, $z_2=x_2+iy_2$:
$$z_1+z_2=(x_1+x_2)+i(y_1+y_2),\qquad z_1z_2=(x_1x_2-y_1y_2)+i(x_1y_2+x_2y_1).$$

**Properties.**
1. Addition and multiplication are associative and commutative.
2. Additive identity $0$; additive inverse of $z$ is $-z$.
3. Multiplicative identity $1$; for $z=x+iy\ne0$, $z^{-1}=\dfrac{x-iy}{x^2+y^2}$, so $zz^{-1}=1$.
4. Distributivity: $z_1(z_2+z_3)=z_1z_2+z_1z_3$.

### Definition — Conjugate and modulus

For $z=x+iy$: **complex conjugate** $\bar z=x-iy$, **modulus** $|z|=\sqrt{x^2+y^2}$.

1. $|z|$ is a non-negative real number, and $|z|=0\iff z=0$.
2. $z\bar z=|z|^2=x^2+y^2$.

**Properties.**
$$\bar{\bar z}=z,\qquad\overline{z_1+z_2}=\bar z_1+\bar z_2,\qquad\overline{z_1z_2}=\bar z_1\,\bar z_2,\qquad|\bar z|=|z|,$$
$$\operatorname{Re}(z)=\frac{z+\bar z}2,\qquad\operatorname{Im}(z)=\frac{z-\bar z}{2i}.$$
In particular $z$ is real exactly when $z=\bar z$.

**Division.** For $z_2\ne0$, $\dfrac{z_1}{z_2}=\dfrac{z_1\bar z_2}{|z_2|^2}$. E.g. $\dfrac{1+2i}{3-i}=\dfrac{(1+2i)(3+i)}{(3-i)(3+i)}=\dfrac{1+7i}{10}$.

### Definition — Argument and polar form

For $z=x+iy\ne0$, an **argument** of $z$ is an angle $\theta\in\mathbb R$ with
$$z=r(\cos\theta+i\sin\theta),\qquad r=|z|.$$
This is the **polar form** of $z$. So $x=r\cos\theta$, $y=r\sin\theta$, and
$$\cos\theta=\frac xr=\frac x{\sqrt{x^2+y^2}},\qquad\sin\theta=\frac yr=\frac y{\sqrt{x^2+y^2}}.$$

1. **Principal argument:** $\arg(z)\in(-\pi,\pi]$.
2. **Set of all arguments:** $\operatorname{Arg}(z)=\{\arg(z)+2\pi n:\ n\in\mathbb Z\}$.

The argument of $0$ is undefined.

### Theorem — Fundamental theorem of algebra

Every polynomial of degree $n\ge1$ with complex coefficients factors as
$$p(z)=c_nz^n+\dots+c_0=c_n(z-\alpha_1)\cdots(z-\alpha_n),\qquad c_n\ne0,$$
where $\alpha_1,\dots,\alpha_n\in\mathbb C$. Hence it has exactly $n$ roots, counted with multiplicity.

### Proposition — Properties of the modulus

For $z_1,z_2\in\mathbb C$:

1. $|z_1z_2|=|z_1|\,|z_2|$;
2. $\left|\dfrac{z_1}{z_2}\right|=\dfrac{|z_1|}{|z_2|}$ for $z_2\ne0$;
3. $|z_1+z_2|\le|z_1|+|z_2|$ (**triangle inequality**);
4. $\big||z_1|-|z_2|\big|\le|z_1-z_2|$ (**reverse triangle inequality**).

**Proof.** (1) Multiplicativity follows by squaring: $|z_1z_2|^2=z_1z_2\bar z_1\bar z_2=|z_1|^2|z_2|^2$.

(2) Apply (1) to $\frac{z_1}{z_2}$ and $z_2$: $\left|\frac{z_1}{z_2}z_2\right|^2=\left|\frac{z_1}{z_2}\right|^2|z_2|^2=|z_1|^2$, so $\left|\frac{z_1}{z_2}\right|^2=\frac{|z_1|^2}{|z_2|^2}$.

(3) Use $\operatorname{Re}(z)\le|z|$. With $z_j=x_j+iy_j$,
$$\begin{aligned}
|z_1+z_2|^2&=(x_1+x_2)^2+(y_1+y_2)^2\\
&=x_1^2+y_1^2+x_2^2+y_2^2+2x_1x_2+2y_1y_2\\
&=|z_1|^2+|z_2|^2+2\operatorname{Re}\big((x_1+iy_1)(x_2-iy_2)\big)\\
&=|z_1|^2+|z_2|^2+2\operatorname{Re}(z_1\bar z_2)\\
&\le|z_1|^2+|z_2|^2+2|z_1|\,|\bar z_2|=(|z_1|+|z_2|)^2.
\end{aligned}$$

(4) $|z_1|=|(z_1-z_2)+z_2|\le|z_1-z_2|+|z_2|$. Rearrange, and interchange $z_1,z_2$.

## 1.3 Argand diagram

Represent $z=x+iy$ by the point $(x,y)$, or by its position vector from the origin.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.1,>=latex]
  \draw[->] (-0.35,0) -- (4.1,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-0.35) -- (0,2.7) node[above] {$\mathrm{Im}$};
  \draw[densely dotted] (0,1.8) node[left] {$y$} -- (3,1.8) -- (3,0) node[below] {$x$};
  \draw[->,red,thick] (0,0) -- (3,1.8) node[midway,above,sloped,text=black] {$r=|z|$};
  \node[above right] at (3,1.8) {$z=x+iy$};
\end{tikzpicture}
\end{document}
```

**1.3.1 Addition and subtraction.**
- $z_1+z_2$: the parallelogram rule (blue).
- $z_1-z_2$: the displacement from $z_2$ to $z_1$ (red; also drawn from the origin).
- $|z_1-z_2|$: the distance between the two points.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.1,>=latex]
  \draw[->] (-1.7,0) -- (4.2,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-0.35) -- (0,3.5) node[above] {$\mathrm{Im}$};
  \draw[->,thick] (0,0) -- (1.2,2.1) node[above left] {$z_1$};
  \draw[->,thick] (0,0) -- (2.25,0.8) node[below right] {$z_2$};
  \draw[->,blue,thick] (0,0) -- (3.45,2.9) node[above right] {$z_1+z_2$};
  \draw[->,blue,dashed] (1.2,2.1) -- (3.45,2.9);
  \draw[->,blue,dashed] (2.25,0.8) -- (3.45,2.9);
  \draw[->,red,thick] (2.25,0.8) -- (1.2,2.1);
  \draw[->,red,thick] (0,0) -- (-1.05,1.3) node[above left] {$z_1-z_2$};
\end{tikzpicture}
\end{document}
```

**1.3.2 Complex conjugation** reflects $x+iy$ in the real axis to $x-iy$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[scale=1.1,>=latex]
  \draw[->] (-0.35,0) -- (3.7,0) node[right] {$\mathrm{Re}$};
  \draw[->] (0,-1.8) -- (0,2) node[above] {$\mathrm{Im}$};
  \draw[densely dotted] (2.4,1.3) -- (2.4,-1.3);
  \draw[->,red,thick] (0,0) -- (2.4,1.3) node[above right] {$x+iy$};
  \draw[->,blue,thick] (0,0) -- (2.4,-1.3) node[below right] {$x-iy$};
\end{tikzpicture}
\end{document}
```

## 1.4 De Moivre's theorem

### Lemma — Multiplying in polar form

For $z_j=r_j(\cos\theta_j+i\sin\theta_j)$, $j=1,2$:
$$z_1z_2=r_1r_2\big(\cos(\theta_1+\theta_2)+i\sin(\theta_1+\theta_2)\big).$$

**Proof.** Expand the product,
$$z_1z_2=r_1r_2\big(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2+i(\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2)\big),$$
and use the angle addition formulae $\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2=\cos(\theta_1+\theta_2)$, $\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2=\sin(\theta_1+\theta_2)$.

**Remarks.** (1) Moduli multiply, arguments add: $\arg(z_1z_2)\equiv\arg(z_1)+\arg(z_2)\pmod{2\pi}$ for $z_1,z_2\ne0$. (2) Division: moduli divide, arguments subtract.

### Theorem — De Moivre's theorem

For $\theta\in\mathbb R$ and $n\in\mathbb Z$,
$$(\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta).$$

**Proof.** For $n\ge0$, induction: $n=0$ is immediate; $n\to n+1$ uses the previous lemma. For $n=-m<0$, use the positive power case and $|\cos\theta+i\sin\theta|=1$:
$$(\cos\theta+i\sin\theta)^{-m}=\frac1{\cos m\theta+i\sin m\theta}=\cos m\theta-i\sin m\theta=\cos(-m\theta)+i\sin(-m\theta).$$

**Consequence.** For $z=r(\cos\theta+i\sin\theta)\ne0$ and $n\in\mathbb Z$: $z^n=r^n(\cos n\theta+i\sin n\theta)$. E.g. $(1+i)^4=(\sqrt2)^4(\cos\pi+i\sin\pi)=-4$.

## 1.5 Exponential and trigonometric functions

### Definition — Complex exponential

For $z\in\mathbb C$,
$$\exp(z)=e^z=\sum_{n=0}^\infty\frac{z^n}{n!}=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots.$$
It converges absolutely for every $z\in\mathbb C$: for $z\ne0$ the ratio of successive absolute values is $\dfrac{|z|^{n+1}}{(n+1)!}\cdot\dfrac{n!}{|z|^n}=\dfrac{|z|}{n+1}\to0$.

### Proposition — Properties of the exponential

For $z,w\in\mathbb C$, $n\in\mathbb Z$:

1. $e^ze^w=e^{z+w}$ (product rule);
2. $e^0=1$;
3. $e^{-z}=1/e^z$;
4. $(e^z)^n=e^{nz}$.

In particular $e^z\ne0$ for all $z\in\mathbb C$.

**Proof.** (2) Set $z=0$ in the series.

(1) Multiply the series:
$$\Big(\sum_{j=0}^\infty\frac{z^j}{j!}\Big)\Big(\sum_{k=0}^\infty\frac{w^k}{k!}\Big)=\sum_{j=0}^\infty\sum_{k=0}^j\frac{z^kw^{j-k}}{k!(j-k)!}=\sum_{j=0}^\infty\frac1{j!}\sum_{k=0}^j\binom jk z^kw^{j-k}=\sum_{j=0}^\infty\frac{(z+w)^j}{j!}=e^{z+w}.$$

> [!note] Explanation
> The first step collects together all terms with total degree $j$; regrouping like this is allowed because both series converge absolutely. The inner sum is then the binomial expansion of $(z+w)^j$.

(3) By the product rule, $e^ze^{-z}=e^0=1$, so $e^{-z}=1/e^z$.

(4) Induction for $n\ge0$: trivial at $n=0$; if $(e^z)^n=e^{nz}$ then $(e^z)^{n+1}=(e^z)^ne^z=e^{nz}e^z=e^{(n+1)z}$. For $n=-m<0$: $(e^z)^{-m}=\dfrac1{(e^z)^m}=\dfrac1{e^{mz}}=e^{-mz}=e^{nz}$.

### Definition — Complex sine and cosine

For $z\in\mathbb C$,
$$\cos z=\frac{e^{iz}+e^{-iz}}2=\sum_{n=0}^\infty(-1)^n\frac{z^{2n}}{(2n)!},\qquad\sin z=\frac{e^{iz}-e^{-iz}}{2i}=\sum_{n=0}^\infty(-1)^n\frac{z^{2n+1}}{(2n+1)!}.$$
For real inputs these are the usual trigonometric functions. Adding the definitions gives **Euler's formula**
$$e^{iz}=\cos z+i\sin z,\qquad z\in\mathbb C.$$

**Real angles.** For $\theta\in\mathbb R$: $\operatorname{Re}(e^{i\theta})=\cos\theta$, $\operatorname{Im}(e^{i\theta})=\sin\theta$, $|e^{i\theta}|=1$. More generally for $x,y\in\mathbb R$:
$$e^{x+iy}=e^x(\cos y+i\sin y),\qquad|e^{x+iy}|=e^x.$$

### Lemma — When the exponential equals 1

For $z\in\mathbb C$: $e^z=1\iff z=2\pi in$ for some $n\in\mathbb Z$.

**Proof.** Write $z=x+iy$. Since $e^z=e^x(\cos y+i\sin y)=1$: taking moduli, $e^x=1$, so $x=0$; then $\cos y=1$ and $\sin y=0$, which happens exactly when $y=2\pi n$, $n\in\mathbb Z$. The converse is immediate.

**Periodicity.** $e^z=e^w\iff z-w=2\pi ni$ for some $n\in\mathbb Z$ (divide by $e^w\ne0$). So the exponential is periodic with period $2\pi i$ and is not one-to-one.

**Exponential polar form.** $z=re^{i\theta}$ with $r=|z|>0$, $\theta\in\operatorname{Arg}(z)$. Then
$$z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)},\qquad z^n=r^ne^{in\theta}.$$

### Roots of unity

Fix an integer $N\ge1$ and solve $z^N=1$. With $z=re^{i\theta}$:
$$r^Ne^{iN\theta}=1\iff r^N=1\ (\text{so }r=1)\ \text{ and }\ N\theta=2\pi n\text{ for some }n\in\mathbb Z.$$
There are $N$ distinct **$N$th roots of unity**:
$$z_k=e^{2\pi ik/N}=\omega^k,\qquad k=0,\dots,N-1,\qquad\omega=e^{2\pi i/N}.$$
They lie on the unit circle, equally spaced by angle $2\pi/N$; for $N\ge3$ they are the vertices of a regular $N$-gon.

**Roots of a non-zero complex number.** For $a=Re^{i\theta}$, $R>0$:
$$z^N=a\iff z=R^{1/N}e^{i(\theta+2\pi n)/N},\qquad n=0,\dots,N-1,$$
where $R^{1/N}$ is the positive real root. The roots are equally spaced on the circle of radius $R^{1/N}$. If $a=0$, the only root is $z=0$, with multiplicity $N$.

## 1.6 Logarithms and complex powers

### Definition — Logarithm

For $z\in\mathbb C$, $z\ne0$, a **logarithm** of $z$ is $w\in\mathbb C$ with $e^w=z$.

The exponential is many-to-one, so a non-zero $z$ has many logarithms: by the previous lemma $e^{w+2\pi ni}=e^w$ for all $n\in\mathbb Z$. With $z=re^{i\theta}$, $z=e^{\log r}e^{i\theta}=e^{\log r+i\theta}$, so the logarithms of $z$ are
$$w=\log r+i\theta,\qquad\theta\in\operatorname{Arg}(z),$$
and $\theta\mapsto\theta+2\pi n$ gives $w\mapsto w+2\pi ni$. To make them unique take $\theta\in(-\pi,\pi]$ and define
$$\log z=\log|z|+i\arg(z)\quad\text{(principal logarithm)},\qquad\operatorname{Log}z=\{\log z+2\pi ni:\ n\in\mathbb Z\}\quad\text{(all logarithms)}.$$

### Definition — Complex powers

For $z\ne0$ and $\alpha\in\mathbb C$, choose $L\in\operatorname{Log}z$ and define $z^\alpha=e^{\alpha L}$. Changing the logarithm, $L\mapsto L+2\pi ni$ gives $z^\alpha\mapsto z^\alpha e^{2\pi in\alpha}$. The **principal value** of $z^\alpha$ is $e^{\alpha\log z}$.

1. If $\alpha=p\in\mathbb Z$, then $e^{2\pi inp}=1$: $z^p$ has a unique value, agreeing with the integer power.
2. If $\alpha=p/q\in\mathbb Q$ (lowest terms, $q>0$), $e^{2\pi inp/q}$ has exactly $q$ distinct values, so $z^{p/q}$ has exactly $q$ values.
3. Otherwise there are infinitely many values.

**Power laws** (for compatible choices of values): $z^\alpha z^\beta=z^{\alpha+\beta}$ and $(z^\alpha)^\beta=z^{\alpha\beta}$.
1. Fix $L\in\operatorname{Log}z$: $z^\alpha z^\beta=e^{\alpha L}e^{\beta L}=e^{(\alpha+\beta)L}$.
2. Choose the value $u=e^{\alpha L}$ of $z^\alpha$, and the logarithm $\mu=\alpha L$ of $u$: $(z^\alpha)^\beta=u^\beta=e^{\beta\mu}=e^{\alpha\beta L}=z^{\alpha\beta}$.

**Examples.**

1. *Logarithms of $i$ and the power $i^i$.* $i=e^{i\pi/2}$, $|i|=1$, $\operatorname{Arg}(i)=\{\frac\pi2+2\pi n\}$, $\log i=i\frac\pi2$, $\operatorname{Log}i=\{i(\frac\pi2+2\pi n):n\in\mathbb Z\}$. The values of $i^i$ are
   $$e^{i(\log i+2\pi ni)}=e^{-(\pi/2+2\pi n)},\qquad n\in\mathbb Z:$$
   infinitely many values, all positive reals; $n=0$ gives the principal value $e^{-\pi/2}$.
2. *Logarithms and square roots of $1+i$.* $1+i=\sqrt2e^{i\pi/4}$, so $\log(1+i)=\frac12\log2+i\frac\pi4$ and $\operatorname{Log}(1+i)=\{\frac12\log2+i(\frac\pi4+2\pi n)\}$. The square roots are
   $$(1+i)^{1/2}=e^{\frac12(\log(1+i)+2\pi ni)}=e^{\frac14\log2+i(\frac\pi8+\pi n)}=2^{1/4}e^{i(\pi/8+\pi n)}=\begin{cases}2^{1/4}e^{i\pi/8},&n\text{ even},\\-2^{1/4}e^{i\pi/8},&n\text{ odd}.\end{cases}$$
   Exactly two roots, of modulus $2^{1/4}$ and opposite directions; the principal square root is $2^{1/4}e^{i\pi/8}$.

## 1.7 Lines and circles

### Lines

A line through $z_0\in\mathbb C$ in a non-zero direction $w\in\mathbb C$ is $z=z_0+\lambda w$, $\lambda\in\mathbb R$. To eliminate the parameter: $\bar z=\bar z_0+\lambda\bar w$ (as $\lambda$ is real), so
$$\frac{z-z_0}w=\frac{\bar z-\bar z_0}{\bar w},\qquad\text{i.e.}\qquad\bar wz-\bar wz_0=w\bar z-w\bar z_0.$$

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
  \draw[<->,blue,thick] (-0.7,2.7)--(2.7,-0.7) node[below right] {$x+y=2$};
  \draw[densely dashed] (0,1)--(1,1)--(1,0);
  \fill (1,1) circle (1.4pt) node[above right] {$z_0=1+i$};
  \draw[->,red,thick] (1,1)--(2,0) node[midway,above right] {$w=1-i$};
\end{tikzpicture}
\end{document}
```
*Example: $z_0=1+i$, $w=1-i$ gives the line $x+y=2$.*

### Circles

For centre $c\in\mathbb C$ and radius $\rho>0$:

1. $z=c+\rho e^{i\theta}$, $\theta\in\mathbb R$ (parametric form);
2. $|z-c|=\rho$ (distance from centre);
3. $|z|^2-c\bar z-\bar cz=\rho^2-|c|^2$ (expanded equation), from $|z-c|^2=\rho^2\Rightarrow(z-c)(\bar z-\bar c)=\rho^2$.

### Geometric transformations

| Transformation | Map |
| --- | --- |
| Translation | $z\mapsto z+z_0$ |
| Scaling | $z\mapsto\lambda z$, $\lambda>0$ |
| Rotation | $z\mapsto ze^{i\theta}$, $\theta\in\mathbb R$ |
| Reflection | $z\mapsto\bar z$ |
| Complex inversion | $z\mapsto1/z$, $z\ne0$ |

**Examples** with $z=1+i$ (blue $=z$, red $=$ image): translation $z\mapsto z+2-i$ gives $3$; scaling $z\mapsto2z$ gives $2+2i$; rotation $z\mapsto iz$ gives $-1+i$; reflection gives $1-i$; negative scaling $z\mapsto-z$ gives $-1-i$; reciprocal $z\mapsto1/z$ gives $\frac{1-i}2$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex,scale=0.8,every node/.style={font=\small}]
  \foreach \x/\y/\t in {0/0/{Translation $z\mapsto z+2-i$},5.5/0/{Scaling $z\mapsto2z$},11/0/{Rotation $z\mapsto iz$},0/-5.5/{Reflection $z\mapsto\overline z$},5.5/-5.5/{Negative scaling $z\mapsto-z$},11/-5.5/{Reciprocal $z\mapsto1/z$}} {
    \begin{scope}[shift={(\x,\y)}]
      \draw[->] (-1.6,0)--(3.4,0) node[right] {$\mathrm{Re}$};
      \draw[->] (0,-1.6)--(0,2.6) node[left] {$\mathrm{Im}$};
      \draw[->,blue,thick] (0,0)--(1,1) node[above] {$1+i$};
      \node[anchor=south] at (0.9,3.05) {\t};
    \end{scope}
  }
  \fill[red!10] (0,0)--(1,1)--(3,0)--cycle;
  \draw[->,blue,thick] (0,0)--(1,1);
  \draw[->] (1,1)--(3,0) node[midway,above right] {$2-i$};
  \draw[->,red,thick] (0,0)--(3,0) node[below] {$3$};
  \draw[->,red,thick] (5.5,0)--(7.5,2) node[right] {$2+2i$};
  \draw[->,red,thick] (11,0)--(10,1) node[above left] {$-1+i$};
  \draw[densely dashed] (12,1) arc[start angle=45,end angle=135,radius=1.4142];
  \draw[densely dashed] (1,-4.5)--(1,-6.5);
  \draw[->,red,thick] (0,-5.5)--(1,-6.5) node[below right] {$1-i$};
  \draw[->,red,thick] (5.5,-5.5)--(4.5,-6.5) node[below left] {$-1-i$};
  \draw[->,red,thick] (11,-5.5)--(11.5,-6) node[below right] {$\frac{1-i}{2}$};
\end{tikzpicture}
\end{document}
```
