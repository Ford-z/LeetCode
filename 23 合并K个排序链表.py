# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        a = []#用于存储所有的数据
        head = point = ListNode(0)
        for junction in lists:
            while (junction!=None):
                a.append(junction.val)
                junction = junction.next
        a=sorted(a)
        for x in a:
            point.next = ListNode(x)
            point = point.next
        return head.next
