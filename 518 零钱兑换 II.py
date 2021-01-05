#给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for i in coins:
            j=0
            while(i+j<=amount):
                dp[j+i]+=dp[j]#枚举硬币，看其能够达到的位置
                j+=1
        return dp[-1]
