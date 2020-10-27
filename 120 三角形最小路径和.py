#给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/triangle
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        if(n<=0):
            return 0
        dp=[0]*(n+1)
        i=n-1
        while(i>=0):
            m=len(triangle[i])
            for j in range(m):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
            i-=1
        return dp[0]
