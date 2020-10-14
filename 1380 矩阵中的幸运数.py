#给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
#幸运数是指矩阵中满足同时下列两个条件的元素：
#在同一行的所有元素中最小
#在同一列的所有元素中最大
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        temp=[]
        l=[]
        for i in range(len(matrix)):
            a=min(matrix[i])
            temp.append(a)#记录同一行的所有元素中最小
            l.append(matrix[i].index(a))#记录下标
        ans=[]
        for i in range(len(l)):
            q=[]
            for k in range(len(matrix)):
                q.append(matrix[k][l[i]])#记录同一列的
            if max(q)==temp[i]:#如果也满足在同一列的所有元素中最大
                ans.append(temp[i])
        return ans
