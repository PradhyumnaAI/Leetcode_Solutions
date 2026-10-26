class Solution:
    def dfs(self,r:int,c:int,grid : List[List[int]]):
        rows,cols = len(grid),len(grid[0])
        if r <0 or r>=rows or c<0 or c>= cols or grid [r][c]==0 :
            return 0 
        current_val = grid[r][c]
        grid[r][c] = 0
        up = self.dfs(r-1,c,grid)
        down = self.dfs(r+1,c,grid)
        right = self.dfs(r,c+1,grid)
        left = self.dfs(r,c-1,grid)
        return current_val + up + down + left +right
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        count = 0
        rows,cols = len(grid),len(grid[0])
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid [r][c] > 0 :
                    island_sum = self.dfs(r,c,grid)
                    if island_sum % k == 0:
                        count += 1
        return count

                    

        