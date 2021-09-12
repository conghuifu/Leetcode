
#### Solution
build the dictionary to decrease the search time  <br />
Complexity: O(n^2) <br />
Space O(1)

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        maxSize = 1
        left, right = 0, 1
        dupIndex = -1
        while right < len(s):
            dupIndex = self.dupString(s, s[right], left, right)
            if dupIndex == -1:
                tmpSize = right - left + 1
                if tmpSize > maxSize:
                    maxSize = tmpSize
            else:
                left = dupIndex + 1
            right += 1
        return maxSize
            
    def dupString(self, s, target, left, right):
        dupIndex = -1
        for i in range(left, right)[::-1]:
            if s[i] == target:
                return i
        return dupIndex
```
Complexity: O(n) <br \>
Space: O(1)
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        maxSize = 1
        left, right = 0, 0
        hashset = dict()
        while right < len(s):
            if s[right] not in hashset:
                hashset[s[right]] = True
                maxSize = max(maxSize, right - left + 1)
                right += 1
            else:
                hashset.pop(s[left])
                left += 1
        return maxSize
```

### recap
1. space: O(1), complexity: O(n^2)
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        l, r = 0, 1
        res = 1
        while r < n:
            dupIndex = self.find(l, r, s[r], s)
            if dupIndex == -1:
                res = max(res, r-l+1)
            else:
                #### remember l=index+1 instead of index
                l = dupIndex + 1
                
            r += 1
        return res
            
    def find(self, l, r, target, s):
        dupIndex = -1
        for i in range(r-1, l-1, -1):
            if s[i] == target:
                return i
        return dupIndex
```
2. space: O(n), complexity: O(n)
```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        
        l, r = 0, 1
        res = 1
        seen = set()
        # add s[l]
        seen.add(s[l])
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r-l+1)
                r += 1
            else:
                # remove s[l] until s[l] != s[r] 
                seen.remove(s[l])
                l += 1
        return res
```