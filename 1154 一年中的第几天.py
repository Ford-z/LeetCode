#给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天。
#通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推。每个月的天数与现行公元纪年法（格里高利历）一致。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/day-of-the-year
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import time
class Solution:
    def dayOfYear(self, date: str) -> int:
        return time.strptime(date, "%Y-%m-%d")[-2]
