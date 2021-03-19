#请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        ans=1
        for i in range(len(s)):
            for j in range(i+ans,len(s)):
                if j-i+1==len(list(set(s[i:j+1]))):
                    ans=j-i+1
                else:
                    break
        return ans
