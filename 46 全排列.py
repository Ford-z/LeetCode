#给定一个 没有重复 数字的序列，返回其所有可能的全排列。
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def back(nums,res):
            if not nums:
                ans.append(res)
                return
            for i in range(len(nums)):
                back(nums[:i]+nums[i+1:],res+[nums[i]])
        back(nums,[])
        return ans
