class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> ans(candies.size(), true);
        for (int i = 0; i < candies.size(); ++i) {
            for(int j = 0; j < candies.size(); ++j){
                if(i!=j&&candies[i]+extraCandies<candies[j]){
                    ans[i]=false;
                    break;
                }
            }
        }
        return ans;
    }
};
