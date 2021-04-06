#给定一个只包含 0 和 1 的网格，找出其中角矩形的数量。

#一个「角矩形」是由四个不同的在网格上的 1 形成的轴对称的矩形。注意只有角的位置才需要为 1。并且，4 个 1 需要是不同的。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/number-of-corner-rectangles
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row-1):
            one=[]
            for k in range(col):
                if grid[i][k]==1:
                    one.append(k)
            for j in range(i+1,row):
                ans=0
                for a in one:
                    if grid[j][a]==1:
                        ans+=1
                res+=ans*(ans-1)//2
        return res
