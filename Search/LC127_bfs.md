#### Solution BFS
thinking process: find the one-step transformation of each curreng queue word, if the new word in dictionary and not seen before, add it into the new queue. <br />

1. search list -> using set <br />
2. queue -> using collections.deque()

```
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0
        
        queue = collections.deque()
        seen = set()
        step = 0
        dicts = 'abcdefghijklmnopqrstuvwxyz'
        n = len(beginWord)
        
        queue.append(beginWord)
        seen.add(beginWord)
        
        while queue:
            step += 1
            queue_size = len(queue)
            while queue_size > 0:
                queue_size -= 1
                vertex = queue.popleft()
                for i in range(n):
                    for j in dicts:
                        if i + 1 == n:
                            newWord = vertex[:i] + j
                        else:
                            newWord = vertex[:i] + j + vertex[i+1:]
                        if newWord == endWord: return step + 1
                        elif (newWord in seen) or (newWord not in wordList): continue
                        else:
                            seen.add(newWord)
                            queue.append(newWord)
        return 0
```