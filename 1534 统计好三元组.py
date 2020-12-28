#给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。

#如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

#0 <= i < j < k < arr.length
#|arr[i] - arr[j]| <= a
#|arr[j] - arr[k]| <= b
#|arr[i] - arr[k]| <= c
#其中 |x| 表示 x 的绝对值。

#返回 好三元组的数量 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/count-good-triplets
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0 
        length = len(arr)
        for j in range(length):
            x=[]
            y=[]
            for i in range(j):
                if abs(arr[i]-arr[j])<=a:
                    x+= [i]
            for k in range(j+1,length):
                if abs(arr[j]-arr[k])<=b:
                    y+= [k]
            for i in x:
                for k in y:
                    if abs(arr[i]-arr[k])<=c:
                        ans+=1
        return ans
