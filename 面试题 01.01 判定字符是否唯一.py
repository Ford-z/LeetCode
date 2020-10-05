#实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
class Solution:
    def isUnique(self, astr: str) -> bool:
        Dict={}
        for i in range(len(astr)):
            if(astr[i] not in Dict):
                Dict[astr[i]]=1
            else:
                return False
        return True
