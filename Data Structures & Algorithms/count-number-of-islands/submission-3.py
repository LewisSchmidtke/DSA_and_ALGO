class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        nr_islands = 0
        visited = set()

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == "0" or (row, col) in visited:
                    continue
                
                nr_islands += self.dfs(grid, row, col, visited)

        return nr_islands

    def dfs(self, matrix, r, c, visited):
        if min(r, c) < 0 or r == self.ROWS or c == self.COLS or (r, c) in visited:
            return
        
        if matrix[r][c] == "0":
            return
        
        visited.add((r, c))

        self.dfs(matrix, r, c + 1, visited)
        self.dfs(matrix, r + 1, c, visited)
        self.dfs(matrix, r, c - 1, visited)
        self.dfs(matrix, r - 1, c, visited)

        return 1
