#给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num<9:
            return num
        t=str(num)
        ans=list(t)
        ans.sort(reverse=True)
        t=list(t)
        res=[]
        tar=-1#表示第一个不合的位
        for i in range(len(ans)):
            if ans[i] !=t[i]:
                tar=i
                break
        if tar==-1:
            return num
        for i in range(len(ans)-1,tar,-1):
            if t[i]==ans[tar]:
                temp=t[tar]
                t[tar]=t[i]
                t[i]=temp
                break
        return int("".join(t))
