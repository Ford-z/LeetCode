#给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；否则，返回 false 。
#数组表示的字符串 是由数组中的所有元素 按顺序 连接形成的字符串。
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1)=="".join(word2)
