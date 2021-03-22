#给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #找出最小的满足 s[i]>s[i+1] 的下标 i，并去除字符 s[i]
        stack=[s[0]]
        for i in range(1,len(s)):
            if s[i] not in stack and s[i]>stack[-1]:#如果栈顶字符大于当前字符 s[i]s[i]，说明栈顶字符为「关键字符」，故应当被去除。
                stack.append(s[i])
            elif s[i] not in stack:
                while stack and s[i]<stack[-1] and stack[-1] in s[i+1:]:#在弹出栈顶字符时，如果字符串在后面的位置上再也没有这一字符，则不能弹出栈顶字符。
                    stack.pop()
                stack.append(s[i])
        return "".join(stack)
