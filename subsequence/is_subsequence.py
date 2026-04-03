class Solution:

    # difficulty (easy)
    # time complexity (O(n))
    # space complexity (O(1))
    def subsequence(self, s: str, t: str) -> bool:
        if not s: return True
        s_ptr = 0

        for char in t:
            if char == s[s_ptr]:
                s_ptr += 1
            if s_ptr == len(s):
                return True
        return False


