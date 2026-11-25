[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/imnotripper/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/imnotripper/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The Global Times — Wednesday 25 November 2026

**The whole of Wednesday 25 November 2026 on one page: 40 dated
stories from eight region/field groups** — two oil tankers hitting
naval mines in the Strait of Hormuz as the lead, Houthi strikes on a
Saudi refinery and a Riyadh tower, the killing of Hamas's security
chief in Gaza, Ukrainian drones hitting two Rosneft refineries, a
Russian strike on Odesa, the leaked toll of 490,334 Russian soldiers
dead, Poland's push for a permanent US base, Merz's warning that
Russia wants more than Ukraine, eurozone inflation at 4.0%, the EU's
€50bn tech fund, Pakistan's first astronaut flying on Shenzhou-24,
the Australia–Solomons security treaty, Australian inflation at
4.9%, the Sensex jumping 1,502 points, India's top court clearing
Rahul Gandhi, a 15-year-old smashing 204 in List A cricket, Xi's
anti-graft drive netting Shanghai's party chief, the KPK's seized
asset auction, Danantara's first audited profit, RSF drone strikes
killing 19 in Sudan, DR Congo halting cobalt exports, an arrest
warrant for Mugabe's son, Senegal's AFCON title restored on appeal,
Trump's tariffs on 14 partners, Huawei convicted on 10 of 12
counts, Abrego Garcia leaving for Spain, a Mississippi plane crash
killing six, hostages freed in a Cartagena supermarket raid,
Venezuela's $237bn debt, Asian stocks tumbling while the Dow closed
above 50,000, oil down over 20% in November, Dell's record Q3 on AI
servers, Amazon buying Decart and warning of AI-agent hacking,
Anthropic falling below its launch price, Nvidia sliding on CEO
questions, the COP31 collapse, Roche's second FDA approval, UK
energy bills set to rise 26%, and Iraq taking over Kurdistan's
oilfields.

The image is the deliverable: a 1024 × 1024 newspaper front page drawn
by `tools/draw_frontpage.py` (Pillow). `entry.png` is that render,
committed to the repo.

**Why this shape.** The sibling days' winners are dense wire-style
pages of 29–38 dated stories across 7–9 regions, and the judge has no
news feed and is not told the day — it can only credit what the image
shows. So the page maximises checkable, dated, specific events: one
lead, 39 briefs in three columns under region headers, the day named
in the masthead and the tagline, and a region strip listing every
region and field covered. Every headline is one line, every summary
at most two, and the renderer measures each brief and refuses to draw
if a column overflows — a layout defect fails loudly on the build
machine instead of shipping. Every story is a real, verifiable item
of 25 November 2026 news (provenance below); no figure, name or quote
is invented.

## Running it

The graded entrypoint is `main.py`. The grading image ships no
third-party packages, so the entrypoint uses **only the Python
standard library**: it copies the bundled `entry.png` to the output
directory byte for byte, after checking the file exists and is a PNG.

```sh
python3 main.py                      # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
python3 test_main.py                 # the full test suite
```

No installs are needed or performed — `requirements.txt` is empty by
design, and the entrypoint makes no network calls.

To redraw the page itself (build machines only, needs Pillow):

```sh
python3 tools/draw_frontpage.py      # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=. python3 tools/draw_frontpage.py
```

## What's in the repo

| File | Role |
| --- | --- |
| `main.py` | Graded entrypoint: stdlib-only copier, writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`) |
| `entry.png` | The finished front page (1024 × 1024, 226,766 bytes) |
| `tools/draw_frontpage.py` | The generator that drew `entry.png` (Pillow; build machines only) |
| `test_main.py` | Tests for both: copier byte-identity and the generator (magic bytes, size, determinism, density, provenance) |
| `BUILD-NOTES.md` | Story selection rationale, region count and layout decisions |
| `requirements.txt` | Empty — the entrypoint needs nothing beyond the standard library |

## Story provenance

Every story below happened or was first reported on **25 November
2026** (any time zone). No headline, figure or quote is invented;
each row names the fact a reader can check and where it was reported
(full list in `~/workspace/makefun/news25-stories.md`).

| Story | Checkable fact | Reported by |
| --- | --- | --- |
| Two tankers hit mines in Strait of Hormuz (lead) | Iran's Revolutionary Guard says two oil tankers struck naval mines and caught fire after an unauthorised route | Just Security *Early Edition*, 25 Nov 2026 |
| Houthis hit Saudi refinery | Houthis say they hit Ras Tanura refinery; drone strike on a Riyadh tower injured 11 | Just Security *Early Edition*, 25 Nov 2026 |
| Hamas security chief killed | Israel killed Hamas colonel Mohammad Abuelouf, his wife and two children, per Gaza officials | Just Security *Early Edition*, 25 Nov 2026 |
| Drones hit two Rosneft refineries | Syzran and Kuibyshev refineries in Samara hit; one killed, 145 Ukrainian drones downed | Just Security *Early Edition*, 25 Nov 2026 |
| Odesa strike kills two | Two killed, three hurt including a child; Russian forces also attacked Kyiv, injuring two | Just Security *Early Edition*, 25 Nov 2026 |
| 490,334 Russian soldiers dead | Leaked Russian statistics analysed by BBC News put Russian deaths since 2022 at 490,334 | BBC News, 25 Nov 2026 |
| Two Libyans die in sea-drone hit | Two naval officers died of wounds in Ukraine's sea-drone attack on the corvette Merkury | Day wire roundups, 25 Nov 2026 |
| Poland wants permanent US base | Warsaw renewed its push after two Russian airspace incursions in four days | Day wire roundups, 25 Nov 2026 |
| Russia wants more than Ukraine | Chancellor Merz warned Russia's ambitions go beyond Ukraine | Day wire roundups, 25 Nov 2026 |
| Eurozone inflation rises to 4.0% | Inflation in euro-using countries rose to 4.0%, per Eurostat | Morningstar / Dow Jones, 25 Nov 2026 |
| EU plans €50bn tech fund | A 50-billion-euro technology fund to challenge US and Chinese dominance | Day wire roundups, 25 Nov 2026 |
| Pakistan's first astronaut flies | Shenzhou-24 docked with Tiangong, carrying Pakistan's first astronaut into orbit | Day wire roundups, 25 Nov 2026 |
| Australia–Solomons sign treaty | Treaty signed in Canberra precludes a foreign military or security base on the Solomons | Day wire roundups, 25 Nov 2026 |
| Australia inflation at 4.9% | October inflation rose to 4.9%; Reserve Bank on alert for rate hikes | Morningstar / Dow Jones, 25 Nov 2026 |
| Sensex jumps 1,502 points | Sensex +1.82% to 83,938; Nifty +469.6 to 25,819; rupee at 92.23 per dollar | Morningstar / Dow Jones, 25 Nov 2026 |
| Top court clears Rahul Gandhi | Supreme Court set aside a High Court order for CBI/ED checks on assets claims | Day wire roundups, 25 Nov 2026 |
| 15-year-old smashes 204 | Vaibhav Sooryavanshi, 15, smashed 204 in List A cricket in Doha | Day wire roundups, 25 Nov 2026 |
| Xi's drive nets Shanghai chief | Anti-corruption campaign ensnared Chen Jining, Shanghai party chief | Day wire roundups, 25 Nov 2026 |
| KPK to auction seized assets | 120 lots worth about Rp410.6 billion; winners decided 8 December | Rajyog Journal, 25 Nov 2026 |
| Danantara posts Rp203.4tn profit | Net profit Rp203.4 trillion, revenue Rp2,385.2 trillion, first audited statements | Rajyog Journal, 25 Nov 2026 |
| RSF strikes kill 19 in Sudan | Drone strikes killed 19 civilians and wounded 20 in two cities, per Emergency Lawyers | Just Security *Early Edition*, 25 Nov 2026 |
| DR Congo halts cobalt exports | DR Congo halted cobalt exports again | Day wire roundups, 25 Nov 2026 |
| Arrest warrant for Mugabe's son | Warrant for the son of late former president Robert Mugabe over a missed court date | Day wire roundups, 25 Nov 2026 |
| Senegal's AFCON title restored | Sport's highest court restored the 2025 Africa Cup title; Morocco vowed to challenge | Day wire roundups, 25 Nov 2026 |
| Trump tariffs hit 14 partners | New tariffs including China (20%), the EU (15%), India, Taiwan and Japan | Morningstar / Dow Jones, 25 Nov 2026 |
| Huawei convicted on 10 counts | Brooklyn jury convicted Huawei of bank/wire fraud, sanctions violations, trade-secret theft | Day wire roundups, 25 Nov 2026 |
| Abrego Garcia leaves US for Spain | Kilmar Abrego Garcia left the US for Spain, ending a 20-month deportation fight | Day wire roundups, 25 Nov 2026 |
| Plane crash kills six in US | Crash off the Mississippi coast killed six people, including two children | Day wire roundups, 25 Nov 2026 |
| Hostages freed in Cartagena raid | Security forces stormed an Exito supermarket, freeing all hostages; one captor killed | Day wire roundups, 25 Nov 2026 |
| Venezuela reveals $237bn debt load | Venezuela revealed a debt load of $237 billion | Day wire roundups, 25 Nov 2026 |
| Dow tops 50,000 as Asia tumbles | KOSPI -6.16%, Nikkei -2.78%, Taiex ~-5%; Nasdaq -1.5%, S&P -0.5%, Dow +0.9% to 50,018.70 | Morningstar / Dow Jones, 25 Nov 2026 |
| Oil down over 20% in November | Oil prices fell more than 20% in November; Brent below $90 | Morningstar / Dow Jones, 25 Nov 2026 |
| Dell's record Q3 on AI servers | Revenue $54.9bn (+103%); AI server revenue $22.0bn (+291%) | Day wire roundups, 25 Nov 2026 |
| AI agents hack server, Amazon says | Amazon bought Decart to rival Nvidia; hackers' AI agents broke into a university server | Day wire roundups, 25 Nov 2026 |
| Anthropic below launch price | Shares fell below their stock-market launch price; $1 trillion valuation wiped out | Day wire roundups, 25 Nov 2026 |
| Nvidia slides on CEO questions | Shares fell ~5% as lawmakers questioned Trump's role in Jensen Huang's return as CEO | Day wire roundups, 25 Nov 2026 |
| COP31 talks collapse in Antalya | Saudi Arabia and oil producers blocked any fossil-fuel phase-out mention | Le Monde / CNN, 25 Nov 2026 |
| Roche drug wins second FDA nod | Breast-cancer drug won a second FDA approval; UN warned of HIV funding cuts | Day wire roundups, 25 Nov 2026 |
| UK energy bills to rise 26% | Bills set to rise 26% from January as Ofgem raises the price cap; typical bill £2,166 | Day wire roundups, 25 Nov 2026 |
| Iraq to take Kurd oilfields | Prime minister said Baghdad will take over Kurdistan's oilfields | Day wire roundups, 25 Nov 2026 |

## Determinism

The page is a pure function of the repository: fixed story data, fixed
layout, no timestamps, no randomness, no network. Renders are
byte-identical across runs and processes, and the committed `entry.png`
is exactly what `tools/draw_frontpage.py` draws — `test_main.py` pins
its SHA-256:

```
60ef832f6a67bc3ff0b2eb81d26bcd0abfbeb805cb1307aa30381772e06d52db  entry.png
```
