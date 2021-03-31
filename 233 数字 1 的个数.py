#给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
class Solution:
    def countDigitOne(self, n: int) -> int:
        a=1
        res=0
        temp=n
        while(n//a>0):
            b=n//a%10
            if (b<1):
                res+=(n//(a*10))*a
            elif b==1:
                res+=(n//(a*10))*a+n%a+1
            else:
                res+=(n//(a*10)+1)*a
            a*=10
        return res
