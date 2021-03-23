#给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#candidates 中的数字可以无限制重复被选取。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/combination-sum
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans=[]
        def div(i,tmsum,tm):
            if tmsum>target or i==n:
                return
            if tmsum==target:
                ans.append(tm)
                return
            for j in range(i,n):
                if tmsum+candidates[i]>target:
                    break
                div(j,tmsum+candidates[j],tm+[candidates[j]])
        div(0,0,[])
        return ans
