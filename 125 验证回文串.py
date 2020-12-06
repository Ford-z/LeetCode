#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub('[^a-zA-Z0-9]','',s)
        ans=s.lower()
        return ans==ans[::-1]
