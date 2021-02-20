#你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。

#如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。

#（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

#返回 words 中与给定模式匹配的单词列表。

#你可以按任何顺序返回答案。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/find-and-replace-pattern
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans=[]
        for j in range(len(words)):
            if len(words[j]) != len(pattern):
                continue
            else:
                for i in range(len(words[j])):
                    if words[j].index(words[j][i])!=pattern.index(pattern[i]):
                        break
                    if(i==len(words[j])-1):
                        ans.append(words[j])
        return ans
