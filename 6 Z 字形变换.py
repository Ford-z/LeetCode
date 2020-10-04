#将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        ans=[[] for _ in range((numRows))]
        for key,value in enumerate(s):
            a=key%(2*numRows-2)
            if(a>numRows-1):
                temp=a
                a=2*numRows-2-temp
            ans[a].append(value)
        res=""
        for i in range(len(ans)):
            res+="".join(ans[i])
        return res
