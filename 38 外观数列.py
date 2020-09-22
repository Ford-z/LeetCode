#给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
3注意：整数序列中的每一项将表示为一个字符串。
#「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
#第一项是数字 1
#描述前一项，这个数是 1 即 “一个 1 ”，记作 11
#描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
#描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
#描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return "1"
        num=self.countAndSay(n - 1)
        s=[]
        i=0
        while(i<len(num)):
            count=1
            while(i<len(num)-1 and num[i]==num[i+1]):
                count+=1
                i+=1
            s.append(str(count))
            s.append(num[i])
            i+=1
        return "".join(s)
