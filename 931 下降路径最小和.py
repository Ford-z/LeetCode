#给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。
#下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[0])):
                if j==0:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                elif j==len(matrix[0])-1:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j]+=min(min(matrix[i-1][j],matrix[i-1][j-1]),matrix[i-1][j+1])
        return min(matrix[-1])
