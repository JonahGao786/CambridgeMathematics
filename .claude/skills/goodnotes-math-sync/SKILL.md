---
name: goodnotes-math-sync
description: "Use when syncing Goodnotes study materials (Cambridge Part IA lecture notes, sheets) from Google Drive into the CambridgeMathematics Obsidian repository, re-organizing existing generated notes, or repairing math notes and TikZ diagrams. Produces navigable, concise, course-level notes with every numbered result individually findable; requires full visual reading of the source PDFs."
---

# Goodnotes Math Sync

Turn Goodnotes study materials into clean, faithful, **easy-to-navigate** Obsidian notes, and publish notes plus the sync manifest together.

The three quality goals, in priority order:

1. **Faithful** — the mathematics matches the visually read source.
2. **Findable** — every definition, lemma, proposition, theorem and corollary has its own heading and an entry in the note's results index, so it can be located from the Obsidian outline, search, or a `[[Note#Heading]]` link.
3. **Lean and at course level** — each fact is stated once, in plain language a first-year student can follow, with nothing beyond the course's own scope.

Read these references before writing any note; they are part of the workflow:

- [Note structure and writing standards](references/note-standards.md) — templates, headings, results index, concision and scope rules. **Most important.**
- [TikZ diagram requirements](references/tikz-diagrams.md)
- [Manifest and publication rules](references/sync-manifest.md)

## Scope and configured targets

- Source: Goodnotes Google Drive folder `1jjUv2Kmh0iaqFYd2Rsq0RXKeBFJ0QCfX` (<https://drive.google.com/drive/folders/1jjUv2Kmh0iaqFYd2Rsq0RXKeBFJ0QCfX>).
- Destination: `JonahGao786/CambridgeMathematics`, an Obsidian vault. Manifest: `.sync/goodnotes-manifest.json`.
- Publication branch: the repository's default branch, unless the session or user names a different branch — then use that one.
- The user's current request sets the scope. Common scopes: a normal sync (new/modified sources), a **re-organization** run (rewrite existing generated notes to the current standards, re-reading sources), or a targeted repair. If the user says to skip a material type (e.g. example sheets), leave those notes and manifest records untouched.
- Creating, installing or editing this skill does not by itself start a sync.

## 1. Inventory

1. Verify Drive read access and repository write access; report blockers rather than claiming success.
2. Inspect the repository: folders (`Part IA/<Course>/Lecture Notes`, `.../Problem Sheets` or `Examples Sheets`, `Concepts/`, `Study Guide.md`), naming, frontmatter, `.gitignore`, and the manifest.
3. List the Drive folder recursively with full pagination (`parentId = '<id>'` searches, following every `nextPageToken`). A listing failure is a failure, never "zero changes".
4. Compare each file's `modifiedTime` against the manifest's `processed_source_modified_timestamp`. A newer timestamp usually means pages were added: diff the page count and read every page anyway.
5. Note files that disappeared from Drive; keep their notes and record them as no longer in inventory.

## 2. Get page images

**Preferred: service account.** If the user has provided a service-account key (JSON, kept outside the repo, e.g. under `~/.claude/uploads/`), use `scripts/drive_sa.py` — it lists the folder recursively and downloads files of any size, so the connector's size crash is avoided:

```
python3 scripts/drive_sa.py KEY.json list 1jjUv2Kmh0iaqFYd2Rsq0RXKeBFJ0QCfX     # id, modifiedTime, size, path
python3 scripts/drive_sa.py KEY.json get FILE_ID <scratchpad>/name.pdf
```

Requirements: the Google Drive API must be enabled in the key's Cloud project, and the Goodnotes folder must be shared (Viewer) with the key's `client_email`. A 403 "API has not been used … or is disabled" or 404 on the folder means one of these is missing: tell the user, and fall back to the connector below. Treat the key as a secret: never copy it into the repo, a commit, the manifest or a report, and never print it. `rclone` with `--drive-service-account-file` is an equivalent alternative.

Fallback — the Drive connector, which works in Claude Code cloud sessions for files up to a few MB:

1. `download_file_content(fileId)` — large results are saved to a JSON file on disk (`{content: base64, id, title, mimeType}`). Decode it with a small Python script (`python3 -I`) into the scratchpad, never into the repo.
2. (Before viewing, run `pagediff.py` as in §3 to learn which pages matter.) Render with Poppler: `pdftoppm -r 130 -png file.pdf out/prefix` (PyMuPDF if available). `pdfinfo` gives the page count.
3. View each PNG with the image-capable Read tool. Crop/zoom (`pdftoppm -r 250 -x … -y … -W … -H …`) when exponents, subscripts, signs, Greek letters or diagram labels are unclear.
4. Very large PDFs (≈7 MB+) can crash the Drive connector. Retry once; if it fails again, mark that source `pending` with the exact failed operation. For a re-organization run you may restructure its existing note conservatively (no new mathematical claims), and must say so in the report and manifest.
5. Extracted text/OCR is an aid only. Never claim visual reading you did not do.

## 3. Read completely, then plan the note

For each source:

1. **Find which pages need viewing.** Run `python3 scripts/pagediff.py diff NEW.pdf .sync/goodnotes-manifest.json FILE_ID --render <scratchpad>/pages`. It compares per-page pixel hashes with `files[FILE_ID].page_hashes`, matching by content so inserted/moved pages are handled, and prints the pages to VIEW (rendered into the output dir). Pages whose hash is already in the baseline are visually identical to what was processed and are **not** re-viewed; "removed/edited old pages" means content that disappeared — check the note for it. No baseline (new source, or record without `page_hashes`) → view **every** page. After processing, store the full list: `python3 scripts/pagediff.py hash NEW.pdf` → `page_hashes` in the record. A hash baseline may be taken from a PDF whose Drive `modifiedTime` equals `processed_source_modified_timestamp` without viewing it (it is what the note was built from).
2. Read every page that is flagged (or all pages without a baseline); record the page count, the pages actually viewed, and that the rest matched the baseline hashes.
3. While reading, build a **results list**: every numbered item (Definition 1.4, Lemma 1.6, Proposition 1.5, Theorem 1.20, Corollary …) with its number, name and page, plus important unnumbered named results. This becomes the note's headings and results index.
4. Identify the lecturer's section structure (chapter → numbered sections). Notes follow that structure, **not** page boundaries.
5. Note crossed-out proofs (→ wrong/incomplete proof), unfinished work, highlighted terms (→ bold defined terms), and diagrams.
6. Classify the material (lecture notes, problem sheet, worked attempts, handout, non-study) by content.

## 4. Write the notes

Follow [note standards](references/note-standards.md) exactly. In summary:

- **Lecture note** (one per source chapter): frontmatter → H1 title → short overview callout → **Results index table** → body organized by the lecturer's sections, with each numbered result as an H3 heading `### Theorem 1.20 — Name` followed by statement, then **Proof.** Examples, remarks and exercises are bold lead-ins, not headings.
- **Concept note** (one per reusable topic): a short hub — definitions, key results with one-line proof ideas, and links to the full proofs in lecture notes. Do **not** copy proofs that already live in a lecture note.
- **Problem-sheet / attempt notes**: preserve question numbering; one `## Question n` heading per question.
- **Study Guide**: per course, the chapter list and concept sequence with links.
- Mathematics in LaTeX (`$…$`, `$$…$$`), TikZ for drawings, `[[wikilinks]]` between notes.
- Normalize obvious slips silently (record in manifest). Use `> [!todo]` only for genuinely unresolved readings, substantive errors, or unfinished work, with page number.
- Supplementary explanation only where a step would otherwise be hard to follow, inside a short `> [!note] Explanation` callout, at course level.

## 5. Update existing notes

- Keep existing file names and paths so links and the user's bookmarks survive; fix titles/headings inside the file instead. Rename only if the user asks.
- Preserve manual additions (content without a source basis that was not written by this workflow — if unsure, keep it).
- Never delete a note automatically. Content duplicated by this workflow's own earlier output may be removed when the rewritten note covers it.
- After rewriting, check that every `[[link]]` and `[[Note#Heading]]` you introduced resolves (see the link-check script in the standards).

## 6. Manifest and publish

Follow [manifest rules](references/sync-manifest.md): update per-file records (status, timestamps, page coverage, normalizations, TODOs), keep manifest prose short, review the full diff, and commit notes + manifest together with a message such as `notes: process Goodnotes files from YYYY-MM-DD` (or `notes: reorganize … ` for a re-organization run). Push without force; verify the remote contains the commit.

## 7. Report

Report concisely: folder checked and counts, sources read (page counts, pages inspected, method), notes created/rewritten, TODOs needing the user's review (with page), sources left pending and why, and the commit hash/branch.
