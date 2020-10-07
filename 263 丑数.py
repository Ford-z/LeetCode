#编写一个程序判断给定的数是否为丑数。丑数就是只包含质因数 2, 3, 5 的正整数。
class Solution:
    def isUgly(self, num: int) -> bool:
        if(num<1):
            return False
        while(num%5==0):
            num/=5
        while(num%3==0):
            num/=3
        while(num%2==0):
            num/=2
        return num==1
