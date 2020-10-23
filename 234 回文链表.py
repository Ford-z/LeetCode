# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s1=0
        s2=0
        t=1

        while head!=None:
            s1=s1*10+head.val
            s2=s2+t*head.val
            t=t*10
            head=head.next
        
        return s1==s2
