#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        ans=[]
        st=list(s)
        while(i<len(s)):
            j=0
            temp=0
            while(i-j>=0 and i+j<len(s)):
                if(st[i-j]!=st[i+j]):
                    break
                temp=j*2+1
                j+=1
            if(temp>len(ans)):
                j-=1#回退
                ans=st[i-j:i+j+1]
            j=0
            while(i-j>=0 and i+j+1<len(s)):
                if(st[i-j]!=st[i+j+1]):
                    break
                temp=j*2+2
                j+=1
            if(temp>len(ans)):
                j-=1#回退
                ans=st[i-j:i+j+2]
            j=0
            i+=1
        return "".join(ans)
            

