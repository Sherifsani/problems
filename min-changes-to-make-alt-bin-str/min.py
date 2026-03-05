class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        window = []
        change = 0

        for c in s:
            if window and window[-1] == c:
                change += 1
                window.pop()
            else:
                window.append(c)
        return change
