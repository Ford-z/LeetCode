#请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

#若队列为空，pop_front 和 max_value 需要返回 -1

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class MaxQueue:

    def __init__(self):
        self.ans=[]


    def max_value(self) -> int:
        if len(self.ans)==0:
            return -1
        else:
            return max(self.ans)


    def push_back(self, value: int) -> None:
        self.ans.append(value)


    def pop_front(self) -> int:
        if len(self.ans)==0:
            return -1
        else:
            return self.ans.pop(0)



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
