---
title: Lines, Planes and Vector Equations
course: Part IA Vectors and Matrices
material_type: concept note
tags: [concept, vectors-and-matrices]
---

# Lines, Planes and Vector Equations

> [!abstract] In one paragraph
> A line is $\mathbf r=\mathbf a+\lambda\mathbf u$; crossing with $\mathbf u$ removes the parameter. A plane is $\mathbf n\cdot\mathbf r=k$ with normal $\mathbf n$. Intersections and distances follow from dot/cross products and the vector triple product.

## Equations

| Object | Parametric | Parameter-free |
| --- | --- | --- |
| Line through $\mathbf a$, direction $\mathbf u$ | $\mathbf r=\mathbf a+\lambda\mathbf u$ | $\mathbf u\times\mathbf r=\mathbf u\times\mathbf a$ |
| Plane through $\mathbf a$, directions $\mathbf u,\mathbf v$ | $\mathbf r=\mathbf a+\lambda\mathbf u+\mu\mathbf v$ | $\mathbf n\cdot\mathbf r=\mathbf n\cdot\mathbf a$, $\mathbf n=\mathbf u\times\mathbf v$ |
| Plane through $A,B,C$ | | $(\mathbf r-\mathbf a)\cdot[(\mathbf b-\mathbf a)\times(\mathbf c-\mathbf a)]=0$ |
| Sphere, centre $\mathbf a$, radius $r$ | | $\lvert\mathbf r-\mathbf a\rvert=r$ |

→ [[Vectors and Matrices - Chapter 2 Vectors#Lines|lines]] · [[Vectors and Matrices - Chapter 2 Vectors#Planes|planes]]

## Key results

- **Distance of plane $\mathbf n\cdot\mathbf r=k$ from $O$:** $|k|/|\mathbf n|$.
- **Line meets plane** in a unique point iff $\mathbf u\cdot\mathbf n\ne0$: $\mathbf r=\frac{(\mathbf n\cdot\mathbf b)\mathbf u-(\mathbf a\times\mathbf u)\times\mathbf n}{\mathbf u\cdot\mathbf n}$. If $\mathbf u\cdot\mathbf n=0$: the line lies in the plane or misses it. → [[Vectors and Matrices - Chapter 2 Vectors#Intersection of a line and a plane|derivation]]
- **Shortest distance between lines** $\mathbf a_i+\lambda\mathbf u_i$: $s=|(\mathbf a_1-\mathbf a_2)\cdot\hat{\mathbf n}|$, $\hat{\mathbf n}\parallel\mathbf u_1\times\mathbf u_2$. *Idea:* $(\mathbf p-\mathbf q)\cdot\hat{\mathbf n}$ is the same for all points, and the bound is attained. → [[Vectors and Matrices - Chapter 2 Vectors#Shortest distance between two lines|proof]]
- **Vector equation** $\mathbf r+\mathbf a\times(\mathbf b\times\mathbf r)=\mathbf c$: dot with $\mathbf a$ to get $\mathbf a\cdot\mathbf r$ first. Unique solution if $\mathbf a\cdot\mathbf b\ne1$; otherwise none or a whole plane. → [[Vectors and Matrices - Chapter 2 Vectors#Vector equations|solution]]

## Related

[[Cross Products and Scalar Triple Products]] · [[Complex Numbers]] (lines and circles in $\mathbb C$)
