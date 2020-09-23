#给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #假设给定字符串s可由一个子串x重复n次构成，即s=nx。 现构造新字符串t=2s，即两个s相加，由于s=nx，则t=2nx。 去掉t的开头与结尾两位，则这两处的子串被破坏掉，此时t中包含2n-2个子串。 由于t中包含2n-2个子串，s中包含n个子串，若t中包含s，则有2n-2>=n，可得n>=2，由此我们可知字符串s可由一个子串x重复至少2次构成，判定为true；反之，若t中不包含s，则有2n-2<n，可得n<2，n只能为1，由此我们可知字符串s=x，假定的子串就为s本身，判定为false。
        t=s+s
        n=len(t)
        t=t[1:n-1]
        if(s in t):
            return True
        else:
            return False
