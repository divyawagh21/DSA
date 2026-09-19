"""
LeetCode #242: Valid Anagram
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-19

Problem:
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determine if string `t` is an anagram of string `s` using a frequency counter.

        Intuition:
        For two strings to be anagrams of each other:
        1. They must have identical lengths. If lengths differ, return False immediately.
        2. Every distinct character must occur with the exact same frequency in both strings.

        Rather than sorting the strings (which takes O(N log N) time), we can count character
        frequencies in a single pass using a fixed-size frequency table of 26 integers
        (or a hash table).
        - For each character in `s`, we increment its frequency count.
        - For each character in `t`, we decrement its frequency count.
        - Finally, if all frequency counts are zero, `t` is a valid anagram of `s`.

        Follow-up (Unicode characters):
        If inputs contain arbitrary Unicode characters instead of just lowercase English
        letters, we can replace the fixed array of 26 with a hash map (e.g. dict or Counter),
        which scales dynamically with unique Unicode code points while retaining O(N) time.

        Complexity:
        - Time Complexity: O(N), where N is the length of strings s and t.
          We traverse both strings in linear time.
        - Space Complexity: O(1) auxiliary space, as the frequency table has a fixed
          size of 26 elements for lowercase English letters (or O(K) where K is the number
          of distinct Unicode characters if using a hash map).
        """
        if len(s) != len(t):
            return False

        # Frequency array for 26 lowercase English letters
        count = [0] * 26

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord("a")] += 1
            count[ord(char_t) - ord("a")] -= 1

        # If all counts returned to 0, every character matched perfectly
        return all(c == 0 for c in count)


# --- Unit Tests ---
def test_is_anagram():
    solver = Solution()

    # Test Case 1: Standard valid anagram
    s1, t1 = "anagram", "nagaram"
    assert solver.isAnagram(s1, t1) is True, f"Failed on '{s1}' vs '{t1}'"

    # Test Case 2: Standard invalid anagram (same length, different characters)
    s2, t2 = "rat", "car"
    assert solver.isAnagram(s2, t2) is False, f"Failed on '{s2}' vs '{t2}'"

    # Test Case 3: Unequal lengths
    s3, t3 = "a", "ab"
    assert solver.isAnagram(s3, t3) is False, f"Failed on '{s3}' vs '{t3}'"

    # Test Case 4: Single identical character
    s4, t4 = "z", "z"
    assert solver.isAnagram(s4, t4) is True, f"Failed on '{s4}' vs '{t4}'"

    # Test Case 5: Single different character
    s5, t5 = "a", "b"
    assert solver.isAnagram(s5, t5) is False, f"Failed on '{s5}' vs '{t5}'"

    # Test Case 6: Same characters but differing frequencies
    s6, t6 = "aacc", "ccac"
    assert solver.isAnagram(s6, t6) is False, f"Failed on '{s6}' vs '{t6}'"

    # Test Case 7: Longer string with varied repetitions
    s7, t7 = "listen", "silent"
    assert solver.isAnagram(s7, t7) is True, f"Failed on '{s7}' vs '{t7}'"

    # Test Case 8: Repeated identical characters
    s8, t8 = "aaaaaa", "aaaaaa"
    assert solver.isAnagram(s8, t8) is True, f"Failed on '{s8}' vs '{t8}'"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_is_anagram()
