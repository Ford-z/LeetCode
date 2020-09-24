/*统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。*/
class Solution {
public:
    int countSegments(string s) {
        s+=' ';
        int count=0;
        for(int i=0;i<s.size()-1;i++){
            if(s[i]!=' '&& s[i+1]==' '){
                count++;
            }
        }
        return count;
    }
};
