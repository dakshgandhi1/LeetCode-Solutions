class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        def dfs(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
            
        areas = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    areas.append(dfs(grid, i, j))

        return max(areas) if areas else 0
