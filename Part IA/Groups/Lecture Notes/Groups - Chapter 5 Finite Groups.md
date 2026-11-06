---
title: Groups - Chapter 5 Finite Groups
course: Part IA Groups
material_type: lecture notes
chapter: 5
source_file: Ch.5 Finite Groups.pdf
drive_file_id: 1ELnkPWzlB1-HPs9ERuMIKGAXEJi70axO
source_url: https://drive.google.com/file/d/1ELnkPWzlB1-HPs9ERuMIKGAXEJi70axO/view
source_pages: 3
tags: [lecture, groups]
---

# Groups — Chapter 5: Finite Groups

> [!abstract] Overview
> Towards listing groups by order. Groups of prime order are cyclic; order $4$ already allows something other than $C_4$, the Klein four-group $C_2\times C_2$. The direct product theorem recognises when a group is the direct product of two subgroups.
> Prerequisites: [[Groups - Chapter 2 Lagrange's Theorem]] (groups of prime order); [[Groups - Chapter 1 Examples and Definitions]] (homomorphisms, kernels).

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition — Direct product]] | $G\times H$ with componentwise operation; $\lvert G\times H\rvert=\lvert G\rvert\lvert H\rvert$ | 1 |
| [[#Example — Klein four-group]] | $K_4=C_2\times C_2$, not cyclic | 1 |
| [[#Theorem 5.1 — Direct product theorem]] | $H_1\cap H_2=\{e\}$, commuting, $G=H_1H_2\Rightarrow G\cong H_1\times H_2$ | 2–3 |

## 5.1 Groups of small order

Let's try to list groups by order.
- $|G|=1\Rightarrow G\cong\{e\}$.
- $|G|=2\Rightarrow G\cong C_2$ and $|G|=3\Rightarrow G\cong C_3$ (as $|G|$ is prime).
- $|G|=4$? There is $C_4$; anything else?

### Definition — Direct product

**Recall.** If $G,H$ are groups, their **product** (sometimes "**direct product**") is
$$G\times H=\{(g,h)\mid g\in G,\ h\in H\},$$
with
- operation $(g_1,h_1)\cdot(g_2,h_2)=(g_1\cdot g_2,\ h_1\cdot h_2)$;
- identity $(e_G,e_H)$;
- inverses $(g,h)^{-1}=(g^{-1},h^{-1})$.

Then $|G\times H|=|G||H|$.

### Example — Klein four-group

The group $K_4=C_2\times C_2$ is often called the **Klein four-group**.
- It has $4$ elements: $(1,1)$, $(-1,1)$, $(1,-1)$, $(-1,-1)$ (writing $C_2=\{1,-1\}$ under multiplication).
- Each element has order dividing $2$, so $K_4$ is **not** cyclic (no element of order $4$). So $K_4\not\cong C_4$.

### Theorem 5.1 — Direct product theorem

If $H_1,H_2\le G$ and
1. $H_1\cap H_2=\{e\}$,
2. $h_1h_2=h_2h_1$ whenever $h_1\in H_1$, $h_2\in H_2$,
3. for each $g\in G$ there exist $h_1\in H_1$ and $h_2\in H_2$ with $g=h_1h_2$ (write $G=H_1H_2$),

then $G\cong H_1\times H_2$.

**Proof.** Define
$$\varphi:H_1\times H_2\to G,\qquad(h_1,h_2)\mapsto h_1h_2.$$
We want $\varphi$ to be an isomorphism.
- *$\varphi$ is a homomorphism:*
$$\begin{aligned}
\varphi(h_1,h_2)\,\varphi(h_1',h_2')&=h_1h_2h_1'h_2'\\
&=h_1h_1'h_2h_2' &&\text{by (2)}\\
&=\varphi(h_1h_1',\ h_2h_2').
\end{aligned}$$
- *$\varphi$ is surjective:* yes, by (3).
- *$\varphi$ is injective:* we need $\ker\varphi=\{e\}$. Suppose $\varphi(h_1,h_2)=e$, i.e. $h_1h_2=e$. Then $h_1=h_2^{-1}\in H_1\cap H_2=\{e\}$ by (1). So $h_1=h_2^{-1}=e$, so $(h_1,h_2)=(e,e)$, i.e. $\varphi$ is injective. $\square$

> [!note] Explanation
> Each hypothesis is used once. (2) lets $h_2$ slide past $h_1'$, which is exactly what makes multiplying in $G$ look like multiplying componentwise. (3) says every element of $G$ is hit. (1) says the two subgroups overlap only in $e$, so $h_1h_2=e$ forces both factors to be $e$.
