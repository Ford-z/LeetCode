#给你一个仅由数字 6 和 9 组成的正整数 num。
#你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
#请返回你可以得到的最大数字。

class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=list(str(num))
        for i in range(len(ans)):
            if(ans[i]=="6"):
                ans[i]="9"
                break
        st="".join(ans)
        a=int(st)
        return a
