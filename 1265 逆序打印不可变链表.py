#给您一个不可变的链表，使用下列接口逆序打印每个节点的值：

#ImmutableListNode: 描述不可变链表的接口，链表的头节点已给出。
#您需要使用以下函数来访问此链表（您 不能 直接访问 ImmutableListNode）：

#ImmutableListNode.printValue()：打印当前节点的值。
#ImmutableListNode.getNext()：返回下一个节点。
#输入只用来内部初始化链表。您不可以通过修改链表解决问题。也就是说，您只能通过上述 API 来操作链表。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/print-immutable-linked-list-in-reverse
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head==None:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()
