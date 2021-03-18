#硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
class Solution:
    def waysToChange(self, n: int) -> int:
        coins=[25,10,5,1]
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(len(coins)):
            for j in range(coins[i], n+1):#每次小循环只用一种硬币可以避免重复
                dp[j] += dp[j-coins[i]]
        return dp[-1] % 1000000007
