---
title: Differential Equations - Examples Sheet 1 Handwritten Proofs
material_type: handwritten worked solutions and incomplete attempts
course: Part IA Differential Equations
date: null
source_file: Examples Sheet 1.pdf
drive_file_id: 13RHsCyXVE8qyIQtepFN5CYrkA5ObHNSo
source_url: https://drive.google.com/file/d/13RHsCyXVE8qyIQtepFN5CYrkA5ObHNSo/view
source_pages: 9
---

# Differential Equations — Examples Sheet 1: Handwritten Proofs

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/13RHsCyXVE8qyIQtepFN5CYrkA5ObHNSo/view).

The supplied questions are now available in [[Differential Equations - Examples Sheet 1 2026]], separately read from two matching question PDFs. This nine-page document contains handwritten answers and attempts; its date is not supplied. The earlier explanations below are retained.

## 1. Differentiating $x^n$ (page 1, upper half)

The supplied calculation uses the finite binomial expansion. For a positive integer $n$,
$$
\begin{aligned}
\frac{d}{dx}(x^n)
&=\lim_{h\to0}\frac{(x+h)^n-x^n}{h}\\
&=\lim_{h\to0}
\frac{\displaystyle\sum_{k=0}^n\binom nkx^{n-k}h^k-x^n}{h}\\
&=\lim_{h\to0}\left(
nx^{n-1}+\sum_{k=2}^n\binom nkx^{n-k}h^{k-1}
\right)\\
&=nx^{n-1}.
\end{aligned}
$$
The sum from $k=2$ to $n$ is empty when $n=1$.

> [!todo] Unaddressed case — page 1, question 1
> The supplied question asks for non-negative integer $n$. The displayed argument covers positive $n$; the constant case $n=0$ is not separately treated in the handwritten answer.

**Explanation.** The $k=0$ term cancels $x^n$, and the $k=1$ term becomes $nx^{n-1}$ after division by $h\ne0$. Every remaining term has a positive power of $h$, so tends to zero. There are only finitely many terms, which permits taking their limits term by term. This calculation does not prove the rule for an arbitrary real exponent.

## 2. Product rule (page 1, lower half)

Assume $u$ and $v$ are differentiable at the real point $x$, and defined in a neighbourhood of $x$. The supplied argument starts with
$$
u(x)v'(x)+v(x)u'(x)
=
\lim_{h\to0}\left(
u(x)\frac{v(x+h)-v(x)}h
+
v(x)\frac{u(x+h)-u(x)}h
\right).
$$
Add and subtract $u(x+h)v(x+h)$ in the numerator. The resulting identity is
$$
\begin{aligned}
&u(x)\bigl(v(x+h)-v(x)\bigr)
+v(x)\bigl(u(x+h)-u(x)\bigr)\\
&\qquad=
u(x+h)v(x+h)-u(x)v(x)\\
&\qquad\quad-
\bigl(v(x+h)-v(x)\bigr)\bigl(u(x+h)-u(x)\bigr).
\end{aligned}
$$
After dividing by $h$ and taking limits, the source writes the last correction as $vu'-vu'$, giving
$$u(x)v'(x)+v(x)u'(x)=(uv)'(x).$$

### Justifying the correction and existence of the derivative

This explains the limiting step implicit in the source. Set
$$D_u(h)=\frac{u(x+h)-u(x)}h,\qquad
D_v(h)=\frac{v(x+h)-v(x)}h\qquad(h\ne0).$$
Both have finite limits. Hence
$$
\frac{u(x+h)v(x+h)-u(x)v(x)}h
=
u(x)D_v(h)+v(x)D_u(h)
+\bigl(v(x+h)-v(x)\bigr)D_u(h).
$$
Differentiability implies continuity: $v(x+h)-v(x)=hD_v(h)\to0$ because $D_v(h)$ has a finite limit and is therefore bounded for sufficiently small non-zero $h$. Meanwhile $D_u(h)\to u'(x)$. The last product tends to zero. Thus the product's difference quotient has a limit, proving both existence of $(uv)'(x)$ and
$$(uv)'(x)=u(x)v'(x)+v(x)u'(x).$$

In the notation of [[Limits, Big O and Little o - A First-Year Guide]],
$$u(x+h)-u(x)=O(h),\qquad v(x+h)-v(x)=O(h),$$
so their product is $O(h^2)$ and division by $h$ leaves $O(h)\to0$.

See [[Differential Equations - Chapter 1 Introduction and Basic Calculus]] for the derivative and limit definitions.

## 3. Repeated derivatives (page 2, upper half)

### (i)(a) Using Leibniz's rule

The source calculates
$$\begin{aligned}
\frac{d^n}{dx^n}(xe^x)
&=\sum_{m=0}^{n}\binom nm x^{(m)}(e^x)^{(n-m)}\\
&=xe^x+ne^x.
\end{aligned}$$
Only $m=0,1$ contribute, since the higher derivatives of $x$ vanish. Here $x^{(m)}$ means the $m$th derivative of the function $x$.

### (i)(b) Using the product rule

For $n\ge1$,
$$\begin{aligned}
\frac{d^n}{dx^n}(xe^x)
&=\frac{d^{n-1}}{dx^{n-1}}(xe^x+e^x)\\
&=e^x+\frac{d^{n-1}}{dx^{n-1}}(xe^x)\\
&=ne^x+xe^x.
\end{aligned}$$
The last line iterates the same product-rule recurrence. See [[Differentiation Rules]].

**(ii) Unanswered:** no calculation of $d^3(\ln x)^2/dx^3$ appears in the source.

## 4. Taylor series and the exponential limit (pages 2–3)

### (i) $e^{ax}$ about $x=1$ (page 2)

For $f(x)=e^{ax}$, the written series is
$$T_f(x)=\sum_{n=0}^{\infty}\frac{(x-1)^n}{n!}f^{(n)}(1)
=\sum_{n=0}^{\infty}\frac{(x-1)^n}{n!}a^ne^a.$$

### (ii) $\ln(1+x)$ about $0$ (pages 2–3)

The source gives
$$\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots
=\sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^n}{n}.$$
The series is used near $x=0$; it is valid for $|x|<1$. The source supplies no convergence proof.

For fixed real $x$, the subsequent attempt substitutes $x/k$ into that series:
$$\begin{aligned}
\lim_{k\to\infty}k\ln\left(1+\frac{x}{k}\right)
&=\lim_{k\to\infty}k\sum_{n=1}^{\infty}
(-1)^{n+1}\frac{x^n}{nk^n}\\
&=\lim_{k\to\infty}\left(x+\sum_{n=2}^{\infty}
(-1)^{n+1}\frac{x^n}{nk^{n-1}}\right)\\
&=x\qquad\text{(claimed)}.
\end{aligned}$$

> [!todo] Incomplete proof — page 3, infinite remainder
> The attempt does not justify that the infinite remainder tends to zero. Limits of individual terms do not alone justify taking a limit through an infinite sum. A remainder estimate or an appropriate convergence argument is missing; no replacement proof is supplied here.

The source then uses $k\ln(1+x/k)=\ln((1+x/k)^k)$ and continuity of the exponential to deduce
$$\lim_{k\to\infty}\left(1+\frac{x}{k}\right)^k=e^x,$$
conditional on the preceding logarithmic limit. For fixed $x$, the logarithm's argument is positive for all sufficiently large $k$.

## 5. Taylor expansions about $0$ (pages 4–5)

### (i) $(x^2+a)^{-3/2}$ (page 4)

For the real expansion, take $a>0$. Set $f(u)=(u+a)^{-3/2}$. Then
$$f'(u)=-\frac32(u+a)^{-5/2},\qquad
f''(u)=\frac{15}{4}(u+a)^{-7/2}.$$
Substituting $u=x^2$ into its Taylor expansion about $u=0$ gives
$$(x^2+a)^{-3/2}
=a^{-3/2}-\frac32a^{-5/2}x^2+\frac{15}{8}a^{-7/2}x^4+O(x^6).$$

### (ii) $\ln(\cos x)$ (page 4)

The written identity is
$$\ln(\cos x)=\frac12\ln(1-\sin^2x)
\qquad\left(0\le x<\frac\pi2\right).$$
Expand $\frac12\ln(1-u)$ at $u=0$ and substitute $u=\sin^2x$:
$$\ln(\cos x)=-\frac12\left(\sin^2x+\frac{\sin^4x}{2}+\frac{\sin^6x}{3}+\cdots\right).$$
Using $\sin x=x-x^3/3!+x^5/5!-\cdots$, the source expands
$$\begin{aligned}
\ln(\cos x)
&=-\frac12\left[
\left(x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots\right)^2
+\frac12\left(x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots\right)^4
+\frac13(x+\cdots)^6+\cdots\right]\\
&=-\frac12\left[
x^2-\frac{x^4}{3}+\frac{2x^6}{45}
+\frac12\left(x^4-\frac{2x^6}{3}\right)
+\frac{x^6}{3}+O(x^8)\right]\\
&=-\frac{x^2}{2}-\frac{x^4}{12}-\frac{x^6}{45}+O(x^8).
\end{aligned}$$

### (iii) $\exp[-(x-a)^{-2}]$ (page 5)

This calculation requires $a\ne0$. Expand $e^u$ about $u=-a^{-2}$:
$$e^u=e^{-a^{-2}}\left[1+(u+a^{-2})+\frac{(u+a^{-2})^2}{2!}
+\frac{(u+a^{-2})^3}{3!}+\cdots\right].$$
Put $u=-(x-a)^{-2}$ and use
$$(x-a)^{-2}=a^{-2}\left(1-\frac xa\right)^{-2}
=a^{-2}\left(1+\frac{2x}{a}+\frac{3x^2}{a^2}+\cdots\right).$$
The resulting source calculation is
$$\begin{aligned}
e^{-(x-a)^{-2}}
&=e^{-a^{-2}}\left[1-\frac1{a^2}\left(\frac{2x}{a}+\frac{3x^2}{a^2}+\cdots\right)
+\frac1{2a^4}\left(\frac{2x}{a}+\frac{3x^2}{a^2}+\cdots\right)^2+\cdots\right]\\
&=e^{-a^{-2}}\left(1-\frac{2x}{a^3}-\frac{3x^2}{a^4}+\frac{2x^2}{a^6}\right)+O(x^3).
\end{aligned}$$
These expansions are as $x\to0$ with the permitted $a$ fixed. See [[Taylor Series and Taylor's Theorem]].

## 6. Factorial bounds (page 6)

The sketch compares $y=\ln x$ with its rightward translate $y=\ln(x-1)$. The dashed step heights represent the logarithms in the factorial sum. It is schematic; the positions marked $N,N+1$ do not specify a numerical $N$.

```tikz
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[>=latex]
  \draw[->] (-0.3,0)--(6,0);
  \draw[->] (0,-1.6)--(0,2.2);
  \draw[thick,domain=0.3:5.2,samples=80] plot (\x,{ln(\x)});
  \draw[thick,domain=1.3:5.2,samples=80] plot (\x,{ln(\x-1)});
  \draw[dashed] (1,-1.5)--(1,2);
  \foreach \x/\lab in {1/1,2/2,4/N,5/{N+1}} {
    \draw (\x,0.04)--(\x,-0.04) node[below] {$\lab$};
  }
  \foreach \x in {2,3,4} {
    \draw[dashed] (\x,0)--(\x,{ln(\x)});
    \draw[dashed] (\x,{ln(\x)})--(\x+1,{ln(\x)});
  }
  \draw[dashed] (5,0)--(5,{ln(5)});
\end{tikzpicture}
\end{document}
```

For $N\ge2$, the lower comparison is
$$\begin{aligned}
\ln(N!)=\sum_{n=1}^{N}\ln n
&>\int_2^{N+1}\ln(x-1)\,dx\\
&=\left[(x-1)(\ln(x-1)-1)\right]_2^{N+1}\\
&=N\ln N-N+1>N\ln N-N.
\end{aligned}$$
The upper comparison is
$$\begin{aligned}
\sum_{n=1}^{N}\ln n
&<\int_1^{N+1}\ln x\,dx\\
&=\left[x(\ln x-1)\right]_1^{N+1}\\
&=(N+1)\ln(N+1)-(N+1)+1\\
&=(N+1)\ln(N+1)-N.
\end{aligned}$$
Hence the stated bounds are
$$N\ln N-N<\ln(N!)<(N+1)\ln(N+1)-N.$$
Subtracting $\ln(N+1)$ from the upper bound gives
$$\ln(N!)-\ln(N+1)<N\ln(N+1)-N,$$
and exponentiating gives
$$\frac{N!}{N+1}<\left(\frac{N+1}{e}\right)^N.$$

> [!todo] Boundary case — page 6, lower integral comparison
> The strict comparison with $\int_2^{N+1}\ln(x-1)\,dx$ requires $N\ge2$: for $N=1$ both sides are zero. The handwritten calculation does not separately address this boundary case for the final bounds.

## 7. Integral solution (page 7)

Write $f(t)=e^{-t^2}$ and take an antiderivative $F$ with $F'=f$. For the integral in the supplied question, the source uses
$$y(x)=\lim_{a\to\infty}(F(a)-F(x)).$$
The derivative calculations are
$$y'(x)=-f(x)=-e^{-x^2},\qquad y''(x)=2xe^{-x^2}.$$
Consequently,
$$y''+2xy'=2xe^{-x^2}+2x(-e^{-x^2})=0.$$

## ★8–★9. Unfinished (pages 8–9)

Page 8 contains only the heading “8*”, and page 9 only “9*”; neither has a written answer. No answers to questions 10–14 are present in this document.
