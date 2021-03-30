#输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:1+index],inorder[:index])#取前序的index位，中序的根节点的前index位
        root.right=self.buildTree(preorder[1+index:],inorder[index+1:])
        return root
