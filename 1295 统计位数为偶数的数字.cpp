class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int sum=0;
        for(int i=0;i<nums.size();i++){
            string str=to_string(nums[i]);
            if(str.size()%2==0){
                sum++;
            }
        }
        return sum;
    }
};
