/*给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int target;
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        for (int i=0;i<nums.size();i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            if ((target = nums[i]) > 0) {
                break;
            }
            int l=i+1,r=nums.size()-1;
            while(l<r){
                if(nums[l] + nums[r] + target < 0) l++;
                else if (nums[l] + nums[r] + target > 0) r--;
                else{
                    ans.push_back({target, nums[l], nums[r]});
                    l++, r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;//去重
                    while (l < r && nums[r] == nums[r + 1]) r--;//去重
                }
            }
        }
        return ans;
    }
};
