class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for r in range(m):
            row = []
            for c in range(n):
                row.append('#')
            grid.append(row)
        
        def carve_path(r: int, c: int):
            grid[r][c] = '.'
            
            if r == m - 1 and c == n - 1:
                return
            
            if c + 1 < n:
                carve_path(r, c + 1)
            elif r + 1 < m:
                carve_path(r + 1, c)

        carve_path(0, 0)
        
        result = []
        for row in grid:
            result.append("".join(row))
        return result