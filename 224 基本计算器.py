#给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sign=1#系数
        ans=0
        s="("+s+")"
        i=0
        while i<len(s):
            if '0'<= s[i] <='9':
                res=int(s[i])
                while '0'<= s[i+1] <='9':
                    i+=1
                    res=res*10+int(s[i])
                ans+=res*sign
            elif s[i]=='(':
                stack.append([ans,sign])
                ans=0
                sign=1
            elif s[i]=='+':
                sign=1
            elif s[i]=='-':
                sign=-1
            elif s[i]==')':
                temp=stack.pop()
                ans=temp[0]+temp[1]*ans
            elif s[i]=='':
                continue
            i+=1
        return ans
