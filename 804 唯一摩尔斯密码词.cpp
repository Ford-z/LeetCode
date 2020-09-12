class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> res;
        string p[26]={".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        for(int i=0;i<words.size();i++){
            // 获得字符串
            string out="";
            for(int k=0;k<words[i].size();k++){
                out+=p[words[i][k]-'a'];
            }

            int check=0;
            for(int l=0;l<res.size();l++){
                if(out==res[l]){
                    check=1;
                    break;
                }
            }
            if(check==0){
                res.push_back(out);
            }
        }
        return res.size();
    }
};
