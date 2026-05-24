class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
            or grid[r][c] == -1 or (r, c) in visit):
                return
            visit.add((r, c))
            q.append([r, c])

        # we want to keep both treasure chests in a queue and mark them as 0
        # so we know where to start
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # need to track distance
        dist = 0
        while q:
            for i in range(len(q)):
                # we pop left so we start with the older ones, len(q) is the number of cells marked as having that distance
                # once that distance i in range len(q) is met we know we checked all those cells
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        
        

        