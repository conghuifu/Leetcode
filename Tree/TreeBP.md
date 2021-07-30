## Binary Tree Traversal
### Recursion (always from left to right, X order up to the order of Root)
Inorder: Left root right; Preorder: root left right; Postorder: left right root
1. Step1 Funtion <br />
2. Step2 Base case: root == null =>return <br />
3. Step3 Subproblem:inorder(root.left) / inorder(root.right) <br />
```
def inorder(root):
	if not root: return

	inorder(root.left)
	print(root.val)
	inorder(root.right)
```
图解：
```
   A
 B   C
D E F G

preorder: ABDECFG
inorder: DBEAFCG
postorder: DEBFGCA
```