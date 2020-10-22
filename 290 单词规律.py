#给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/word-pattern
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str2=s.split(" ")
        if len(pattern) != len(str2):
            return False
        return list(map(pattern.index, pattern))==list(map(str2.index,str2))
