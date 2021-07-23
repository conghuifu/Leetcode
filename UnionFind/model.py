# for union find. find complexity is O(n), union is also O(n). 
# If we have k connections and n numbers, the complexity will be Union + Find
# Union: O(n); Find: O(1)


class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        
    def find(self, x):
        #说明x的头头就是它自己，不用找了
        if x == self.parents[x]:
            return x

        # 如果不是的话，就找他爷爷，反正继续找，最后一定能找到，然后把找到的值，赋值给x
        self.parents[x] = self.find(parents[parents[x]])
        return self.parents[x]
    
    def union(self, x, y):
        d1 = self.find(x)
        d2 = self.find(y)
        
        if d1 != d2:
            self.parents[d1] = d2
            
data = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 8], [7, 9]]
uf = UnionFind(10)
for x, y in data:
    uf.union(x, y)
for x in range(10):
    uf.find(x)