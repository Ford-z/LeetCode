#给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if(len(s1)!=len(s2)):
            return False
        flag=True
        a=list(s2)
        for i in range(len(s1)):
            if(s1[i] not in a):
                flag=False
                break
            else:
                a.remove(s1[i])#去掉当前第一个找到的
        return flag
