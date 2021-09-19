#### Solution BFS
trick: starts from the gate can guarantee every grid is reachable. then compare the vertex value and current value and get minimum one
```
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue = collections.deque([[i, j]])
                    seen = set((i, j))
                    while queue:
                        queueSize = len(queue)
                        for _ in range(queueSize):
                            vertex = queue.popleft()
                            for direc in direcs:
                                x = vertex[0] + direc[0]
                                y = vertex[1] + direc[1]
                                if (x < 0) or (x == m) or (y < 0) or (y == n) or ((x, y) in seen) or (rooms[x][y] in [-1, 0]):
                                    continue
                                queue.append([x, y])
                                seen.add((x, y))
                                rooms[x][y] = min(rooms[vertex[0]][vertex[1]] + 1, rooms[x][y])
                                
        return rooms
```


### recap
```
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        direcs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        queue = collections.deque()
        ct = 0
        
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    
        while queue:
            size = len(queue)
            ct += 1
            for _ in range(size):
                i, j = queue.popleft()
                for direc in direcs:
                    x = i + direc[0]
                    y = j + direc[1]
                    if (x >= 0) and (y >= 0) and (x < m) and (y < n) and (rooms[x][y] == 2147483647):
                        rooms[x][y] = ct
                        queue.append((x, y))
        
```