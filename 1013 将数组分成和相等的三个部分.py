#给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#形式上，如果可以找出索引 i+1 < j 且满足 A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1] 就可以将数组三等分。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if(sum(A)%3!=0):
            return False
        a=sum(A)//3

        i=0
        j=len(A)-1
        flag=False
        lans,rans = A[i],A[j]
        while(i<j):
            if lans!=a:
                i+=1
                lans+=A[i]   
            if rans!=a:
                j-=1
                rans+=A[j]
            if lans==a and rans==a:
                break
        if(j-i>1):
            flag=True
        return flag


