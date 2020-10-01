#一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor, ans = 0, [0, 0]
        for num in nums:
            xor ^= num
        flag=(-xor)&xor#最低位为1的二进制（从右到左）
        for num in nums:
            if(flag&num==0):
                ans[0]^=num
            else:
                ans[1]^=num
        return ans
