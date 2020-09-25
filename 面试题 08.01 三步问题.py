#三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def waysToStep(self, n: int) -> int:
        if(n <= 2):
            return n
        if (n == 3):
            return 4
        
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        dp[2]=4
        for i in range(3,n):
            dp[i]=(dp[i-1]+dp[i-2])%1000000007+dp[i-3]
            dp[i]%=1000000007
        return dp[n-1]
