## Binary search summary
Binary search usually can be applied into 4 kinds of problems.
### 1. find target in sorted array
#### model
complexity: O(log(r-l)(f(m) + g(m)))
space: O(1)
```
def binary_search(l, r):
	while l < r:
		m = l + int((r - l) / 2)
		if decision(m: return m # optional
		if g(m):
			r = m
		else:
			l = m + 1
	return l # or not found
```
#### examples
##### 1. return the index of an alement in an sorted array. Elements are unique