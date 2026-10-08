---
title: Vectors and Matrices - Chapter 1 Complex Numbers
material_type: handwritten lecture notes
course: Part IA Vectors and Matrices
date: null
source_file: Ch.1 Complex Numbers.pdf
drive_file_id: 1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh
source_url: https://drive.google.com/file/d/1E1KSgIxdchM_LG5KujUe6JeqPhS3FChh/view
source_pages: 9
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

### 1.2.4 Further properties (pages 5–6)

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

**Proof of the triangle inequality.** Use $\operatorname{Re}(z)\le |z|$. Then
$$
\begin{aligned}
|z_1+z_2|^2
&=|z_1|^2+|z_2|^2+2\operatorname{Re}(z_1\overline{z_2})\\
&\le |z_1|^2+|z_2|^2+2|z_1|\,|\overline{z_2}|\\
&=|z_1|^2+|z_2|^2+2|z_1|\,|z_2|\\
&=(|z_1|+|z_2|)^2.
\end{aligned}
$$
Take non-negative square roots. For the reverse inequality,
$$|z_1|=|(z_1-z_2)+z_2|\le |z_1-z_2|+|z_2|.$$
Rearrange and interchange $z_1,z_2$ to obtain both bounds and hence the reverse triangle inequality. $\square$

## 1.3 Argand diagram (page 7)

Represent $z=x+iy$ by the point $(x,y)$, or by its position vector from the origin. Horizontal axis: $\operatorname{Re}$; vertical axis: $\operatorname{Im}$.

The source diagrams are reconstructed below as LaTeX schematics. Spacing is not a numerical scale; coloured arrows retain the mathematical relationships in the drawings.

$$
\begin{array}{rccccc}
 &\operatorname{Im}&&&&\\
 &\uparrow&&&&\\
y&\cdot&\cdots&\cdots&\color{red}{\bullet\ z=x+iy}&\\
 &\vdots&&\color{red}{\nearrow\ r=|z|}&\vdots&\\
 &0&\longrightarrow&\longrightarrow&x&\longrightarrow\ \operatorname{Re}
\end{array}
$$

### 1.3.1 Addition and subtraction (page 7, lower part)

- $z_1+z_2$: the parallelogram rule.
- $z_1-z_2$: the displacement from $z_2$ to $z_1$.
- $|z_1-z_2|$: the distance between the two points.

Addition: the top and right sides correspond to the dashed translated vectors in the source. The blue diagonal is the position vector of the sum.

$$
\begin{array}{ccccc}
z_1&&\overset{z_2\ \text{(translated)}}{\color{blue}{\dashrightarrow}}&&\color{blue}{z_1+z_2}\\
\uparrow\scriptstyle z_1&&\color{blue}{\nearrow\ (z_1+z_2)}&&\color{blue}{\uparrow}\scriptstyle z_1\ \text{(translated)}\\
0&&\xrightarrow{\quad z_2\quad}&&z_2
\end{array}
$$

Subtraction: both red arrows below have displacement $z_1-z_2$. The left arrow starts at the origin; the right starts at $z_2$ and ends at $z_1$.

$$
\begin{array}{ccccc}
\color{red}{z_1-z_2}&&z_1&&\\
&\color{red}{\nwarrow}&&\color{red}{\nwarrow}&\\
&&0&\xrightarrow{\quad z_2\quad}&z_2
\end{array}
\qquad
\text{each red arrow has length }|z_1-z_2|.
$$

### 1.3.2 Complex conjugation (page 8, top)

Conjugation reflects $x+iy$ across the real axis to $x-iy$. The dotted projection is shared by the two points.

$$
\begin{array}{ccccc}
\operatorname{Im}&&&\color{red}{\bullet\ (x+iy)}&\\
\uparrow&&\color{red}{\nearrow}&\vdots&\\
0&\longrightarrow&\longrightarrow&x&\longrightarrow\ \operatorname{Re}\\
&&\color{blue}{\searrow}&\vdots&\\
&&&\color{blue}{\bullet\ (x-iy)}&
\end{array}
$$

## 1.4 De Moivre's theorem (pages 8–9)

**Lemma** (page 8). For
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

**[[De Moivre's Theorem]]** (page 9). For $\theta\in\mathbb R$ and $n\in\mathbb Z$,
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
This proves the integer-power statement. $\square$

**Consequence.** For $z=r(\cos\theta+i\sin\theta)\ne0$ and $n\in\mathbb Z$,
$$z^n=r^n\bigl(\cos(n\theta)+i\sin(n\theta)\bigr).$$
For example,
$$ (1+i)^4=(\sqrt2)^4(\cos\pi+i\sin\pi)=-4.$$
