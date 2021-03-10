#数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

#如果满足以下条件，则称子数组(P, Q)为等差数组：

#元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

#函数要返回数组 A 中所有为等差数组的子数组个数。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/arithmetic-slices
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return 0
        dp=0
        ans=0
        d1=nums[1]-nums[0]
        for i in range(1,len(nums)-1):
            d2=nums[i+1]-nums[i]
            if d1==d2:
                dp+=1
                ans+=dp
            else:
                dp=0
            d1=d2
        return ans
