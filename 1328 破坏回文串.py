#给你一个回文字符串 palindrome ，请你将其中 一个 字符用任意小写英文字母替换，使得结果字符串的字典序最小，且 不是 回文串。
#请你返回结果字符串。如果无法做到，则返回一个空串。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/break-a-palindrome
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        m=len(palindrome)
        if m<=1:
            return ""
        if set(palindrome) == set(palindrome[0]):
            if palindrome[0]=='a':
                return palindrome[:-1]+"b"
            else:
                return "a"+palindrome[1:]
        if len(set(palindrome))==2 and m%2!=0 and palindrome[0]==palindrome[-1]=='a':
            return palindrome[:-1]+"b"
        for i in range(m):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
