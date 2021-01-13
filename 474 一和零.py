#给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

#请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

#如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/ones-and-zeroes
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        def c(s):
            c=[0]*2
            for i in range(len(s)):
                if(s[i]=='0'):
                    c[0]+=1
                else:
                    c[1]+=1
            return c
        for s in strs:
            count=c(s)
            for i in range(m,count[0]-1,-1):
                for j in range(n,count[1]-1,-1):
                    dp[i][j] = max(1 + dp[i - count[0]][j - count[1]], dp[i][j])
        return dp[m][n]
        
