#给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

#注意:

#可以认为区间的终点总是大于它的起点。
#区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/non-overlapping-intervals
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        if n<=1:
            return 0
        intervals.sort(key=lambda x:x[1])
        count=1
        a=intervals[0][1]
        for i in range(1,n):
            if intervals[i][0]>=a:
                count+=1
                a=intervals[i][1]
        return n-count
