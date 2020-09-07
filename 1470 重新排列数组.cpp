class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> ans(nums.size(), 0);
        for(int i=0;i<=n-1;i++)
        {
            ans[2*i]=nums[i];
        }
        int q=1;
        for(int i=n;i<nums.size();i++)
        {
            ans[q]=nums[i];
            q+=2;
        }
        return ans;
    }
};
