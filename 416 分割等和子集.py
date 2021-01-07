#给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        a=sum(nums)
        if a%2==1:
            return False#元素和为奇数，一定不可能分割
        v=a//2#转化为sum一半的背包问题
        dp=[0]*(v+1)
        for i in range(0,len(nums)):
            for j in range(v,nums[i]-1,-1):
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])#表示每一轮分析中j空间最多装下的数字总和
        return dp[-1]==v
