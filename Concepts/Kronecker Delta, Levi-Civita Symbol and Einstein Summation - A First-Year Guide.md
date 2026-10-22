---
title: Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices, index-notation]
---

# Kronecker Delta, Levi-Civita Symbol and Einstein Summation

> [!abstract] In one paragraph
> In a right-handed orthonormal basis of $\mathbb R^3$, write vectors by components $a_i$. A repeated index means "sum over $1,2,3$". $\delta_{ij}$ picks out matching indices (dot products), $\varepsilon_{ijk}$ records orientation (cross products), and the identity $\varepsilon_{ijk}\varepsilon_{pqk}=\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp}$ turns vector identities into index bookkeeping.

## Rules of the summation convention

| Expression | Summed | Free | Meaning |
| --- | --- | --- | --- |
| $a_ib_i$ | $i$ | — | $\mathbf a\cdot\mathbf b$ (a scalar) |
| $\delta_{ij}a_j$ | $j$ | $i$ | $a_i$ |
| $\varepsilon_{ijk}a_jb_k$ | $j,k$ | $i$ | $(\mathbf a\times\mathbf b)_i$ |
| $A_{ij}x_j$ | $j$ | $i$ | $(A\mathbf x)_i$ |

1. An index appearing **once** in a term is **free**; **twice**, it is summed (a dummy — its name doesn't matter: $a_ib_i=a_jb_j$).
2. No index may appear more than twice in a term ($a_ib_ic_i$ is meaningless; write $\sum_i$ explicitly).
3. Every term of an equation has the same free indices ($c_i=a_i+b_j$ is invalid).

## Kronecker delta

$\delta_{ij}=1$ if $i=j$, $0$ otherwise; $\mathbf e_i\cdot\mathbf e_j=\delta_{ij}$; symmetric.

- **Selection:** $\delta_{ij}a_j=a_i$ — in the sum over $j$ only the $j=i$ term survives.
- $\mathbf a\cdot\mathbf b=\delta_{ij}a_ib_j=a_ib_i$.
- $\delta_{ii}=\delta_{11}+\delta_{22}+\delta_{33}=3$ (summed!), $\delta_{ij}\delta_{jk}=\delta_{ik}$.

## Levi-Civita symbol

$\varepsilon_{ijk}=+1$ for $123,231,312$; $-1$ for $132,213,321$; $0$ if any two indices coincide.

- **Swap** two indices: sign changes ($\varepsilon_{jik}=-\varepsilon_{ijk}$). **Cyclic shift**: unchanged ($\varepsilon_{ijk}=\varepsilon_{jki}=\varepsilon_{kij}$).
- $\mathbf e_i\times\mathbf e_j=\varepsilon_{ijk}\mathbf e_k$, so $(\mathbf a\times\mathbf b)_i=\varepsilon_{ijk}a_jb_k$. E.g. $(\mathbf a\times\mathbf b)_1=\varepsilon_{123}a_2b_3+\varepsilon_{132}a_3b_2=a_2b_3-a_3b_2$.
- $[\mathbf a,\mathbf b,\mathbf c]=\varepsilon_{ijk}a_ib_jc_k$.

## Contraction identities

$$\varepsilon_{ijk}\varepsilon_{pqk}=\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp},\qquad\varepsilon_{ijk}\varepsilon_{pjk}=2\delta_{ip},\qquad\varepsilon_{ijk}\varepsilon_{ijk}=6.$$
→ [[Vectors and Matrices - Chapter 2 Vectors#Proposition — Epsilon identities|lecture]]

*Why the first holds:* if $i=j$ both sides are $0$. If $i\ne j$, one $k$ survives, and $\varepsilon_{pqk}\ne0$ only for $(p,q)=(i,j)$ (giving $+1$) or $(j,i)$ (giving $-1$).

**Align the contracted index first.** The identity contracts the *last* slot of both symbols. For $\varepsilon_{ijk}\varepsilon_{kpq}$ use the cyclic shift $\varepsilon_{kpq}=\varepsilon_{pqk}$; for $\varepsilon_{ijk}\varepsilon_{pkq}$ a swap gives a minus sign.

## Worked examples

- **Vector triple product.** $[\mathbf a\times(\mathbf b\times\mathbf c)]_i=\varepsilon_{ijk}\varepsilon_{pqk}a_jb_pc_q=(\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp})a_jb_pc_q=(\mathbf a\cdot\mathbf c)b_i-(\mathbf a\cdot\mathbf b)c_i$. → [[Vectors and Matrices - Chapter 2 Vectors#Proof of the vector triple product identity|lecture]]
- **Symmetry kills a sum.** $\varepsilon_{ijk}a_ja_k=0$: the $(j,k)$ and $(k,j)$ terms cancel. This is $\mathbf a\times\mathbf a=\mathbf 0$.
- **Numbers.** $\mathbf a=(1,2,3)$, $\mathbf b=(4,-1,2)$: $a_ib_i=8$, $\mathbf a\times\mathbf b=(7,10,-9)$, and $\mathbf a\cdot(\mathbf a\times\mathbf b)=7+20-27=0$.

## Practice

1. Simplify $\delta_{ij}b_j$ and $\delta_{ij}\delta_{ij}$.
2. Evaluate $\varepsilon_{231},\varepsilon_{213},\varepsilon_{122}$.
3. Simplify $\varepsilon_{ijk}\varepsilon_{pjk}v_p$.

> [!note]- Answers
> 1. $b_i$; $3$. 2. $1,-1,0$. 3. $2\delta_{ip}v_p=2v_i$.

## Related

[[Orthonormal Bases and Vector Coordinates]] · [[Cross Products and Scalar Triple Products]] · [[Real Inner Products and Cauchy-Schwarz]]
