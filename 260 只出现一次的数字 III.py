#给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Dict={}
        for i in range(len(nums)):
            if nums[i] not in Dict:
                Dict[nums[i]]=1
            else:
                Dict[nums[i]]+=1
        ans=[]
        t=2
        for key,value in Dict.items():
            if value==1:
                ans.append(key)
                t-=1
            if t<=0:
                break
        return ans    
            
