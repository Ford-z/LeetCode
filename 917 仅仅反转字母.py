#给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        t=len(S)
        if t<=1:
            return S
        a=[0]*t
        stack=[]
        for i in range(t):
            if S[i]>='a' and S[i]<='z':
                stack.append(S[i])
            elif S[i]>='A' and S[i]<='Z':
                stack.append(S[i])
            else:
                a[i]=S[i]
        for i in range(t):
            if a[i]==0:
                a[i]=stack.pop()
        S="".join(a)
        return S
        
