#给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/target-sum
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        a=sum(nums)
        if(a<S or (a + S) % 2 == 1):
            return 0
        w=int((a+S)/2)
        # sum(P) - sum(N) = target 
        #=> sum(nums) + sum(P) - sum(N) = target + sum(nums)
        #=> 2 * sum(P) = target + sum(nums) 
        #=> sum(P) = (target + sum(nums)) / 2
        dp=[0]*(w+1)
        dp[0]=1
        for i in range(len(nums)):
            for j in range(w,nums[i]-1,-1):
                dp[j]+=dp[j-nums[i]]
        return dp[w]
