from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        key = {'D': "Dire", 'R': "Radiant"}

        queue = deque(senate)
        # Tracks how many senators of each party are scheduled to be banned
        # the next time they appear in the queue.
        pending_bans = {'D': 0, 'R': 0}

        # Stop when only one party is left in the queue.
        while len(set(queue)) > 1:
            current = queue.popleft()
            opponent = 'R' if current == 'D' else 'D'

            if pending_bans[current] > 0:
                # This senator was already targeted; they lose their vote and
                # are eliminated (not re-queued).
                pending_bans[current] -= 1
            else:
                # No ban pending: senator exercises their right, scheduling the
                # next opponent encountered to be banned, then rejoins the end
                # of the queue for future rounds.
                pending_bans[opponent] += 1
                queue.append(current)

        return key[queue.popleft()]


sol = Solution()
print(sol.predictPartyVictory("RD"))   # Radiant
print(sol.predictPartyVictory("RDD"))  # Dire
