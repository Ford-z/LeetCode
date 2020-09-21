#冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/heaters
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters = [float("-inf")] + heaters + [float("inf")]
        n=len(houses)
        dp=[0]*n
        for i in range(len(houses)):
            loc = bisect.bisect_left(heaters, houses[i])
            temp=min(abs(houses[i]-heaters[loc-1]),abs(houses[i]-heaters[loc]))
            dp[i]=temp
        return max(dp)
