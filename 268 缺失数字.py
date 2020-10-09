#给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        a=n*(n+1)//2
        b=sum(nums)
        return a-b
