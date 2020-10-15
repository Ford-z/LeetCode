#给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        a=sum(nums)
        nums.sort()
        temp=[]#用于记录余数
        for i in range(len(nums)):
            temp.append(nums[i]%3)
        if(a%3==0):
            return a
        elif(a%3==1):#减去一个最小的模为1的数或者两个最小模为2的数
            if(len(nums)<=1):
                return 0
            q,p=0,0
            if(1 in temp):
                q=a
                q-=nums[temp.index(1)]
            if(temp.count(2)>1):
                p=a
                p-=nums[temp.index(2)]
                nums.pop(temp.index(2))
                temp.remove(2)
                p-=nums[temp.index(2)]
                nums.pop(temp.index(2))
                temp.remove(2)
            if(1 not in temp and temp.count(2)<=1):
                return 0
            return max(q,p)
        elif(a%3==2):#减去一个最小的模为2的数或者两个最小模为1的数
            if(len(nums)<=1):
                return 0
            q,p=0,0
            if(2 in temp):
                q=a
                q-=nums[temp.index(2)]
            if(temp.count(1)>1):
                p=a
                p-=nums[temp.index(1)]
                nums.pop(temp.index(1))
                temp.remove(1)
                p-=nums[temp.index(1)]
                nums.pop(temp.index(1))
                temp.remove(1)
            if(2 not in temp and temp.count(1)<=1):
                return 0
            return max(q,p)

