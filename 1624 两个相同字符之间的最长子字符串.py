#给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。

#子字符串 是字符串中的一个连续字符序列。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans=-1
        for i in range(0,len(s)):
            a=s[i]
            b=s.rfind(a)
            if(i!=b):
                temp=b-i-1
                ans=max(temp,ans)
        return ans
