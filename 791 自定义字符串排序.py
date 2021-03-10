#字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

#S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

#返回任意一种符合条件的字符串T

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/custom-sort-string
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans=0
        T=list(T)
        for i in S:
            for j in range(0,len(T)):
                if T[j]==i:
                    temp=T[ans]
                    T[ans]=T[j]
                    T[j]=temp
                    ans+=1
        return "".join(T)
