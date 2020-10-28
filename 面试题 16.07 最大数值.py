#编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
class Solution:
    def maximum(self, a: int, b: int) -> int:
        return ((a + b) + abs(a - b)) // 2#max(a, b)的本质是补齐ab之间的相对距离
