"""Regenerate STATUS.csv: one row per Jyotish Vidya video, with transcript path and notes-page status."""
import csv, glob, os, re
root = os.path.join(os.path.dirname(__file__), "..")
pages = {}
for p in glob.glob(os.path.join(root, "docs/notes/*-jyotish-vidya-ep*.html")):
    pages.setdefault(int(re.search(r"-ep(\d+)(?:-pt\d+)?\.html$", p).group(1)), []).append(os.path.relpath(p, root))
rows = []
for f in sorted(os.listdir(os.path.join(root, "transcripts"))):
    m = re.match(r"Jyotish Vidya - Ep\. (\d+)(?: \(Part-(\d)\))?", f)
    if m:
        ep, part = int(m[1]), m[2] or ""
        vid = re.search(r"\[([^\]]+)\]\.txt$", f)[1]
        pg = pages.get(ep, [])
        rows.append([ep, part, vid, "transcripts/" + f, "done" if pg else "todo", ";".join(pg)])
rows.sort(key=lambda r: (r[0], r[1]))
with open(os.path.join(root, "STATUS.csv"), "w", newline="") as o:
    w = csv.writer(o); w.writerow(["ep", "part", "video_id", "transcript", "notes", "page"]); w.writerows(rows)
print(len(rows), "videos;", sum(r[4] == "todo" for r in rows), "todo")
