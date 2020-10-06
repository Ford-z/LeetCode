#给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
class Solution:
    def longestPalindrome(self, s: str) -> int:
        Dict={}
        for i in range(len(s)):
            if(s[i] in Dict):
                Dict[s[i]]+=1
            else:
                Dict[s[i]]=1
        ans=0
        temp=0
        for key, value in Dict.items():
            if(value>1 and value %2==0):
                ans+=value
            if(value>1 and value %2==1):
                ans+=(value-1)
                if(temp==0):
                    temp+=1
            if(value==1 and temp==0):
                temp+=1
        return ans+temp
