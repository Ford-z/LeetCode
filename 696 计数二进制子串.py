#给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

#重复出现的子串要计算它们出现的次数。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/count-binary-substrings
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #先统计连续的0和1分别有多少个，如：111100011000，得到4323；在4323中的任意相邻两个数字，取小的一个加起来，就是3+2+2 = 7.
        la=0
        temp=1
        ans=0
        for i in range (1,len(s)):
            if s[i]==s[i-1]:
                temp+=1
            else:
                la=temp
                temp=1
            if la>=temp:
                ans+=1
        return ans

