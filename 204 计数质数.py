#统计所有小于非负整数 n 的质数的数量。
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0#不能等于自身
        #叫做厄拉多塞筛法. 比如说求20以内质数的个数,首先0,1不是质数.2是第一个质数,然后把20以内所有2的倍数划去.2后面紧跟的数即为下一个质数3,然后把3所有的倍数划去.3后面紧跟的数即为下一个质数5,再把5所有的倍数划去.以此类推。
        ans=[1]*n
        ans[0]=0
        ans[1]=0
        for i in range(2,int(pow(n,0.5))+1):
            if ans[i]==1:
                m=i*i#根据索引值划去质数的倍数
                while m<n:
                    ans[m]=0
                    m+=i
        return sum(ans)
