#有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。
#你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/paint-fence
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2: # 如果只有2根栏杆,则可以刷 K*K种方法
            return k*k
        
        dp=[0]*n
        dp[0]=k
        dp[1]=k*k

        for i in range(2,n):
            dp[i]=dp[i-1]*(k-1)+dp[i-2]*(k-1)#第三根栏杆刷第二根栏杆颜色(这时候就需要考虑第二根栏杆是不是和第一根栏杆一样颜色) ,第三根不能和前两根一样
        return dp[n-1]
