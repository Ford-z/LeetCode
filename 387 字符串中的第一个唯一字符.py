#给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dp=[0]*26
        for i in range(len(s)):
            dp[ord(s[i])-ord('a')]+=1
        for i in range(len(s)):
            if dp[ord(s[i])-ord('a')]==1:
                return i
        return -1
