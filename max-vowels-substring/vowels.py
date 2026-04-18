class Solution:
    def maxVowels(self, s: str, k: int) -> int:
            vowels = set("aeiou")
            count = 0
            
            for i in range(k):
                if s[i] in vowels:
                    count += 1
            res = count
            
            for i in range(k, len(s)):
                if s[i] in vowels:
                    count += 1
                    
                if s[i - k] in vowels:
                    count -= 1
                res = max(res, count)
            return res