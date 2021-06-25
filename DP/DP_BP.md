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
```
# 未/行使过权利两种状态
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        
        # p：未行权， q: 行权
        p = nums[0]
        q = 1
        
        res = max(p, q)

        for i in range(1, n):
            p_tmp, q_tmp = p, q
            p = (p_tmp + 1) * nums[i]
            q = max((q_tmp + 1) * nums[i], p_tmp + 1)
            res = max(p, q, res)
        return res
```

##### II类基本型 - “时间序列”加强型
给一个序列，其中每个元素可以认为是‘一天’，但今天的状态是和之前的某一天有关，需要挑选 <br />
套路： <br />
1. dp[i]:表示ith状态，一半这个状态要求和元素i有直接关系 <br />
2. 关联dp[i]和dp[i'] （但是肯定不能和大于i的状态有关系）<br />
3. 最终结果是dp[i]中的某一个

###### 例题
1. LC300
```
# 两个for 循环
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
```
2. 368 <br />
这题需要打印其中一条path，所以需要两个dp数组，count存数量，dp存上一个index。index起始应该是一个distinguished value，以便结尾再回溯的时候有终止条件。然后res从count最大index开始粘，while maxIndex != -1: res.append(nums[maxIndex]), maxIndex = dp[maxIndex]
```
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1: return nums
        
        nums.sort()
        dp = [-1 for i in range(n)]
        count = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if count[j] + 1 >= count[i]:
                        count[i] = count[j] + 1
                        dp[i] = j
        maxIndex = count.index(max(count))
        res = []
        while maxIndex != -1:
            res.append(nums[maxIndex])
            maxIndex = dp[maxIndex]
        return res
```
3. 1186 <br />
这题巧妙之处在于，dp每个元素，存的是到i时的total height
```
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0: return 0
        if n == 1: return arr[0]
        
        # p: havent deleted, q: deleted
        p, q = arr[0], 0
        res = p
        for i in range(1, n):
            p_tmp, q_tmp = p, q
            p = max(0, p_tmp) + arr[i]
            q = max(q_tmp + arr[i], p_tmp, arr[i])
            res = max(res, p, q)
        return res
```

##### III双时间序列型
给两个序列s和t，让你对他们搞事情 <br />
longtest common subsequence, shortest common sequence, edit distances <br />
套路： <br />
1. 定义dp[i][j]: 表示针对s[1:i]和t[1:j]的子问题的求解（基本问啥设啥，加一个定语） <br />
2. 千方百计将dp[i][j]往之前的状态去转移：dp[i-1][j], dp[i][j-1]和dp[i-1][j-1] <br />
3. 最终结果是dp[m][n] <br />

###### 例题
1. 1143 <br />
看两个序列是否match，建立dp[i][j]表示s[i]和t[j]之间的关系。如果满足则dp[i-1][j-1] + val，否则引用dp[i-1][j]或者dp[i][j-1]的值。这里一个trick，比较两遍string大小，dp设m+1, n+1 dims，这样第一位为空，则都是0，不用考虑边界问题。就是记得for looping循环locate原array要减1
```
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        if (m == 0) or (n == 0): return 0
        
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
```
2. LC1092 <br />
这道题就是要多打一个path，回溯dp[i][j]的值是从哪里来的就好了
```
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        
        if m == 0: return str2
        if n == 0: return str1
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        
        # then trace back the routh
        i, j = m, n
        res = ''
        while (i > 0) and (j > 0):
            if str1[i-1] == str2[j-1]:
                res = str1[i-1] + res
                i -= 1
                j -= 1
            else:
                if dp[i][j] == dp[i-1][j] + 1:
                    res = str1[i-1] + res
                    i -= 1
                else:
                    res = str2[j-1] + res
                    j -= 1
        if i > 0:
            res = str1[:i] + res
        if j > 0:
            res = str2[:j] + res
        
        return res
```
3. LC72 
```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m == 0: return n
        if n == 0: return m
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    
        return dp[-1][-1]
```
4. LC97 <br />
这题要小心，把0，0的边界指标写进loop，因为可以不选，不能从1，1开始啦
```
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        if m == 0: return s2 == s3
        if n == 0: return s1 == s3
        if m + n != len(s3): return False
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = 1
        
        for i in range(m+1):
            for j in range(n+1):
                if (i == 0) and (j == 0):
                    dp[0][0] = 1
                elif j == 0:
                    if dp[i-1][j] == 1:
                        dp[i][j] = int(s1[i-1] == s3[i-1])
                elif i == 0:
                    if dp[i][j-1] == 1:
                        dp[i][j] = int(s2[j-1] == s3[j-1])
                else:
                    if (s1[i-1] == s3[i+j-1]) and (dp[i-1][j] == 1):
                        dp[i][j] = 1
                    elif (s2[j-1] == s3[i+j-1]) and (dp[i][j-1] == 1):
                        dp[i][j] = 1
        return dp[-1][-1] == 1
```