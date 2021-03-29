#编写一个函数来查找字符串数组中的最长公共前缀。

#如果不存在公共前缀，返回空字符串 ""。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #只需要比较最大最小的公共前缀就是整个数组的公共前缀
        if not strs: 
            return ""
        s1=min(strs)
        s2=max(strs)
        res=[]
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                res.append(s1[i])
            else:
                break
        return "".join(res)
