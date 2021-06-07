### DFS template
```
result = []

def backtrack(path, choose_list):
	if f(x):
		result.add(path)
		return

	for choose in choose_list:
		filter
		backtrack(path, choose_list)
		reverse choose
```
1. dfs <br />
2. 外部空间dfs(用stack写成iterative way，for examples tree traversal) <br />
3. DFS + memo (DP剪枝) <br />
4. 使用模拟流程，寻找所有情况的全排列解（所有可能的解）
