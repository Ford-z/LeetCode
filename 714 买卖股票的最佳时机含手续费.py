#给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
#你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#返回获得利润的最大值。
#注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        if n<2:
            return 0
        dp1=[0]*n#第i天手上有股票时的最大收益
        dp2=[0]*n#第i天手上没有股票时的最大收益
        dp1[0] = -prices[0]#买入价
        for i in range(1,n):
            dp1[i]=max(dp1[i-1], dp2[i-1] - prices[i])#若持有，看看前面有没有手握股票，若没有，则买入；若有，保持原买入价
            dp2[i]=max(dp1[i-1]+prices[i]-fee,dp2[i-1])#若不持有，看看前面有没有手握股票，若没有，则保持收益；若有，获得卖出价
        return max(dp1[-1],dp2[-1])
