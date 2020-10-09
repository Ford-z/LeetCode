#给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n=int(sqrt(num))
        a=2*n-1
        s=(1+a)*n//2
        return s==num
