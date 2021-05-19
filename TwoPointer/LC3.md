
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