#给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int>dp (rowIndex+1,1);
        for(int i = 2;i < rowIndex+1;i++){
            for(int j = i - 1;j > 0;j--)
                dp[j] = dp[j] + dp[j - 1];//等于上一行的两个叠加
        }
        return dp;
    }
};
