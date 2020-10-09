#给定两个数组，编写一个函数来计算它们的交集。
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=list(set(nums1) & set(nums2))#set用于数组中单个出现，&求交集
        return ans
