from typing import List

class Solution:

    # brute force approach
    def minOperationsBrute(self, boxes: str) -> List[int]:
        n = len(boxes)

        answer = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] != '0':
                    answer[i] += abs(i - j) * int(boxes[j])
        return answer