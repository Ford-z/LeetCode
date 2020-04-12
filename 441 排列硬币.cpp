class Solution {
public:
    int arrangeCoins(int n) {
        int i=1;
        long sum=0;
        for(;i<=n;i++){
            sum=sum+i;
            if(sum>n){
                break;
            }
        }
        return i-1;
    }
};
