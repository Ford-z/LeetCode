#你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#给定一个数字 n，找出可形成完整阶梯行的总行数。
#n 是一个非负整数，并且在32位有符号整型的范围内。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/arranging-coins
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if(n==1):
            return 1
        a=n//2
        for i in range(1,a+2):
            temp=i*(i+1)//2
            if(temp>n):
                return i-1
            if(temp==n):
                return i
