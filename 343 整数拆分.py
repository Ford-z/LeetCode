#给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
class Solution:
    def integerBreak(self, n: int) -> int:
        if(n==2):
            return 1
        if(n==3):
            return 2
        if(n==4):
            return 4
        a=1
        while(n>4):
            n=n-3
            a*=3
        return a*n
