class Solution:
    def clumsy(self, n: int) -> int:
        # Stack holds independently summable terms. High-precedence ops (* /)
        # fold into the current top; low-precedence ops (+ -) start a new term.
        stack = [n]
        ops = ['*', '/', '+', '-']
        index = 0
        num = n - 1

        while num > 0:
            op = ops[index % 4]

            if op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                # int() truncates toward zero (matches problem spec; // would floor)
                stack.append(int(stack.pop() / num))
            elif op == '+':
                stack.append(num)
            else:
                # Push as negative so the next * / pair operates on a negative
                # base (e.g. -6 * 5 / 4 → stack top becomes -7, not +7).
                stack.append(-num)

            index += 1
            num -= 1

        return sum(stack)


sol = Solution()
print(sol.clumsy(10))  # 12  →  10*9/8+7 - 6*5/4+3 - 2*1
print(sol.clumsy(4))   # 7   →  4*3/2+1


class SolutionMath:
    def clumsy(self, N: int) -> int:
        # O(1) math solution: the result always lands near N with a small fixed
        # offset that repeats on a cycle of 4. After the first block (N*(N-1)/(N-2)),
        # each subsequent group of four consecutive integers (+a - b*c/d) contributes
        # a net offset of roughly 0, making the total predictable by N mod 4.
        if N <= 2:
            return N
        if N <= 4:
            return N + 3  # 3→6, 4→7

        if (N - 4) % 4 == 0:
            return N + 1
        elif (N - 4) % 4 <= 2:
            return N + 2
        else:
            return N - 1


sol2 = SolutionMath()
print(sol2.clumsy(10))  # 12
print(sol2.clumsy(4))   # 7
