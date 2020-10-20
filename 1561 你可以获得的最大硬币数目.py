#有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：
#每一轮中，你将会选出 任意 3 堆硬币（不一定连续）。
#Alice 将会取走硬币数量最多的那一堆。
#你将会取走硬币数量第二多的那一堆。
#Bob 将会取走最后一堆。
#重复这个过程，直到没有更多硬币。
#给你一个整数数组 piles ，其中 piles[i] 是第 i 堆中硬币的数目。
#返回你可以获得的最大硬币数目。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/maximum-number-of-coins-you-can-get
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        l=len(piles)
        j=l//3
        t=l-2
        for i in range(j):
            ans+=piles[t]
            t-=2
        return ans
