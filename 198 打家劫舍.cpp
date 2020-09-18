/*你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
#include<algorithm>
class Solution {
public:
    int rob(vector<int>& nums) {
        int ans;
        int n=nums.size();
        if(n>=2){
        int a[n];
        a[0]=nums[0];
        a[1]=max(a[0],nums[1]);
        for(int i=2;i<nums.size();i++){
            a[i]=max(a[i-1],a[i-2]+nums[i]);
        }
        ans=a[n-1];
        }
        else if(n==0){
            ans=0;
        }
        else{
            ans=nums[0];
        }    
        return ans;
    }
};
