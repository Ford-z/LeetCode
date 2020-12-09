#公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
#返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/two-city-scheduling
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)#a这个人去A100，去B110.然后b这个人去A10，去B50。我们不用考虑100,110,10,50这四个数的比较，只要知道a去A比B便宜10.而b去A比B便宜40。肯定是选择便宜的多的
        sum1=0
        for i in range(n):
            sum1+=costs[i][0]
        ans=[]
        for i in range(n):
            ans.append(costs[i][0]-costs[i][1])
        ans.sort()
        i=len(ans)-1
        while(i>=n//2):
            sum1-=ans[i]
            i-=1
        return sum1#在分别计算 A - B的费用存入数组，由小到大排序，得到每个人去A 市比去B市多花的钱。 用sum 减去多花钱最多的前一般的钱数，即为最终最低总费用
