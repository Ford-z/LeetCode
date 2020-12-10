//给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n));
        string ans;
        for(int k=0;k<n;k++){//k为右移位数
            for(int i=0;i+k<n;i++){//i为子串起始位置
                int j=i+k;
                if(j>=n){
                    break;
                }
                if(k==0){
                    dp[i][j]=1;
                }
                else if(k==1){
                    dp[i][j]=(s[i] == s[j]);
                }
                else{
                    dp[i][j]=(s[i] == s[j] && dp[i + 1][j - 1]);
                }
                if(dp[i][j] &&k+1>ans.size()){
                    ans=s.substr(i, k + 1);
                }
            }
        }
        return ans;
    }
};
