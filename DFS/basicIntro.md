### Recursion
Recursion needs to decide two things: basic cases and recursion relation. <br />
basic cases: end case/ final case <br />
recursion relation: depart into smaller questions.
```
## LC 700
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # basic case
        if not root: return None
        if root.val == val: return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
```
<br />
Recursion usually has 3 extensions:  <br />
1. memorization <br />
2. divide and conquer <br />
3. backtracking <br />

##### 1. memorization
to record the historical results to avoid the duplicated computation <br />
Example: LC 509. <br />
1. without memorization
```
class Solution:
    def fib(self, n: int) -> int:
        # basic case
        if n <= 1: return n
        
        # recursion
        return self.fib(n - 1) + self.fib(n-2)
```
2. with memorization
```
class Solution:
    def __init__(self):
        self.cache = {}
    
    def fib(self, n: int) -> int:
        # basic case
        if n <= 1: return n
        if n in self.cache:
            return self.cache[n]
        
        else:
            res = self.fib(n - 1) + self.fib(n-2)
            self.cache[n] = res
        # recursion
        return res
```
3. climbing stairs <br />
a. dp
```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
```
2. recursion with memorization
```
class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2}
        
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = res
        
        return res
```

##### Divide and conquer
divide into small questions, then combine the results
```
def divideConquer(S):
	# 1. divide into n small questions
	divide[S] = [S1, S2, ..., Sn]

	# 2. solve the small q in recursion ways
	[R1, R2, ... , Rn] = [divideConquer(Si) for i in divide[S]]

	# 3. combine the results
	return combine([R1, R2, ..., Rn])
```
Example: LC 98
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.divideConquer(root)        
        
    def divideConquer(self, node, low = -sys.maxsize, high = sys.maxsize):
        if not node:
            return True
        
        if (node.val <= low) or (node.val >= high):
            return False
        
        return self.divideConquer(node.left, low, node.val) and self.divideConquer(node.right, node.val, high)
```
##### backtracking
寻找所有满足条件的结果，并且问题可以用recursion解决 <br />
```
def backtrack(candidate):
	if find_solution(candidate):
		output(candidate)
		return

	# iterate all possible candidates
	for next_candidate in list_of_candidates:
		if is_valid(next_candidate):
			# try this partial candidate solution
			place(next_candidate)
			# given the candidate, explore more
			backtrack(next_candidate)
			# backtrack
			remove(next_candidate)
```
Example: LC 22 <br />
find all possible solutions
```
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(left, right, S):
            # base case
            if len(S) == n*2:
                res.append(S)
                return 
            
            # other candidates
            # notice here we did not remove the next_candidate, cuz we did not change on the S. if we use list, we need to pop the changes on next candidate
            if left < n:
                backtrack(left + 1, right, S + '(')
            if right < left:
                backtrack(left, right + 1, S + ')')
        
        backtrack(0, 0, '')
        return res
```

#### Summary
recursion: <br />
two steps: basic case + recursion relation <br />
1. duplicates: memorization <br />
2. child problems: divide and conquer <br />
3. return all satisfied answer: backtracking
