class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        DETERMINE IF TWO STRINGS ARE CLOSE
        ====================================
        Two strings are "close" if you can make one equal to the other using:
            - Op1: Swap any two characters        → order doesn't matter
            - Op2: Transform all of char X ↔ Y   → swaps frequency ownership between characters

        KEY INSIGHT:
            - Op1 + Op2 together mean we only need to check two conditions:
                1. Same unique character set  → can't create characters that don't exist
                2. Same multiset of frequencies → Op2 just shuffles which char owns which frequency

        EXAMPLE:
            word1 = "cabbba"  → freq: {c:1, a:2, b:3} → sorted freqs: [1, 2, 3]
            word2 = "abbccc"  → freq: {a:1, b:2, c:3} → sorted freqs: [1, 2, 3]
            char sets: {a,b,c} == {a,b,c} ✓  |  freqs: [1,2,3] == [1,2,3] ✓  →  Close!

        GOTCHA:
            Use sorted() NOT set() when comparing frequencies.
            set() drops duplicates, so [2,2,5,5] and [2,5] would wrongly appear equal.
            sorted() preserves duplicates: [2,2,5,5] != [2,3,3,5] ✓

        COMPLEXITY: Time O(n) | Space O(1) (at most 26 characters)
        """

        # Condition 1: early exits — lengths must match, and both must have the same unique chars
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        # Build frequency maps for both strings
        freq1 = dict()
        for char in word1:
            freq1[char] = freq1.get(char, 0) + 1

        freq2 = dict()
        for char in word2:
            freq2[char] = freq2.get(char, 0) + 1

        # Condition 2: multiset of frequencies must match (sorted preserves duplicates)
        return sorted(freq1.values()) == sorted(freq2.values())