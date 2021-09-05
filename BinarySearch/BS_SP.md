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
##### 1. return the index of an alement in an sorted array. Elements are unique. If not, return -1
A = [1, 2, 5, 7, 8, 12]
binary_search(A, 8) = 4
binary_search(A, 6) = -1
```
def binary_search(A, target):
	left = 0
	right = len(A)
	while left < right:
		mid = left + int((right - left) / 2)
		if A[mid] == target:
			return mid
		if A[mid] > target:
			right = mid
		else:
			left = mid + 1
	return -1
```
##### 2. return the lower bound / upper bound of a val in a list
lower_bound: first index of i, such that A[i] >= x
upper_bound: first index of i, such that A[i] > x
A = [1, 2, 2, 2, 4, 4, 5]
lower_bound(A, 2) = 1, lower_bound(A, 3) = 4
upper_bound(A, 2) = 4, upper_bound(A, 5) = 7
```
# lower_bound
def binary_search(A, target):
	left = 0
	right = len(A)
	while left < right:
		mid = left + int((right - left) / 2)
		if A[mid] >= target:
			right = mid
		else:
			left = mid + 1
	return left
```

```
# upper_bound
def binary_search(A, target):
	left = 0
	right = len(A)
	while left < right:
		mid = left + int((right - left) / 2)
		if A[mid] > target:
			right = mid
		else:
			left = mid + 1
	return left
```
##### 3. find root (LC 69)
because digits are truncated, it equals to find the smallest num^2 larger than target, and return num -1 => upper bound
```
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left += 1
        return left - 1
```

##### 4. first bad version 
find first bad version => lower bound
```
def binary_search(A, target):
	left = 0
	right = len(A)
	while left < right:
		mid = left + int((right - left) / 2)
		if isBadVersion(mid):
			right = mid
		else:
			left = mid + 1
	return left
```

### 2. Kth number (LC 378)
we have two methods to solve this question.
a. sort the matrix first and get the kth number
Complexity: O(mnlog(mn))
Space: O(mn)
b. binary search
attention: I made the mistake in using the index at the first time. It is wrong because if we use index, it is required the numbers are strictly sorted. e.g. [[a,b,c], [d,e,f]], but we cannot decide the order between b and d, c and e. so we should use the number instead of the index.
also we should use the upper bound instead of the lower bound. it is because the upper/lower bound return the index, but we want the numbers smaller than current number. 
```
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def upper_bound(A, target):
            left = 0
            right = len(A)
            while left < right:
                mid = left + int((right - left) / 2)
                if A[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        left = 0
        right = matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            cur_poi = 0
            for row in matrix:
                cur_poi += upper_bound(row, mid)
            if cur_poi >= k:
                right = mid
            else: 
                left = mid + 1
                
        return left
```

### 3. find the best number can satisfy requirements (LC 875)
we are trying the number within a range, and try to figure out the number can satisfy the question => find the number from the sorted array
2 tricks:
a. in python3, devide exactly using //
b. p/m upper devide:  (p-1)/m + 1 (p >= 1 int)
Complexity: O(nlogn)
Space: O(1)
```
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        
        while left < right:
            mid = left + (right - left) // 2
            hours = 0
            for p in piles:
                hours += (p-1)//mid + 1
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
```

#### Find the position to be inserted
e.g [1,3,5], 0 insert at index 0, 2 insert at index 1, 7 insert at 3, 1 return (same value no need for insert)
```
def findLoc(A, target):
    l, r = 0, len(A)-1
    while l <= r:
        mid = l + (r - l)//2
        print(l, r, mid, A[mid])
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l
```

#### Find the position smaller or equal to target
```
def findLoc(A, target):
    l, r = 0, len(A)-1
    ans = -1
    while l <= r:
        mid = l + (r-l)//2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            r = mid - 1
        else:
            ans = mid
            l = mid + 1
    return ans
```