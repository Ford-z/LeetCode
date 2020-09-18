#请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。
class Solution:
    def arrangeWords(self, text: str) -> str:
        a=list(text.split(" "))
        t=[]
        t.append(a[0][0].swapcase())
        for i in range(len(a[0])):
            if(i!=0):
                t.append(a[0][i])
        a[0]="".join(t)
        a.sort(key = lambda i:len(i)) #按照字符长度排序
        t=[]
        t.append(a[0][0].swapcase())
        for i in range(len(a[0])):
            if(i!=0):
                t.append(a[0][i])
        a[0]="".join(t)
        ans=" ".join(a)
        return ans
