class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        l = len(grid)
        w = len(grid[0])
        visited = set()
        def dfs(i, j):
            if (i,j) in visited:
                return 
            visited.add((i,j))
            if i<=l-2 and grid[i+1][j] == "1":
                dfs(i+1,j)
            if i>0 and grid[i-1][j] == "1":
                dfs(i-1, j)
            if j>0 and grid[i][j-1] == "1":
                dfs(i, j-1)
            if j<=w-2 and grid[i][j+1] == "1":
                dfs(i, j+1)

        i = 0
        count = 0
        while i < l:
            j = 0
            while j < w:
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    print(i,j)
                    count+=1
                j+=1
            i+=1

        return count

