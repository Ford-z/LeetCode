#翻转一棵二叉树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if(root==None):
            return root
        else:
            treeNode = root.left
            root.left = root.right
            root.right = treeNode
            root.left=self.invertTree(root.left)#针对子树
            root.right=self.invertTree(root.right)
        return root
