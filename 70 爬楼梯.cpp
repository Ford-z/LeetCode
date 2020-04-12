class Solution {
public:
    int climbStairs(int n) {
        if(n<=1){
            return 1;
        }
        else if(n==2){
            return 2;
        }
        else{
            long f = 0;
            long i = 1, j = 2;
            int k = 3;
            for(;k<=n;k++){
                f=i+j;/*f(n)=f(n-1)+f(n-2)*/
                i=j;
                j=f;
            }
            return f;
        }
    }
};
