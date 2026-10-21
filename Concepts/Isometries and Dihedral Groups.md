---
title: Isometries and Dihedral Groups
material_type: source-backed definitions, lemmas and proof status with supplementary explanation
course: Part IA Groups
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: [19, 20, 21, 22, 23, 24, 33]
---

# Isometries and Dihedral Groups

For $X\subseteq\mathbb C$, an **isometry** is a bijection $f:X\to X$ such that
$$|f(x)-f(y)|=|x-y|\qquad(x,y\in X).$$
The identity, composites and inverses preserve distances, so
$$\operatorname{Isom}(X)\le\operatorname{Sym}(X).$$
The proof and diagrams are in [[Groups - Chapter 1 Examples and Definitions]], pages 19–24. The corrected coordinate distance is $|z-w|=\sqrt{(x-u)^2+(y-v)^2}$ for $z=x+iy$, $w=u+iv$; the lecture note now explains and repairs the erroneous source formula.

## Dihedral group

For $n\ge3$, use the vertex set $X_n=\{e^{2\pi ij/n}:j=0,\ldots,n-1\}$ of the regular $n$-gon. Define $D_{2n}=\operatorname{Isom}(X_n)$. The edges in the diagrams visualize the cyclic order. The lecture supplement also proves corner preservation for the boundary or filled-polygon interpretation by extending an isometry to an affine plane isometry; the same classification follows there.

Lemma 1.22 proves that the following are isometries:
$$r_k(z)=e^{2\pi ik/n}z,\qquad s_\ell(z)=e^{2\pi i\ell/n}\overline z,
\qquad k,\ell=0,\ldots,n-1.$$
Here $r_0$ is the identity, the $r_k$ are pairwise distinct rotations, and $s_\ell$ reflects in the line $\{re^{\pi i\ell/n}:r\in\mathbb R\}$; verification of that reflection description is an exercise.

Proposition 1.25 states
$$D_{2n}=\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}.$$
**Completed proof — supplementary.** Write $\zeta=e^{2\pi i/n}$. An isometry sends $1$ to some $\zeta^k$ and its neighbour $\zeta$ to either $\zeta^{k+1}$ or $\zeta^{k-1}$, because adjacent vertices have the smallest positive chord distance. Compose with the inverse of the matching $r_k$ or $s_k$ to obtain an isometry $h$ fixing $1,\zeta$. The other neighbour $\zeta^2$ of $\zeta$ must also be fixed, since injectivity excludes its mapping to $1$. These three vertices are non-collinear, so the three point lemma gives $h=\operatorname{id}$.

Thus every isometry is on the displayed list. The maps are distinct: their values at $1$ distinguish their indices, and for equal index their values at $\zeta$ distinguish a rotation from a reflection when $n\ge3$. Hence $|D_{2n}|=2n$. The lecture note contains the full chord-distance and distinctness checks. The earlier 23-page source version stopped after the forward inclusion. The updated source continues the proof on page 24; its corner-preservation exercise is resolved in the supplementary lecture argument, which also covers the polygon boundary or filled polygon.

Writing $r=r_1$, $s=s_0$, the identities $r_k=r^k$ and $s_\ell=r^\ell s$ show that $\{r,s\}$ generates $D_{2n}$. Lemma 1.26 proves $sr=r^{-1}s$ by evaluating the two composites at $z$; both give $e^{-2\pi i/n}\overline z$.

Page 33 extends the relation: $sr^2=r^{-1}sr=r^{-2}s$, and by induction
$$sr^k=r^{-k}s\qquad(k\in\mathbb Z).$$

**Lemma 1.40 (statement only).** If $a,b$ in a group $G$ satisfy
$$a^n=e_G,\qquad b^2=e_G,\qquad ab=ba^{-1},$$
then
$$\varphi(r^k)=a^k,\qquad\varphi(r^ks)=a^kb$$
defines a homomorphism $D_{2n}\to G$. The source ends after this statement, without supplying its proof. See [[Homomorphisms and Isomorphisms]].

## Geometric lemmas

**Kite lemma (1.23).** If
$$|w_1-z_1|=|w_2-z_1|,\qquad |w_1-z_2|=|w_2-z_2|,$$
then $(z_1-z_2)\perp(w_1-w_2)$. The geometric proof uses the equal adjacent angles where the kite's diagonals meet.

**Three point lemma (1.24).** An isometry of $X\subseteq\mathbb C$ fixing three non-collinear points $z_1,z_2,z_3$ is the identity. Otherwise, for a moved point $y$,
$$|f(y)-z_i|=|f(y)-f(z_i)|=|y-z_i|.$$
The kite lemma makes both $z_1-z_2$ and $z_2-z_3$ perpendicular to the non-zero vector $f(y)-y$, forcing collinearity, a contradiction.

Related: [[Groups]], [[Subgroups and Generated Subgroups]], [[Bijections and Permutations]], [[Roots of Unity]].

## Scope of the kite proof — supplementary verification

The picture-based angle argument covers the depicted kite. The points $z_1,z_2$ can lie on the same ray of the perpendicular bisector of $w_1w_2$, so an intersection of the two diagonal **segments** is not guaranteed by the hypotheses. The lemma itself is valid in all cases: identify complex numbers with real vectors and expand
$$\|w_1-z_i\|^2=\|w_2-z_i\|^2
\quad\Longrightarrow\quad
2\langle z_i,w_1-w_2\rangle=\|w_1\|^2-\|w_2\|^2.$$
Subtract the equations for $i=1,2$ to obtain
$$\langle z_1-z_2,w_1-w_2\rangle=0.$$
This also covers zero difference vectors. See [[Real Inner Products and Cauchy-Schwarz]] for the dot-product interpretation.
