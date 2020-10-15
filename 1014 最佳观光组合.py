#给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
#一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
#返回一对观光景点能取得的最高分。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/best-sightseeing-pair
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left=A[0]
        res=-sum(A)
        for i in range(1,len(A)):
            res=max(res,left+A[i]-i)#A[j]-j，此处j为i
            left=max(left,A[i]+i)#观察A[i]+i
        return res
