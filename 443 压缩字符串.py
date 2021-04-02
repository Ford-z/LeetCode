#给定一组字符，使用原地算法将其压缩。
#压缩后的长度必须始终小于或等于原数组长度。
#数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
#在完成原地修改输入数组后，返回数组的新长度。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/string-compression
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def compress(self, chars: List[str]) -> int:
        count=1
        a=len(chars)
        res=[]
        for i in range(a-1,-1,-1):
            if i>0 and chars[i]==chars[i-1]:
                count+=1
            else:
                end=i+count
                chars[i:end]=[chars[i]] if count==1 else [chars[i]] +  list(str(count))
                count=1
        return len(chars)
