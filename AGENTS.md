# Agent guide

Study-notes site built from raw YouTube transcripts of the channel "The Anchor Of Life With Brajesh Gautam" (Hindi/Hinglish astrology and self-inquiry). Any cloud agent or session can pick up work from this file alone.

## Source of truth: the raw transcripts

- `transcripts/` holds 466 untouched `.txt` files, one per video. Never edit them. Notes must be written from these files, read in full.
- File name ends with the YouTube video id in brackets: `... [qCGLzTPuf_8].txt`. Names contain Hindi, spaces, `#` and emoji, so always look files up by video id (`ls transcripts | grep 'qCGLzTPuf_8'`) or through the manifests below.
- Layout of each file: line 1 title, line 2 URL, line 3 duration, line 4 source (YouTube auto-captions or Whisper), then lines like `[HH:MM:SS] text`. Captions are noisy. Omit or hedge anything garbled. Never guess a Hindi term.
- `INDEX.md` / `index.csv`: every video with minutes, words, link.
- `STATUS.csv`: the Jyotish Vidya series (36 videos), with transcript path, `done|todo`, and the published page. Regenerate with `python3 tools/make_status.py`.

## What to build

One technical notes page per Jyotish Vidya episode: planets, houses, signs, problem -> cause -> remedy, concrete remedies, speaker opinions marked, SVG diagrams, and a `{{t:HH:MM:SS}}` timestamp link on nearly every bullet so a reader can verify against the video. Quality target: `docs/notes/rahu-and-remedies-jyotish-vidya-ep27.html`.

Todo (see `STATUS.csv`): Ep 1, 2, 3, 4, 5, 6 (parts 1 and 2), 8 (parts 1 and 2), 11. Two-part episodes get one page, both videos, timestamps linked to the right part.

Full step-by-step brief: `tools/AGENT_BRIEF.md`. Pipeline: `tools/build.py epNN.json` (see an existing `tools/epNN.json`, `epNN_sections/`, `epNN_diagrams.py`, `diagrams.py`).

## Rules

- Read the whole transcript by hand in chunks (about 100 lines). No summarising scripts.
- Mark the speaker's opinions on religion, politics, communities, health, fertility, legal and money as his own. No medicine or herb dosing. Do not endorse claims. Do not repeat names of public figures.
- No em dashes, no emojis, in files or messages.
- Never delete with `rm`; use the system trash.
- Do not commit `tools/__pycache__/`.
- Commit messages: plain, no co-author or AI attribution trailers.
- One commit per episode: `Add Ep. NN <Title> notes`, then `git pull --rebase origin main && git push origin main`.
- Only the orchestrator edits `docs/index.html` and `README.md` (a card and a line per new page), then regenerates `STATUS.csv`.
- Verify after publishing: the live URL returns 200, 200+ `class="ts"` links, 5 figures, zero em dashes.

Site: https://codersacademy006.github.io/astro-notes/
