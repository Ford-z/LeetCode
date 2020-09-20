/*给你一个字符串 S，返回只含 单一字母 的子串个数。*/
class Solution {
public:
    int countLetters(string S) {
        int ans=0;
        if(S.size()>0){
            for(int i=0;i<S.size();i++){
            for(int j=i+1;j<S.size();j++){
                if(S[i]!=S[j]){
                    break;
                }
                else{
                    ans++;
                }
            }
        }
        ans+=S.size();
        }
        else{
            ans=1;
        }
        return ans;
    }
};
