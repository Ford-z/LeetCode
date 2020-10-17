#给定一个无序的整数数组，找到其中最长上升子序列的长度
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        dp=[1]*size
        for i in range(1,size):
            for j in range(i):
                if(nums[i]>nums[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
