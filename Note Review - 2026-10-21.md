---
title: Note Review - 2026-10-21
material_type: repository mathematical review and classroom corrections
date: 2026-10-21
---

# Note Review — 2026-10-21

## Scope and method

This review continues the complete reading of all **44 study notes** recorded in [[Note Review - 2026-10-17]]. At the start, SHA-256 comparisons confirmed that all 44 notes exactly matched that reviewed state. Their definitions, proof dependencies and course connections were checked using that full reading; the classroom review items and affected derivations were reread and repaired in place. The study guide and earlier review record were also checked. This initial stage contained 44 study notes and three navigation/review documents. Publication checks then found newer remote commits; the reconciliation below brings the current total to 55 study notes and 58 Markdown documents.

The user's instruction specifically authorizes correcting classroom knowledge points and proofs marked for review. The repairs below are labelled mathematical corrections or supplementary proofs; they do not claim to transcribe new source content. Original PDFs and TikZ renderings were not visually reread, and Drive inventory/source timestamps were not advanced. All existing diagrams and exercise attempts are preserved.

## Original classroom review items resolved

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

## Initial validation before remote reconciliation

Validation passed for all 47 Markdown documents: YAML metadata, code fences, mathematical delimiters/environments, 356 internal links (including six heading targets), and coverage of all 44 study notes in the guide and review table. All eight lecture notes were checked for the original review callouts; all six were resolved. Existing TikZ blocks, the seven exercise documents and source-version/visual-reading metadata are unchanged from the start of this pass.

Symbolic checks confirmed the kite identity, coordinate-increment split, Cauchy mean-value auxiliary identity and uniform area-bound arithmetic. Exhaustive vertex permutations for regular polygons with $3\le n\le8$ gave exactly the listed $2n$ isometries; this is a finite consistency check supporting, not replacing, the general proof. `git diff --check` passed. At that stage the changes were saved only in the cloud workspace. The subsequent publication follow-up below records their reconciliation with the current remote branch.

## Original per-note coverage

The following table records the original 44-note review. Where remote commits later expanded a note, the reconciliation section below supersedes its earlier source/proof-status description. “Retained” means the prior full reading was carried forward after a matching-content check and no additional correction was required in this pass; existing exercise warnings still apply.

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

## Publication follow-up: reconciliation with current GitHub notes

The user requested checking and pushing the cloud-workspace changes. The discovered default branch was `master`, whose head `0021c461439c86ab34778e2a7fcada4d2febb202` was four commits ahead of the review's original base. Those updates added 11 study notes and expanded several existing lectures and concepts. Their mathematical Markdown was read during reconciliation; the original PDFs were not reread. All remote source-version, inventory and visual-inspection records were preserved as records of those earlier sync runs. All remote TikZ blocks were preserved byte for byte.

The newer Numbers and Sets lecture now includes source proofs of Bézout's identity, Euclid's lemma and unique factorization. The newer Groups lecture continues the dihedral argument on page 24 and proceeds through homomorphisms, cyclic groups and element orders. Old statements that these source proofs were missing were updated; the labelled supplementary arguments were retained as alternative learning routes. Navigation now includes all 55 study notes.

Five further classroom review locations in the incoming material were repaired:

| Note and location | Correction or completed proof |
| --- | --- |
| [[Groups - Chapter 1 Examples and Definitions]], page 23 | Proved corner preservation for boundary/filled polygons by extending an isometry to an affine plane isometry and preserving extreme points. Distinguished this from the vertex-set model and justified adjacency. |
| [[Numbers and Sets - Chapter 1 Elementary Number Theory]], page 15 | Defined units, irreducibles and prime elements; used the multiplicative norm to prove the factors are non-associate irreducibles, and gave explicit failures of primality. |
| [[Differential Equations - Chapter 3 Partial Differentiation]], page 10 | Uniform convergence of parameter difference quotients on a compact rectangle justifies the fixed-interval limit–integral interchange. |
| [[Differential Equations - Chapter 3 Partial Differentiation]], page 11 | An integrable exponential bound controls every parameter derivative locally; compact-interval convergence and uniform tail bounds justify repeated improper-integral differentiation without circular use of the factorial formula. |
| [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]], page 3 | Stated the homogeneous dimension theorem with continuous coefficients and non-zero leading coefficient; supplied existence/uniqueness and the dimension proof via first-order systems. Distinguished the inhomogeneous affine family and initial conditions from arbitrary boundary conditions. |

Together with the original six locations, this resolves 11 classroom review locations across the two source snapshots. The current nine lecture notes have no remaining TODO/warning callouts. Deliberately assigned exercises, statement-only results and unfinished problem-sheet attempts remain identified as such; the count does not claim that every theorem in the course has now been proved.

### Additional note coverage

| Incoming note | Reconciliation result |
| --- | --- |
| [[Bezout's Identity and Linear Diophantine Equations]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Cyclic Groups and Element Orders]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Differentiation Under the Integral Sign]] | Read; synchronized the two completed interchange justifications. |
| [[First-Order Linear Differential Equations]] | Read; corrected the solution-space statement and synchronized its supplementary proof. |
| [[Forward Euler Method]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Homomorphisms and Isomorphisms]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Implicit Differentiation]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Kronecker Delta, Levi-Civita Symbol and Einstein Summation - A First-Year Guide]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Lines, Planes and Vector Equations]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Modular Arithmetic]] | Read; retained the incoming mathematical content and explicit proof scope. |
| [[Differential Equations - Chapter 4 First-Order Linear Differential Equations]] | Read; corrected the solution-space statement and synchronized its supplementary proof. |

### Final publication checks

Final validation passed for all 58 Markdown documents and 55 study notes: 454 internal links including six heading targets resolve, all nine lecture notes have no TODO/warning callouts, all 52 remote TikZ blocks are byte-identical, and the seven exercise documents match the earlier reviewed versions. Exact finite dihedral checks and symbolic kite, mean-value, epsilon-contraction, vector-product and ring-norm identities passed. Latest remote source/inventory metadata is unchanged, and `git diff --check` passed. Detailed results are recorded in the manifest. Notes, guide, review history and manifest are committed together; remote publication is confirmed by checking the pushed branch and its Git tree. No new Drive sync or PDF visual-reading claim is made by this publication follow-up.
