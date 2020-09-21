#给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#以右->根->左的顺序遍历二叉树，将遍历顺序的前一个结点的累加值记录起来，和当前结点相加，得到当前结点的累加值。

class Solution:
    num=0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if(root!=None):
            self.convertBST(root.right)
            root.val = root.val + self.num
            self.num = root.val
            self.convertBST(root.left)
            return root
        return None

