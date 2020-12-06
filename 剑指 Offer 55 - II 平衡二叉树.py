#输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if(root==None):
            return True
        l=self.height(root.left)
        r=self.height(root.right)
        if(abs(l-r)>1):
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    

    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
