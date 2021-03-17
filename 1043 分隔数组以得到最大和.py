#给你一个整数数组 arr，请你将该数组分隔为长度最多为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
#返回将数组分隔变换后能够得到的元素最大和。

 

#注意，原数组和分隔后的数组对应顺序应当一致，也就是说，你只能选择分隔数组的位置而不能调整数组中的顺序。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/partition-array-for-maximum-sum
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        for i in range(1,n+1):
            j = i - 1
            mx = -float('inf')
            while i - j <= k and j >= 0:
                mx = max(mx,arr[j])#前面k-1个最大的
                dp[i] = max(dp[i],dp[j]+mx * (i - j))#作用：求位置 i 的时候 k 种情况 的最大值
                j -= 1
        return dp[n]
