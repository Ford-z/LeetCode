#给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if(num<=0):
            return False
        n=4 ** int(math.log(num, 4))
        return n==num
