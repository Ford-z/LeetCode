#给你一个不同学生的分数列表，请按 学生的 id 顺序 返回每个学生 最高的五科 成绩的 平均分。
#对于每条 items[i] 记录， items[i][0] 为学生的 id，items[i][1] 为学生的分数。平均分请采用整数除法计算。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/high-five
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hash_table={}
        for item in items:
            if item[0] in hash_table:
                hash_table[item[0]].append(item[1])
            else:
                hash_table[item[0]]=[item[1]]
        
        table=sorted(hash_table.items())#按学号排序
        ans=[]
        for key,value in table:
            avg=sum(sorted(value,reverse=True)[:5])//5#选最高的5科
            ans.append([key,avg])
        return ans
