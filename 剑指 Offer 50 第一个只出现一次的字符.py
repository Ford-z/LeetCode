#在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        # write code here
        n=len(s)
        if(n==0):
            return " "
        if(n==1):
            return s
        for i in range(n):
            a=s[0:i]+s[i+1:n]
            if s[i] not in a:
                return s[i]
        return " "
