#给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/meeting-rooms
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        time = sorted(intervals, key = lambda x: x[0])#按开始时间排序
        for x in range(1,len(time)):
            if(time[x][0]<time[x-1][1]):#下一个开始时间是否在上一个前面
                return False
        return True
