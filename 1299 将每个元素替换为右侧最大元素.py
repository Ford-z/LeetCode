#给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
#完成所有替换操作后，请你返回这个数组。

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans=[]
        a=arr
        if(len(arr)>1):
            for i in range(len(arr)-1):
                a.pop(0)
                ans.append(max(a))
        ans.append(-1)
        return ans
