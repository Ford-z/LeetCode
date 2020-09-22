#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=list(s)
        ans=0
        for i in range(len(a)):
            j=i+1
            while(j<len(a)):
                if(a[j] in a[i:j]):
                    break
                j+=1
            if(j-i>ans):
                ans=j-i
        return ans
