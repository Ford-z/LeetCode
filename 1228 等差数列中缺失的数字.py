#有一个数组，其中的值符合等差数列的数值规律，也就是说：
#在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。
#我们会从该数组中删除一个 既不是第一个 也 不是最后一个的值，得到一个新的数组  arr。
#给你这个缺值的数组 arr，请你帮忙找出被删除的那个数。
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        a=(arr[0]+arr[-1])*(len(arr)+1)//2
        b=sum(arr)
        return a-b
