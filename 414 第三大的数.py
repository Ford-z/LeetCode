#给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if(len(nums)<=2):
            return max(nums)
        nums.sort()
        third=nums[-1]
        count=1
        i=len(nums)-2
        while(i>=0):
            if(count==3):
                break
            if(third>nums[i]):
                third=nums[i]
                count+=1
            i-=1
        if(count!=3):
            return max(nums)
        return third
