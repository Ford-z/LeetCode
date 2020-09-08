class Solution {
public:
    vector<int> r;
    vector<vector<int>> res;
    void dfs(int cur,int n,int k){
        for(int i=cur+1;i<=n-k+1;i++){
            r.push_back(i);
            if(k-1==0){
                res.push_back(r);
            }
            else{
                dfs(i,n,k-1);
            }
            r.pop_back();
        }
    }
    vector<vector<int>> combine(int n, int k) {
         dfs(0,n,k);
         return res;
    }
};
