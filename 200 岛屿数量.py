#给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#此外，你可以假设该网格的四条边均被水包围。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/number-of-islands
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def dfs(self,grid,r,c):
        grid[r][c]=0
        n=len(grid)
        m=len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        n=len(grid)
        if(n==0):
            return 0
        m=len(grid[0])


        for r in range(n):
            for c in range(m):
                if(grid[r][c]=="1"):
                    ans=ans+1
                    self.dfs(grid,r,c)
        return ans
