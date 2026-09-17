"""
DSA Streak Runner & Progression Manager
Automates daily LeetCode practice, tracks streak, renders README dashboard,
and commits/pushes to GitHub for the daily contribution green dot.
"""

import sys
import os
import json
import datetime
import shutil
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM_PATH = os.path.join(REPO_ROOT, "data", "curriculum.json")
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")
README_PATH = os.path.join(REPO_ROOT, "README.md")


def get_git_executable():
    """Find git executable across standard paths."""
    git_cmd = shutil.which("git")
    if git_cmd:
        return git_cmd
    candidate = r"C:\Users\Divya\AppData\Local\Programs\Git\cmd\git.exe"
    if os.path.exists(candidate):
        return candidate
    return "git"


def run_git(args, check=True):
    """Execute git commands."""
    git_bin = get_git_executable()
    cmd = [git_bin] + args
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Git command failed: {' '.join(cmd)}")
        print(result.stderr)
        raise RuntimeError(f"Git failed: {result.stderr}")
    return result


def load_curriculum():
    """Load curriculum database."""
    if not os.path.exists(CURRICULUM_PATH):
        raise FileNotFoundError(f"Curriculum not found at {CURRICULUM_PATH}")
    with open(CURRICULUM_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_curriculum(data):
    """Save curriculum database."""
    with open(CURRICULUM_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_next_problem():
    """Find the next unsolved problem in the roadmap."""
    data = load_curriculum()
    for item in data["roadmap"]:
        if not item.get("completed", False):
            return item
    return None


def mark_completed(day_id, solution_folder):
    """Mark a problem as solved, calculate streak, update history."""
    data = load_curriculum()
    today_str = datetime.date.today().isoformat()
    
    matched = None
    for item in data["roadmap"]:
        if item["id"] == day_id:
            item["completed"] = True
            item["date_solved"] = today_str
            item["folder"] = solution_folder
            matched = item
            break
            
    if not matched:
        raise ValueError(f"Problem id {day_id} not found in roadmap.")
        
    last_date = data.get("last_solved_date")
    if last_date:
        last_dt = datetime.date.fromisoformat(last_date)
        today_dt = datetime.date.fromisoformat(today_str)
        diff = (today_dt - last_dt).days
        if diff == 1:
            data["current_streak"] = data.get("current_streak", 0) + 1
        elif diff == 0:
            pass
        else:
            data["current_streak"] = 1
    else:
        data["current_streak"] = 1
        
    data["last_solved_date"] = today_str
    data["current_day"] = sum(1 for x in data["roadmap"] if x.get("completed"))
    
    if not any(h.get("id") == day_id for h in data.get("history", [])):
        data.setdefault("history", []).append({
            "day": matched["id"],
            "date": today_str,
            "title": matched["title"],
            "difficulty": matched["difficulty"],
            "topic": matched["topic"],
            "folder": solution_folder
        })
        
    save_curriculum(data)
    render_readme(data)
    return matched


def render_readme(data=None):
    """Generate professional README dashboard with badges and solved log."""
    if data is None:
        data = load_curriculum()
        
    total_problems = len(data["roadmap"])
    solved_problems = [p for p in data["roadmap"] if p.get("completed")]
    solved_count = len(solved_problems)
    
    easy_count = sum(1 for p in solved_problems if p["difficulty"] == "Easy")
    med_count = sum(1 for p in solved_problems if p["difficulty"] == "Medium")
    hard_count = sum(1 for p in solved_problems if p["difficulty"] == "Hard")
    streak = data.get("current_streak", 0)
    
    total_easy = sum(1 for p in data["roadmap"] if p["difficulty"] == "Easy")
    total_med = sum(1 for p in data["roadmap"] if p["difficulty"] == "Medium")
    total_hard = sum(1 for p in data["roadmap"] if p["difficulty"] == "Hard")
    
    table_rows = []
    for item in solved_problems:
        day_num = item["id"]
        date_val = item.get("date_solved", "Today")
        title = item["title"]
        diff = item["difficulty"]
        if diff == "Easy":
            diff_badge = "🟢 Easy"
        elif diff == "Medium":
            diff_badge = "🟡 Medium"
        elif diff == "Hard":
            diff_badge = "🔴 Hard"
        else:
            diff_badge = diff
            
        topic = item["topic"]
        folder = item.get("folder", f"solutions/Day-{day_num:03d}_{item['slug']}")
        lc_id = item.get("leetcode_id", "")
        lc_link = f"https://leetcode.com/problems/{item['slug']}/"
        row = f"| Day {day_num:02d} | `{date_val}` | [#{lc_id} {title}]({lc_link}) | {diff_badge} | {topic} | [View Solution]({folder}/) |"
        table_rows.append(row)
        
    table_content = "\n".join(table_rows) if table_rows else "| - | - | *No problems logged yet* | - | - | - |"
    
    content = f"""# 🚀 Daily DSA Journey (Beginner to Advanced)

Welcome to my daily Data Structures & Algorithms (DSA) progression repository.
Every single day, one curated problem is solved from foundational basics to advanced mastery, keeping skills sharp and the GitHub contribution graph green! 🟩

---

## 📊 Streak & Progress Dashboard

<div align="center">

| 🔥 Current Streak | 🏆 Solved / Total | 🟢 Easy | 🟡 Medium | 🔴 Hard |
| :---: | :---: | :---: | :---: | :---: |
| **{streak} Day(s)** | **{solved_count} / {total_problems}** | **{easy_count} / {total_easy}** | **{med_count} / {total_med}** | **{hard_count} / {total_hard}** |

</div>

---

## 🗺️ Curriculum Roadmap

The problem set follows a curated Beginner-to-Advanced trajectory (Arrays → Two Pointers → Sliding Window → Stack → Binary Search → Linked Lists → Trees → Graphs → Dynamic Programming):

1. **Arrays & Hashing** (Foundational Easy & Medium)
2. **Two Pointers & Sliding Window** (Linear Algorithms)
3. **Stack & Binary Search** (Logarithmic & Monotonic Patterns)
4. **Linked List, Trees & Heaps** (Non-linear Data Structures)
5. **Backtracking & Graphs** (Exhaustive & Network Traversal)
6. **1D & 2D Dynamic Programming** (Optimization & State Machines)
7. **Intervals, Greedy, Geometry & Bit Manipulation** (Advanced Techniques)

---

## 📅 Daily Problem Log

| Day | Date | Problem | Difficulty | Topic | Solution |
| :---: | :---: | :--- | :---: | :--- | :---: |
{table_content}

---

## 📁 College Assignments

All earlier laboratory assignments are preserved in the [`college-labs/`](college-labs/) directory:
- Labs 1 through 8 (Data Structures and Algorithms lab coursework)

---

<div align="center">
  <sub>Generated automatically via Antigravity Daily DSA Workflow. Keep the streak alive! 🔥</sub>
</div>
"""
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated README.md dashboard with {solved_count} solved problem(s).")


def git_commit_and_push(day_id, title, difficulty):
    """Stage, commit, and push changes to GitHub remote."""
    today_str = datetime.date.today().isoformat()
    msg = f"feat(dsa): Day {day_id:02d} - {title} ({difficulty}) [{today_str}]"
    
    print("Staging changes...")
    run_git(["add", "."])
    
    print(f"Committing: {msg}")
    run_git(["commit", "-m", msg])
    
    print("Pushing to GitHub (origin main)...")
    res = run_git(["push", "origin", "main"])
    print("Successfully pushed to GitHub! Green dot contribution registered! 🟩")
    return res


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "status"
    
    if action == "status":
        curr = load_curriculum()
        nxt = get_next_problem()
        solved = sum(1 for p in curr["roadmap"] if p.get("completed"))
        print(f"Current Streak: {curr.get('current_streak', 0)} days")
        print(f"Total Solved: {solved} / {len(curr['roadmap'])}")
        if nxt:
            print(f"Next Up: Day {nxt['id']} - {nxt['title']} ({nxt['difficulty']}) [{nxt['topic']}]")
        else:
            print("All problems in curriculum completed!")
            
    elif action == "next":
        nxt = get_next_problem()
        if nxt:
            print(json.dumps(nxt))
        else:
            print("null")
            
    elif action == "render":
        render_readme()
        
    elif action == "complete":
        if len(sys.argv) < 3:
            print("Usage: dsa_runner.py complete <day_id> <folder>")
            sys.exit(1)
        day = int(sys.argv[2])
        folder = sys.argv[3]
        item = mark_completed(day, folder)
        print(f"Marked Day {day}: {item['title']} as completed!")
        
    elif action == "push":
        if len(sys.argv) < 5:
            print("Usage: dsa_runner.py push <day_id> <title> <difficulty>")
            sys.exit(1)
        day = int(sys.argv[2])
        title = sys.argv[3]
        diff = sys.argv[4]
        git_commit_and_push(day, title, diff)