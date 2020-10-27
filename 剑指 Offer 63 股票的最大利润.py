#假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if(n<=1):
            return 0
        dp=[0]*n
        for i in range(n-1):
            if(i<n-1):
                a=prices[i:]
                dp[i]=max(a)-prices[i]
        return max(dp)
