#给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
class Solution:
    def cuttingRope(self, n: int) -> int:
        if(n>2):
            dp=[0]*(n+1)
            for m in range(2,n):
                a=n//m
                t=n%m
                q=m-t
                dp[m]=pow(a,q)*pow(a+1,t)
            return max(dp)
        if(n==2):
            return 1
        if(n==1):
            return 0
