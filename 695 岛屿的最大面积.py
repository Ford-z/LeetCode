#给定一个包含了一些 0 和 1 的非空二维数组 grid 。
#一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
#找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/max-area-of-island
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.cnt = 0
        n=len(grid)
        if(n==0):
            return 0
        m=len(grid[0])

        def dfs(grid,r,c):
            n=len(grid)
            m=len(grid[0])
            if(r<0 or r>=n or c<0 or c>=m or grid[r][c]==0):
                return 0
            self.cnt+=1
            grid[r][c]=0
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(grid, x, y)

        for r in range(n):
            for c in range(m):
                if(grid[r][c]==1):
                    self.cnt=0
                    dfs(grid,r,c)
                    self.ans=max(self.ans,self.cnt)
        return self.ans
