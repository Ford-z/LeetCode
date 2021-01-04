#给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

#你可以按任意顺序返回答案。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/find-common-characters
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans=[]
        if not A:
            return ans
        key=set(A[0])
        for i in key:
            q=min(a.count(i) for a in A)#数每一个i在A中每一个单词出现的次数，选择最小
            ans+=q*i
        return ans
