#给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp=[-2]#不能用-1，会有-1,0,1情况
        count=0
        for i in range(len(arr)):
            if(arr[i]%2==1):
                temp.append(i)
                count+=1
        if(count<3):
            return False
        temp.append(-2)
        for i in range(1,len(temp)-1):
            if temp[i]-temp[i-1]==1 and temp[i+1]-temp[i]==1:
                return True
        return False
