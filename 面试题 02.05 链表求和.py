#给定两个用链表表示的整数，每个节点包含一个数位。

#这些数位是反向存放的，也就是个位排在链表首部。

#编写函数对这两个整数求和，并用链表形式返回结果。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tem=0
        a=1
        while(l1!=None):
            tem+=pow(10,a-1)*l1.val
            l1=l1.next
            a+=1
        res=0
        b=1
        while(l2!=None):
            res+=pow(10,b-1)*l2.val
            l2=l2.next
            b+=1
        ans=res+tem
        ans=str(ans)
        head = ListNode(-1)
        p = head
        for i in range(len(ans)-1,-1,-1):
            p.next = ListNode(int(ans[i]))
            p = p.next
        return head.next
