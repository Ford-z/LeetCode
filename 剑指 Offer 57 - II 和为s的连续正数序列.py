#输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans=[]
        l=1
        r=2
        while l<r:
            temp=[]
            tempsum=(l+r)*(r-l+1)/2
            if(tempsum<target):
                r+=1
            elif(tempsum>target):
                l+=1
            else:
                for i in range(l,r+1):
                    temp.append(i)
                ans.append(temp)
                l+=1#同时向右滑动
                r+=1
        return ans
