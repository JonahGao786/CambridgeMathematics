#!/usr/bin/env python3
"""Per-page content hashes, so only new or changed pages need to be viewed.

  pagediff.py hash PDF                  # JSON list of page hashes (render at 100 dpi, grayscale, SHA-256 of pixels)
  pagediff.py diff PDF MANIFEST FILE_ID # compare with files[FILE_ID].page_hashes in the manifest
  pagediff.py diff PDF MANIFEST FILE_ID --render OUTDIR   # also render the pages to view (130 dpi PNG)

Pages are matched by hash, not by index, so a page inserted in the middle is reported as one new page
and the pages after it as unchanged (with their new numbers). Needs poppler's pdftoppm.
"""
import hashlib, json, subprocess, sys, tempfile, pathlib

def hashes(pdf):
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["pdftoppm", "-r", "100", "-gray", pdf, d + "/p"], check=True, stderr=subprocess.DEVNULL)
        return [hashlib.sha256(f.read_bytes()).hexdigest()[:20] for f in sorted(pathlib.Path(d).glob("p-*.pgm"))]

if __name__ == "__main__":
    cmd, pdf = sys.argv[1], sys.argv[2]
    new = hashes(pdf)
    if cmd == "hash":
        print(json.dumps(new))
    else:
        rec = json.load(open(sys.argv[3]))["files"][sys.argv[4]]
        old = rec.get("page_hashes")
        if not old:
            print(f"no baseline: view all {len(new)} pages"); sys.exit(0)
        seen = set(old)
        changed = [i + 1 for i, h in enumerate(new) if h not in seen]
        gone = [i + 1 for i, h in enumerate(old) if h not in set(new)]
        print(f"pages now {len(new)} (was {len(old)}); VIEW pages: {changed or 'none'}; removed/edited old pages: {gone or 'none'}")
        if "--render" in sys.argv and changed:
            out = sys.argv[sys.argv.index("--render") + 1]; pathlib.Path(out).mkdir(parents=True, exist_ok=True)
            for p in changed:
                subprocess.run(["pdftoppm", "-r", "130", "-png", "-f", str(p), "-l", str(p), pdf, f"{out}/p"], check=True, stderr=subprocess.DEVNULL)
