#### Solution BFS
the extra point needs to search whether the nearby grids have mines, If yes, return the mine number; Else firstly label the B, and do the expansion.

```
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        queue = collections.deque([click])
        seen = set((click[0], click[1]))
        m = len(board)
        n = len(board[0])
        direcs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        
        
        while queue:
            vertex = queue.popleft()
            mine = self.nearbyMineNum(board, direcs, vertex[0], vertex[1])
            if mine > 0:
                board[vertex[0]][vertex[1]] = str(mine)
            else:
                board[vertex[0]][vertex[1]] = 'B'
                for direc in direcs:
                    x = vertex[0] + direc[0]
                    y = vertex[1] + direc[1]
                    if (x < 0) or (x == m) or (y < 0) or (y == n) or ((x, y) in seen): continue
                    else:
                        queue.append([x, y])
                        seen.add((x, y))
                        
        return board
            
    def nearbyMineNum(self, board, direcs, x, y):
        m = len(board)
        n = len(board[0])
        
        mine = 0
        for direc in direcs:
            xNew = x + direc[0]
            yNew = y + direc[1]
            if (xNew < 0) or (xNew == m) or (yNew < 0) or (yNew == n):
                continue
            elif board[xNew][yNew] == 'M':
                mine += 1
        return mine
```

### recap
先check再拓展
```
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.m = len(board)
        if self.m == 0:
            return board
        self.n = len(board[0])
        self.direcs = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        queue = collections.deque([(click[0], click[1])])
        visited = set()
        visited.add((click[0], click[1]))
        
            
        while queue:
            i, j = queue.popleft()
            ct = self.check(board, i, j)
            if ct > 0:
                board[i][j] = str(ct)
            else:
                board[i][j] = 'B'
                for direc in self.direcs:
                    x = i + direc[0]
                    y = j + direc[1]
                    if (x >= 0) and (y >= 0) and (x < self.m) and (y < self.n) and ((x, y) not in visited):
                        queue.append((x, y))
                        visited.add((x, y))
        return board
    
    def check(self, board, x, y):
        ct = 0
        for direc in self.direcs:
            xn = x + direc[0]
            yn = y + direc[1]
            if (xn >= 0) and (yn >= 0) and (xn < self.m) and (yn < self.n):
                if board[xn][yn] == 'M':
                    ct += 1
        return ct
```