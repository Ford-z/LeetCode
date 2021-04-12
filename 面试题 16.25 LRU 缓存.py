#设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。

#它应该支持以下操作： 获取数据 get 和 写入数据 put 。

#获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
#写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/lru-cache-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ans=collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.ans:
            return -1
        res=self.ans[key]
        self.ans.pop(key)
        self.ans[key]=res
        return res

    def put(self, key: int, value: int) -> None:
        if key not in self.ans:
            if self.capacity<=0:
                for k in self.ans.keys():
                    self.ans.pop(k)
                    break
            else:
                self.capacity-=1
        else:
            self.ans.pop(key)
        self.ans[key]=value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
