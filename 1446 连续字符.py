#给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

#请你返回字符串的能量。
class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        tmp=1
        i=0
        for i in range(len(s) - 1):
            if s[i]==s[i+1]:
                tmp+=1
                ans=max(ans,tmp)
            else:
                tmp=1
        return ans
