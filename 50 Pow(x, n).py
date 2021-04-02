#实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n==0):
            return 1
        if (n<0):
            return 1/self.myPow(x,-n)
        mid=self.myPow(x,n//2)
        if (n&1):
            return mid*mid*x
        return mid*mid
