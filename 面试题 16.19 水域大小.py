#你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/pond-sizes-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        a=[]
        n=len(land)
        if(n==0):
            return 0
        m=len(land[0])
        def dfs(land,r,c):
            nonlocal cnt
            n=len(land)
            m=len(land[0])
            if land[r][c] == 0:
                cnt +=1
            land[r][c]=1
            for x,y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1),(r+1,c+1),(r+1,c-1),(r-1,c+1),(r-1,c-1)]:
                if(0<=x<n and 0<=y<m and land[x][y]==0):
                    dfs(land,x,y)

        for r in range(n):
            for c in range(m):
                if(land[r][c]==0):
                    cnt=0
                    dfs(land,r,c)
                    a.append(cnt)
        a.sort()
        return a
