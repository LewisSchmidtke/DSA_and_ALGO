class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.ROWS, self.COLS = len(grid), len(grid[0])

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if grid[row][col] == 1:
                    a = self.dfs(grid, row, col)
                    max_area = max(max_area, a)

        return max_area

    def dfs(self, matrix, r, c):
        if min(r,c) < 0 or r == self.ROWS or c == self.COLS or matrix[r][c] == 0:
            return 0

        matrix[r][c] = 0 # mark visited
        area = 1
        
        area += self.dfs(matrix, r + 1, c)
        area += self.dfs(matrix, r - 1, c)
        area += self.dfs(matrix, r, c + 1)
        area += self.dfs(matrix, r, c - 1)

        return area


