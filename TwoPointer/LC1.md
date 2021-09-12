### Solution
we cannot use BS here cuz we need to return the index, sort the list will disorder the original index. Also there are duplicates, we cannot index the original list. so we use the dictionary. space: O(n), complexity: O(n)
```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num], index]
            seen[num] = index
        return [-1, -1]
```