### Solution
1. Walls and Gates (LC 286)
```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        direcs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(rooms), len(rooms[0])
        
        # search all gates
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                cur = queue.popleft()
                for direc in direcs:
                    x = cur[0] + direc[0]
                    y = cur[1] + direc[1]
                    if (x >= 0) and (y >= 0) and (x < m) and (y < n) and (rooms[x][y] == 2147483647):
                        rooms[x][y] = step
                        queue.append((x, y))
                        
        return rooms
            
```

2. shortest distance from all buildings
```python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # find all buildings & lands
        buildings = []
        lands = set()
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append([i, j])
                elif grid[i][j] == 0:
                    lands.add((i, j))
                    
        # bfs
        for building in buildings:
            queue = collections.deque([building])
            visited = set()
            visited.add((building[0], building[1]))
            step = 0
            while queue:
                step += 1
                size = len(queue)
                for _ in range(size):
                    cur = queue.popleft()
                    for direc in direcs:
                        x = cur[0] + direc[0]
                        y = cur[1] + direc[1]
                        if ((x, y) in lands) and ((x, y) not in visited):
                            grid[x][y] += step
                            visited.add((x, y))
                            queue.append((x, y))

            lands = lands.intersection(visited)

        # calculate res
        res = sys.maxsize//2
        for i, j in lands:
            if grid[i][j] < res:
                res = grid[i][j]
        return res if res < sys.maxsize//2 else -1
```