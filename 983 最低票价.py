#在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。
#火车票有三种不同的销售方式：
#一张为期一天的通行证售价为 costs[0] 美元；
#一张为期七天的通行证售价为 costs[1] 美元；
#一张为期三十天的通行证售价为 costs[2] 美元。
#通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。
#返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/minimum-cost-for-tickets
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        m=days[-1]
        dp=[0]*(m+1)
        dp[0]=0
        for i in range(n):
            dp[days[i]]=float("inf")
        for i in range(1,m+1):
            if(dp[i]!=0):
                dp[i]=dp[i-1]+costs[0]
                if(i>7):
                    dp[i]=min(dp[i-7]+costs[1],dp[i])
                else:
                    dp[i]=min(dp[i],costs[1])
                if(i>30):
                    dp[i]=min(dp[i-30]+costs[2],dp[i])
                else:
                    dp[i]=min(dp[i],costs[2])
            else:
                dp[i]=dp[i-1]
        return dp[-1]
