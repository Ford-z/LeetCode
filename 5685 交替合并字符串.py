#给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        i=0
        while(i<len(word1) and i<len(word2)):
            ans.append(word1[i])
            ans.append(word2[i])
            i+=1
        q="".join(ans)
        if i==len(word1) and i<len(word2):
            q+=word2[i:]
        if i==len(word2) and i<len(word1):
            q+=word1[i:]
        return q
