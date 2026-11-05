class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.ROWS, self.COLS = len(image), len(image[0])
        self.target_color = image[sr][sc]
        self.dfs(image, sr, sc, color, set())
        return image

    def dfs(self, grid, r, c, color, visited):
        # Positional conditions
        if min(r, c) < 0 or r == self.ROWS or c == self.COLS or (r, c) in visited:
            return 
        
        # Color conditions
        if grid[r][c] != self.target_color:
            return

        grid[r][c] = color
        visited.add((r, c))

        self.dfs(grid, r + 1, c, color, visited)
        self.dfs(grid, r, c + 1, color, visited)
        self.dfs(grid, r - 1, c, color, visited)
        self.dfs(grid, r, c - 1, color, visited)

        return
        