#给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        ans=[]
        cur=root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()#回溯
                ans.append(cur.val)
                cur=cur.right
        return ans
