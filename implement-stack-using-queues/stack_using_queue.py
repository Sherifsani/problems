from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        n = len(self.q)
        self.q.append(x)
        # Rotate all previously stored elements to the back so the newest
        # element always sits at the front — making pop/top O(1).
        while n != 0:
            self.q.append(self.q.popleft())
            n -= 1

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())   # 2
print(obj.pop())   # 2
print(obj.empty()) # False
