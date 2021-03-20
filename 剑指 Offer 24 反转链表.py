#定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack=[]
        q=head
        p=head
        while(p!=None):
            stack.append(p.val)
            p=p.next
        while(stack):
            q.val=stack.pop()
            q=q.next
        return head
        
