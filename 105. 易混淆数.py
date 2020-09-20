#给定一个数字 N，当它满足以下条件的时候返回 true：
#原数字旋转 180° 以后可以得到新的数字。
#如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。
#2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。
#易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且新数字的每一位都是有效的。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/confusing-number
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def confusingNumber(self, N: int) -> bool:
        temp=N
        a=list(str(temp))
        b=[]
        l=len(a)-1
        for i in range(len(a)):
            if(a[l-i]=="2" or a[l-i]=="3" or a[l-i]=="4" or a[l-i]=="5" or a[l-i]=="7"):
                return False
            elif(a[l-i]=="6"):
                b.append("9")
            elif(a[l-i]=="9"):
                b.append("6")
            else:
                b.append(a[l-i])
        temp=int("".join(b))
        if(temp!=N):
            return True
        else:
            return False
