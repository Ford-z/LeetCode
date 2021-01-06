#给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or  not head.next:
            return None
        fast=head
        slow=head
        for i in range(n):#找正数
            if(fast.next):
                fast=fast.next
            else:
                return head.next
        while(fast.next):
            fast=fast.next
            slow=slow.next#找倒数
        slow.next=slow.next.next
        return head
