
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1
        a=ListNode(0)
        ans=a
        while l1!=None and l2!=None:
            if (l1.val<l2.val):
                ans.next=l1
                l1=l1.next
            else:
                ans.next=l2
                l2=l2.next
            ans=ans.next
        ans.next=l1 if l1 else l2
        return a.next
