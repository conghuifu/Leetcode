#### Solution BFS
attention: build the temp list to save the current looping list
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            queueSize = len(queue)
            cur = []
            for _ in range(queueSize):
                vertex = queue.popleft()
                cur.append(vertex.val)
                if vertex.left:
                    queue.append(vertex.left)
                if vertex.right:
                    queue.append(vertex.right)
            res.append(cur)
        return res
```