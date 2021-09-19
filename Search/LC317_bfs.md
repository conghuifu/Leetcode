### Solution BFS
key point: build a dictionary to save the shortest path length from empty land and building. 
```
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        position = dict() # <[x, y], val>
        buildings = []
        
        # find all buildings and empty lands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append([i, j])
                elif grid[i][j] == 0:
                    position[(i, j)] = 0

        # calculate the shortest dis between buildings and lands
        for building in buildings:      
            step = 0
            queue = collections.deque([building])
            seen = set()
            seen.add((building[0], building[1]))
            while queue:
                step += 1
                queueSize = len(queue)
                for _ in range(queueSize):
                    vertex = queue.popleft()
                    for direc in direcs:
                        x = direc[0] + vertex[0]
                        y = direc[1] + vertex[1]
                        if ((x, y) not in seen) and ((x, y) in position):
                            seen.add((x, y))
                            queue.append([x, y])
                            position[(x, y)] += step
            # remove the positions once it cannot reach any of building
            dif_path = set(position.keys()) - seen
            for i in dif_path:
                position.pop(i)
                
        if len(position) == 0: return -1
        return min(position.values())
```

### recap
```
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        buildings = []
        pos = dict()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings.append((i, j))
                elif grid[i][j] == 0:
                    pos[(i, j)] = 0
        
        for build in buildings:
            queue = collections.deque([(build[0], build[1])])
            seen = set()
            seen.add((build[0], build[1]))
            ct = 0
            while queue:
                size = len(queue)
                ct += 1
                for _ in range(size):
                    i, j = queue.popleft()
                    for direc in direcs:
                        x = i + direc[0]
                        y = j + direc[1]
                        if (x >= 0) and (y >= 0) and (x < m) and (y < n) and ((x, y) in pos) and ((x, y) not in seen):
                            queue.append((x, y))
                            seen.add((x, y))
                            pos[(x, y)] += ct
            
            rem = set(pos.keys()) - seen
            for key in rem:
                pos.pop(key)
        
        return min(pos.values()) if len(pos)>0 else -1
```