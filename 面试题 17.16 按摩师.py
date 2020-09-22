#一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/the-masseuse-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def massage(self, nums: List[int]) -> int:
        if(len(nums)>=2):
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            i=2
            while(i<len(nums)):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])#不选以及选的利益最大化
                i+=1
            return dp[len(nums)-1]
        elif(len(nums)==1):
            return nums[0]
        else:
            return 0
