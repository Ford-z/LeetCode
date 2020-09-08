class Solution {
public:
    int xorOperation(int n, int start) {
        vector<int> ans(n, 0);
        int sum=0;
        for(int i=0;i<n;i++){
            ans[i]=start+2*i;
            sum=sum^ans[i];
        }
        return sum;
    }
};
