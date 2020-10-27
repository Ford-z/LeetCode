#给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
#一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#若这两个字符串没有公共子序列，则返回 0。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/longest-common-subsequence
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        if n<=0 or m<=0:
            return 0
        dp=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    if i-1>=0 and j-1>=0:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
