#斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1):
            return 1
        ans = [0, 1]
        for i in range(n-1):
            ans.append(ans[-1]+ans[-2])
        return ans[-1]
