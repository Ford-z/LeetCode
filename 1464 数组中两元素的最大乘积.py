#给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
#请你计算并返回该式的最大值。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=nums
        if(len(nums)>1):
            i=max(nums)
            k=a.index(i)
            a.pop(k)
            j=max(a)
            ans=(i-1)*(j-1)
            return ans
        else:
            return 0
