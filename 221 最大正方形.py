#在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        if(n<=0):
            return 0
        m=len(matrix[0])

        ans=0
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(matrix[i-1][j-1]=="1"):
                    a=int(min(dp[i-1][j-1],dp[i-1][j]))
                    b=min(a,dp[i][j-1])
                    dp[i][j]=1+b
                    ans=max(ans,dp[i][j])
        return (ans*ans)
