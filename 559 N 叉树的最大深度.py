#给定一个 N 叉树，找到其最大深度。

#最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

#N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(a)+1 for a in root.children)
