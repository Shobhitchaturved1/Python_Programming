class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        starting from top left we will add smallest element in an array
        using min heap would be better
        extract next smaller element from minheap 
        """
        ROW, COL = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        
        # Min-heap for dynamically processing grid values
        minheap = [(grid[0][0], 0, 0)]
        heapq.heapify(minheap)
        
        visit = set()
        visit.add((0,0))
        
        # Sort queries with index tracking for output
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)
        
        count = 0  # Count of points that are < current query value
        while sorted_queries:
            q_index, q_value = sorted_queries.pop(0)
            
            # Expand heap dynamically while grid value < query value
            while minheap and minheap[0][0] < q_value:
                val, r, c = heapq.heappop(minheap)
                count += 1  # Increase count of accessible points
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROW and 0 <= col < COL and (row, col) not in visit:
                        heapq.heappush(minheap, (grid[row][col], row, col))
                        visit.add((row, col))
            
            res[q_index] = count
        
        return res