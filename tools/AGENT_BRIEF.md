Task: build GitHub Pages study notes for 3 episodes of the Hindi astrology channel "The Anchor Of Life With Brajesh Gautam", one page per episode, to the same quality as existing pages.

Repo: CodersAcademy006/astro-notes (branch main). Transcripts: transcripts/ in this repo (find by the video id, see STATUS.csv). They are YouTube auto-captions in Hindi/Hinglish, lines like "[HH:MM:SS] text". Read the WHOLE transcript by hand in chunks of ~100 lines with the Read tool (offset/limit). No summarising shortcuts, no scripts that summarise.

Study the existing finished episode first: tools/ep28.json, tools/ep28_diagrams.py, tools/ep28_sections/p1..p5.html, tools/build.py, tools/diagrams.py, and docs/notes/rahu-and-ketu-jyotish-vidya-ep28.html. Copy that structure exactly.

Per episode NN (video id given):
1. After each ~100-line chunk, write a section file tools/epNN_sections/pK.html (sections `<section id="..."><h2>N. Title {{t:HH:MM:SS}}</h2>...`). Use the same CSS classes as ep28: lead, three/card prob|why|fix, box, tablewrap table, ul, op (opinion note). Put {{t:HH:MM:SS}} timestamps on nearly every bullet (build converts them to YouTube links). Cover: planets, houses, signs, problem -> cause -> remedy, concrete remedies, self-checks, Q&A, and a remedy cheat-sheet table plus an "About these notes" section at the end (last file). Mark the speaker's opinions on religion, politics, communities, health, fertility, legal and money claims as his own, with an `op` paragraph. Never include medicine dosing. Do not endorse claims.
2. Write tools/epNN_diagrams.py with 5 diagrams (helpers box/arr/lab/fig from diagrams.py, viewBox width 420, keep box text short: about width/9 characters per line) and a dict D.
3. Write tools/epNN.json (keys vid,title,len,sub,desc,sections_dir,diagrams_module,out,points,puts). out = "../docs/notes/<slug>-jyotish-vidya-epNN.html". Build from the tools dir: `cd tools && python3 build.py epNN.json`. puts anchors must be exact prefixes of lines in your section files.
4. Render the diagrams headless in Chrome to a PNG in your scratch space and look at them; fix any overflowing text.
5. Verify: count of class="ts" links is large (200+), 5 figures, zero em dashes and zero emojis in the output html.
6. Commit ONLY that episode's files (docs/notes page, tools/epNN*), one commit per episode, message "Add Ep. NN <Title> notes". Do NOT add any Co-Authored-By or AI/Claude attribution line anywhere. Then `git pull --rebase origin main && git push origin main`. Retry the pull/push if rejected.

Do NOT: edit docs/index.html or README.md (the orchestrator will); touch other episodes' files; use `rm` (use trash if you must delete); use emojis or em dashes anywhere; invent facts not in the transcript or guess Hindi terms you are unsure of (transcripts have errors, omit rather than guess); include herb or medicine dosing; spawn sub-agents.

When finished, report for each episode: the page path, timestamp count, commit hash, and anything you were unsure of or left out.
