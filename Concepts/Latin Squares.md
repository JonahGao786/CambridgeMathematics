---
title: Latin Squares
material_type: source-backed definition
course: Part IA Groups
---

# Latin Squares

A Latin square is an array of symbols such that each row and column contains the same set of symbols, and no row or column contains a duplicated entry. A correctly completed Sudoku puzzle forms a Latin square.

## Cayley tables of finite groups

For a fixed group element $a$, if $ab=ac$, cancellation gives $b=c$. Likewise, $ba=ca$ gives $b=c$. Thus no row or column of a finite group's Cayley table repeats an entry; each contains every group element, so the table is a Latin square.

The identity is found in the row and column that leave the ordered labels unchanged. A product equal to the identity identifies an inverse pair. For an abelian group, the table is symmetric about its main diagonal.

## Associative Latin-square operations

If $S$ is a non-empty finite set and $*:S\times S\to S$ is associative with a Latin-square table, then $(S,*)$ is a [[Groups|group]]. The revised argument constructs an identity using row surjectivity and cancellation. Column cancellation makes the resulting left identities agree; the same cancellation shows that right inverses are also left inverses.

Sources: [[Groups - Introductory Sheet 2026]], page 2, question 8, and [[Groups 0 - Handwritten Attempts]], pages 9–10, questions 8(a) and 8(c). The attempt at 8(b) still incorrectly identifies a non-associative Latin square as a group table and retains its review flag.
