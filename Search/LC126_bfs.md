#### Solution BFS + DFS
different from wordLadder I: <br />
1. cannot break down when found the newWord == endWord, but we know we wont do the next looping because the further steps are not the shortest. Also we know that the words appeared in last looping should not appear again in current looping, because if yes the steps will be longer. But the words can apeear several times in current looping, we have different paths to the shortest path. So we need a dummy found to indicate should we finish in current loop, and also the seen and localSeen. <br />
2. we need the parents(<key, set()>) to record the relationships between nodes and parents. one node can have several parents. <br />
3. we need steps to record how mant step we need to trace back in DFS.
```
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList: return []
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        queue = collections.deque([beginWord])
        seen = set([beginWord])
        l = len(beginWord)
        parents = {beginWord: None}
        step = 0
        found = False
        dicts = 'abcdefghijklmnopqrstuvwxyz'
        
        while (queue) and (not found):
            queue_size = len(queue)
            step += 1
            localSeen = set()
            for _ in range(queue_size):
                vertex = queue.popleft()
                for i in range(l):
                    for j in dicts:
                        newWord = vertex[:i] + j + vertex[i+1:]
                        if (newWord in seen) or (newWord not in wordList): continue
                        else:
                            if newWord in parents:
                                parents[newWord].add(vertex)
                            else:
                                parents[newWord] = set([vertex])
                            localSeen.add(newWord)
                            queue.append(newWord)
                            if newWord == endWord:
                                found=True
            seen = seen.union(localSeen)
        if len(parents) == 1:
            return []
        
        def dfs(node, path, step):
            if step == 0:
                ans.append(path[::-1])
                return
            else:
                for parent in parents[node]:
                    path.append(parent)
                    dfs(parent, path, step-1)
                    path.pop()
        
        ans = []
        dfs(endWord, [endWord], step)
        return ans
```


### recapping
```
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        replace = 'abcdefghijklmnopqrtsuvwxyz'
        queue = collections.deque([(beginWord, [beginWord])])
        wordList = set(wordList)
        visited = set()
        ct = 1
        
        while queue:
            size = len(queue)
            ct += 1
            tmp = set()
            for _ in range(size):
                cur, curlist = queue.popleft()
                for i in range(len(cur)):
                    for j in replace:
                        new = cur[:i] + j + cur[i+1:]
                        if (new in wordList) and (new not in visited):
                            if new == endWord:
                                res.append(curlist + [new])
                            tmp.add(new)
                            queue.append((new, curlist + [new]))
            visited = visited.union(tmp)
        return res
```