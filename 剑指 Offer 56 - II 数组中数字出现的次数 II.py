#在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            a=nums[0:i]+nums[i+1:n]
            if nums[i] not in a:
                return nums[i]
        return -1
