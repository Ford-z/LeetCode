#有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#求所能获得硬币的最大数量。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/burst-balloons
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#https://qoogle.top/leetcode-312-burst-balloons/
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        if(n>2):
            nums = [1] + nums + [1]#不需要处理上下界
            dp=[[0]*len(nums) for _ in range((len(nums)))]
            for i in range(len(nums) - 1, -1, -1):
                for j in range(i + 2, len(nums)):
                    for k in range(i + 1, j):
                        dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
            return dp[0][-1]
        elif(n==2):
            temp=max(nums[0],nums[-1])
            ans+=nums[0]*nums[-1]+temp
            return ans
        elif(n==1):
            return nums[0]
        elif(n==0):
            return 0


            
