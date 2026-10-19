---
title: Isometries and Dihedral Groups
material_type: source-backed definitions, lemmas and proof status
course: Part IA Groups
source_file: Ch.1 Introduction.pdf
drive_file_id: 1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB
source_url: https://drive.google.com/file/d/1aDCWwXyAhzhPdQe-mhQZ6rIg1Wo5FIcB/view
source_pages: [19, 20, 21, 22, 23, 24]
---

# Isometries and Dihedral Groups

For $X\subseteq\mathbb C$, an **isometry** is a bijection $f:X\to X$ such that
$$|f(x)-f(y)|=|x-y|\qquad(x,y\in X).$$
The identity, composites and inverses preserve distances, so
$$\operatorname{Isom}(X)\le\operatorname{Sym}(X).$$
The proof and diagrams are in [[Groups - Chapter 1 Examples and Definitions]], pages 19–24. The source note also flags an incorrect coordinate-distance formula on page 19.

## Dihedral group

For $n\ge3$, let $X_n$ be the regular $n$-gon with vertices $e^{2\pi ij/n}$, $j=0,\ldots,n-1$. Define $D_{2n}=\operatorname{Isom}(X_n)$.

Lemma 1.22 proves that the following are isometries:
$$r_k(z)=e^{2\pi ik/n}z,\qquad s_\ell(z)=e^{2\pi i\ell/n}\overline z,
\qquad k,\ell=0,\ldots,n-1.$$
Here $r_0$ is the identity, the $r_k$ are pairwise distinct rotations, and $s_\ell$ reflects in the line $\{re^{\pi i\ell/n}:r\in\mathbb R\}$; verification of that reflection description is an exercise.

Proposition 1.25 states
$$D_{2n}=\{r_k,s_\ell:k,\ell=0,\ldots,n-1\}.$$
The reverse-inclusion argument on pages 23–24 assumes the corner-preservation claim, which is left as an exercise with a distance-maximizing-diagonal idea. If $f(1)=\zeta^m$, where $\zeta=e^{2\pi i/n}$, it sends the adjacent vertices $\zeta,\zeta^{-1}$ to $\zeta^{m-1},\zeta^{m+1}$ in either order. It therefore agrees with $r_m$ or $s_m$ on three non-collinear vertices; the three point lemma gives equality on $X_n$. The localized TODO now concerns the unproved corner-preservation claim, rather than the formerly missing continuation.

Writing $r=r_1$, $s=s_0$, the identities $r_k=r^k$ and $s_\ell=r^\ell s$ show that $\{r,s\}$ generates $D_{2n}$. Lemma 1.26 proves $sr=r^{-1}s$ by evaluating the two composites at $z$; both give $e^{-2\pi i/n}\overline z$.

## Geometric lemmas

**Kite lemma (1.23).** If
$$|w_1-z_1|=|w_2-z_1|,\qquad |w_1-z_2|=|w_2-z_2|,$$
then $(z_1-z_2)\perp(w_1-w_2)$. The geometric proof uses the equal adjacent angles where the kite's diagonals meet.

**Three point lemma (1.24).** An isometry of $X\subseteq\mathbb C$ fixing three non-collinear points $z_1,z_2,z_3$ is the identity. Otherwise, for a moved point $y$,
$$|f(y)-z_i|=|f(y)-f(z_i)|=|y-z_i|.$$
The kite lemma makes both $z_1-z_2$ and $z_2-z_3$ perpendicular to the non-zero vector $f(y)-y$, forcing collinearity, a contradiction.

Related: [[Groups]], [[Subgroups and Generated Subgroups]], [[Bijections and Permutations]], [[Roots of Unity]].
