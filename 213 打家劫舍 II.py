#你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/house-robber-ii
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def rob(self, nums: List[int]) -> int:
        #其实就是把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。
        n = len(nums)
        if n == 0:
          return 0
        if n <= 2:
          return max(nums)
        dp1=[0]*n
        dp1[1]=max(0,nums[1])
        dp2=[0]*n
        dp2[0]=nums[0]
        dp2[1]=max(nums[0],nums[1])
        for i in range(2,n):#不抢第一个
            dp1[i]=max(dp1[i-1],dp1[i-2]+nums[i])
        for i in range(2,n-1):#不抢最后一个
            dp2[i]=max(dp2[i-1],dp2[i-2]+nums[i])
        return max(dp1[-1],dp2[-2])
