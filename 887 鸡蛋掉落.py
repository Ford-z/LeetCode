#你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。

#每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。

#你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。

#每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。

#你的目标是确切地知道 F 的值是多少。

#无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-egg-drop
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        head.next=self.deleteDuplicates(head.next)
        if(head.val==head.next.val):
            head=head.next
        return head
