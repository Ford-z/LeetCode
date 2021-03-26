#有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/get-kth-magic-number-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans=[0]*k
        ans[0]=1
        a=0
        b=0
        c=0
        for i in range(1,k):
            temp=min(ans[a]*3,ans[b]*5,ans[c]*7)
            if (temp%3==0):
                a+=1
            if (temp%5==0):
                b+=1
            if (temp%7==0):
                c+=1
            ans[i]=temp
        return ans[-1]
