#给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
#请你返回让 s 成为回文串的 最少操作次数 。
#「回文串」是正读和反读都相同的字符串。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minInsertions(self, s: str) -> int:
        rs = s[::-1]
        n = len(s)
        dp=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s[i] == rs[j]:
                    if i-1>=0 and j-1>=0:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        r=max(max(num) for num in dp)
        return n-r
