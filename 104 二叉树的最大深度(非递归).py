#给定一个二叉树，找出其最大深度。

#二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

#说明: 叶子节点是指没有子节点的节点。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        queue = collections.deque()#双端队列
        queue.append(root)
        ans=0
        while queue:
            ans+=1
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
