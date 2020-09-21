#给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(s)
        a=list(s)
        temp=[]
        ans=[]
        for i in range(len(a)):
            if(a[i]==" "):
                ans.extend(temp[::-1])
                ans.extend(a[i])
                temp=[]
            else:
                temp.append(a[i])
            if(i==n-1):
                ans.extend(temp[::-1])
        b="".join(ans)
        s=b
        return s
