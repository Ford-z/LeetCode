#班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
#给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/friend-circles
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n=len(M)
        temp=[0]*n
        ans=0
        def dfs(M,i,temp):
            temp[i]=1
            n=len(M)
            for j in range(n):
                if(M[i][j]!=0 and temp[j]==0):
                    dfs(M,j,temp)
        for i in range(n):
            if(temp[i]==0):
                ans+=1
                dfs(M,i,temp)
        return ans
