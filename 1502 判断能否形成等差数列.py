#给你一个数字数组 arr 。
#如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
#如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if(len(arr)<=1):
            return True
        arr.sort()
        temp=0
        for x in range(len(arr)-1):
            if(x==0):
                temp=arr[x+1]-arr[x]
            else:
                if temp!=arr[x+1]-arr[x]:
                    return False
        return True
