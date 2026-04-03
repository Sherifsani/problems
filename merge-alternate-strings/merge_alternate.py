class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        extra = ""
    
        if len(word1) > len(word2):
            extra = word1[len(word2) : ]
            word1 = word1[:len(word2)]
        elif len(word1) < len(word2):
            extra = word2[len(word1) : ]
            word2 = word2[:len(word1)]
            
        n = len(word1) #or word2
            
        for i in range(n):
            res.append(word1[i])
            res.append(word2[i])
        res.append(extra)
        return "".join(res)
