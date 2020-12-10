#给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        ans=0
        for l in range(n):
            for i in range(n):
                j=i+l
                if(j>=n):
                    break
                if(l==0):
                    dp[i][j]=1
                elif(l==1):
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j]=(s[i]==s[j] and dp[i+1][j-1])
                if(dp[i][j]):
                    ans+=1
        return ans
