#给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
#商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
#请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = list()#用于记录下标
        n = len(prices)
        ans = prices

        for key, value in enumerate(prices):
            if stack:#栈非空时
                while stack and prices[stack[-1]] >= value:
                    #当现在元素比栈顶元素小的时候
                    a=stack.pop()#弹出
                    ans[a]=prices[a]-prices[key]#栈顶元素获得离其最近的
            stack.append(key)#下标入栈
        return ans

