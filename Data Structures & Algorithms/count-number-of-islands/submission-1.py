class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        numrows = len(grid)
        numcols = len(grid[0])
        visited = set()
        islands = 0
        def bfs(r,c):
            queue = deque()
            queue.append((r, c))
            visited.add((r,c))
            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row >= 0 and col >= 0 and row < numrows and col < numcols and grid[row][col] == "1" and (row, col) not in visited:
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
        
        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1 
        return islands


        