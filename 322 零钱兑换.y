#给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#你可以认为每种硬币的数量是无限的。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/coin-change
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf') for _ in range(amount + 1)]
        res[0]=0

        for i in range(1, amount + 1):
            for c in coins:
                if i-c>=0:
                    res[i]=min(res[i],res[i-c]+1)
        if(res[-1]==float('inf')):
            return -1
        return res[-1]
