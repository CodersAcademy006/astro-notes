Task: build GitHub Pages study notes for the "ASAP" series, a second technical talk series by the same channel, "The Anchor Of Life With Brajesh Gautam". Same rules as tools/AGENT_BRIEF.md (read AGENTS.md and AGENT_BRIEF.md first, they are binding). This file only adds the ASAP-specific naming convention and video list, since AGENT_BRIEF.md was written for the numbered Jyotish Vidya series.

The 13 transcripts (14 videos, Ep.10 is two parts) are in transcripts/, titled "EP N ASAP - ...":

- EP 1 — Consciousness vs Kundli (opener) — eRjwFBaBJzc
- EP 2 — Sun — MCX9ftn2vO4
- EP 3 — Moon — UhLy_wG5Udc
- EP 4 — Mars — czrROae2_DA
- EP 5 — Mercury — uqY50BoDoHE
- EP 6 — Jupiter — NHmKAxgFAhg
- EP 7 — Venus — MI5B0YN29JQ
- EP 8 — Saturn — 68gaGMxkZcY
- EP 9 — Rahu — QIMCfGO3GNM
- EP 10 — Ketu, two parts, ONE page — _0f4gz1oweA (Part-1), GjvVnFjohZY (Part-2)
- EP 11 — Uranus — 4BaOPgrFoUE
- EP 12 — Neptune — ZvLNSuqhcno

Naming convention (parallel to the Jyotish Vidya "-jyotish-vidya-epNN" suffix, kept distinct so the two series never collide):
- Page: docs/notes/<slug>-asap-epNN.html, e.g. docs/notes/mars-asap-ep4.html, docs/notes/ketu-asap-ep10.html, docs/notes/consciousness-vs-kundli-asap-ep1.html.
- Tool files: tools/asapNN.json, tools/asapNN_diagrams.py, tools/asapNN_sections/pK.html (same build.py pipeline, same CSS classes, same helpers in diagrams.py).
- Commit message: "Add ASAP Ep. NN <Title> notes" (no attribution trailer, per AGENTS.md).

Quality bar and structural template: same as AGENT_BRIEF.md — study tools/ep28.json / tools/ep28_diagrams.py / tools/ep28_sections/*.html / tools/build.py / tools/diagrams.py, and for the two-part Ep.10 study tools/ep9.json or tools/ep10.json for how a two-part page handles two video ids.

Tracking: there is no ASAP_STATUS.csv yet. Do not create or edit one and do not touch STATUS.csv (that is the Jyotish Vidya series' own tracker) — report your per-episode results in your final message instead; the orchestrator will fold them into tracking once all ASAP batches land.

Do NOT edit docs/index.html or README.md (orchestrator-only). Do NOT touch Jyotish Vidya or standalone files. No rm (use trash). No em dashes, no emojis. No sub-agents.
