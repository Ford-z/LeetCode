/*给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int>ans(nums.size(),0);
        int t=0;
        for(int i=0;i<nums.size();i++){
            t=0;
            for(int j=0;j<nums.size();j++){
                if(i!=j && nums[i]>nums[j]){
                    t++;
                }
            }
            ans[i]=t;
        }
        return ans;
    }
};
