class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, visit):
            if ((r,c) in visit or r<0 or c<0 or r == rows or c == cols or board[r][c] != 'O'):
                return
            visit.add((r,c))
            dfs(r+1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c+1, visit)
            dfs(r, c-1, visit)

        for c in range(cols):
            dfs(0, c, visited)
            dfs(rows-1, c, visited)

        for r in range(rows):
            dfs(r, 0, visited)
            dfs(r, cols-1, visited)

        print(visited)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited:
                    board[r][c] = "X"