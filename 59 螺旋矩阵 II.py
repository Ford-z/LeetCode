#给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a=[[0]*n for _ in range(n)]
        c=1
        j=0
        while(c<=n*n):
            for i in range(j,n-j):#右移
                a[j][i]=c
                c+=1
            for i in range(j+1,n-j):#下移
                a[i][n-j-1]=c
                c+=1
            for i in range(n-j-2,j-1,-1):#左移
                a[n-j-1][i]=c
                c+=1
            for i in range(n-j-2,j,-1):#上移
                a[i][j]=c
                c+=1
            j+=1
        return a
            
