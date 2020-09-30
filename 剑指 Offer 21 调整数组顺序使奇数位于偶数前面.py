#输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if i%2==0:
                b.append(i)
            else:
                a.append(i)
        return a+b
