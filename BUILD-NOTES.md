# Build notes — news-image-20261125

## Design brief

**Competition:** news-image-20261125 — "Sum up 25 November's world
news in one image". $100 pot, top 50 paid, pairwise-judged by
z-ai/glm-5.3-flash, which has no news feed and is not told the day.
Deadline 2026-11-27 00:00 UTC (07:00 WIB 27 Nov).

**Approach:** a dense wire-style front page ("The Global Times") drawn
with Pillow — one lead story plus 39 briefs in three columns under
region headers. This follows the winner forensics from the sibling
days: the winning pages carry 29–38 dated stories across 7–9
regions, and the judge can only credit what the image shows, so
density of checkable, dated, specific events is the strategy. The
previous day's entry (news-image-20261124, v2) used the same wire
structure with 20 stories; this one pushes to 40 because the layout
budget allows it at 13/11 pt.

**Rubric angles that decide winning (in judge order):**
1. One day's news, names the day — the masthead date line
   "WEDNESDAY, 25 NOVEMBER 2026" in red, the tagline "40 STORIES,
   EVERY REGION", and the footer "REPORTED 25 NOVEMBER 2026".
2. Selection and breadth — the lead is the day's most consequential
   story (Hormuz tanker mines: shipping, oil, Iran), and the briefs
   span 8 region/field groups with a region strip under the masthead
   so breadth is visible at a glance.
3. Reads — every brief is a headline plus a one- or two-line summary
   a viewer can follow without any other context; no story depends
   on knowing the day from elsewhere.
4. Faithful — every headline and summary is a shortened form of a
   story in `~/workspace/makefun/news25-stories.md` (researched
   25 Nov 2026 ~22:00 WIB from Just Security Early Edition, One
   Turn, Principia, Le Monde, Morningstar/Dow Jones, huddleworld,
   Rajyog Journal). No number, name or quote goes beyond that list;
   where a headline was shortened for one-line fit, the dropped
   detail stays in the summary (e.g. "HAMAS SECURITY CHIEF KILLED"
   keeps "Gaza" and the family deaths in the summary).
5. Craft — one composition, DejaVu text only (no AI image
   generation, which garbles text), fixed palette, rules and
   region-coloured headers; legible at full size and readable at
   ~300 px across for the masthead, date and lead.

## Story selection

All 40 verified stories from news25-stories.md are used — nothing
cut, because the density standard (>=25 stories, >=7 regions) is met
with margin and every story in the list earned its place by being
reported on 25 November 2026. Region/field count: **8** — Middle
East, Europe, Asia–Pacific, Africa, Americas, Markets, Tech,
Science (Sport is the ninth label in the masthead strip, covered by
the AFCON story under Africa). Lead: Hormuz (story 1) — the day's
biggest consequential event, with oil-market and regional-security
reach; it also matches the previous day's lead theme without
repeating its facts.

## Layout decisions

- 1024×1024, masthead 150 px (name 46 pt serif, date 24 pt red,
  tagline + region strip), lead panel 126 px, briefs area to y=1000,
  footer sources line at the bottom.
- Three columns of 13 briefs (314 px each, 16 px gutters). Briefs:
  headline 13 pt bold, one line (headlines shortened to ~32 chars);
  summary 11 pt, at most two lines (~95 chars). Region header
  (12 pt bold, coloured, ruled) wherever the region changes inside
  a column.
- First render overflowed (tallest column 887 px vs 702 available)
  because DejaVu Sans Bold at 14 pt wraps 35+ char headlines to two
  lines. Fixed by dropping to 13/11 pt and shortening every headline
  to one line; final column heights 710 / 697 / 677 px vs 716
  available. The renderer measures every brief and aborts with a
  clear error if a column overflows, so this class of defect cannot
  ship silently.
- First render also left ~90 px of white space above the footer;
  fixed by raising the brief gap from 5 to 9 px, which spreads the
  columns evenly to the footer.

## Verification

- `entry.png`: 1024×1024 PNG, 226,766 bytes (limit 1,048,576).
  SHA-256 `60ef832f6a67bc3ff0b2eb81d26bcd0abfbeb805cb1307aa30381772e06d52db`.
- `python3 test_main.py`: 13 tests, all pass (copier byte-identity,
  PNG magic, dimensions, size cap, determinism, generator == bundled
  PNG, density standard, lead is Hormuz, date line, columns fit,
  provenance facts for all 40 stories).
- `python3 main.py` run against real `/output`: wrote
  `/output/entry.png`, byte-identical to the bundled file (cmp clean).
- Image read visually: masthead, date, lead, all 39 briefs and
  footer legible, no garbled text, no overlapping text, no
  clipped lines.

## Handoff to the parent (bundle + submit)

- The README badge lines use repo name `news-image-20261125`
  (repo name = slug, per the build brief) — create the GitHub repo
  with exactly that name, or the rank/reward badges will 404.
- Nothing is bundled or submitted from this session: the parent runs
  the kit check, bundle (with `--muse-usage`) and submit steps.
- `tools/draw_frontpage.py` is the only file that needs Pillow; the
  graded path (`main.py` + `entry.png`) is stdlib-only.

## Known limits

- At ~300 px across only the masthead, date line, lead and region
  headers stay readable; the brief text is small by design — the
  same trade-off the sibling days' winners make, and the judge is
  shown the full image.
- The entrypoint is a stdlib-only copier (no Pillow in the grader
  image); the generator lives in `tools/` for the build machine.
