"""
Comprehensive Test Suite Runner
Runs unit tests for all completed solutions across the DSA curriculum.
"""

import os
import sys
import subprocess
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")


def run_all_tests():
    solution_dirs = sorted([
        d for d in os.listdir(SOLUTIONS_DIR)
        if os.path.isdir(os.path.join(SOLUTIONS_DIR, d)) and d.startswith("Day-")
    ])

    print(f"==================================================")
    print(f"🚀 Running DSA Test Suite ({len(solution_dirs)} Problems)")
    print(f"==================================================")

    passed = 0
    failed = 0
    total_start = time.time()

    for idx, folder in enumerate(solution_dirs, 1):
        sol_path = os.path.join(SOLUTIONS_DIR, folder, "solution.py")
        if not os.path.exists(sol_path):
            print(f"[{idx:02d}/{len(solution_dirs)}] ⚠️  {folder}: Missing solution.py")
            continue

        start = time.time()
        res = subprocess.run([sys.executable, sol_path], capture_output=True, text=True)
        elapsed = (time.time() - start) * 1000

        if res.returncode == 0:
            passed += 1
            print(f"[{idx:02d}/{len(solution_dirs)}] ✅ {folder:<50} ({elapsed:.1f}ms)")
        else:
            failed += 1
            print(f"[{idx:02d}/{len(solution_dirs)}] ❌ {folder} FAILED:")
            print(res.stderr)

    total_time = time.time() - total_start
    print(f"==================================================")
    print(f"🎯 Results: {passed} Passed, {failed} Failed | Total Time: {total_time:.2f}s")
    print(f"==================================================")

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
