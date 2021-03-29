#有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

#如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

#你允许：

#装满任意一个水壶
#清空任意一个水壶
#从一个水壶向另外一个水壶倒水，直到装满或者倒空

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/water-and-jug-problem
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        #找到x,y的最大公约数能否z被整除
        if targetCapacity==0:
            return True
        if jug1Capacity+jug2Capacity<targetCapacity:
            return False
        if jug1Capacity<jug2Capacity:
            jug1Capacity,jug2Capacity=jug2Capacity,jug1Capacity
        if jug1Capacity==0:
            return jug2Capacity==targetCapacity
        while jug2Capacity%jug1Capacity!=0:
            jug2Capacity,jug1Capacity=jug1Capacity,jug2Capacity%jug1Capacity
        return targetCapacity%jug1Capacity==0
