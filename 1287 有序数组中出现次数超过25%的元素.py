#给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。请你找到并返回这个整数
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for x in arr:
            num = arr.count(x)
            if num > n/4:
                return x
