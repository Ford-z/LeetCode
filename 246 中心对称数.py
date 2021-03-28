#中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

#请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/strobogrammatic-number
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        lookup = {
            "6" : "9",
            "9" : "6",
            "8" : "8",
            "1" : "1",
            "0" : "0"
            }
        res=""
        for i in num:
            if i in lookup:
                res+=lookup[i]
            else:
                return False
        return res==num[::-1]
