#给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。
class Solution:
    def removeVowels(self, S: str) -> str:
        ans=[]
        for i in range(len(S)):
            if(S[i]!="a" and S[i]!="e" and S[i]!="i" and S[i]!="o" and S[i]!="u"):
                ans.append(S[i])
        a="".join(ans)
        return a
