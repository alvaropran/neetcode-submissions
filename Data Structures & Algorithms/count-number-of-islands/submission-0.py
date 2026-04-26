class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c): #iterative
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q: # while not empty expand island
                row, col = q.popleft() # pop from q
                directions = [[1,0], [-1,0], [0,1], [0,-1]]#check adjacent of popped use loop

                for dr, dc in directions: #each direction
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c)) #add since set


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands