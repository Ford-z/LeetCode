#在本次游戏中，店家说出的数字为 x = 1 和 y = 0，小扣说出的计算指令记作仅由大写字母 A、B 组成的字符串 s，字符串中字符的顺序表示计算顺序，请返回最终 x 与 y 的和为多少。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/nGK0Fy
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def calculate(self, s: str) -> int:
        x=1
        y=0
        ans=0
        for i in range(len(s)):
            if(s[i]=="A"):
                x=2*x+y
            if(s[i]=="B"):
                y=y*2+x
        ans=x+y
        return ans
