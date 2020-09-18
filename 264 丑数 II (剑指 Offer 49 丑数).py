#编写一个程序，找出第 n 个丑数。
#丑数就是质因数只包含 2, 3, 5 的正整数。
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[0 for _ in range(n)]
        dp[0]=1
        a=0
        b=0
        c=0
        i=1
        while(i<n):
            dp[i]=min(min(dp[a]*2,dp[b]*3),dp[c]*5)
            if(dp[i]/dp[a]==2):
                a+=1
            if(dp[i]/dp[b]==3):
                b+=1
            if(dp[i]/dp[c]==5):
                c+=1
            i+=1
        return dp[n-1]
