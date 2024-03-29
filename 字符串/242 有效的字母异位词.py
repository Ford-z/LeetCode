#给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

#注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/valid-anagram
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record=[0]*26
        for i in range(len(s)):
            record[ord(s[i])-ord("a")]+=1
        for i in range(len(t)):
            record[ord(t[i])-ord("a")]-=1
        if record.count(0)!=26:
            return False
        return True
