#!/usr/bin/env python3
"""Finite math regressions and active-material link checks for Lessons 5-8.

Run from any directory with Python 3.10+: python3 tools/check_lessons_05_08.py
Finite checks catch regressions; the lesson proofs establish general results.
External URL accessibility is NOT inferred from the local-link check.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import re
import unittest
from urllib.parse import unquote


def distances(points):
    return Counter(abs(a - b) for a, b in combinations(points, 2))


def apply_ops(word, x):
    for op in word:
        if op == "A":
            x = abs(x)
        elif op == "R":
            x = -x
        else:
            raise ValueError(f"Unknown operation: {op}")
    return x


def classify(word):
    if any(op not in "AR" for op in word):
        raise ValueError("Only A and R are valid operations")
    if "A" not in word:
        return "I" if len(word) % 2 == 0 else "R"
    tail = word[word.rfind("A") + 1:]
    return "A" if len(tail) % 2 == 0 else "N"


def connected(n, edges):
    seen = {0}
    while True:
        new = seen | {v for a, b in edges for u, v in ((a, b), (b, a)) if u in seen}
        if new == seen:
            return len(seen) == n
        seen = new


def folded(t, speed, phase=0, length=6):
    q = (phase + speed * t) % (2 * length)
    return q if q <= length else 2 * length - q


class LessonChecks(unittest.TestCase):
    def test_l5_chain_and_erasure(self):
        def ok(s):
            return s[0] == s[1] and s[1] != s[2] and s[2] == s[3] and s[3] != s[4] and s[4] == s[5]
        self.assertEqual(sum(ok(s) for s in product((-1, 1), repeat=6)), 2)
        self.assertEqual(sum(s[0] == s[1] and s[1] != s[2] and s[3] != s[4] and s[4] == s[5]
                             for s in product((-1, 1), repeat=6)), 4)
        edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
        self.assertTrue(all(connected(5, edges[:i] + edges[i+1:]) for i in range(5)))
        for candidate in combinations(list(combinations(range(5), 2)), 4):
            self.assertFalse(all(connected(5, candidate[:i] + candidate[i+1:]) for i in range(4)))

    def test_jmo_2023_b6(self):
        edges = [(0, 1), (1, 2), (2, 3), (3, 0), (2, 4)]
        for colours, expected in ((3, 36), (2, 2)):
            self.assertEqual(sum(all(s[i] != s[j] for i, j in edges)
                                 for s in product(range(colours), repeat=5)), expected)

    def test_l6_order_and_classification(self):
        self.assertEqual(apply_ops("AR", -3), -3)
        self.assertEqual(apply_ops("RA", -3), 3)
        rules = {"I": lambda x: x, "R": lambda x: -x, "A": abs, "N": lambda x: -abs(x)}
        for n in range(10):
            for letters in product("AR", repeat=n):
                word = "".join(letters)
                for x in (Fraction(-7, 3), Fraction(0), Fraction(5, 2)):
                    self.assertEqual(apply_ops(word, x), rules[classify(word)](x))
        self.assertEqual(len({tuple(f(x) for x in (2, -2)) for f in rules.values()}), 4)

    def test_l6_integer_packing(self):
        for count, minimum, expected_count in ((7, 12, 1), (8, 16, 2)):
            candidates = list(combinations(range(-6, 7), count))
            best = min(sum(abs(x) for x in s) for s in candidates)
            optimal = [s for s in candidates if sum(abs(x) for x in s) == best]
            self.assertEqual((best, len(optimal)), (minimum, expected_count))
        nonzero = [x for x in range(-6, 7) if x]
        for count, minimum, expected_count in ((5, 9, 2), (6, 12, 1), (7, 16, 2)):
            values = [sum(abs(x) for x in s) for s in combinations(nonzero, count)]
            self.assertEqual((min(values), values.count(min(values))), (minimum, expected_count))

    def test_jmo_2024_b3_signed(self):
        def possible(n):
            # Fix magnitude 1 to remove rotations from the existence search.
            def walk(path, left):
                if not left:
                    return path[-1] % 2 != 1 and abs(path[-1] - 1) != 1
                for v in left:
                    if v % 2 != path[-1] % 2 and abs(v - path[-1]) != 1:
                        if walk(path + [v], left - {v}):
                            return True
                return False
            return walk([1], set(range(2, n+1)))
        self.assertEqual([n for n in range(2, 9) if possible(n)], [8])
        witness = [-1, 6, -3, 8, -5, 2, -7, 4]
        self.assertTrue(all((a < 0) != (b < 0) and abs(abs(a) - abs(b)) != 1
                            for a, b in zip(witness, witness[1:] + witness[:1])))

    def test_l7_rank_formula(self):
        for k in range(1, 6):
            for multiplicities in product((1, 2), repeat=k):
                for with_zero in (False, True):
                    orders = set()
                    for signs in product((-1, 1), repeat=k):
                        points = []
                        label = 0
                        for r, (m, sign) in enumerate(zip(multiplicities, signs), 1):
                            points.append((sign * r, label))
                            label += 1
                            if m == 2:
                                points.append((-sign * r, label))
                                label += 1
                        if with_zero:
                            points.append((0, label))
                        orders.add(tuple(name for value, name in sorted(points)))
                    exp = k if with_zero or multiplicities[0] == 2 else k - 1
                    self.assertEqual(len(orders), 2 ** exp)
        # Weak absolute-value bound: forward strictness can fail; inverse survives.
        for a, b in product(range(-8, 9), repeat=2):
            if abs(a) <= abs(b) and a < b:
                self.assertGreater(b, 0)
        self.assertFalse(1 < 1)

    def test_amc_2023_p25(self):
        candidates = []
        for a in range(1, 11):
            for d in range(1, 30):
                if 13 <= a+d <= 20 and 241 <= a+14*d <= 250:
                    candidates.append((a, d, a+13*d))
        self.assertEqual(candidates, [(3, 17, 224)])
        variant = [(a, d, a+4*d) for a in range(2, 5) for d in range(1, 20)
                   if 8 <= a+d <= 10 and 33 <= a+5*d <= 35]
        self.assertEqual(variant, [(3, 6, 27), (4, 6, 28)])

    def test_l8_reconstructions(self):
        examples = (
            (9, [2, 3, 4, 5, 7, 9], [(0, 2, 5, 9), (0, 4, 7, 9)]),
            (6, [1, 2, 3, 4, 5, 6], [(0, 1, 4, 6), (0, 2, 5, 6)]),
        )
        for span, ds, expected in examples:
            found = [(0, *inside, span) for inside in combinations(range(1, span), 2)
                     if distances((0, *inside, span)) == Counter(ds)]
            self.assertEqual(found, expected)
        known = Counter([2, 3, 4, 5, 7, 9, 11, 13, 16])
        valid = []
        for inside in combinations(range(1, 16), 3):
            pts = (0, *inside, 16)
            ds = distances(pts)
            if not (known - ds) and sum((ds - known).values()) == 1:
                n = next(iter(ds - known))
                if 1 <= n <= 15:
                    valid.append((pts, n))
        self.assertEqual({n for _, n in valid}, {2, 6, 12})
        self.assertEqual(len(valid), 6)
        # Independently verify the restricted candidate table used in the proof.
        fixed13 = [(0, x, y, 13, 16) for x, y in combinations((2, 4, 5, 7, 9, 11), 2)]
        survivors = [s for s in fixed13 if not (known - distances(s))]
        self.assertEqual(survivors, [(0, 4, 11, 13, 16), (0, 7, 11, 13, 16), (0, 9, 11, 13, 16)])

    def test_homometric_example(self):
        a = (0, 1, 4, 10, 12, 17)
        b = (0, 1, 8, 11, 13, 17)
        self.assertEqual(distances(a), distances(b))
        self.assertEqual(distances(a), Counter(list(range(1, 14)) + [16, 17]))
        self.assertNotEqual(tuple(sorted(17-x for x in a)), b)
        self.assertNotEqual(tuple(y-x for x, y in zip(a, a[1:])), tuple(y-x for x, y in zip(b, b[1:])))

    def test_motion(self):
        meets = [t for t in range(1, 101) if folded(t, 1) == folded(t, 2, 6)]
        self.assertEqual(meets, list(range(2, 101, 4)))
        for steps in range(20):
            left = set(range(-steps, steps+1, 2))
            right = {9+x for x in range(-steps, steps+1, 2)}
            self.assertFalse(left & right)
        vals = [(n, k) for n in range(1, 450) for k in range(n+1) if 5*n-8*k == 2023]
        self.assertEqual(min(vals), (411, 4))
        vals = [(n, k) for n in range(1, 40) for k in range(n+1) if 4*n-7*k == 50]
        self.assertEqual(min(vals), (16, 2))

    def test_distance_sum(self):
        for half in range(-30, 41):
            x = Fraction(half, 2)
            d5 = sum(abs(x-a) for a in (-4, -1, 2, 6, 9))
            self.assertGreaterEqual(d5, 20)
            self.assertEqual(d5 == 20, x == 2)
            d4 = sum(abs(x-a) for a in (-4, -1, 6, 9))
            self.assertGreaterEqual(d4, 20)
            self.assertEqual(d4 == 20, -1 <= x <= 6)

    def test_active_material_link_targets(self):
        root = Path(__file__).resolve().parents[1]
        base = root / "grade-07/semester-1/01-number-system"
        slugs = ("05-absolute-value-part1", "06-absolute-value-part2",
                 "07-rational-number-comparison", "08-number-line-integration")
        files = []
        for slug in slugs:
            files.extend([
                base / f"{slug}.md",
                base / "exercises" / f"{slug}-homework.md",
                base / "solutions" / f"{slug}-classroom.md",
                base / "solutions" / f"{slug}-homework.md",
                base / "solutions" / f"{slug}-ceiling-v2.4.md",
                base / "sources" / f"{slug}-provenance.md",
                base / "diagnostics" / f"{slug}-habits.md",
                base / "reviews" / f"{slug}-release-review-v2.4.md",
            ])
        files.extend([root / "README.md", root / "docs/standards/CURRENT.md",
                      root / "grade-07/semester-1/README.md",
                      root / "docs/audits/lessons-05-08-v2.4-remediation-2026-09-15.md"])
        for path in files:
            with self.subTest(file=str(path.relative_to(root))):
                self.assertTrue(path.is_file(), f"Missing course component: {path}")
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                    if target.startswith(("http://", "https://", "mailto:", "#")):
                        continue
                    local = unquote(target.split("#", 1)[0].split("?", 1)[0])
                    self.assertTrue((path.parent / local).exists(), f"Broken local link: {path}: {target}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
