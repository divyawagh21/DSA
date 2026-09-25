"""
LeetCode #49: Group Anagrams
Difficulty: Medium
Topic: Arrays & Hashing
Date Solved: 2026-09-25

Problem:
Given an array of strings `strs`, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group strings that are anagrams of each other using a character
        frequency tuple as a canonical hash key.

        Intuition:
        Two strings are anagrams if and only if they contain the exact same
        characters with the exact same frequencies. We need a "canonical form"
        that is identical for all anagrams of the same set of characters.

        Approach 1 — Sort as key (simpler, O(N * K log K)):
            sorted_word = tuple(sorted(word))
            Use this as the dictionary key. Sorting produces the same
            alphabetically-ordered tuple for all anagrams.

        Approach 2 — Frequency array as key (optimal, O(N * K)):
            For each word, build a 26-integer frequency count array for
            lowercase English letters. Convert the array to a tuple so it is
            hashable and can serve as a dictionary key. This avoids the
            O(K log K) sort cost, reducing the inner loop to O(K).

        We use Approach 2 for optimal performance.

        Algorithm:
        1. Initialise a defaultdict(list).
        2. For each word in `strs`:
            a. Build a 26-element count array (index 0 = 'a', ..., 25 = 'z').
            b. Convert to tuple → the canonical key.
            c. Append the word to groups[key].
        3. Return list(groups.values()).

        Complexity:
        - Time Complexity: O(N * K) where N = len(strs) and K = max word length.
          We iterate over all N words, and for each word we process K characters.
        - Space Complexity: O(N * K) to store all words across the grouped buckets,
          plus O(26) = O(1) per word for the temporary frequency array.
        """
        groups: dict = defaultdict(list)

        for word in strs:
            # Build 26-element frequency count for lowercase English letters
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            # Tuple is hashable → usable as dict key
            key = tuple(count)
            groups[key].append(word)

        return list(groups.values())


# --- Unit Tests ---
def test_group_anagrams():
    solver = Solution()

    # Helper: compare groups regardless of internal/external order
    def same_groups(result, expected):
        normalize = lambda g: sorted([sorted(x) for x in g])
        return normalize(result) == normalize(expected)

    # Test Case 1: LeetCode Example 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert same_groups(solver.groupAnagrams(strs1), expected1), "TC1 failed"

    # Test Case 2: LeetCode Example 2 — single empty string
    strs2 = [""]
    expected2 = [[""]]
    assert same_groups(solver.groupAnagrams(strs2), expected2), "TC2 failed"

    # Test Case 3: LeetCode Example 3 — single non-empty string
    strs3 = ["a"]
    expected3 = [["a"]]
    assert same_groups(solver.groupAnagrams(strs3), expected3), "TC3 failed"

    # Test Case 4: All words are anagrams of each other
    strs4 = ["abc", "bca", "cab", "cba"]
    expected4 = [["abc", "bca", "cab", "cba"]]
    assert same_groups(solver.groupAnagrams(strs4), expected4), "TC4 failed"

    # Test Case 5: No words are anagrams of each other
    strs5 = ["dog", "cat", "pig"]
    expected5 = [["dog"], ["cat"], ["pig"]]
    assert same_groups(solver.groupAnagrams(strs5), expected5), "TC5 failed"

    # Test Case 6: Mix of empty strings and real words
    strs6 = ["", "", "a", "a"]
    expected6 = [["", ""], ["a", "a"]]
    assert same_groups(solver.groupAnagrams(strs6), expected6), "TC6 failed"

    # Test Case 7: Words with repeated characters
    strs7 = ["aab", "baa", "aba", "xyz"]
    expected7 = [["aab", "baa", "aba"], ["xyz"]]
    assert same_groups(solver.groupAnagrams(strs7), expected7), "TC7 failed"

    # Test Case 8: Longer words
    strs8 = ["listen", "silent", "enlist", "hello", "world"]
    expected8 = [["listen", "silent", "enlist"], ["hello"], ["world"]]
    assert same_groups(solver.groupAnagrams(strs8), expected8), "TC8 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_group_anagrams()
