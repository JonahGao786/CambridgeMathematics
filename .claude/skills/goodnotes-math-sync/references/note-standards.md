# Note structure and writing standards

Apply to every note this workflow creates or rewrites.

## A. Faithfulness (unchanged core)

- Preserve definitions, statements, hypotheses, quantifiers, domains, notation and the essential steps of every proof. Do not shorten a proof by dropping reasoning.
- Attribute to the source only what it contains. Anything added goes in a labelled callout (§E).
- Normalize obvious slips silently when the intended meaning is clear from context (e.g. `(x-2)(x-5)` in a line that factorizes $x^2-5x+6$ → `(x-3)`; $\cup$ used for logical "or" → $\lor$). Record each normalization in the manifest, not in the note.
- A crossed-out "Proof" or crossed-out end-of-proof square marks a **wrong proof** in this user's convention. Keep the argument inside `> [!warning] Wrong proof` and say in one or two sentences what is wrong. Distinguish it from ordinary algebraic cancellation strokes.
- Omit end-of-proof squares and editing narration ("crossed out", "highlighted", "the source writes …").
- `> [!todo] p. N — …` only for: an unresolved reading after zooming, a substantive mathematical error, a missing step that matters, or genuinely unfinished work.

## B. Lecture-note template

```markdown
---
title: Groups - Chapter 1 Examples and Definitions
course: Part IA Groups
material_type: lecture notes
chapter: 1
source_file: Ch.1 Introduction.pdf
drive_file_id: <id>
source_url: https://drive.google.com/file/d/<id>/view
source_pages: 33
tags: [lecture, groups]
---

# Groups — Chapter 1: Examples and Definitions

> [!abstract] Overview
> Two to four sentences: what the chapter builds and its main results.
> Prerequisites: [[Concept A]], [[Concept B]].

## Results index

| Result | Statement in brief | Page |
| --- | --- | --- |
| [[#Definition 1.4 — Group]] | group axioms (G1)–(G3) | 5 |
| [[#Proposition 1.5 — Basic properties of groups]] | left/right inverses and identity agree; uniqueness | 6 |
| [[#Lemma 1.6 — Inverse of a product]] | $(ab)^{-1}=b^{-1}a^{-1}$ | 10 |

## 1.1 Section title from the lecture

Short connecting prose (one or two sentences) only when it helps.

### Definition 1.4 — Group

Statement, with the defined term in **bold**.

### Proposition 1.5 — Basic properties of groups

Let $(G,\cdot,e)$ be a group. Then …

**Proof.** …

**Example.** … **Remark.** … **Exercise.** …
```

Rules:

1. **Headings follow the lecturer's structure.** `##` for numbered sections/topics of the lecture, `###` for each result. Never put page numbers in headings; pages go in the results index only.
2. **Every numbered result gets its own `###` heading**: `### <Type> <number> — <short name>`. Use the lecturer's type and number exactly (Definition, Lemma, Proposition, Theorem, Corollary, Claim). If the lecturer gives no name, invent a short descriptive one ("Uniqueness of inverses"). If the result is unnumbered but important (a named theorem, a key method), use `### Theorem — Name` / `### Method — Name`.
3. **No LaTeX in headings** (it breaks `[[Note#Heading]]` links and the outline). Write "Inverse of a product", not "$(ab)^{-1}$".
4. **Results index**: one row per `###` result, in order, linking with `[[#Exact heading text]]`. The brief statement column may contain short inline math. Put the source page in the last column.
5. **Proofs** start with `**Proof.**` on the line after the statement. Multi-part proofs use `**(i)**`, `**(ii)**` lead-ins. Justify steps in aligned displays with `&&\text{by (G1)}` tags rather than prose after the display.
6. Examples, remarks, exercises, warnings: bold lead-ins (`**Example.**`), not headings — they would flood the outline. A long worked example that the lecture treats as a section may be a `###` heading `### Example — Name`.
7. Definitions inside running text: make the defined term **bold** at the point of definition.
8. Diagrams go right after the text they illustrate (see the TikZ reference).
9. Course-outline or administrative pages ("there will be 4 sheets") get at most one short line or are omitted.

## C. Concept-note template

Concept notes are **hubs**, not second copies of the lecture.

```markdown
---
title: Subgroups
course: Part IA Groups
material_type: concept note
tags: [concept, groups]
---

# Subgroups

> [!abstract] In one paragraph
> What the idea is and why it matters, in plain words.

## Definition

$H\le G$ if … (the precise definition, as in the lecture).

## Key results

- **Proposition 1.16 — Subgroups of ℤ.** Every subgroup of $(\mathbb Z,+)$ is $n\mathbb Z$ for a unique $n\ge 0$. *Idea:* take the least positive element and divide with remainder. → [[Groups - Chapter 1 Examples and Definitions#Proposition 1.16 — Subgroups of the integers|proof]]
- **Lemma 1.18 — …** statement. → [[…|proof]]

## Examples

- two to five short examples, one line each.

## Pitfalls

- at most three bullets, only real misconceptions.

## Related

[[Groups]] · [[Cyclic Groups and Element Orders]]
```

Rules:

1. State each definition precisely, each key result with its hypotheses, plus a one-line proof idea and a link to the full proof (`[[Lecture Note#Heading|proof]]`). Do **not** reproduce full proofs that exist in a lecture note.
2. Bold the result label (`**Theorem 2.3 — Name.**`) so it is searchable; keep lecture numbering so the user can match it to lectures.
3. Target length: 25–70 lines. If a concept note grows beyond that, it is duplicating the lecture.
4. No page references in prose; no "See X, pages 4–5" sentences. One `## Related` line at the end replaces scattered "see also" sentences.
5. Prefer updating an existing concept note over creating a near-duplicate. Keep file names stable.

## D. Concision rules (the user found earlier notes long-winded)

- **State each fact once per note.** If a property was stated in the definition section, do not restate it in a later summary.
- **No meta-narration.** Ban phrases such as "the lecture states", "the source", "the notes record", "this note", "as shown on page N", "recorded remark", "proof omitted in the lecture" (write **Exercise** or "Proof not given in lectures." once if needed).
- **No closing summaries** that repeat the section ("Thus we have shown that…" paragraphs), and no "Reading the dependencies" / "Why this matters" appendices.
- Prefer a displayed equation over a sentence that describes the equation.
- Prefer a table for parallel facts (truth tables, lists of standard derivatives, group examples).
- Keep connecting prose to one or two sentences between results.

## E. Scope and clarity rules (the user found earlier notes obscure and beyond the syllabus)

- **Course level only.** Write for a Part IA student who has attended these lectures. Do not introduce concepts, terminology or rigour from later courses (e.g. accumulation points, topology, measure, research literature, complexity theory, arXiv references, historical digressions) unless the lecture itself uses them.
- **Do not add external citations or current-research commentary.**
- When a source step is genuinely hard to follow, add at most a short explanation (≤ 5 lines) in:
  ```markdown
  > [!note] Explanation
  > Why the step holds, in plain words.
  ```
  Use these sparingly — roughly one per page of source at most — and never to restate what the line above already says.
- When the lecture defers something ("proved in Analysis I"), say so in one line; do not prove it.
- Prefer concrete language: name the axiom or earlier result used at each step (`by (G1)`, `by Lemma 1.6`).
- Standard notation: ℕ convention as the lecturer defines it; write logical or as $\lor$, and as $\land$.

## F. Problem sheets and attempts

- `## Question n` per question; `**(a)**` lead-ins for parts. Keep the supplied question text distinct from handwritten answers (`**Answer.**`).
- Keep unfinished attempts unfinished; do not solve them. Keep wrong attempts in `> [!warning]` callouts with a one-line diagnosis.
- Do not reconstruct a missing question from memory; mark it with `> [!todo]`.

## G. Frontmatter

Keep it compact and consistent: `title`, `course`, `material_type`, `chapter` (lecture notes), `source_file`, `drive_file_id`, `source_url`, `source_pages`, `tags`; add `additional_sources` (list of `{source_file, drive_file_id, source_url, source_pages}`) when one note combines several files. No prose fields in frontmatter.

## H. Link check before committing

Run a quick check that every wikilink target exists and every `#Heading` anchor matches an actual heading in the target note, e.g.:

```python
import re, pathlib
root = pathlib.Path('.')
notes = {p.stem: p for p in root.rglob('*.md') if '.claude' not in p.parts}
heads = {k: {re.sub(r'^#+\s*', '', l).strip() for l in p.read_text().splitlines() if l.startswith('#')} for k, p in notes.items()}
for k, p in notes.items():
    for m in re.finditer(r'\[\[([^\]|#]*)(?:#([^\]|]+))?(?:\|[^\]]*)?\]\]', p.read_text()):
        tgt, h = m.group(1) or k, m.group(2)
        if tgt not in notes: print(p, 'missing note', tgt)
        elif h and h.strip() not in heads[tgt]: print(p, 'missing heading', tgt, '#', h)
```

(Run it from the repo root with `python3 -I`; pipes inside table cells must be escaped as `\|` in Obsidian tables — the check above treats `\|` as part of the alias.)
