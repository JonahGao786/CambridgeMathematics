---
title: Numbers and Sets - Introductory Sheet 2026
material_type: problem sheet
course: Part IA Numbers and Sets
date: Michaelmas 2026
author: G. Taylor
source_file: ns_intro_2026.pdf
drive_file_id: 1mo2Nr9PicjKtfXPtp14krUd1wY0oi0Fr
source_url: https://drive.google.com/file/d/1mo2Nr9PicjKtfXPtp14krUd1wY0oi0Fr/view
source_pages: 2
---

# Numbers & Sets — Introductory Sheet

Related handwritten work: [[Numbers and Sets 0 - Handwritten Attempts]]. This sheet supplies questions, not worked answers.

Original PDF: [View source in Google Drive](https://drive.google.com/file/d/1mo2Nr9PicjKtfXPtp14krUd1wY0oi0Fr/view).

## Instructions (page 1)

Please attempt questions $1$–$9$.

Some questions may be unfamiliar in style and on some you might get stuck. This is okay! If you can't do a question, don't panic — write down your ideas, then we can discuss them and work towards a solution in the supervision. However, please don't look up any solutions. I can help you if I get to see your attempts, but it's fairly useless if I just get to see someone else's answer!

You are welcome to mail me for help (glt1000@cam.ac.uk), but you should tell me what you've tried.

## Questions 1–5 (page 1)

### 1

By considering $(r+1)^3-r^3$, derive the formula
$$\sum_{r=1}^n r^2=\frac16n(n+1)(2n+1).$$

### 2

Use induction to prove that, for every positive integer $n$,

- (i) $1^2+3^2+\cdots+(2n-1)^2=\frac13(4n^3-n)$.
- (ii) $n^3+5n$ is divisible by $6$.
- (iii) $2^{n+2}+3^{2n+1}$ is divisible by $7$.

### 3

Give alternative solutions to question $2$, as follows:

- (i) For $2$(i), by using the formula in question $1$.
- (ii) For $2$(ii), by factorising a suitable expression.
- (iii) For $2$(iii), by using modular arithmetic (or, if you haven't met modular arithmetic, using the result that $a-b$ divides $a^k-b^k$ for $a,b\in\mathbb Z$ and $k\in\mathbb N$).

### 4

**Theorem (deliberately flawed claim in the exercise).** All horses are the same colour.

**Supplied proof.** We will use induction to show that, for each $n$, any $n$ horses are the same colour. The base case, $n=1$, is easy: any one horse is the same colour as itself. Now suppose the result is true for any set of $n$ horses, and that we have $n+1$ horses. Call them $h_1,\ldots,h_{n+1}$.

By induction, we know horses $h_1,\ldots,h_n$ are the same colour (because there are $n$ of them), and that horses $h_2,\ldots,h_{n+1}$ are the same colour (because there are $n$ of them). So we deduce that horses $h_1,\ldots,h_{n+1}$ are the same colour. Hence, by induction, all horses are the same colour.

However, not all horses are the same colour. So where is the mistake?

### 5

The [[Fibonacci Numbers]] are defined by $F_1=F_2=1$, and $F_n=F_{n-1}+F_{n-2}$ for $n\ge3$.

(a) Let $n$ be a positive integer. By observing that
$$F_{n+2}=F_{n+1}+F_n,\qquad F_{n+3}=2F_{n+1}+F_n,\qquad F_{n+4}=3F_{n+1}+2F_n,\quad\ldots,$$
guess a formula for $F_{n+k}$ in terms of $F_{n+1}$ and $F_n$, and verify it by induction on $k$.

Deduce that $F_{n+1}^2+F_n^2$ and $F_{n+2}^2-F_n^2$ are Fibonacci numbers.

Deduce also that $F_{kn}$ is a multiple of $F_n$ for all $k\in\mathbb N$, and hence show that if $F_n$ is prime then either $n$ is prime or $n=4$.

(b) For each $n$, let $f_n$ be the last digit of $F_n$. For example, $F_7=13$, so $f_7=3$. Prove that the sequence $f_n$ is periodic. (That is, prove that there is some positive integer $k$ such that $f_{n+k}=f_n$ for all $n$.)

## Questions 6–9 (page 2)

### 6

(a) Find all positive integers $n$ such that $n!$ is the difference of two squares.

(b) Find all positive integers $n$ such that $n$ divides $(n-1)!$.

(c) Find the smallest positive integer $n$ such that $n!$ ends in (at least) $2026$ zeroes.

### 7

(a) Prove that $\sqrt[3]{4}$ and $\log_3 4$ are irrational.

(b) Show that if there are $m,n\in\mathbb N$ such that $\frac mn=\sqrt{11}$, then also
$$\frac{11n-3m}{m-3n}=\sqrt{11}.$$
By considering the size of $m-3n$, deduce that $\sqrt{11}$ is irrational.

How would you alter this for $\sqrt{111}$? At what step does the method fail for $\sqrt{121}$?

(c) Let $r,\alpha,\beta\in\mathbb R$, with $r$ rational and $\alpha,\beta$ irrational. Which, if any, of $r+\alpha$, $r\alpha$, $\alpha+\beta$, $\alpha\beta$, $r^\alpha$, $\alpha^r$ and $\alpha^\beta$ must be irrational? Give proofs or counterexamples.

(If you give a counterexample, try to use $\alpha,\beta$ that you can prove are irrational.)

### 8

Let $S$ be a set of $n+1$ distinct integers chosen from $\{1,\ldots,2n\}$. Prove that $S$ contains:

- (i) Two numbers which are coprime.
- (ii) Two numbers whose sum is $2n+1$.
- (iii) Two numbers such that one divides the other.
- (iv) Two numbers whose difference is also in $S$.

Give examples (with $n>1$) to show that each result can fail if $S$ contains only $n$ integers. Is there such an example where all four results fail simultaneously?

### 9

There are six towns, such that between each pair of towns there is either a train or bus service (but not both). Prove that there are three towns that can be visited in a loop, going via no other towns, using only one mode of transport.

Is the result still true if there are only five towns?

## Additional questions (page 2)

These are optional. Attempt them if they interest you, but not at the expense of other work.

### 10

You are asked to drive a lunar rover around the moon (which is just a circle in this question). There are some fuel depots on the way, with the total amount of fuel stored in them enough to get around the moon exactly once. Prove that there exists a depot from which you can start driving and travel the whole way around the moon, picking up fuel at each depot as you pass, without running out of fuel between depots.

### 11

Some red balls and blue balls are distributed among $99$ boxes. Your task is to choose $50$ of the boxes in such a way that you have claimed at least half of the balls of each colour. Can you always do this, no matter how many balls there are or how they are distributed?

### 12

Let $n$ be a natural number that isn't a multiple of $10$. Prove that some multiple of $n$ is a palindrome when written in base $10$. (For example, $43$ divides $15351$.)
