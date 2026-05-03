from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Positive = moving right, negative = moving left.
        # Collision only happens when a rightward asteroid is on top and the
        # incoming asteroid is leftward; same-direction pairs never meet.
        stack = []
        is_destroyed = False  # True when equal-size collision destroys both

        for asteroid in asteroids:
            # Keep colliding the incoming (leftward) asteroid against rightward
            # survivors on the stack until one of them wins or no target remains.
            while not is_destroyed and stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) <= abs(asteroid):
                    if abs(stack[-1]) == abs(asteroid):
                        # Equal size: incoming asteroid dies too
                        is_destroyed = True
                    stack.pop()  # Stack top is destroyed regardless
                else:
                    # Stack top is larger; incoming asteroid is destroyed
                    break

            if is_destroyed:
                is_destroyed = False
                continue  # Incoming asteroid was destroyed; skip appending

            # Append only when no collision is pending. If we broke out above
            # (stack top survived), the condition is still True so we skip.
            if not stack or not (stack[-1] > 0 and asteroid < 0):
                stack.append(asteroid)

        return stack

sol = Solution()
res = sol.asteroidCollision([-2,1,1,-1])
print(res)
