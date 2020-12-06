#运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
#实现 LRUCache 类：
#LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
#int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/lru-cache
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:# 如果 key 存在，先通过哈希表定位，进行修改,再移到头部
            node = self.cache[key]
            node.value=value
            self.moveToHead(node)
        else:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size> self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
    
    def addToHead(self, node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev = node
        self.head.next=node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
