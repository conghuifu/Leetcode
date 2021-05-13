#### Solution BFS
for the two dimension grid does the expansion, and each time expands once, usually we use BFS to solve the problem. <br />
Thinking process: <br />
scan the grid firstly, and put the coordinates of rotten oranges into queue, also records the number of fresh oranges. Then using BFS to go through the queues, while it meets the fresh oranges, turn the fresh oranges into the rotten, and add the coordinates into the queue. <br />
dont use deep copy (memory cost), use queue size <br />
Complexity: O(mn) <br />
Space: O(mn)

```
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = collections.deque()
        m = len(grid)
        n = len(grid[0])
        seen = set()
        minu = 0
        direcs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    seen.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while (fresh > 0) and (len(queue) > 0):
            queue_size = len(queue)
            minu += 1
            while queue_size > 0:
                vertex = queue.pop(0)
                queue_size -= 1
                for direc in direcs:
                    x = vertex[0] + direc[0]
                    y = vertex[1] + direc[1]
                    if ((x, y) in seen) or (x < 0) or (x >= m) or (y < 0) or (y >= n) or (grid[x][y] == 0):
                        continue
                    else:
                        grid[x][y] = 2
                        fresh -= 1
                        seen.add((x, y))
                        queue.append([x, y])
                        
        if fresh == 0:
            return minu
        else:
            return -1
```