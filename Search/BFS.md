### tutorial link
https://www.youtube.com/watch?v=oLtvUWpAnTQ <br />
https://www.youtube.com/watch?v=bD8RT0ub--0 <br />

#### 1. basic bfs
print the path
```
graph = {
	'A': ['B', 'C'],
	'B': ['A', 'C', 'D'],
	'C': ['A', 'B', 'D', 'E'],
	'D': ['B', 'C', 'E', 'F'],
	'E': ['C', 'D'],
	'F': ['D']
}

def BFS(graph, s):
	queue = []
	queue.append(s)
	seen = set()
	seen.add(s)
	while len(queue) > 0:
		vertex = queue.pop(0)
		nodes = graph[vertex]
		for w in nodes:
			if w not in seen:
				queue.append(w)
				seen.add(w)
		print(vertex)
```

#### 2. find the shortest distance between two points
```
def BFS(graph, s):
	queue = []
	queue.append(s)
	seen = set()
	seen.add(s)
	parent = {s: None}

	while len(queue) > 0:
		vertex = queue.pop(0)
		# expand
		nodes = graph[vertex]
		for w in nodes:
			if w not in seen:
				queue.append(w)
				seen.add(w)
				parent[w] = vertex
		print(vertex)
	return parent

parent = BFS(graph, 'E')
node = 'B'
while node != None:
	print(node)
	node = parent[node]
```