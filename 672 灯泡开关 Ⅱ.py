#现有一个房间，墙上挂有 n 只已经打开的灯泡和 4 个按钮。在进行了 m 次未知操作后，你需要返回这 n 只灯泡可能有多少种不同的状态。
#假设这 n 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下：
#将所有灯泡的状态反转（即开变为关，关变为开）
#将编号为偶数的灯泡的状态反转
#将编号为奇数的灯泡的状态反转
#将编号为 3k+1 的灯泡的状态反转（k = 0, 1, 2, ...)

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/bulb-switcher-ii
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def flipLights(self, n: int, m: int) -> int:
        #所有的操作进行偶数次是会抵消的，那么所有操作只存在0,1两种，即无效果和有效果；且各一次操作2,3等效为一次操作1；
        #只有0000到1111
        #0000=1110、0001=1111、0010=1100、0100=1010、0011=1101、0101=1011、0110=1000、0111=1001
        #https://blog.csdn.net/lemonmillie/article/details/86619755
        if n==0:
            return 0
        if m==0:
            return 1
        if n==1:
            return 2
        if n==2:
            return 3 if m==1 else 4
        if m==2:
            return 7
        if m==1:
            return 4
        return 8
