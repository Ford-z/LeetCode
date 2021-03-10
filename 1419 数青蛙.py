#给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。

#注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。

#如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        #c一定在最前--k一定在最后
        c,r,o,a,k=0,0,0,0,0
        ans=0
        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i]=="c":
                c+=1
            if croakOfFrogs[i]=="r":
                r+=1
            if croakOfFrogs[i]=="o":
                o+=1
            if croakOfFrogs[i]=="a":
                a+=1
            if croakOfFrogs[i]=="k":
                k+=1
            ans=max(c-k,ans)
            if(c>=r and r>=o and o>=a and a>=k):
                continue
            else:
                break
        if (c==r and r==o and o==a and a==k):
            return ans
        else:
            return -1
