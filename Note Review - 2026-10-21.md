---
title: Note Review - 2026-10-21
material_type: repository mathematical review and classroom corrections
date: 2026-10-21
---

# Note Review — 2026-10-21

## Scope and method

This review continues the complete reading of all **44 study notes** recorded in [[Note Review - 2026-10-17]]. At the start, SHA-256 comparisons confirmed that all 44 notes exactly matched that reviewed state. Their definitions, proof dependencies and course connections were checked using that full reading; the classroom review items and affected derivations were reread and repaired in place. The study guide and earlier review record were also checked. The repository has 44 study notes and, after this update, three navigation/review documents.

The user's instruction specifically authorizes correcting classroom knowledge points and proofs marked for review. The repairs below are labelled mathematical corrections or supplementary proofs; they do not claim to transcribe new source content. Original PDFs and TikZ renderings were not visually reread, and Drive inventory/source timestamps were not advanced. All existing diagrams and exercise attempts are preserved.

## Classroom review items resolved

| Location | Problem | Resolution |
| --- | --- | --- |
| [[Differential Equations - Chapter 2 Integration]], pages 2–3 | Summing pointwise $O((\Delta x)^2)$ terms did not establish a uniform error bound. | Added the bounded-derivative hypothesis and proved total error $\le M(b-a)^2/(2N)$. Also proved convergence under continuity alone using upper/lower sums and uniform continuity. |
| [[Differential Equations - Chapter 3 Partial Differentiation]], page 3 | The moving-base-point remainder was uncontrolled. | A coordinatewise mean-value argument under continuous first partials proves a remainder $o(\sqrt{h^2+k^2})$ without requiring mixed second derivatives. |
| [[Differential Equations - Chapter 3 Partial Differentiation]], page 4 | $df$ was incorrectly defined as the unscaled limit of a change in $f$. | Defined $df_p$ as the linear map in the first-order approximation and proved the chain rule with the path remainder controlled. |
| [[Groups - Chapter 1 Examples and Definitions]], page 19 | The displayed complex-coordinate distance formula was wrong. | Derived $|z-w|=\sqrt{(x-u)^2+(y-v)^2}$ and explained the failure of the original expression. |
| [[Groups - Chapter 1 Examples and Definitions]], page 23 | The dihedral classification proved only one inclusion. | Specified the vertex-set model and proved every isometry is a listed rotation/reflection using adjacency and the three point lemma. Verified distinctness, so the order is $2n$. |
| [[Numbers and Sets - Chapter 0 Proofs]], page 3 | The August 2026 prime-gap remark had no reference. | Located a matching primary paper and explained the implication from its stated bound to the lecture's assertion. The note distinguishes finding a reference from independently verifying the research proof. |

All **six** explicit classroom TODO/warning blocks present at the start have a mathematical correction, completed proof or matching reference. Intentionally false examples in the chapter on proofs remain teaching examples with their existing diagnoses; they are not unfinished repairs.

## Additional coherence repairs

- [[Differential Equations - Chapter 2 Integration]] now proves the fundamental theorem under its stated continuity hypothesis, including both signs of the increment, and derives antiderivative evaluation.
- [[Differential Equations - Chapter 1 Introduction and Basic Calculus]] and [[L'Hôpital's Rule]] retain the source's Taylor special case and add a full proof under the stated hypotheses using Rolle's theorem and the Cauchy mean-value identity. No continuity of the derivatives or non-zero derivative at the limiting point is imposed by the added proof.
- The kite lemma now has a complete dot-product proof in the Groups lecture; the pictured diagonal-intersection argument alone did not cover all configurations.
- [[Numbers and Sets - Chapter 1 Elementary Number Theory]] now points directly to the supplementary Bézout/Euclid/unique-factorization proofs in the correct dependency order.
- Related concept pages and [[Study Guide]] were updated so they no longer describe repaired classroom proofs as pending. Statement 4 in the Proofs lecture now explicitly distinguishes a discussion claim about factoring from an established complexity theorem and specifies why the computation model matters.

## External references checked

For the dated remark, [Julia Stadlmann, *Bounded gaps between primes*, arXiv:2608.31126](https://arxiv.org/abs/2608.31126) supplies an August 2026 reference matching the stated bound; its abstract and introductory theorem were inspected. For the computation-model qualification, [Peter W. Shor, *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*](https://arxiv.org/abs/quant-ph/9508027) was checked for its randomized quantum polynomial-time result. These citations establish the reported statements, not independent verification of the full papers or an exact cubic running-time bound.

## Remaining exercise work

The three handwritten-attempt notes retain the proof-status flags and unfinished questions documented in the earlier review. This update does not recast those attempts as complete solutions. In particular, the Fibonacci prime-index argument, some pigeonhole and graph arguments, the group interchange-law attempt, and the infinite-remainder argument in the calculus exercises still require work. Printed questions remain questions. The request to repair classroom review items has been completed separately from these exercise records.

## Validation

Validation passed for all 47 Markdown documents: YAML metadata, code fences, mathematical delimiters/environments, 356 internal links (including six heading targets), and coverage of all 44 study notes in the guide and review table. All eight lecture notes were checked for the original review callouts; all six were resolved. Existing TikZ blocks, the seven exercise documents and source-version/visual-reading metadata are unchanged from the start of this pass.

Symbolic checks confirmed the kite identity, coordinate-increment split, Cauchy mean-value auxiliary identity and uniform area-bound arithmetic. Exhaustive vertex permutations for regular polygons with $3\le n\le8$ gave exactly the listed $2n$ isometries; this is a finite consistency check supporting, not replacing, the general proof. `git diff --check` passed. Changes are saved locally; no commit or push was made in this pass.

## Per-note coverage

The following table covers all 44 study notes. “Retained” means the prior full reading was carried forward after a matching-content check and no additional correction was required in this pass; existing exercise warnings still apply.

| Note | This review |
| --- | --- |
| [[Bijections and Permutations]] | Retained; no additional mathematical correction required in this pass. |
| [[Complex Exponential and Trigonometric Functions]] | Retained; no additional mathematical correction required in this pass. |
| [[Complex Logarithms and Powers]] | Retained; no additional mathematical correction required in this pass. |
| [[Complex Numbers]] | Retained; no additional mathematical correction required in this pass. |
| [[Cross Products and Scalar Triple Products]] | Retained; no additional mathematical correction required in this pass. |
| [[De Moivre's Theorem]] | Retained; no additional mathematical correction required in this pass. |
| [[Differentiation Rules]] | Retained; no additional mathematical correction required in this pass. |
| [[Divisibility and Prime Numbers]] | Retained; no additional mathematical correction required in this pass. |
| [[Fibonacci Numbers]] | Retained; no additional mathematical correction required in this pass. |
| [[Fundamental Theorem of Algebra]] | Retained; no additional mathematical correction required in this pass. |
| [[Greatest Common Divisors and Euclid's Algorithm]] | Retained; no additional mathematical correction required in this pass. |
| [[Groups]] | Updated the classification cross-reference to completed status. |
| [[Integration by Substitution and by Parts]] | Retained; no additional mathematical correction required in this pass. |
| [[Isometries and Dihedral Groups]] | Synchronized the corrected distance, vertex-set model and complete classification. |
| [[L'Hôpital's Rule]] | Added the proof under the stated hypotheses and synchronized the lecture reference. |
| [[Latin Squares]] | Retained; no additional mathematical correction required in this pass. |
| [[Limits, Big O and Little o - A First-Year Guide]] | Retained; no additional mathematical correction required in this pass. |
| [[Logical Connectives and Quantifiers]] | Retained; no additional mathematical correction required in this pass. |
| [[Natural Numbers and Mathematical Induction]] | Retained; no additional mathematical correction required in this pass. |
| [[Orthonormal Bases and Vector Coordinates]] | Retained; no additional mathematical correction required in this pass. |
| [[Partial Derivatives and the Multivariate Chain Rule]] | Synchronized the repaired differentiability and chain-rule proof status. |
| [[Proof by Contradiction and Contraposition]] | Retained; no additional mathematical correction required in this pass. |
| [[Real Inner Products and Cauchy-Schwarz]] | Retained; no additional mathematical correction required in this pass. |
| [[Riemann Integration and the Fundamental Theorem of Calculus]] | Synchronized the uniform bound and continuity-based proofs; removed stale TODO status. |
| [[Roots of Unity]] | Retained; no additional mathematical correction required in this pass. |
| [[Subgroups and Generated Subgroups]] | Retained; no additional mathematical correction required in this pass. |
| [[Taylor Series and Taylor's Theorem]] | Retained; no additional mathematical correction required in this pass. |
| [[Triangle Inequality for Complex Numbers]] | Retained; no additional mathematical correction required in this pass. |
| [[Vectors and Linear Span]] | Retained; no additional mathematical correction required in this pass. |
| [[Differential Equations - Examples Sheet 1 2026]] | Retained; no additional mathematical correction required in this pass. |
| [[Differential Equations - Examples Sheet 1 Handwritten Proofs]] | Retained; no additional mathematical correction required in this pass. |
| [[Differential Equations - Chapter 1 Introduction and Basic Calculus]] | Added a complete proof under the stated L’Hôpital hypotheses; clarified the acceleration example. |
| [[Differential Equations - Chapter 2 Integration]] | Repaired uniform area estimates, proved the continuous-case fundamental theorem and derived antiderivative evaluation. |
| [[Differential Equations - Chapter 3 Partial Differentiation]] | Repaired the increment derivation, differential definition and chain-rule proof. |
| [[Groups - Chapter 1 Examples and Definitions]] | Corrected distance; completed the kite and dihedral proofs; specified the vertex-set model. |
| [[Groups - Example Sheet 1 2025]] | Retained; no additional mathematical correction required in this pass. |
| [[Groups - Introductory Sheet 2026]] | Retained; no additional mathematical correction required in this pass. |
| [[Groups 0 - Handwritten Attempts]] | Retained; no additional mathematical correction required in this pass. |
| [[Numbers and Sets - Chapter 0 Proofs]] | Resolved the dated reference and qualified the factoring discussion claim. |
| [[Numbers and Sets - Chapter 1 Elementary Number Theory]] | Linked the supplementary proof chain in dependency order. |
| [[Numbers and Sets - Introductory Sheet 2026]] | Retained; no additional mathematical correction required in this pass. |
| [[Numbers and Sets 0 - Handwritten Attempts]] | Retained; no additional mathematical correction required in this pass. |
| [[Vectors and Matrices - Chapter 1 Complex Numbers]] | Retained; no additional mathematical correction required in this pass. |
| [[Vectors and Matrices - Chapter 2 Vectors]] | Retained; no additional mathematical correction required in this pass. |
