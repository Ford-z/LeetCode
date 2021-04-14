#编写一段程序来查找第 n 个超级丑数。
#超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp=[0 for _ in range(n)]
        dp[0]=1
        j=1
        Dict={}
        for i in range(len(primes)):
            Dict[primes[i]]=0
        while j<n:
            a=[]
            for i in range(len(primes)):
                a.append(dp[Dict[primes[i]]]*primes[i])
            dp[j]=min(a)
            for i in range(len(primes)):
                if (dp[j]/dp[Dict[primes[i]]]==primes[i]):
                    Dict[primes[i]]+=1
            j+=1
        return dp[-1]
