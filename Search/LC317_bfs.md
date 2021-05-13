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