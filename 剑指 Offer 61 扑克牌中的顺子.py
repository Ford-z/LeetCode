#从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        a=nums.count(0)
        if a==0:
            for i in range(len(nums)-1):
                if(nums[i+1]!=nums[i]+1):
                    return False
            return True
        else:
            diff=0
            for i in range(a,len(nums)-1):
                if(nums[i+1]==nums[i]):
                    return False#排除重复
                else:
                    diff+=nums[i + 1] - nums[i] - 1#计算缺几张牌    
            if(diff<=a):
                return True
            else:
                return False
