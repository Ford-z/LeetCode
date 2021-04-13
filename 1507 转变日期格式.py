#给你一个字符串 date ，它的格式为 Day Month Year ，其中：

#Day 是集合 {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"} 中的一个元素。
#Month 是集合 {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"} 中的一个元素。
#Year 的范围在 ​[1900, 2100] 之间。
#请你将字符串转变为 YYYY-MM-DD 的格式，其中：

#YYYY 表示 4 位的年份。
#MM 表示 2 位的月份。
#DD 表示 2 位的天数

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/reformat-date
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def reformatDate(self, date: str) -> str:
        a=date.split()
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        ans=""
        ans+=a[2]
        ans+="-"
        ans+=("0"+str(month.index(a[1])+1))[-2:]+"-"
        if a[0][1].isdigit():
            ans+=a[0][:2]
        else:
            ans+="0"+a[0][0]
        return ans
