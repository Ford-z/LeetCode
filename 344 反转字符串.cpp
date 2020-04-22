class Solution {
public:
    void reverseString(vector<char>& s) {
        int num = s.size();
        if(num == 1) {
            return;
        }
        for(int i=0;i<num/2;i++){
            char c;
            c=s[i];
            s[i]=s[num-i-1];
            s[num-i-1]=c;
        }
    }
};
