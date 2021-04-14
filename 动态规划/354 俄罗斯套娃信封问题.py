#给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

#当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

#请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

#注意：不允许旋转信封。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/russian-doll-envelopes
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))#可以按 w 进行升序排序，若 w 相同则按 h 降序排序

        size = len(envelopes)
        if size <= 1:
            return size
        dp=[1]*size
        for i in range(1,size):
            for j in range(i):
                if(envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
