#给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。
#你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。
#请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        now=0
        m=0
        for i in range(len(nums)):
            now+=nums[i]
            m=min(m,now)
        return 1-m
