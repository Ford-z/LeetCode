#有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。
#剩下的乘客将会：
#如果他们自己的座位还空着，就坐到自己的座位上，
#当他们自己的座位被占用时，随机选择其他座位
#第 n 位乘客坐在自己的座位上的概率是多少？
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/airplane-seat-assignment-probability
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if(n==1):
            return 1
        else:
            return 0.5#最后的第n个乘客上飞机时，只有两种情况，要么位置被坐了，要么没有被坐，所以是0.5
