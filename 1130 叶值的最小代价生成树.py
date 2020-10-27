#给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：
#每个节点都有 0 个或是 2 个子节点。
#数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
#每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
#在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import sys
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack=[]
        ans=0
        for i in range(len(arr)):
            while stack and stack[-1]<arr[i]:
                a=stack.pop()
                if stack:
                    ans+=a*min(stack[-1],arr[i])
                else:
                    ans+=a*arr[i]
            stack.append(arr[i])
        while(len(stack)>1):
            ans+=stack.pop()*stack[-1]
        return ans
