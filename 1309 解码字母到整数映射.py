#给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：
#字符（'a' - 'i'）分别用（'1' - '9'）表示。
#字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
#返回映射之后形成的新字符串。
#题目数据保证映射始终唯一。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping
3著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha_dict = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i',
        '10#':'j', '11#':'k', '12#':'l', '13#':'m', '14#':'n', '15#':'o', '16#':'p', '17#':'q', '18#':'r', 
        '19#':'s', '20#':'t', '21#':'u', '22#':'v', '23#':'w', '24#':'x', '25#':'y', '26#':'z'}
        for i in range(10,27):
            t=str(i)+"#"
            s=s.replace(t,alpha_dict[t])
        for i in range(1,10):
            s=s.replace(str(i),alpha_dict[str(i)])
        return s
