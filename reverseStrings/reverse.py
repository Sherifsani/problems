class Solution:
    def reverseWords(self, s: str) -> str:

        # simple solution
        reverse =  s.strip().split()
        result = reverse[::-1]
        return " ".join(result)

        # manual solution
        # s = s.strip()
        # arr = []
        # word = ""
    
        # # extract all words
        # for i in range(len(s)):
        #     if s[i] == " ":
        #         continue
        #     word += s[i]
        
        #     if i + 1 <= len(s) -1 and s[i + 1] == " ":
        #         arr.append(word)
        #         word = ""
                
        #     if i == len(s) - 1:
        #         arr.append(word)
        #         word = ""
        
        # # reverse the array
        # reversed_arr = list(reversed(arr))
        # res = ""
        # for s in reversed_arr:
        #     res += s
        #     res += " "
        # return res.strip()

        
            