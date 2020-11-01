#给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。
#如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/binary-gap
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def binaryGap(self, n: int) -> int:
        a=format(n,"b")
        a=list(a)
        l=len(a)
        ans=0
        d=a.index("1")
        for i in range(d,l):
            if(a[i]=="1"):
                ans=max(ans,i-d)
                d=i
        return ans
