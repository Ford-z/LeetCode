#一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。
#给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。
#如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。
#请注意：
#石子的数量 ≥ 2 且 < 1100；
#每一个石子的位置序号都是一个非负整数，且其 < 231；
#第一个石子的位置永远是0
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/frog-jump
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if(stones[1]>1):
            return False
        n=len(stones)
        dp=[[False]*n for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,n):
            for j in range(i):
                #dp[i][k] 表示能否由前面的某一个石头 j 通过跳 k 步到达当前这个石头 i ，这个 j 的范围是 [1, i - 1]
                k=stones[i]-stones[j]
                if(k <= j + 1):
                    dp[i][k]=dp[j][k-1] or dp[j][k] or dp[j][k+1] 
                    if(i==n-1 and dp[i][k]==True):
                        return True
        return False
