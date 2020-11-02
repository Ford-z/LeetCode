#编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] ^= numbers[1]#a^b
        numbers[1] ^= numbers[0]#b^(a^b)=a
        numbers[0] ^= numbers[1]#a^b^a
        return numbers
