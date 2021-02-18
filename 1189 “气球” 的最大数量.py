#给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

#字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/maximum-number-of-balloons
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a=text.count("a")
        b=text.count("b")
        l=text.count("l")//2
        o=text.count("o")//2
        ans=min(a,b,l,o)
        return ans
