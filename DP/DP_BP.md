### DP 套路
此处见huifeng大神channel: https://www.youtube.com/watch?v=FLbqgyJ-70I <br />

#### DP的两大特点 
a. 无后效性 <br />
a1. 一旦f(i, j)确定，就不需要关心如何计算f(i, j) <br />
a2. 想要确定f(i, j), 只需要知道f(i-1, j)和f(i, j-1)的值，而至于他们是如何计算得出的，对当前或之后的任何子问题都没有影响<br />
a3. “过去不依赖将来，将来不影响过去”<br />
b. 最优子结构 <br />
b1. f(i, j)已经蕴含最优 <br />
b2. 大问题的最优解可以由若干个小问题的最优解推出 <br />


#### 套路start
##### I类基本型 - “时间序列”型
给出一个序列，其中每一个元素可以认为“一天”，并且“今天”的状态只取决于“昨天”的状态 <br />
套路： <br />
1. 定义dp[i][j]: 表示ith轮的jth状态 <br />
2. 定义dp[i][j] 和d[i - 1][j]的关系 <br />
3. 最终结果是dp[last][j]中的某种aggregation <br />
根据图表关系画一画，状态转移之间的关系
###### 例题
1. LC 198
```
# 0: 这轮我抢的最大收益
# 1: 这轮我不抢的最大收益
#for i in range(1, N):
#	dp[i][0] = dp[i-1][1] + val[i]
#	dp[i][1] = max(dp[i-1][0], dp[i-1][1])
#ans = max(dp[-1][0], dp[-1][1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        
        # initiate
        n = len(nums)
        dp = [[0, 0] for i in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = nums[0]
        
        # status 0 -> no rob, 1->rob
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1])
```
2. LC 213 <br />
```
#1. 第一个房子不抢 => house[1]~house[-1]基本问题
#2. 最末尾房子不抢 => house[0]~house[-2]基本问题
#注意边界问题：如果nums length <= 1 ，会越界，还有dp初始化0之后，for loop是从1开始
class Solution:
    def rob(self, nums: List[int]) -> int:
        # initiate 
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))
        
    def dp(self, nums):
        n = len(nums)

        dp = [[0, 0] for i in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1])
```
3. LC 123 
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        dp = [[0, 0, 0, 0] for i in range(n)]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][1] - prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][2] + prices[i], dp[i-1][3])
        return max(dp[-1])
```
4. LC 309
```
# 3种状态
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        dp = [[0,0,0] for i in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][2] - prices[i], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1])
```
5. LC 376
```
# 2种状态
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # greedy search
        # just include all the turning points
        n = len(nums)
        if n == 0: return 0
        
        p, q = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                p = q + 1
            elif nums[i] < nums[i-1]:
                q = p + 1
        
        return max(p, q)
```
6. LC 276 (paint fence)
```
1. 只和上一个状态有关的，不需要length = n的dp，只需要一个p_tmp, q_tmp表示上一个状态，和p, q表示当前状态即可。然后更新p,q,p_tmp,q_tmp。而且这个tmp必须有，不然轮换的时候，例如这题，p更新值了，q用到p，就不对了，要用p_tmp
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if (n == 0) or (k == 0): return 0
        if n == 1: return k
        
        # p: 前两个相同，q:前两个不同
        p = k
        q = k*(k-1)
        
        for i in range(2, n):
            p_tmp = p
            q_tmp = q
            p = q_tmp
            q = (p_tmp + q_tmp) * (k - 1)
        return p+q
```
7. minumum falling path sum II
```
# 931 minumum falling path sum I
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 0: return 0
        if n == 1: return min(matrix[0])
        m = len(matrix[0])
        
        direcs = [1, 0, -1]
        dp = matrix[0]
        for i in range(1, n):
            dp_tmp = dp.copy()
            for j in range(m):
                local_min = sys.maxsize
                for direc in direcs:
                    if (j + direc >= 0) and (j + direc < m):
                        local_min = min(local_min, dp_tmp[j+direc])
                dp[j] = local_min + matrix[i][j]
        return min(dp)
```
```
# 1289 minumum falling path sum II
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 0: return 0
        if n == 1: return min(arr[0])
        m = len(arr[0])
        
        dp = arr[0]
        for i in range(1, n):
            dp_tmp = dp.copy()
            for j in range(m):
                local_min = sys.maxsize
                for z in range(m):
                    if z != j:
                        local_min = min(local_min, dp_tmp[z])
                dp[j] = local_min + arr[i][j]
        return min(dp)
```
8. LC487 <br />
···
未/行使过权利两种状态
···