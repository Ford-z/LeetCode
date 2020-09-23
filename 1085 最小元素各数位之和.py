#给你一个正整数的数组 A。
#然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。
#最后，假如 S 所得计算结果是 奇数 的请你返回 0，否则请返回 1。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        a=min(A)
        t=str(a)
        ans=0
        for i in range(len(t)):
            ans+=int(t[i])
        q=ans%10
        if(q%2==1):
            return 0
        return 1
