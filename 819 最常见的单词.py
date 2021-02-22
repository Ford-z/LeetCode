#给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

#题目保证至少有一个词不在禁用列表中，而且答案唯一。

#禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/most-common-word
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace('.',' ')
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace('\'',' ')#先把标点符号替换成空格
        paragraph=paragraph.split()
        res=collections.Counter(paragraph)
        count=0
        ans=''
        for word in res:
            if word not in banned:
                if res[word]>count:
                    count=res[word]
                    ans=word
        return ans
