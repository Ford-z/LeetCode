#给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/distribute-candies
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        #最大极端情况，所有糖都不重样，那妹妹也只能得到一半。 中间情况，每个糖都有两个，那妹妹刚好能得到所有种类，数量跟第一种一样。 最小极端情况，就一种糖，那妹妹就只能得到一种。
        a=len(candies) // 2#全部的一半
        b=len(set(candies))#种类的全部
        return min(a,b)
