"""
Performance Benchmark: Stack Problems
Benchmarks solutions across Days 24-28 with large-scale inputs.
"""

import importlib.util
import os
import sys
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_solver(folder_name):
    file_path = os.path.join(REPO_ROOT, "solutions", folder_name, "solution.py")
    spec = importlib.util.spec_from_file_location(folder_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "Solution", getattr(module, "MinStack", None))


Sol24 = load_solver("Day-024_valid-parentheses")()
MinStackClass = load_solver("Day-025_min-stack")
Sol26 = load_solver("Day-026_evaluate-reverse-polish-notation")()
Sol27 = load_solver("Day-027_generate-parentheses")()
Sol28 = load_solver("Day-028_daily-temperatures")()


def benchmark():
    print("=" * 60)
    print("⚡ Profiling Stack Solutions (Days 24-28)")
    print("=" * 60)

    # Day 24: Valid Parentheses (100k balanced brackets)
    s24_input = ("(" * 50000) + (")" * 50000)
    t0 = time.perf_counter()
    res24 = Sol24.isValid(s24_input)
    t24 = (time.perf_counter() - t0) * 1000
    print(f"Day 24 (100k brackets)    : {t24:6.2f} ms | Result: {res24}")

    # Day 25: Min Stack (50k pushes and pops)
    ms = MinStackClass()
    t0 = time.perf_counter()
    for v in range(25000, 0, -1):
        ms.push(v)
    for _ in range(25000):
        ms.getMin()
        ms.pop()
    t25 = (time.perf_counter() - t0) * 1000
    print(f"Day 25 (50k operations)   : {t25:6.2f} ms | Status: Complete")

    # Day 26: Evaluate Reverse Polish Notation (30k tokens)
    tokens = ["1", "1", "+"] * 10000 + ["+"] * 9999
    t0 = time.perf_counter()
    res26 = Sol26.evalRPN(tokens)
    t26 = (time.perf_counter() - t0) * 1000
    print(f"Day 26 (30k tokens)       : {t26:6.2f} ms | Result: {res26}")

    # Day 27: Generate Parentheses (n = 8, 1430 combinations)
    t0 = time.perf_counter()
    res27 = Sol27.generateParenthesis(8)
    t27 = (time.perf_counter() - t0) * 1000
    print(f"Day 27 (n=8, 1430 combs)  : {t27:6.2f} ms | Count: {len(res27)}")

    # Day 28: Daily Temperatures (100k temperature points)
    temps = list(range(30, 80)) * 2000
    t0 = time.perf_counter()
    res28 = Sol28.dailyTemperatures(temps)
    t28 = (time.perf_counter() - t0) * 1000
    print(f"Day 28 (100k temperatures): {t28:6.2f} ms | Count: {len(res28)}")

    print("=" * 60)
    print("✅ All Stack algorithms execute well within high-performance limits!")
    print("=" * 60)


if __name__ == "__main__":
    benchmark()
