### Solution
新建之后，cur=head,然后值都是接在cur.next后面。错误的写法: head=ListNode(), cur = head.next, (in looping) cur = ListNode(...)这样cur实际和head就没关系了。正确的写法：head=ListNode(0), cur = head, (in looping)cur.next = ListNode(...)。
最后记得如果还余pre，要加1
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        
        cur1 = l1
        cur2 = l2
        cur = head
        pre = 0
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            cur.next = ListNode((val1 + val2 + pre)%10)
            pre = (val1 + val2 + pre)//10
           
            cur = cur.next
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        if pre:
            cur.next = ListNode(pre)
        return head.next
```