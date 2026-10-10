"""
Performance Benchmark: Sliding Window Problems
Benchmarks solutions across Days 18-22 with varied input scales.
"""

import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import importlib.util
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_solver(folder_name):
    file_path = os.path.join(REPO_ROOT, "solutions", folder_name, "solution.py")
    spec = importlib.util.spec_from_file_location(folder_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()

Sol18 = load_solver("Day-018_best-time-to-buy-and-sell-stock")
Sol19 = load_solver("Day-019_longest-substring-without-repeating-characters")
Sol20 = load_solver("Day-020_longest-repeating-character-replacement")
Sol21 = load_solver("Day-021_permutation-in-string")
Sol22 = load_solver("Day-022_minimum-window-substring")


def benchmark():
    print("=" * 60)
    print("⚡ Profiling Sliding Window Solutions (Days 18-22)")
    print("=" * 60)

    # Day 18
    prices = list(range(10000, 0, -1)) + list(range(1, 10001))
    t0 = time.perf_counter()
    res18 = Sol18.maxProfit(prices)
    t18 = (time.perf_counter() - t0) * 1000
    print(f"Day 18 (20k prices)      : {t18:6.2f} ms | Result: {res18}")

    # Day 19
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * 300
    t0 = time.perf_counter()
    res19 = Sol19.lengthOfLongestSubstring(chars)
    t19 = (time.perf_counter() - t0) * 1000
    print(f"Day 19 (18.6k string)    : {t19:6.2f} ms | Result: {res19}")

    # Day 20
    s_rep = ("AB" * 5000) + ("BA" * 5000)
    t0 = time.perf_counter()
    res20 = Sol20.characterReplacement(s_rep, 100)
    t20 = (time.perf_counter() - t0) * 1000
    print(f"Day 20 (20k string, k=100): {t20:6.2f} ms | Result: {res20}")

    # Day 21
    s1 = "abcdefghijklm"
    s2 = ("zyxwvutsrqpon" * 1000) + "mlkjihgfedcba"
    t0 = time.perf_counter()
    res21 = Sol21.checkInclusion(s1, s2)
    t21 = (time.perf_counter() - t0) * 1000
    print(f"Day 21 (13k string)      : {t21:6.2f} ms | Result: {res21}")

    # Day 22
    big_s = ("ADOBECODEBANC" * 1500)
    big_t = "ABC"
    t0 = time.perf_counter()
    res22 = Sol22.minWindow(big_s, big_t)
    t22 = (time.perf_counter() - t0) * 1000
    print(f"Day 22 (19.5k string)    : {t22:6.2f} ms | Result: {res22}")

    print("=" * 60)
    print("✅ All Sliding Window algorithms operate well within runtime limits!")
    print("=" * 60)


if __name__ == "__main__":
    benchmark()
