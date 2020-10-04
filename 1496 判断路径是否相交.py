#给你一个字符串 path，其中 path[i] 的值可以是 'N'、'S'、'E' 或者 'W'，分别表示向北、向南、向东、向西移动一个单位。
#机器人从二维平面上的原点 (0, 0) 处开始出发，按 path 所指示的路径行走。
#如果路径在任何位置上出现相交的情况，也就是走到之前已经走过的位置，请返回 True ；否则，返回 False 。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/path-crossing
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        if("NS" in path or "SN"in path or "EW" in path or "WE"in path):
            return True 
        x=0
        y=0
        for i in range(len(path)):
            if(path[i]=="N"):
                y+=1
            if(path[i]=="S"):
                y-=1
            if(path[i]=="E"):
                x+=1
            if(path[i]=="W"):
                x-=1
            print(x,y)
            if(x==0 and y==0):
                return True 
        return False


