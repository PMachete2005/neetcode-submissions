class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        numrows = len(grid)
        numcols = len(grid[0])
        islands = 0
        def bfs(r,c):
            queue = deque()
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row >= 0 and col >= 0 and row < numrows and col < numcols and grid[row][col] == "1":
                        grid[row][col] = "0"
                        queue.append((r + dr, c + dc))
        
        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1 
        return islands


        