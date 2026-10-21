---
title: Modular Arithmetic
material_type: source-backed definitions, well-definedness calculations and worked example
course: Part IA Numbers and Sets
source_file: Ch.1 Elementary Number Theory.pdf
drive_file_id: 1UTg7i2PPaEujlaMuByJELly5mOqiUrxW
source_url: https://drive.google.com/file/d/1UTg7i2PPaEujlaMuByJELly5mOqiUrxW/view
source_pages: [18, 19]
---

# Modular Arithmetic

For a natural number $n\ge2$,
$$x\equiv y\pmod n
\quad\Longleftrightarrow\quad n\mid(x-y)
\quad\Longleftrightarrow\quad x=y+kn\text{ for some }k\in\mathbb Z.$$
For example, $2\equiv16\pmod7$.

The integers modulo $n$, written $\mathbb Z_n$ or $\mathbb Z/n\mathbb Z$, regard integers differing by a multiple of $n$ as the same element.

## Addition and multiplication

If $a\equiv a'\pmod n$ and $b\equiv b'\pmod n$, then
$$n\mid(a-a')+(b-b')=(a+b)-(a'+b'),$$
$$n\mid(a-a')b+a'(b-b')=ab-a'b'.$$
Consequently,
$$a+b\equiv a'+b'\pmod n,\qquad ab\equiv a'b'\pmod n.$$
These operations are independent of the representatives chosen and inherit the usual arithmetic rules from $\mathbb Z$.

## Ruling out an integer solution

Suppose $2a^2+3b^2=1$ for integers $a,b$. Modulo $3$, this requires $2a^2\equiv1$. But $a\equiv0,1,2$ gives $2a^2\equiv0,2,2$, respectively. None gives $1$, so the equation has no integer solution.

Source: [[Numbers and Sets - Chapter 1 Elementary Number Theory]], pages 18–19, including the cyclic residue diagram as TikZ. Related: [[Divisibility and Prime Numbers]], [[Greatest Common Divisors and Euclid's Algorithm]], and the additive groups $\mathbb Z_n$ in [[Groups]].
