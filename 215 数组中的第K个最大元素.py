#在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(left,right):
            i=left
            j=right
            if(i<j):
                temp=nums[i]
                while(i<j):
                    while(i<j and nums[j]>=temp):
                        j-=1
                    if(i<j):
                        nums[i]=nums[j]
                        i+=1
                    while(i<j and nums[i]<temp):
                        i+=1
                    if(i<j):
                        nums[j]=nums[i]
                        j-=1
                nums[i]=temp
                quicksort(left,i-1)
                quicksort(i+1,right)
        n=len(nums)
        quicksort(0,n-1)
        return nums[n-k]
