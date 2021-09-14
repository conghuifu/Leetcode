## Heap
Heap本质是用一个array实现的complete binary tree，这个tree的root节点代表整个heap里最大(max heap)或者最小值(min heap)，只有root节点很重要，其他的节点都没啥关系，当然parent是比儿子大的<br />
common apis: <br />
1. peek() -> 查看堆顶元素O(1) <br />
2. poll() -> 拿出堆顶元素O(logN) <br />
3. offer() -> 添加元素O(logN) <br />
```
heapq.heappush(heap, item)
将 item 的值加入 heap 中，保持堆的不变性。

heapq.heappop(heap)
弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

heapq.heappushpop(heap, item)
将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。

heapq.heapify(x)
将list x 转换成堆，原地，线性时间内。
```
### Online vs Offline Algorithms
#### Online algorithm (using heap):
针对一组流数据，没有固定长度，可以随时根据需求scalable
#### Offline algorithm (using sorting):
针对一组固定长度数据，每次scale后要重新计算

### Top K 问题
1. LC215 <br />
本题有三种解法： <br />
a. sorting O(nlogn) <br />
b. max heap O(n+klogn) <br />
heapify the array, then pool k times <br />
c. min heap O(nlogk) <br />
c1. maintain a size k min heap <br />
c2. add element to min heap if greater than or equal to the top element, adjust size if necessary <br />
c3. at the end top of heap is the kth largest <br />
Explaination: since we are adding greater elemnts if the heap every time. At the end, the top of min heap is the smaleest amoung elemnts in the heap, but it is still greater than the other element in the array, which in other words: kth largest element <br />
```
# 1. initialize a min heap
# 2. for each element x in array
# 	a. offer to heap size < k or x >= top of heap
# 	b. adjust heap size if necessary
# 3. return the top of heap

```
2. LC23（先学下tree和linkedlist）