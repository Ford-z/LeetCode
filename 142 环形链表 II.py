#给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

#为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return None
        hare,t=head,head
        while(hare!=None and hare.next!=None):
            hare=hare.next.next
            t=t.next
            if(hare==t):
                break
        if(hare!=t):
            return None
        q=head
        while(q!=t):
            q=q.next
            t=t.next
        return t
