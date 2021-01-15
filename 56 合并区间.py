#给出一个区间的集合，请合并所有重叠的区间。
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        b=intervals
        b.sort(key=lambda x:x[0])
        ans=[]
        temp=b[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]>temp[1]:
                ans.append(temp)
                temp=intervals[i]
            elif intervals[i][1]>temp[1]:
                temp[1]=intervals[i][1]
        ans.append(temp)
        return ans
