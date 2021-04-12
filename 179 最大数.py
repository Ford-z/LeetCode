#给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
#注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans=''
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                    nums[i],nums[j]=nums[j],nums[i]
        for i in nums:
            ans+=str(i)
        return str(int(ans))
