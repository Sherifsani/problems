from typing import List

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            # Already equal: a swap only helps if two identical chars exist
            # (swap them → string unchanged, still equals goal).
            return len(set(s)) < len(s)

        if len(s) != len(goal):
            return False

        # Each entry is [s[i], goal[i]] — the character pair that must be fixed
        # at that position by the single swap.
        diffs: List[List[str]] = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append([s[i], goal[i]])

        if len(diffs) != 2:
            return False

        # Guard against same-direction diffs like [['a','b'],['a','b']]:
        # both positions need a→b, but swapping two a's leaves them as a's.
        # (e.g. s="abcaa", goal="abcbb")
        if diffs[0] == diffs[1]:
            return False

        # Valid swap: the two diffs must be mirror images, e.g. ['a','b'] and
        # ['b','a'], meaning swapping those two characters in s fixes both spots.
        return set(diffs[0]) == set(diffs[1])


sol = Solution()
print(sol.buddyStrings("ab", "ba"))      # True
print(sol.buddyStrings("aa", "aa"))      # True  (duplicate char, already equal)
print(sol.buddyStrings("abcaa", "abcbb")) # False (same-direction diffs)
print(sol.buddyStrings("ab", "ab"))      # False (no duplicate to swap)
