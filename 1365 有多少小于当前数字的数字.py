#给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
#换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
#以数组形式返回答案。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            t=nums[i]
            for j in range(0,i):
                if(nums[j]<t):
                    ans[i]+=1
            for j in range(i,n):
                if(nums[j]<t):
                    ans[i]+=1
        return ans
