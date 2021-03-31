#给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

#() 得 1 分。
#AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
#(A) 得 2 * A 分，其中 A 是平衡括号字符串。
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        return eval(S.replace(')(',')+(').replace('()','1').replace('(','2*('))
