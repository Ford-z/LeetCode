#给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动将会使 n - 1 个元素增加 1。
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        m = min(nums)
        for x in nums:
            ans+=x-m
        return ans
