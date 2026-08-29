class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        numrows = len(grid)
        numcols = len(grid[0])
        minutes = 0
        ffcntr = 0
        q = deque()
        for r in range(numrows):
            for c in range(numcols):
                if grid[r][c] == 1:
                    ffcntr += 1 
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        while q:
            current = q.popleft()
            r = current[0]
            c = current[1]
            minutes = max(minutes, current[2])
            for dr, dc in directions:
                if r + dr >= 0 and c + dc >= 0 and r + dr < numrows and c + dc < numcols and grid[r+dr][c+dc] == 1:
                    q.append((r + dr, c + dc, current[2] + 1))
                    grid[r + dr][c + dc] = 2
                    ffcntr -= 1 
        if ffcntr > 0:
            return -1
        return minutes

                
