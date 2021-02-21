#我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

#如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

#现在我们有一个正整数 N, 计算从 1 到 N 中有多少个数 X 是好数？

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/rotated-digits
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans=0
        for i in range(1,N+1):
            if '3' in str(i) or '4' in str(i) or  '7'  in str(i):
                continue
            if '2' in str(i) or '5' in str(i) or  '6'  in str(i) or  '9'  in str(i):
                ans+=1
        return ans
