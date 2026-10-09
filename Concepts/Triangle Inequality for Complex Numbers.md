---
title: Triangle Inequality for Complex Numbers
material_type: source-backed theorem and proof
course: Part IA Vectors and Matrices
---

# Triangle Inequality for Complex Numbers

For $z_1,z_2\in\mathbb C$,
$$|z_1+z_2|\le|z_1|+|z_2|,$$
and the reverse triangle inequality is
$$\bigl||z_1|-|z_2|\bigr|\le|z_1-z_2|.$$

Using conjugation and modulus from [[Complex Numbers]],
$$
\begin{aligned}
|z_1+z_2|^2
&=|z_1|^2+|z_2|^2+2\operatorname{Re}(z_1\overline{z_2})\\
&\le|z_1|^2+|z_2|^2+2|z_1|\,|z_2|\\
&=(|z_1|+|z_2|)^2.
\end{aligned}
$$
Here $\operatorname{Re}(w)\le|w|$, $|z_1\overline{z_2}|=|z_1|\,|z_2|$, and all moduli are non-negative. Take square roots to obtain the triangle inequality.

Next,
$$|z_1|=|(z_1-z_2)+z_2|\le|z_1-z_2|+|z_2|.$$
Rearrange to bound $|z_1|-|z_2|$, and interchange $z_1,z_2$ to bound its negative. This gives the absolute-value inequality.

Source: [[Vectors and Matrices - Chapter 1 Complex Numbers]], pages 6–7.
