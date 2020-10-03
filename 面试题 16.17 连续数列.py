#给定一个整数数组，找出总和最大的连续数列，并返回总和。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value, cur_value = nums[0], 0
        for num in nums:
            cur_value += num
            max_value = max(max_value, cur_value)#记录最大值
            cur_value = max(cur_value, 0)#比较是否需要排除
        return max_value
