#设计一个算法，算出 n 阶乘有多少个尾随零。
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        while(n):
            n//=5
            ans+=n
        return ans
