#给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        i, j, temp = len(num1) - 1, len(num2) - 1, 0
        while(i>=0 or j>=0 or temp!=0):
            if(i>=0): 
                temp+=int(num1[i])
            if(j>=0): 
                temp+=int(num2[j])
            ans+= str(temp%10)
            temp=temp//10
            i-=1
            j-=1
        a=list(ans)
        b=a[::-1]
        return "".join(b)
