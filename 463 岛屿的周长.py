#给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
#网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/island-perimeter
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        if(n==0):
            return 0
        m=len(grid[0])


        for r in range(n):
            for c in range(m):
                if(grid[r][c]==1):
                    ans+=4
                    if(grid[r-1][c]==1and r-1>=0):
                        ans-=2
                    if(grid[r][c-1]==1and c-1>=0):
                        ans-=2
        return ans
    
        
