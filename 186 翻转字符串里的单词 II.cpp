//给定一个字符串，逐个翻转字符串中的每个单词。
class Solution {
public:
    void reverseWords(vector<char>& s) {
        int n=s.size();
        int m=n-1;
        vector<char>ans (n,' ');
        int temp=m;
        int mid=0;
        for(int i=0;i<n;i++){
            if(s[i]==' '){
                for(int j=1;j<=i-mid;j++){
                    ans[temp]=s[i-j];
                    temp--;
                }
                mid=i+1;
                ans[temp]=s[i];
                temp--;
            }
            if(i==m){//最后补齐
                for(int j=0;j<=i-mid;j++){
                    ans[temp]=s[i-j];
                    temp--;
                }
            }
        }
        s=ans;
    }
};
