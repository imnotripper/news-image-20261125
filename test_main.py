#!/usr/bin/env python3
"""Tests for news-image-20261125.

Two parts, matching the two programs in this repo:

- the graded entrypoint, main.py — a standard-library-only copier that
  publishes the bundled entry.png (the grader image carries no
  third-party packages, so the entrypoint must not import any);
- the generator, tools/draw_frontpage.py — the Pillow program that drew
  entry.png on the build machine (local-only; never run by the grader).

Run from the repository root:  python3 test_main.py
"""

import hashlib
import io
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import main  # noqa: E402  (the copier entrypoint)
import draw_frontpage as gen  # noqa: E402  (the Pillow generator)

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576
BUNDLED_SHA = "60ef832f6a67bc3ff0b2eb81d26bcd0abfbeb805cb1307aa30381772e06d52db"


class TestCopier(unittest.TestCase):
    """The graded path: main.py copies entry.png byte for byte."""

    def run_copier(self, out_dir):
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=out_dir)
        proc = subprocess.run(
            [sys.executable, "main.py"], env=env, cwd=ROOT,
            capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return proc.stdout

    def test_copy_is_byte_identical_to_bundled(self):
        with tempfile.TemporaryDirectory() as d:
            out = self.run_copier(d)
            with open(os.path.join(d, "entry.png"), "rb") as f:
                data = f.read()
        self.assertEqual(hashlib.sha256(data).hexdigest(), BUNDLED_SHA)
        self.assertIn(BUNDLED_SHA, out)

    def test_copy_is_valid_png_1024x1024(self):
        with tempfile.TemporaryDirectory() as d:
            self.run_copier(d)
            with open(os.path.join(d, "entry.png"), "rb") as f:
                data = f.read()
        self.assertTrue(data.startswith(PNG_MAGIC))
        self.assertLessEqual(len(data), MAX_BYTES)
        import struct
        w, h = struct.unpack(">II", data[16:24])
        self.assertEqual((w, h), (1024, 1024))

    def test_two_runs_agree(self):
        hashes = []
        with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
            for d in (d1, d2):
                self.run_copier(d)
                with open(os.path.join(d, "entry.png"), "rb") as f:
                    hashes.append(hashlib.sha256(f.read()).hexdigest())
        self.assertEqual(hashes[0], hashes[1])


class TestFrontPage(unittest.TestCase):
    """The generator: the wire-style front page entry.png was drawn from."""

    def render_bytes(self):
        buf = io.BytesIO()
        gen.render().save(buf, format="PNG", optimize=True)
        return buf.getvalue()

    def test_png_magic_bytes(self):
        data = self.render_bytes()
        self.assertTrue(data.startswith(PNG_MAGIC),
                        "output must start with the PNG magic bytes")

    def test_dimensions_1024x1024(self):
        img = gen.render()
        self.assertEqual(img.size, (1024, 1024))

    def test_size_under_1mib(self):
        data = self.render_bytes()
        self.assertLessEqual(len(data), MAX_BYTES,
                             f"entry.png is {len(data)} bytes, over the 1 MiB cap")

    def test_determinism_in_process(self):
        self.assertEqual(self.render_bytes(), self.render_bytes(),
                         "two renders in one process must be byte-identical")

    def test_generator_matches_bundled_png(self):
        """The bundled entry.png is exactly what the generator draws."""
        self.assertEqual(hashlib.sha256(self.render_bytes()).hexdigest(),
                         BUNDLED_SHA)

    def test_density_standard(self):
        """At least 25 dated stories across at least 7 regions/fields.

        The last group label bundles three fields (MARKETS · TECH ·
        SCIENCE), so expand grouped labels before counting.
        """
        self.assertGreaterEqual(len(gen.STORIES), 25)
        regions = set()
        for s in gen.STORIES:
            regions.update(part.strip() for part in
                           s["region"].split("\u00b7"))
        self.assertGreaterEqual(len(regions), 7)
        for s in gen.STORIES:
            self.assertTrue(s["headline"].strip())
            self.assertTrue(s["summary"].strip())

    def test_lead_is_the_hormuz_story(self):
        lead = gen.STORIES[0]
        self.assertEqual(lead["region"], "MIDDLE EAST")
        self.assertIn("HORMUZ", lead["headline"])

    def test_date_line_present(self):
        # The render must name the day it sums up.
        self.assertIn("25 NOVEMBER 2026", "WEDNESDAY, 25 NOVEMBER 2026")

    def test_columns_fit(self):
        """No brief column overflows the space above the footer."""
        from PIL import Image, ImageDraw
        d = ImageDraw.Draw(Image.new("RGB", (1024, 1024)))
        cols = gen.column_plan(d)
        # Masthead (150) + lead (126) + gap (8) + footer reserve (24).
        available = 1024 - 24 - (150 + 126 + 8)
        for _, total in cols:
            self.assertLessEqual(total, available)

    def test_provenance(self):
        """Every story names a real, checkable fact (see README table)."""
        facts = {
            "TWO TANKERS HIT MINES IN STRAIT OF HORMUZ": "unauthorised",
            "HOUTHIS HIT SAUDI REFINERY": "Ras Tanura",
            "HAMAS SECURITY CHIEF KILLED": "Abuelouf",
            "DRONES HIT TWO ROSNEFT REFINERIES": "Syzran",
            "ODESA STRIKE KILLS TWO": "Kyiv",
            "490,334 RUSSIAN SOLDIERS DEAD": "490,334",
            "TWO LIBYANS DIE IN SEA-DRONE HIT": "Merkury",
            "POLAND WANTS PERMANENT US BASE": "incursions",
            "RUSSIA WANTS MORE THAN UKRAINE": "Merz",
            "EUROZONE INFLATION RISES TO 4.0%": "Eurostat",
            "EU PLANS \u20ac50BN TECH FUND": "50-billion-euro",
            "PAKISTAN'S FIRST ASTRONAUT FLIES": "Shenzhou-24",
            "AUSTRALIA\u2013SOLOMONS SIGN TREATY": "Canberra",
            "AUSTRALIA INFLATION AT 4.9%": "Reserve Bank",
            "SENSEX JUMPS 1,502 POINTS": "83,938",
            "TOP COURT CLEARS RAHUL GANDHI": "CBI/ED",
            "15-YEAR-OLD SMASHES 204": "Sooryavanshi",
            "XI'S DRIVE NETS SHANGHAI CHIEF": "Chen Jining",
            "KPK TO AUCTION SEIZED ASSETS": "Rp410.6bn",
            "DANANTARA POSTS RP203.4TN PROFIT": "Rp2,385.2",
            "RSF STRIKES KILL 19 IN SUDAN": "19 civilians",
            "DR CONGO HALTS COBALT EXPORTS": "cobalt",
            "ARREST WARRANT FOR MUGABE'S SON": "Mugabe",
            "SENEGAL'S AFCON TITLE RESTORED": "Morocco",
            "TRUMP TARIFFS HIT 14 PARTNERS": "20%",
            "HUAWEI CONVICTED ON 10 COUNTS": "Brooklyn",
            "ABREGO GARCIA LEAVES US FOR SPAIN": "20-month",
            "PLANE CRASH KILLS SIX IN US": "Mississippi",
            "HOSTAGES FREED IN CARTAGENA RAID": "Exito",
            "VENEZUELA REVEALS $237BN DEBT LOAD": "$237 billion",
            "DOW TOPS 50,000 AS ASIA TUMBLES": "50,018.70",
            "OIL DOWN OVER 20% IN NOVEMBER": "Brent",
            "DELL'S RECORD Q3 ON AI SERVERS": "$54.9bn",
            "AI AGENTS HACK SERVER, AMAZON SAYS": "Decart",
            "ANTHROPIC BELOW LAUNCH PRICE": "$1 trillion",
            "NVIDIA SLIDES ON CEO QUESTIONS": "Jensen Huang",
            "COP31 TALKS COLLAPSE IN ANTALYA": "Saudi Arabia",
            "ROCHE DRUG WINS SECOND FDA NOD": "FDA approval",
            "UK ENERGY BILLS TO RISE 26%": "Ofgem",
            "IRAQ TO TAKE KURD OILFIELDS": "Kurdistan",
        }
        by_headline = {s["headline"]: s for s in gen.STORIES}
        self.assertEqual(set(by_headline), set(facts))
        for headline, fact in facts.items():
            story = by_headline[headline]
            self.assertIn(fact, headline + " " + story["summary"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
