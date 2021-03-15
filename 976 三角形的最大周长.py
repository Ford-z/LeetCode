#给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

#如果不能形成任何面积不为零的三角形，返回 0。
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            if nums[i]<nums[i-1]+nums[i-2]:
                return nums[i]+nums[i-1]+nums[i-2]
        return 0
