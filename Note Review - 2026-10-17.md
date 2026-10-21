---
title: Note Review - 2026-10-17
material_type: repository mathematical review record
date: 2026-10-17
---

# Note Review — 2026-10-17

> [!note] Historical snapshot
> The classroom issues listed below were subsequently repaired on 2026-10-21. See [[Note Review - 2026-10-21]] for current proof status. This record preserves the findings and validation of the earlier review.

## Scope and method

All **44 pre-existing Markdown notes** were read in full: 29 concept notes, 8 lecture notes, 4 printed problem sheets and 3 handwritten-attempt notes. The review checked definitions, hypotheses, algebra, proof dependencies, domains, exceptional cases, agreement between lecture and concept pages, and the mathematical descriptions in the existing TikZ code. No PDFs were downloaded or visually reread, and no diagrams were changed or rendered. This is a review of the repository’s mathematical content, not a fresh source-transcription or Drive-inventory verification. Historical visual-reading claims in existing notes refer to earlier runs.

Edits preserve original attempts and source metadata. Additional proofs and qualifications are explicitly supplementary. [[Study Guide]] provides a course-by-course reading order covering all 44 notes. The existing Groups attempt filename remains unchanged; its inconsistent “Groups 1” heading and title now agree with “Groups 0”.

## Main findings

The most direct statement error was a missing hypothesis in the generated-subgroup concept page: the finite-word description covers all of $G$ only when $X$ generates $G$. This is now explicit and agrees with Lemma 1.18 in the lecture.

Several sound topics lacked their connecting definitions or justification. Added explanations connect Euclid’s algorithm to unique factorization, span to bases and coordinates, and first-order remainders to total differentiability. The fundamental theorem now has a supplementary proof under continuity, while the source’s stronger-hypothesis proof and its scope remain visible.

The review also found unmarked limitations in existing exercise attempts: the Fibonacci divisibility step can invoke undefined $F_0$; the prime-index argument needs a genuine non-trivial-divisor argument; the last claim in the pigeonhole exercise lacks proof; and the Taylor coefficient in question 5(iii) vanishes at $a^2=2/3$. These are localized review flags, not silently completed answers.

## Remaining work and proof status

- [[Numbers and Sets 0 - Handwritten Attempts]]: page 7, question 5(a), Fibonacci indexing and prime-index argument; page 12, question 7(c), irrationality prerequisites for the final example; page 13, question 8, final claim; page 15, question 9, reduction to the diagram cases. Questions 11–12 remain blank.
- [[Groups 0 - Handwritten Attempts]]: question 2(viii) retains its incorrect original identity assessment beside the correction; question 7(b) lacks a valid common-domain non-commuting example; question 8(b) is an incorrect answer with a verified associativity counterexample; question 9’s commutativity proof remains invalid. Questions 10–12 remain unanswered. The five-term bracketing count remains the source’s abbreviated counting argument.
- [[Groups - Chapter 1 Examples and Definitions]]: page 23, the reverse inclusion in the dihedral classification remains unfinished. The separate kite-lemma verification resolves the mathematical generality issue without changing the original argument or diagram.
- [[Differential Equations - Examples Sheet 1 Handwritten Proofs]]: question 1 omits a separate constant-case argument; question 3(ii) is unanswered; question 4(ii) lacks an infinite-remainder estimate; question 5(iii) needs exceptional-parameter treatment; question 6 does not handle its boundary case separately. Questions 8–14 remain unanswered.
- [[Differential Equations - Chapter 2 Integration]] and [[Differential Equations - Chapter 3 Partial Differentiation]] retain their source proof-status notes. The linked supplementary explanations provide valid learning routes but do not claim that the original source proofs were complete.
- [[Numbers and Sets - Chapter 0 Proofs]]: the dated prime-gap historical remark still lacks a reference. Its list includes claims for discussion, not a list of verified theorems.
- Printed exercise questions remain questions. In particular, the domain and regularity qualifications appended to [[Differential Equations - Examples Sheet 1 2026]] are reading guidance, not completed solutions.

## Per-note coverage

“Reviewed; retained” means the existing material was read and no additional edit was needed for this review. It does not certify an already labelled wrong or unfinished proof as correct, or independently verify historical/source claims.

| Note | Review outcome |
| --- | --- |
| [[Bijections and Permutations]] | Defined injectivity/surjectivity, proved equivalence, and clarified inverse-function notation. |
| [[Complex Exponential and Trigonometric Functions]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Complex Logarithms and Powers]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Complex Numbers]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Cross Products and Scalar Triple Products]] | Explained degenerate volume, linear dependence and operation order. |
| [[De Moivre's Theorem]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Differentiation Rules]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Divisibility and Prime Numbers]] | Added a supplementary uniqueness proof and clarified divisor terminology. |
| [[Fibonacci Numbers]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Fundamental Theorem of Algebra]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Greatest Common Divisors and Euclid's Algorithm]] | Added the algorithm-to-Bézout-to-Euclid chain as a supplementary proof. |
| [[Groups]] | Added justified cancellation and operation-dependent notation. |
| [[Integration by Substitution and by Parts]] | Added the definite formulas, branch restrictions and improper-integral interpretation. |
| [[Isometries and Dihedral Groups]] | Added a kite-lemma verification that covers configurations outside the drawn case. |
| [[L'Hôpital's Rule]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Latin Squares]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Limits, Big O and Little o - A First-Year Guide]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Logical Connectives and Quantifiers]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Natural Numbers and Mathematical Induction]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Orthonormal Bases and Vector Coordinates]] | Explained coordinate extraction and orientation requirements. |
| [[Partial Derivatives and the Multivariate Chain Rule]] | Defined total differentiability, gave a partial-derivative counterexample and justified path remainders. |
| [[Proof by Contradiction and Contraposition]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Real Inner Products and Cauchy-Schwarz]] | Connected complex modulus with real inner products; distinguished complex inner-product axioms. |
| [[Riemann Integration and the Fundamental Theorem of Calculus]] | Added separate continuity-based proofs, uniform error control and antiderivative evaluation. |
| [[Roots of Unity]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Subgroups and Generated Subgroups]] | Restored the generating-set hypothesis; explained well-ordering, integer division, and empty generation. |
| [[Taylor Series and Taylor's Theorem]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Triangle Inequality for Complex Numbers]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Vectors and Linear Span]] | Added linear independence and basis definitions between span and coordinates. |
| [[Differential Equations - Examples Sheet 1 2026]] | Qualified domains, inverse derivatives, antiderivative constants and improper limits separately from questions. |
| [[Differential Equations - Examples Sheet 1 Handwritten Proofs]] | Flagged exceptional parameters in the three-non-zero-term Taylor question. |
| [[Differential Equations - Chapter 1 Introduction and Basic Calculus]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Differential Equations - Chapter 2 Integration]] | Linked continuity-based proofs and substitution-domain explanations. |
| [[Differential Equations - Chapter 3 Partial Differentiation]] | Linked the rigorous differentiability and chain-rule explanation. |
| [[Groups - Chapter 1 Examples and Definitions]] | Linked the supplementary kite verification while retaining the unfinished classification. |
| [[Groups - Example Sheet 1 2025]] | Added missing prerequisite definitions for element order, cyclic groups, homomorphisms and isomorphisms. |
| [[Groups - Introductory Sheet 2026]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Groups 0 - Handwritten Attempts]] | Aligned title with filename; clarified modulo-six identity and singular-matrix group identity. |
| [[Numbers and Sets - Chapter 0 Proofs]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Numbers and Sets - Chapter 1 Elementary Number Theory]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Numbers and Sets - Introductory Sheet 2026]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Numbers and Sets 0 - Handwritten Attempts]] | Flagged Fibonacci boundary/proof gaps and the unsupported simultaneous-failure claim; clarified real powers. |
| [[Vectors and Matrices - Chapter 1 Complex Numbers]] | Reviewed; retained existing mathematical content and proof-status distinctions. |
| [[Vectors and Matrices - Chapter 2 Vectors]] | Reviewed; retained existing mathematical content and proof-status distinctions. |

## Validation

All 46 resulting Markdown files passed frontmatter parsing, control-character, code-fence and display-math delimiter checks. All 295 wikilinks resolve, including 5 heading targets. Both this report and the study guide cover every original note. Symbolic/algebraic checks verified the exceptional Taylor coefficient, the general kite identity, the Bézout arithmetic, the modulo-six identity and the singular-matrix group products. The complete note diff was reviewed and `git diff --check` passed.

The sync manifest records this Markdown-only review separately. Historical source timestamps, processing statuses and visual page-coverage records were preserved. These checks do not substitute for visual comparison with the original PDFs or rendering in Obsidian.
