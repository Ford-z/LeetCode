#给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
#nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/next-greater-element-i
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = list()#用于记录下标
        n = len(nums1)
        ans=[]
        Dict={}

        for key,value in enumerate(nums2):
            if stack:
                while stack and stack[-1]<value:
                   Dict[stack.pop()]=value#由于nums1为2的子集，可以找到对应数值在nums2中最近的最大的数字
            stack.append(value)
        for x in nums1:
            ans.append(Dict.get(x,-1))
        return ans
