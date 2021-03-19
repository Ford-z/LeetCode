#给定一个整数 n，返回 n! 结果尾数中零的数量。
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        while(n>=5):
            ans+=n//5#计算有多少个5的因子。必须要整除
            n//=5
        return ans
