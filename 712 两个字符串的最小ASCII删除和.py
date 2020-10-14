#给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n=len(s1)
        m=len(s2)
        dp=[[float('inf') for _ in range(m+1)] for i in range(n+1)]
        dp[0][0]=0
        for i in range(n):
            dp[i+1][0]=dp[i][0]+ord(s1[i])#横排为字符串1
        for i in range(m):
            dp[0][i+1]=dp[0][i]+ord(s2[i])#竖排为字符串2

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:#新增的两个字符相等的情况下，没有必要删除之前的结果
                    dp[i][j]=dp[i-1][j-1]
                else:#保留s2串，删除s1串的字符或保留s1串，删除s2串的字符，每一次选择最小
                    dp[i][j]=min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))

        return dp[-1][-1]
        
