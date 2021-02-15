#给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        ans=[]
        for i in range(1,len(s)+1):
            left=s[:i]
            right=s[i:]
            if left==left[::-1]:
                right=self.partition(right)
                for i in range(len(right)):
                    ans.append([left]+right[i])
        return ans
        #对于一个字符串s，有len(s)种方法把它分成左右两个部分（分割方法看代码），假如左侧的不是回文，则舍弃这次尝试；假如左侧的是回文串，则把右侧的进行递归的分割，并返回右侧的分割的所有情况
