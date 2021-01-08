#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k<=n:
            times=n-k
            for i in range(0,times):
                a=nums.pop(0)
                nums.append(a)
        else:
            for i in range(0,k%n):
                a=nums.pop(-1)
                nums.insert(0,a)
