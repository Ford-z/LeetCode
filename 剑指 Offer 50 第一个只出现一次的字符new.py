#在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
class Solution:
    def firstUniqChar(self, s: str) -> str:
        table=dict()
        for char in s:
            table[char]=not char in table
        for k,v in table.items():
            if v:
                return k
        return " "
