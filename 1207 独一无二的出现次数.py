#给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=set(arr)
        ans=[]
        for i in a:
            x=arr.count(i)
            if x not in ans:
                ans.append(x)
            else:
                return False
        return True
