#给出 字符串 text 和 字符串列表 words, 返回所有的索引对 [i, j] 使得在索引对范围内的子字符串 text[i]...text[j]（包括 i 和 j）属于字符串列表 words。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/index-pairs-of-a-string
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for i in range(len(text)):
            for j in range(i, len(text)):
                if text[i:j+1] in words:
                    ans.append([i,j])
        return ans
