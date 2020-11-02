#给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<3):
            return 0
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
