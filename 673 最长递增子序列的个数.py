#给定一个未排序的整数数组，找到最长递增子序列的个数。
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size=len(nums)
        if(size<=1):
            return size
        dp=[1]*size
        count=[1]*size
        for i in range(1,size):
            for j in range(i):
                if(nums[j]<nums[i]):
                    if(dp[j]+1>dp[i]):#新状态长度没有更长，长度更新为最长，次数不变
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif(dp[j]+1==dp[i]):#新状态长度比以前状态大1，长度不用更新，次数累计
                        count[i]+=count[j]
        a=max(dp)
        ans=0
        for i in range(size):
            if(dp[i]==a):
                ans+=count[i]
        return ans
