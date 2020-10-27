#一个厨师收集了他 n 道菜的满意程度 satisfaction ，这个厨师做出每道菜的时间都是 1 单位时间。
#一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 time[i]*satisfaction[i] 。
#请你返回做完所有菜 「喜爱时间」总和的最大值为多少。
#你可以按 任意 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/reducing-dishes
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        s=0
        ans=0
        n=len(satisfaction)
        i=n-1
        while(i>=0):
            s+=satisfaction[i]
            if(s<=0):
                break
            ans+=s#包含时间顺序
            i-=1
        return ans
