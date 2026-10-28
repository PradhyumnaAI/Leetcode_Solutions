class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Edge Case: Single cell
        if m == 1 and n == 1:
            return grid[0][0]
        
        # Edge Case: Only one row (can only move right)
        if m == 1:
            current_xor = 0
            for val in grid[0]:
                current_xor ^= val
            return current_xor
            
        # Edge Case: Only one column (can only move down)
        if n == 1:
            current_xor = 0
            for row in grid:
                current_xor ^= row[0]
            return current_xor

        from collections import deque

        # Queue stores tuples of (r, c, current_xor)
        queue = deque([(0, 0, grid[0][0])])
        
        # visited[r][c] stores a set of XOR values already achieved at cell (r, c)
        # to prune redundant states and prevent TLE.
        visited = [[set() for _ in range(n)] for _ in range(m)]
        visited[0][0].add(grid[0][0])
        
        min_xor = float('inf')

        while queue:
            r, c, current_xor = queue.popleft()
            
            # If we reached the bottom-right cell
            if r == m - 1 and c == n - 1:
                min_xor = min(min_xor, current_xor)
                continue
            
            # Move Right
            if c + 1 < n:
                next_xor = current_xor ^ grid[r][c + 1]
                if next_xor not in visited[r][c + 1]:
                    visited[r][c + 1].add(next_xor)
                    queue.append((r, c + 1, next_xor))
                    
            # Move Down
            if r + 1 < m:
                next_xor = current_xor ^ grid[r + 1][c]
                if next_xor not in visited[r + 1][c]:
                    visited[r + 1][c].add(next_xor)
                    queue.append((r + 1, c, next_xor))
                    
        return min_xor