#给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
#子数组 定义为原数组中的一个连续子序列。
#请你返回 arr 中 所有奇数长度子数组的和 
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=sum(arr)
        if(len(arr)>2):
            i=3
            while(i<=len(arr)):
                j=0
                while(i+j-1<len(arr)):
                    for k in range(i):
                        ans+=arr[j+k]
                    j+=1
                i+=2
        return ans
