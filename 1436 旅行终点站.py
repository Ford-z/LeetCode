#给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

#题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/destination-city
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        m=[]
        for i in paths:
            m.append(i[0])
        for j in paths:
            if j[1] not in m:
                return j[1]#把起点和终点做成两个集合,然后终点集减去起点集，终结点剩下的一个元素就是结果
