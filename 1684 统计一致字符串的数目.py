#给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
#请你返回 words 数组中 一致字符串 的数目。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/count-the-number-of-consistent-strings
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        flag=0
        for i in words:
            for j in i:
                if j not in allowed:
                    flag=1
            if flag==1:
                flag=0
                continue
            c+=1
        return c
