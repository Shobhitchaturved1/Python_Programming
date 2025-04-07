from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[ROW - 1][COL - 1] != 0:
            return -1
        
        direction = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]
        queue = deque([(0, 0, 1)])  # row, col, path length
        visited = set((0, 0))
        
        while queue:
            r, c, dist = queue.popleft()
            if r == ROW - 1 and c == COL - 1:
                return dist
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        return -1
