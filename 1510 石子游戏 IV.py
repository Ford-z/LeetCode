#Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。
#一开始，有 n 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 任意 非零 平方数 个石子。
#如果石子堆里没有石子了，则无法操作的玩家输掉游戏。
#给你正整数 n ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 True ，否则返回 False 。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/stone-game-iv
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(0,n+1):
            k=1
            while k * k <= i:
                if not dp[i - k * k]:
                    dp[i] = True
                    break
                k+=1
        return dp[n]==1
