#给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

#以任意顺序返回这两个数字均可。
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        ans=[]
        temp=set(nums)
        for i in range(1,len(nums)+3):
            if i not in temp:
                ans.append(i)
            if len(ans)==2:
                break
        return ans
