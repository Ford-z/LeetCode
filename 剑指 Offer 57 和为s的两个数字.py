#输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        while l<r:
            temp=nums[l]+nums[r]
            if temp==target:
                return [nums[l],nums[r]]
            elif temp>target:
                r-=1
            else:
                l+=1
        return []
