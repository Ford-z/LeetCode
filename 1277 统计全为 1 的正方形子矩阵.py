#给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        if(m<=0):
            return sum(matrix)
        n=len(matrix[0])
        #dp[i][j]表示 matrix[i][j] 这个点可以往左上构造的最大正方形的边长，然后求和就行了
        dp=[[0]*n for _ in range(m)]
        ans=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    continue
                if i==0 or j==0:
                    dp[i][j]=matrix[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                ans+=dp[i][j]
        return ans
