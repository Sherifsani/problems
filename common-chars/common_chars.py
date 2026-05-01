# Problem: Common Characters (with duplicates)
# Given a string array, return all characters that appear in every string,
# including duplicates.
#
# Example:
#   Input:  ["bella", "label", "roller"]
#   Output: ["e", "l", "l"]
#
# Key insight:
#   For each character, the number of times it can appear in the result
#   is the MINIMUM count across all words. If it's missing from any word,
#   it's excluded entirely.
#
# Approach:
#   1. Build a frequency map per word        e.g. "bella" -> {b:1, e:1, l:2, a:1}
#   2. Use the first word as a baseline
#   3. For each remaining word, take min count — or delete if missing
#   4. Convert baseline back to a list
#
# Worked example:
#   baseline (bella)  -> {b:1, e:1, l:2, a:1}
#   + label           -> {b:1, e:1, l:2, a:1}   (all mins the same)
#   + roller          -> {e:1, l:2}              (b and a missing in roller)
#   output            -> ["e", "l", "l"]
#
# Complexity:
#   Time:  O(n * m)  where n = number of words, m = average word length
#   Space: O(1)      frequency map holds at most 26 characters
#
# Watch out for:
#   - Never modify a dict while iterating it directly.
#     Use list(start.keys()) to iterate a copy of the keys.
#   - A character missing from any word means its count is 0 — remove it.

from typing import List

def commonChars(words: List[str]) -> List[str]:
    freqs = []
    for word in words:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        freqs.append(freq)

    start = freqs[0]
    for i in range(1, len(freqs)):
        for k in list(start.keys()):       # iterate a copy to allow deletion
            if k not in freqs[i]:
                del start[k]               # missing from this word — remove
            else:
                start[k] = min(start[k], freqs[i][k])   # take the min count

    res = []
    for k, v in start.items():
        res.extend([k] * v)                # repeat char by its final count
    return res
