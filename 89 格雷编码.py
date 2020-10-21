#格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
#给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
#格雷编码序列必须以 0 开头。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/gray-code
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if(n==0):
            return [0]
        ans=[]
        tim=2**n
        for i in range(tim):
            ans.append(i ^ i >> 1)# 关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2)
        return ans
