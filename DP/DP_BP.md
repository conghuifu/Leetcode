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

##### IV：第I类区间型DP
给出一个序列，明确要求分割成K个连续区间，要你计算这些区间的某个最优性质。一般看到让分成k个子串，就是区间型的DP <br />
套路：<br />
1. 状态定义: dp[i][k]表示针对s[i:]分成k个区间，此时能够得到的最优解 <br />
2. 搜寻最后一个区间的起始位置j，将dp[i][k]分割成dp[j-1][k-1]和s[j:i]两部分 <br />
3. 最终结果是dp[N][K] <br />
find the best j: <br />
xxxxxxxxxxxx | jxxxxi <br />
dp[j-1][k-1]   s[j:i] <br />
```
###
状态的转移：
1. 第一层循环遍历i
2. 第二层循环遍历k
3. 第三层循环寻找最优的位置j作为一个分区的起始位置
4. 将dp[i][k]分成dp[j-1][k-1]和s[j:i]求解
###

for i in range(1, n+1):
	# K不能太大，否则不够i个元素分
	for k in range(1, min(i, K)):
		# j不能太小，否则不够分成k-1组
		for j in range(i, k-1, -1):
			dp[j-1][j-1] + count[j][i]
Ans = dp[N][K]

# 注意边界条件: dp[x][0], dp[0][0]
```

1. LC1278 <br />
一般不知道怎么定义dp就直接照抄题目啦～  <br />
dp[i][k]: the minimal number of characters that you need to change to divide the string s[0:i] into k (k is different from K) substrings that they are all palindromes. <br />
[XXXXXX][j XX i] <br />
1. 算[j XX i]的操作: helper(s[j:i]) <br />
2. 算s[:j-1]分成k-1份的最小操作数: dp[i-1][k-1]<br />
3. dp[i][k] = min{dp[j-1][k-1] + helper(s[j:i])} for j=1,....,i

```
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        m = len(s)
        
        dp = [[m+1 for j in range(k+1)] for i in range(m+1)]
        dp[0][0] = 0
        
        for i in range(1, m+1):
            for K in range(1, min(i, k)+1):
                for j in range(K, i+1):
                    dp[i][K] = min(dp[i][K], dp[j-1][K-1] + self.helper(s, j, i))   
        return dp[-1][-1]
    
    def helper(self, s, i, j):
        ct = 0
        while i < j:
            if s[i-1] != s[j-1]:
                ct += 1
            i += 1
            j -= 1
            
        return ct
```
这里运行时间久，主要是每次都要重复调用helper函数计算次数，这可以预先算好存起来，这个也是dp的一种。之后再说
2. LC1335
3. LC410

##### V：第II类区间型DP
只给出一个序列S（数组/字符串），求一个针对这个序列的最优解<br />
适用条件：这个最优解对于序列的index而言，没有“后效性”。即无法设计dp[i]，使得dp[i]仅依赖于dp[j](j<i)。但是最大区间的最优解，可以依赖小区间的最优解<br />
套路：<br />
1. 定义dp[i][j]：表示针对s[i:j]的子问题求解<br />
2. 千方百计将区间dp[i][j]往小区间的dp[i'][j']转移（第一层循环时区间大小，第二层循环是起始点）<br />
3. 最终的结果是dp[1][N]

###### 例题
1. LC516 <br />
2. LC312 <br />
3. LC375 <br />
4. LC1246

##### VI：第I类+第II类区间型DP Boss题
第I类是分成K个区间，第II类是小问题到大问题，你得先找到[i:j]分成k堆的最优解，再找到全局的最优解。所以是dp[i][j][k].<br />
iXXXXXXXXXXXXXXmXXXXXXXXXXj <br />
dp[i][m-1][k-1] dp[m][j][1]
套路: <br />
```
# dp[i][j][k]表示将区间[i:j]归并成k堆的最小代价
for length in range(1, N+1):
    for i in range(1, N-length+2):
        j = i+lenngth-1
        for k in range(2, K+1):
            for m in range(i, j+1):
                dp[i][j][k] = min(dp[i][j][k], dp[i][m-1][k-1] + dp[m][j][1])
        dp[i][j][1] = dp[i][j][K] = sum[i:j]
return dp[1][N][1]
# 特别注意：当k=1时，dp[i][j][1]只能由dp[i][j][K]转化而来
```

###### 例题
1. LC 1000
```
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1)%(k-1) != 0: return -1 # 这个条件没有很懂
        
        dp = [[[sys.maxsize for K in range(k+1)] for j in range(n+1)] for i in range(n+1)]
        for i in range(1, n+1):
            dp[i][i][1] = 0
        
        summ = [0 for i in range(n+1)]
        for i in range(1, n+1):
            summ[i] = summ[i-1] + stones[i-1]
        
        
        for length in range(2, n+1):
            for i in range(1, n-length+2):
                j = i+length-1
                for K in range(1, k+1):
                    # 优化1
                    if K > length: continue
                    for m in range(i, j):
                        # 如果没有更新就说明不能分啦，所以continue
                        if (dp[i][m][K-1] == sys.maxsize) or (dp[m+1][j][1] == sys.maxsize): continue
                        dp[i][j][K] = min(dp[i][j][K], dp[i][m][K-1]+dp[m+1][j][1])
                # 一样没有更新就不能分
                if dp[i][j][k] != sys.maxsize:
                    dp[i][j][1] = dp[i][j][k] + summ[j] - summ[i-1]
        
        if dp[1][n][1] == sys.maxsize: return -1
        return dp[1][n][1]
```

##### VII：背包入门问题
给出N个物品，每个物品可用可不用或者有若干个不同的用法（！！！！）要求以某个有上/下限的C的代价来实现最大收益。利用了物品的无后效性：在前四件物品中做选择的最大收益，和第五件物品没关系。其将各个物品是否使用的高维向量，替换成了代价的解空间。上限是C。<br />
套路：<br />
1. 定义dp[i][c]:表示考虑只从前i件物品的子集里选择代价为c的最大收益,c=1,2,...,C <br />
2. 千方百计把dp[i][c]往dp[i-1][c']转移，即考虑如何使用物品i，对代价/收益的影响 <br />
2a.第一层循环是物品编号<br />
2b.第二层循环是所有可能的代价c' <br />

3. 最终的结果是max(dp[N][c]) 1<=c<=N <br />
这里要注意哦，最大值不一定在代价最大的地方招。注意这个套路是exactly代价为c的时候哦，不是不超过c
```
for i in range(1, N+1):
    for c in range(1, C+1):
        dp[i][c] = max(dp[i-1][c], dp[i-1][c-wi]+vi)
Ans = maxc{dp[N][c]}
# 注意边界条件: dp[0][0] = 0
# dp[0][c] = NA (非法值，可以定义取不到的)

```

###### 例题
1. LC 494 <br />
这道题能想到dp主要因为：1. 给每个元素加正负号-》每个元素可加可不加-〉相当于用不用 2. 空间不是很大，target最多就是-sum~sum <br />
2. LC1049 <br />
3. LC474 <br />
4. LC879 <br />
5. LC956


##### 状态压缩
#### 这个太难了，以后再说吧
对于比较复杂的状态，dp经常会用到“状态压缩”的技巧。比如：有些情况下如果想设计状态代表一个01向量（不超过32位），我们可以用一个整形的bit位来表示<br/>
例如[1,0,1,1,0,0,1] => b1011001 => 89 <BR />
1. LC648 <br />
2. LC943


##### homework
1. I类基本LC903 2. II类基本LC983 3. II类区间LC546（过于险恶先不做了） 4. 背包LC518