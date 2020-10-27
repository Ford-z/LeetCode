#给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#说明：每次只能向下或者向右移动一步。
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if(n==0):
            return 0
        m=len(grid[0])
        if(m==0):
            return 0
        dp=[[float('inf')]*m for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[0][i]=dp[0][i-1]+grid[0][i]#0行处理方式
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]+grid[i][0]#0列处理方式
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        return dp[-1][-1]
