#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(1, n):
            nums[i]= nums[i] + max(nums[i-1], 0)#到前一项为止的最大子序和
        return max(nums)
