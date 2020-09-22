#将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            nums1=nums[0:mid]
            nums2=nums[mid+1:len(nums)]
            root.left=self.sortedArrayToBST(nums1)
            root.right=self.sortedArrayToBST(nums2)
            return root 
