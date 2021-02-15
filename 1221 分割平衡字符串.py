#在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

#给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

#返回可以通过分割得到的平衡字符串的 最大数量 。
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        m=0
        num=0
        for i in range(len(s)):
            if s[i]=="R":
                m+=1
            if s[i]=="L":
                m-=1
            if(m==0):
                num+=1
        return num
