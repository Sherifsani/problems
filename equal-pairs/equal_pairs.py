from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        freq = {}
        for row in grid:
            t_row = tuple(row)
            freq[t_row] = freq.get(t_row, 0) + 1
        columns = []
        for i in range(len(grid[0])):
            column = []
            for row in grid:
                column.append(row[i])
            columns.append(column)
        count = 0

        for column in columns:
            t_column = tuple(column)
            if t_column in freq:
                count += freq[t_column]

        return count