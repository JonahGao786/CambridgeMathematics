# Manifest and publication rules

## Location and shape

The manifest lives at `.sync/goodnotes-manifest.json` (keep an existing location/schema; extend conservatively). It holds **per-file facts**, keyed by Drive file ID. Policies belong in this skill, not in the manifest — keep top-level prose fields short and do not add new essay-length fields.

Per-file record:

```json
{
  "drive_file_id": "…",
  "source_file_name": "Ch.2 Vectors.pdf",
  "source_url": "https://drive.google.com/file/d/…/view",
  "drive_folder_path": "GoodNotes/Part IA/Vectors and Matrices",
  "observed_source_modified_timestamp": "…",
  "processed_source_modified_timestamp": "…",
  "status": "processed | pending | skipped_non_study | not_in_current_inventory",
  "classification": "study_material | non_study",
  "material_type": "lecture notes | problem sheet | handwritten attempts | …",
  "course": "Part IA Vectors and Matrices",
  "markdown_paths": ["…"],
  "total_page_count": 29,
  "visually_inspected_pages": "1-29",
  "page_hashes": ["<20-hex per page, from scripts/pagediff.py hash>", "..."],
  "normalizations": ["p. 6: (x-2)(x-5) → (x-3)"],
  "unresolved_todos": ["p. 12: …"],
  "pending_reason": null
}
```

Existing extra fields may stay; update the ones that change.

## Status rules

- `processed_source_modified_timestamp` advances only when every page of that version was visually read and the note was published.
- Failed downloads, unread pages or missing essential diagrams → `pending` with `pending_reason` naming the failed operation; partial page coverage is recorded honestly.
- Files absent from the current Drive listing → `not_in_current_inventory`; keep their notes.
- Duplicate-looking files keep separate records even if they share a note.
- Record the run in a short `last_run` object: date, scope, sources read, sources pending, commit message.

## Review and commit

1. Review the full diff: mathematics, Markdown validity, TikZ blocks closed, tables intact.
2. Run the link check from the note standards; fix every missing note or heading anchor you introduced.
3. Commit only notes, the manifest, and (when the user asked) the skill files. Never commit PDFs, rendered pages, previews or an `Attachments/` folder; honor `.gitignore`.
4. Message: `notes: process Goodnotes files from YYYY-MM-DD` (sync) or `notes: reorganize <scope> (YYYY-MM-DD)` (re-organization).
5. Push without force to the target branch (default branch unless the session names one). If the branch moved, fetch, reconcile conservatively, retry.
6. Confirm the remote contains the commit before reporting success.
7. If nothing needs changing, make no commit and say why.


`page_hashes` (one entry per page of the processed PDF) lets the next run view only new or changed pages (`scripts/pagediff.py diff`). Update it on every processed run; `visually_inspected_pages` then lists the pages actually viewed, with a note that the rest matched the baseline.
