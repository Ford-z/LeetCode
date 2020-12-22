#反转一个单链表。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p,ans=head,None
        while p:
            ans,ans.next,p=p,ans,p.next
        return ans
