#求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
class Solution:
    def sumNums(self, n: int) -> int:
        return n and (n+self.sumNums(n-1))
