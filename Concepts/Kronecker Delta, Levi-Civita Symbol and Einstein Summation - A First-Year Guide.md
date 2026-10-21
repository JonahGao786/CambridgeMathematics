---
title: Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide
material_type: concept note
course: Part IA Vectors and Matrices
source_file: Ch.2 Vectors.pdf
drive_file_id: 1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN
source_url: https://drive.google.com/file/d/1xCtvnNzKKZxIqkqMOLAWlC1qHbq_9TFN/view
source_pages: [9, 19, 20, 21, 22, 23]
---

# Kronecker Delta, Levi-Civita Symbol and Einstein Summation

Index notation makes vector calculations compact. The Kronecker delta selects matching components, the Levi-Civita symbol keeps track of orientation, and Einstein summation abbreviates repeated sums. See [[Vectors and Matrices - Chapter 2 Vectors]], pages 9 and 19–23.

Work in $\mathbb R^3$ with a **right-handed orthonormal basis** $\mathbf e_1,\mathbf e_2,\mathbf e_3$. Unless stated otherwise, every index ranges over $1,2,3$. These are Cartesian coordinates, with the lecture's convention of writing all indices downstairs.

| Idea | Job | First example |
| --- | --- | --- |
| Kronecker delta $\delta_{ij}$ | Tests whether two index values match | $\delta_{22}=1$, $\delta_{23}=0$ |
| Levi-Civita symbol $\varepsilon_{ijk}$ | Records the orientation/sign of three index values | $\varepsilon_{123}=1$, $\varepsilon_{213}=-1$ |
| Einstein summation convention | Omits a sum when an index occurs twice in a term | $a_ib_i=\sum_{i=1}^3a_ib_i$ |

The symbols $\delta$ and $\varepsilon$ are arrays of numbers. The summation convention is a rule for reading expressions containing them.

## 1. An index selects a component

For
$$\mathbf a=(a_1,a_2,a_3)
=a_1\mathbf e_1+a_2\mathbf e_2+a_3\mathbf e_3,$$
$a_i$ means “the $i$th component.” It is a scalar, not the whole vector. The subscript is a label, not a power.

For example, if $\mathbf a=(1,2,3)$, then $a_2=2$. Writing $c_i=a_i+b_i$ means three equations:
$$c_1=a_1+b_1,\qquad c_2=a_2+b_2,\qquad c_3=a_3+b_3.$$
There is no summation in any term here: each term contains its index only once.

## 2. Free and dummy indices: read the sums first

An index occurring **twice within one term** is a **dummy**, **summed** or **contracted** index. Replace it by a summation sign if unsure:
$$a_ib_i=\sum_{i=1}^3a_ib_i=a_1b_1+a_2b_2+a_3b_3.$$
After summing, $i$ disappears. Its name is immaterial:
$$a_ib_i=a_jb_j=a_kb_k.$$
Rename both occurrences together, using a name that does not collide with another index in that term.

An index occurring **once within a term** is a **free index**. Hold it fixed while doing the sums. For example,
$$c_i=\varepsilon_{ijk}a_jb_k
=\sum_{j=1}^3\sum_{k=1}^3\varepsilon_{ijk}a_jb_k.$$
Here $i$ is free, while $j,k$ are independently summed. First choose $i=1$, then $2$, then $3$ to obtain the three components.

| Expression | Summed indices | Free indices | Result |
| --- | --- | --- | --- |
| $a_ib_i$ | $i$ | none | one scalar |
| $\delta_{ij}a_j$ | $j$ | $i$ | components of a vector |
| $\varepsilon_{ijk}a_jb_k$ | $j,k$ | $i$ | components of a vector |
| $\delta_{ij}$ | none | $i,j$ | entries of the identity matrix |
| $A_{ik}B_{kj}$ | $k$ | $i,j$ | entries of the matrix product $AB$ |

The result column concerns scalar component expressions. An expression with explicit basis vectors, such as $\mathbf a=a_i\mathbf e_i$, is a vector: the sum combines vectors, even though no free component index remains.

### Bookkeeping rules

1. A dummy index occurs exactly twice in each term. Three occurrences, such as $a_ib_ic_i$, are invalid under this convention. If a three-factor componentwise sum is intended, write $\sum_{i=1}^3a_ib_ic_i$ explicitly.
2. Every term of a component equation must have the same free indices. Thus $c_i=a_i+b_i$ is valid, while $c_i=a_i+b_j$ is not a valid vector-component identity.
3. Count indices separately in each additive term and on each side of an equality. The occurrence of $i$ in $c_i$ does not turn $i$ in the separate term $a_i$ into a summed index.
4. A literal number is a fixed index value: $\delta_{11}$ has no hidden sum.

For a matrix-vector product,
$$y_i=A_{ij}x_j=A_{i1}x_1+A_{i2}x_2+A_{i3}x_3.$$
The free index $i$ chooses a row; the summed index $j$ runs along that row.

## 3. Kronecker delta: why it selects a component

By definition,
$$\delta_{ij}=
\begin{cases}1,&i=j,\\0,&i\ne j.\end{cases}
\qquad
(\delta_{ij})=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&1
\end{pmatrix}.$$
Thus $\delta_{ij}=\delta_{ji}$. Orthonormality is exactly
$$\mathbf e_i\cdot\mathbf e_j=\delta_{ij}.$$

The important selection identity is
$$\delta_{ij}a_j=a_i.$$
For each fixed $i$, all terms except the one with $j=i$ vanish. For example, with $i=2$,
$$\sum_{j=1}^3\delta_{2j}a_j
=0a_1+1a_2+0a_3=a_2.$$
Similarly,
$$a_i\delta_{ij}=a_j.$$
In the first identity $j$ is summed; in the second $i$ is summed. The index that remains free labels the answer.

“The delta makes the indices equal” is shorthand for this selection **inside a sum**. A free $\delta_{ij}$ is not always $1$: $\delta_{12}=0$.

### Why the dot product contains a delta

Start with explicit sums:
$$\begin{aligned}
\mathbf a\cdot\mathbf b
&=\left(\sum_i a_i\mathbf e_i\right)\cdot
\left(\sum_j b_j\mathbf e_j\right)\\
&=\sum_i\sum_j a_ib_j(\mathbf e_i\cdot\mathbf e_j)\\
&=\sum_i\sum_j a_ib_j\delta_{ij}\\
&=\sum_i a_ib_i.
\end{aligned}$$
The delta removes the six off-diagonal terms. In Einstein notation this becomes
$$\mathbf a\cdot\mathbf b=a_ib_j\delta_{ij}=a_ib_i.$$
The dummy index in the final scalar sum could equally be called $j$.

### Why $\delta_{11}=1$ but $\delta_{ii}=3$

With the summation convention in force,
$$\delta_{ii}=\sum_{i=1}^3\delta_{ii}
=\delta_{11}+\delta_{22}+\delta_{33}=3.$$
By contrast, a single diagonal entry is $1$. If a formula explicitly says **no sum over $i$**, then $\delta_{ii}=1$ for that fixed $i$.

In $n$ dimensions the summed trace is $n$. This trace is not an extra property of delta; it counts the diagonal ones.

Two useful contractions are
$$\delta_{ij}\delta_{jk}=\delta_{ik},
\qquad
\delta_{ij}\delta_{ij}=3.$$
The first sums over $j$ only. The second sums over both $i,j$; just three of the nine squared entries are non-zero.

## 4. Levi-Civita symbol: zero first, then the sign

The three-index symbol used here is
$$\varepsilon_{ijk}=
\begin{cases}
1,&(i,j,k)=(1,2,3),(2,3,1),(3,1,2),\\
-1,&(i,j,k)=(1,3,2),(2,1,3),(3,2,1),\\
0,&\text{two or more index values coincide}.
\end{cases}$$

| Value | Triples |
| --- | --- |
| $+1$ | $123,\ 231,\ 312$ |
| $-1$ | $132,\ 213,\ 321$ |
| $0$ | every triple with a repeated value, such as $112,\ 232,\ 333$ |

To evaluate one entry:

1. If two values are equal, the answer is $0$.
2. Otherwise, count the parity of swaps needed to turn $123$ into the given order: an even number gives $+1$, an odd number gives $-1$.

For example, $123\to213$ is one swap, so $\varepsilon_{213}=-1$. The cyclic change $123\to231$ can be made by two swaps, so $\varepsilon_{231}=1$.

A **swap** of two positions changes the sign:
$$\varepsilon_{jik}=-\varepsilon_{ijk}.$$
A **cyclic rotation** of all three positions preserves it:
$$\varepsilon_{ijk}=\varepsilon_{jki}=\varepsilon_{kij}.$$
These are different operations.

### How epsilon encodes the cross product

In a right-handed orthonormal basis,
$$\mathbf e_i\times\mathbf e_j=\varepsilon_{ijk}\mathbf e_k.$$
Here $i,j$ are free and $k$ is summed. With $i=1,j=2$,
$$\mathbf e_1\times\mathbf e_2
=\varepsilon_{121}\mathbf e_1+
\varepsilon_{122}\mathbf e_2+
\varepsilon_{123}\mathbf e_3
=\mathbf e_3.$$
Reversing $1,2$ gives $-\mathbf e_3$.

Bilinearity then gives the component formula
$$c_i=(\mathbf a\times\mathbf b)_i
=\varepsilon_{ijk}a_jb_k.$$
For $i=1$, the double sum has nine terms, but only two survive:
$$\begin{aligned}
c_1
&=\sum_{j=1}^3\sum_{k=1}^3\varepsilon_{1jk}a_jb_k\\
&=\varepsilon_{123}a_2b_3+\varepsilon_{132}a_3b_2\\
&=a_2b_3-a_3b_2.
\end{aligned}$$
The zero terms have repeated values in $\varepsilon_{1jk}$. The other two components are
$$c_2=a_3b_1-a_1b_3,\qquad
c_3=a_1b_2-a_2b_1.$$

The lecture also writes the whole vector as
$$\mathbf a\times\mathbf b=\varepsilon_{pqk}a_pb_q\mathbf e_k.$$
Taking its $i$th component gives $\varepsilon_{pqi}a_pb_q$. Cyclically move $i$ to the front, then rename $p,q$ as $j,k$ to get $\varepsilon_{ijk}a_jb_k$. This explains why the two index arrangements describe the same cross product.

The sign convention above relies on a right-handed basis; changing orientation changes the coordinate cross-product signs.

## 5. One numerical example using all three ideas

Let
$$\mathbf a=(1,2,3),\qquad\mathbf b=(4,-1,2).$$

**Selection:**
$$\delta_{2j}a_j=0\cdot1+1\cdot2+0\cdot3=2.$$

**Dot product:**
$$a_ib_i=1\cdot4+2(-1)+3\cdot2=8.$$
The repeated $i$ produces one scalar.

**Cross product:**
$$\begin{aligned}
(\mathbf a\times\mathbf b)_1&=2\cdot2-3(-1)=7,\\
(\mathbf a\times\mathbf b)_2&=3\cdot4-1\cdot2=10,\\
(\mathbf a\times\mathbf b)_3&=1(-1)-2\cdot4=-9.
\end{aligned}$$
Thus $\mathbf a\times\mathbf b=(7,10,-9)$. Check perpendicularity:
$$\mathbf a\cdot(\mathbf a\times\mathbf b)=7+20-27=0,$$
$$\mathbf b\cdot(\mathbf a\times\mathbf b)=28-10-18=0.$$

## 6. Contracting two epsilon symbols

“Contract over $k$” means sum over the repeated $k$. The main identity is
$$\boxed{\varepsilon_{ijk}\varepsilon_{pqk}
=\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp}.}$$
Written out, its left side is
$$\sum_{k=1}^3\varepsilon_{ijk}\varepsilon_{pqk}.$$
The four indices $i,j,p,q$ are free; the identity holds for every fixed choice of them.

### Proof by cases

If $i=j$, the first epsilon is always zero and the two terms on the right cancel.

If $i\ne j$, exactly one value of $k$ makes $\varepsilon_{ijk}$ non-zero. For that $k$, the second epsilon is non-zero only when $(p,q)$ is either $(i,j)$ or $(j,i)$:

- The same ordered pair gives $+1$, selected by $\delta_{ip}\delta_{jq}$.
- The reversed ordered pair gives $-1$, selected by $-\delta_{iq}\delta_{jp}$.
- Every other pair gives $0$ on both sides.

For example, $i=1,j=2,p=2,q=1$ gives
$$\sum_k\varepsilon_{12k}\varepsilon_{21k}
=1(-1)=-1,$$
and
$$\delta_{12}\delta_{21}-\delta_{11}\delta_{22}=0-1=-1.$$

### Align the contracted positions before applying the identity

The displayed identity contracts the **last position** in each symbol. For
$$\varepsilon_{ijk}\varepsilon_{kpq},$$
first use $\varepsilon_{kpq}=\varepsilon_{pqk}$, a cyclic rotation with positive sign.

If instead the second symbol is $\varepsilon_{pkq}$, swapping its last two positions gives
$$\varepsilon_{ijk}\varepsilon_{pkq}
=-\bigl(\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp}\bigr).$$
Do not move an index without checking whether the move is a swap or a cycle.

### Why the other contractions give $2$ and $6$

For fixed $i,p$,
$$\sum_j\sum_k\varepsilon_{ijk}\varepsilon_{pjk}=2\delta_{ip}.$$
If $i=p$, exactly two ordered pairs $(j,k)$ give non-zero entries; their squares are both $1$. If $i\ne p$, no pair makes both entries non-zero.

Contracting all three indices gives
$$\varepsilon_{ijk}\varepsilon_{ijk}=6.$$
There are $27$ triples, but only the six permutations of $123$ contribute, each with square $1$.

## 7. The vector triple-product proof, one step at a time

The lecture proves
$$\mathbf a\times(\mathbf b\times\mathbf c)
=(\mathbf a\cdot\mathbf c)\mathbf b-(\mathbf a\cdot\mathbf b)\mathbf c.$$
Here is the component proof with its contractions expanded.

Keep $i$ free:
$$\begin{aligned}
[\mathbf a\times(\mathbf b\times\mathbf c)]_i
&=\varepsilon_{ijk}a_j(\mathbf b\times\mathbf c)_k\\
&=\varepsilon_{ijk}\varepsilon_{kpq}a_jb_pc_q\\
&=(\delta_{ip}\delta_{jq}-\delta_{iq}\delta_{jp})a_jb_pc_q.
\end{aligned}$$
In the second line, $j,k,p,q$ are all dummy indices. Cyclically rotating $\varepsilon_{kpq}$ puts $k$ last, allowing the contraction identity.

In the first delta term, summing over $p$ selects $b_i$ and summing over $q$ selects $c_j$:
$$\delta_{ip}\delta_{jq}a_jb_pc_q=a_jb_ic_j
=(a_jc_j)b_i=(\mathbf a\cdot\mathbf c)b_i.$$
In the second term, the selections are $c_i$ and $b_j$:
$$\delta_{iq}\delta_{jp}a_jb_pc_q
=a_jb_jc_i=(\mathbf a\cdot\mathbf b)c_i.$$
Subtract. The free index is still $i$ on every term, so these are the components of the claimed vector identity.

For the numerical vectors above and $\mathbf c=(2,0,1)$,
$$\mathbf b\times\mathbf c=(-1,0,2),\qquad
\mathbf a\times(\mathbf b\times\mathbf c)=(4,-5,2).$$
The other side is
$$5\mathbf b-8\mathbf c=(4,-5,2).$$

## 8. Symmetry can make a sum vanish

For example,
$$\varepsilon_{ijk}a_ja_k=0.$$
The factor $a_ja_k$ is symmetric in $j,k$, while epsilon is antisymmetric. In the double sum, the term with $(j,k)$ cancels the term with $(k,j)$; terms with $j=k$ are already zero.

This is the index explanation of $\mathbf a\times\mathbf a=\mathbf0$. It is cancellation across a sum, not a claim that every distinct-index epsilon entry is zero.

## 9. Practice with answers

1. Simplify $\delta_{ij}b_j$ and $\delta_{ij}\delta_{ij}$.
2. Evaluate $\varepsilon_{231}$, $\varepsilon_{213}$ and $\varepsilon_{122}$.
3. Expand $\varepsilon_{2jk}a_jb_k$.
4. Identify the free and summed indices in $\varepsilon_{ijk}\varepsilon_{pjk}v_p$ and simplify.
5. With the numerical vectors above and $\mathbf c=(2,0,1)$, check Lagrange's identity.

**Answers.**

1. $b_i$ (free $i$), and $3$ (both indices summed).
2. $1,-1,0$.
3. $a_3b_1-a_1b_3$; $j,k$ are summed and the output component is fixed at $2$.
4. $i$ is free; $j,k,p$ are summed. Contracting epsilon first gives $2\delta_{ip}v_p=2v_i$.
5. Since $\mathbf a\times\mathbf b=(7,10,-9)$ and $\mathbf b\times\mathbf c=(-1,0,2)$, their dot product is $-25$. Also
   $$(\mathbf a\cdot\mathbf b)(\mathbf b\cdot\mathbf c)
   -(\mathbf a\cdot\mathbf c)|\mathbf b|^2
   =8\cdot10-5\cdot21=-25.$$

When stuck, write every sum sign, circle the free indices, evaluate the zeros in $\delta$ or $\varepsilon$, and only then simplify the remaining terms.

Related: [[Orthonormal Bases and Vector Coordinates]], [[Cross Products and Scalar Triple Products]], [[Real Inner Products and Cauchy-Schwarz]].
