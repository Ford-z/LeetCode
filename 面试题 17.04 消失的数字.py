#数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(nums)
        n=len(nums)+1
        return n*(n-1)//2-a
