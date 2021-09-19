#### Solution BFS
It equals to find the shared path for PAC and ATL. the start point is the border line of two oceans. <br />
quque using deque. seen using seen. be careful the set format <br />
Complexity: O(mn(m+n)) <br />
Space: O(mn)
```
class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = [[0, j] for j in range(len(heights[0]))] + [[i, 0] for i in range(len(heights))]
        atl = [[len(heights)-1, j] for j in range(len(heights[0]))] + [[i, len(heights[0]) - 1] for i in range(len(heights))]
        return list(self.bfs(heights, pac).intersection(self.bfs(heights, atl)))
    
        
    def bfs(self, graph, s):
            queue = collections.deque(s)
            seen = set()
            m = len(graph)
            n = len(graph[0])
            direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            for q in queue:
                seen.add((q[0], q[1]))
                
            while queue:
                queueSize = len(queue)
                vertex = queue.popleft()
                for direc in direcs:
                    x = vertex[0] + direc[0]
                    y = vertex[1] + direc[1]
                    if (x < 0) or (x == m) or (y < 0) or (y == n) or ((x, y) in seen) or (graph[vertex[0]][vertex[1]] > graph[x][y]):
                        continue
                    else:
                        queue.append([x, y])
                        seen.add((x, y))
            return seen    
```

### recap
```
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])
        atl_queue = collections.deque()
        pac_queue = collections.deque()
        for i in range(self.m):
            pac_queue.append((i, 0))
            atl_queue.append((i, self.n-1))
        for j in range(self.n):
            pac_queue.append((0, j))
            atl_queue.append((self.m-1, j))

        atl = self.bfs(heights, atl_queue)
        pac = self.bfs(heights, pac_queue)

        return list(atl.intersection(pac))
    
    def bfs(self, heights, queue):
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        seen = set()
        
        for i, j in queue:
            seen.add((i, j))
        
        while queue:
            i, j = queue.popleft()
            for direc in direcs:
                x = i + direc[0] 
                y = j + direc[1]
                if (x >= 0) and (y >= 0) and (x < self.m) and (y < self.n) and ((x, y) not in seen) and (heights[x][y] >= heights[i][j]):
                    seen.add((x, y))
                    queue.append((x, y))
        return seen
            
```