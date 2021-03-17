#编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
class Solution:
    def reverseVowels(self, s: str) -> str:
        yuanyin="aeiouAEIOU"
        stack=[]
        for i in s:
            if i in yuanyin:
                stack.append(i)
        ans=[]
        for i in s:
            if i not in yuanyin:
                ans.append(i)
            else:
                ans.append(stack.pop())
        return "".join(ans)
