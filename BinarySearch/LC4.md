#### Solution 1 sorting
sort nums1 + nums2, then get medium <br />
complexity: O((n+m)log(n+m)) <br />
Space: (n+m)


#### Solution 2 two pointer
define x and y, if nums1[x] < nums[y]: newlist.append(nums1[x]); x += 1; <br />
else: newlist.append(nums2[y]); y += 1; <br />
stop looping while x or y touches boundary <br />
then return the medium in newlist <br />
complexity: O(m+n) <br />
Space: (n+m)

```
import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        new_list = []
        x = 0
        y = 0
        while (x < n) & (y < m):
            if nums1[x] < nums2[y]:
                new_list.append(nums1[x])
                x += 1
            else:
                new_list.append(nums2[y])
                y += 1
        if (x == n) and (y < m):
            new_list += nums2[y:]
        elif (y == m) and (x < n):
            new_list += nums1[x:]
        
        if (n + m) % 2 == 0:
            return (new_list[(n+m)//2 - 1] + new_list[(n+m)//2]) / 2
        else:
            return new_list[(n+m)//2]
```


#### Solution 3 binary search
because the medium number is fixed, that means if we know the where to split on nums1, the split point on nums2 is fixed. That means we just need to know where to split on nums1 (shorter list). <br />
The question comes to how to decide whether the split point number is medium. we can know that the numbers at the split left side should smaller than the split point on right right for both two lists <=> maxleft <= minright <br />
if xleft > yright: split is too large, need to smaller the split => right = x - 1. elif xright < yleft: split is too small, needs to larger the split => left = x + 1. <br />
######important points:
1. x and y here means the number in each list. so the split point should be x-1 nad y - 1 <br />
2. why we use left <= right and right = mid - 1, left = mid + 1; instead of left < right and right = mid, the reason is that the later one would judge on the border point, when it touches the border, it will end the loop. While in this question, we need to compare the xright with yleft and xleft with yright. <br />
the first model output: left == right, and wont compare the border <br />
the later model output: left != right, but will go with the border <br />

complexity: O(logmin{m, n}) <br />
space: O(1)
```
import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        medium_num = (n + m - 1) // 2 + 1
        
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
    
        left = 0
        right = n
                
        while left <= right:
            x = left + (right - left) // 2
            y = medium_num - x 
            
            if x == 0: xleft = -sys.maxsize
            else: xleft = nums1[x - 1]
            if x == n: xright = sys.maxsize
            else: xright = nums1[x]
            if y == 0: yleft = -sys.maxsize
            else: yleft = nums2[y - 1]
            if y == m: yright = sys.maxsize
            else: yright = nums2[y]
            
            maxleft = max(xleft, yleft)
            minright = min(xright, yright)

            if maxleft <= minright:
                if (n+m) % 2 == 0:
                    return (maxleft + minright) / 2
                else:
                    return maxleft
                
            elif xleft > yright:
                right = x - 1
            elif xright < yleft:
                left = x + 1
```

3a. complexity: O(m+n), Space: O(1)
```
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        if (m + n) % 2 == 0:
            flag = 2
        else:
            flag = 1
        ct = 0
        res = 0
        k = (m + n)//2
        i, j = 0, 0
        
        while (i < m) or (j < n):
            val1 = nums1[i] if i < m else sys.maxsize
            val2 = nums2[j] if j < n else sys.maxsize
            
            if val1 < val2:
                val = val1
                i += 1
            else:
                val = val2
                j += 1
            
            ct += 1
            if (ct == k) and (flag == 2):
                res += val
            if (ct == k+1):
                res += val
                break
        
        return res/flag
```
3b. <br />
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn)))-solution-with-explanation <br />
找到直接return。因为这题出来太不好判断，因此用另一个模板。
```
l, r = 0, len(A)
while l <= r:
    mid = l + (r - l)//2
    cal = func(mid)
    if cal == target:
        return mid
    elif cal > target:
        r = mid
    else:
        l = mid 
```
Answer
```
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if (m + n) % 2 == 0:
            flag = True
        else:
            flag = False
        
        l, r = 0, m
        while l <= r:
            x = l + (r - l)//2
            y = (m + n + 1)//2 - x
            
            xleft = nums1[x-1] if x > 0 else -sys.maxsize
            yleft = nums2[y-1] if y > 0 else -sys.maxsize
            xright = nums1[x] if x < m else sys.maxsize
            yright = nums2[y] if y < n else sys.maxsize
            
            if (xleft <= yright) and (yleft <= xright):
                if flag:
                    return (max(xleft, yleft) + min(xright, yright))/2
                else:
                    return max(xleft, yleft)
            elif xleft > yright:
                r = x - 1
            else:
                l = x + 1
            
# j = (m+n+1)//2 - i => m<=n     
# j = (m + n + 1)//2 - i (keep left = right|right+1. name y and x as the index of right, and the index starts from 0, so if m+n == 3, x=0, y=2, leftlength=0+2, right=1+0,make sense)
# 0 <= i < m
# 0 <= j < n
# a0, a1, a2 | a3, a4, a5
# b0, b1, b2 | b3, b4

```