#在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        for i in range(1, m): 
            grid[0][i] += grid[0][i - 1] #初始化第一行
        for j in range(1, n): 
            grid[j][0] += grid[j - 1][0] #初始化第一列
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j]) #比较上一步应该走右边还是走左边
        return grid[n-1][m-1]
