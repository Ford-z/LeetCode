#给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

#整数除法仅保留整数部分。
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num=10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op=="+":
                    stack.append(num)
                elif pre_op=="-":
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop()*num)
                elif pre_op == '/':
                    temp=stack.pop()
                    if temp<0:
                        stack.append(int(temp / num))
                    else:
                        stack.append(temp // num)
                pre_op=each
                num=0
        return sum(stack)
