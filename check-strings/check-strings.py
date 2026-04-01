from typing import List

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # 1. initializing empty arrays for s1 and s2 to count characters at even and odd positions
        freq_s1 = [[0] * 26, [0] * 26]
        freq_s2 = [[0] * 26, [0] * 26]

        # 2. iterating s1 to get frequencies at even and odd positions
        for i in range(n):
            c = ord(s1[i]) - ord('a')
            if i % 2 == 0:
                freq_s1[0][c] += 1
            else:
                freq_s1[1][c] += 1
        
        # 3. iterating s2 to get frequencies at even and odd positions
        for i in range(n):
            c = ord(s2[i]) - ord('a')
            if i % 2 == 0:
                freq_s1[0][c] += 1
            else:
                freq_s1[1][c] += 1
        
        #4. if both frequencies are equal then return True else False
        return freq_s1 == freq_s2