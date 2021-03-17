#给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

#如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        res=0
        a=-1
        b=-1
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
                res+=1
                if a==-1:
                    a=i
                elif b==-1:
                    b=i
        return res==2 and s1[a]==s2[b] and s1[b]==s2[a]
