#给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
#两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。

#如果 a 和 b 相似，返回 true ；否则，返回 false 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/determine-if-string-halves-are-alike
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a='aeiouAEIOU'
        n=len(s)
        k=n//2
        cnt1=0
        cnt2=0
        for i in range (0,k):
            if s[i] in a:
                cnt1+=1
        for i in range (k,n):
            if s[i] in a:
                cnt2+=1
        return cnt1==cnt2
