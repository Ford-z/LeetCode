#给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1#双指针
        while l<r:
            if(s[l]==s[r]):
                l+=1
                r-=1
            else:
                a = s[l + 1 : r + 1]#不要左边的
                b= s[l:r]#不要右边的
                if(a==a[::-1]):
                    return True
                if(b==b[::-1]):
                    return True
                else:
                    return False
