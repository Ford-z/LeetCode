#房间中有 n 个灯泡，编号从 0 到 n-1 ，自左向右排成一行。最开始的时候，所有的灯泡都是 关 着的。

#请你设法使得灯泡的开关状态和 target 描述的状态一致，其中 target[i] 等于 1 第 i 个灯泡是开着的，等于 0 意味着第 i 个灯是关着的。

#有一个开关可以用于翻转灯泡的状态，翻转操作定义如下：

#选择当前配置下的任意一个灯泡（下标为 i ）
#翻转下标从 i 到 n-1 的每个灯泡
#翻转时，如果灯泡的状态为 0 就变为 1，为 1 就变为 0 。

#返回达成 target 描述的状态所需的 最少 翻转次数。



#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/bulb-switcher-iv
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minFlips(self, target: str) -> int:
        ans=0
        for i in range(1,len(target)):
            if target[i]!=target[i-1]:#比较字符串每一位与前一位是否不同，若不同需要累加
                ans+=1
        if target[0]=="1":#若开头为1，需要进位
            ans+=1
        return ans
