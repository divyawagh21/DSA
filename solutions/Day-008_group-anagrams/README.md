# Day 08: Group Anagrams

- **Problem Link:** [LeetCode #49 - Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- **Difficulty:** 🟡 Medium
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-25

---

## 📝 Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
```text
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

### Example 2:
```text
Input:  strs = [""]
Output: [[""]]
```

### Example 3:
```text
Input:  strs = ["a"]
Output: [["a"]]
```

### Constraints:
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

---

## 💡 Algorithmic Approaches

### 1. Sort Each Word as Key
- Sort each word alphabetically → anagrams produce the same sorted string.
- Use `tuple(sorted(word))` as the hash map key.
- **Time Complexity:** $O(N \cdot K \log K)$ where $N$ = number of words, $K$ = max word length.
- **Space Complexity:** $O(N \cdot K)$

### 2. Character Frequency Tuple as Key (Optimal) 🚀
- For each word, build a fixed-size array of 26 integers counting character frequencies.
- Convert to a tuple (hashable) to use as the dictionary key.
- All anagrams produce the **exact same** frequency tuple → land in the same bucket.
- **Time Complexity:** $O(N \cdot K)$ — no sorting cost, pure linear scan per word.
- **Space Complexity:** $O(N \cdot K)$ for storing all words in grouped buckets.

---

## 💻 Python Implementation

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(word)

        return list(groups.values())
```

---

## 🧪 Verification & Test Cases

The solution includes 8 automated unit tests (order-independent comparison):
1. LeetCode Example 1 — mixed anagram groups
2. LeetCode Example 2 — single empty string
3. LeetCode Example 3 — single word
4. All words are anagrams of each other → one big group
5. No two words share any anagram → all separate groups
6. Mix of empty strings and identical characters
7. Words with repeated characters (`"aab"`, `"baa"`, `"aba"`)
8. Longer real-world anagrams (`"listen"`, `"silent"`, `"enlist"`)
