#给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if(n==1):
            return [0]
        if(n%2==1):
            ans=[0]
            a=(n-1)//2
            for i in range(1,a+1):
                ans.append(i)
                ans.append(-i)
        else:
            a=n//2
            ans=[]
            for i in range(1,a+1):
                ans.append(i)
                ans.append(-i)
        return ans
