class Solution {
public:
    int subtractProductAndSum(int n) {
        string str = to_string(n);
        int mul=1,sum=0;
        for(int i=0;i<str.size();i++){
            int a=str[i]-'0';
            sum=sum+a;
            mul=mul*a;
        }
        return (mul-sum);
    }
};
