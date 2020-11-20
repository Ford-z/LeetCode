#统计一个数字在排序数组中出现的次数。
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if(n<=0):
            return 0
        l,r=0,n-1
        while l<r:#找最右侧
            mid=(l+r+1)//2
            if(nums[mid]<=target):
                l=mid
            else:
                r=mid-1
        if(nums[r]!=target):
            return 0
        a=r
        l,r=0,n-1
        while l<r:#找最左侧
            mid=(l+r)//2
            if(nums[mid]>=target):
                r=mid
            else:
                l=mid+1
        return a-l+1
