from typing import List

class Solution:

    # brute force approach
    def minOperationsI(self, boxes: str) -> List[int]:
        n = len(boxes)

        answer = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] != '0':
                    answer[i] += abs(i - j) * int(boxes[j])
        return answer
    
    # optimal solution
    def minOperationsII(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        specific_ops = ball_count = 0

        for i in range(n):
            answer[i] +=  1
            if boxes[i] == '1':
                ball_count += 1
            
            specific_ops += ball_count
        
        specific_ops = ball_count = 0

        for i in range(n-1, 1, -1):
            answer[i] += specific_ops
            if boxes[i] == 1:
                ball_count += 1
            
            specific_ops += ball_count
        
        return answer

