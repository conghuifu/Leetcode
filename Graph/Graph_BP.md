### 拓扑排序
https://www.youtube.com/watch?v=B5hxqxBL2d0
#### BFS入度表法（kahn算法）
1. 从图中选出一个入度为0的顶点，输出该顶点 <br />
2. 从图中删除该节点及其所有出边（即与之邻接的所有顶点入度为-1）<br />
3. 反复执行这两个步骤，直至所有节点都输出，即整个拓扑排序完成；或者直至图里再没有入度为0的电，就说明图中有回路，不可能进行拓扑排序。<br />
通常，一个有向无环图可能有几种拓扑排序 <br />
整个流程可以归结为： 建图 -> 建入度 -> 找入口 -> BFS拓扑排序 <br />
```
# BFS model

# build graph
# input: N int, edges [][]
map = collections.defauldict(list)

# build indegree
indegree = [0 for i in range(N)]
for edge in edges:
	# [0, 1]图的方向事1指向0，0的入度有所增加，end <- start
	end, start = edge[0], edge[1]
	graph[start].append(end)
	indegree[end] += 1

# find all the nodes with 0 indegree
queue = collections.deque()
for i in range(N):
	if indegree[i] == 0:
		queue.append(i)

# BFS topological sort
count = 0
while queue:
	cur = queue.popleft()
	count += 1
	for nei in graph.get(cur):
		indegree[nei] -= 1
		if indegree[nei] == 0:
			queue.append(nei)

# if not equal, this is not the topological
return count == N
```

#### DFS
先找到最低点。存入stack，然后往前找，找到除了当前的另一个底点，如此直到头。stack FILO。 <br />
但是implement起来好像不太轻松。有一些改进方法：<br />

##### 三色法
对于图中任意一个节点，它在搜索过程中有三种数字颜色状态，即：<br />
1. 白色：未搜索 <br />
2. 灰色：搜索中。我们搜索过这个节点，但还没回溯到该节点，即该节点还未入栈，还有相邻的节点没有搜索完成 <br />
3. 黑色：已完成。已经进栈 <br />
notes: 有环情况：三个灰色的碰在一起 <br />
流程： 建图 -> 建visited -> 所有unvisited展开 -> DFS内部逻辑 <br />
DFS内部逻辑： 遍历当前点为进行中灰色1 -> 遍历neighbors：a. 遇到1则有环 b.遇到0继续bfs -> 所有neighbor遍历结束，标记当前点为黑色2，已遍历结束 <br />
```
# build graph
for edge in edges:
	# [0, 1]图的方向事1指向0，0的入度有所增加，end <- start
	end, start = edge[0], edge[1]
	graph[start].append(end)
	indegree[end] += 1

# build visited
self.visited = [0 for i in range(N)]
self.valid = True

# expansion on unvisited
for i in range(N):
	if self.visited[i] == 0:
		dfs[i]
return valid

# dfs
def dfs(u):
	self.visited[u] = 1
	for v in graph.get(u):
		if self.visited[v] == 0:
			dfs(v)
		# meet grey == circle (!topology)
		elif self.visited[v] == 1:
			self.valid = False 
	self.visited[u] = 2
```

