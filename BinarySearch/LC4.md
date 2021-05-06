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