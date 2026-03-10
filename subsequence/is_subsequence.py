class Solution:
    def subsequence(self, s: str, t: str) -> bool:
        if not s: return True
        s_ptr = 0

        for char in t:
            if char == s[s_ptr]:
                s_ptr += 1
            if s_ptr == len(s):
                return True
        return False


