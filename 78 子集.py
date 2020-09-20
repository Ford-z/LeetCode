#给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。说明：解集不能包含重复的子集。

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]#直接从后遍历，遇到一个数就把所有子集加上该数组成新的子集
        for i in range(len(nums)):
            for subres in res[:]: res.append(subres+[nums[i]])
        return res
