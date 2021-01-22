#给你个整数数组 arr，其中每个元素都 不相同。
#请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        a=abs(arr[1]-arr[0])
        for i in range(2,len(arr)):
            a=min(a,abs(arr[i]-arr[i-1]))
        for i in range(1,len(arr)):
            if(abs(arr[i]-arr[i-1])==a):
                ans.append([arr[i-1],arr[i]])
        return ans
