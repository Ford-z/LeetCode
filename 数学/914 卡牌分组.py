#给定一副牌，每张牌上都写着一个整数。

#此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

#每组都有 X 张牌。
#组内所有的牌上都写着相同的整数。
#仅当你可选的 X >= 2 时返回 true。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        #统计各个数出现的次数，然后求次数之间是否存在公约数
        ans=0
        a=list(set(deck))
        for i in a:
            ans=math.gcd(ans,deck.count(i))
            if ans==1:
                return False
        return ans>=2
        
