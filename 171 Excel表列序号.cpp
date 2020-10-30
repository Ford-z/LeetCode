/*给定一个Excel表格中的列名称，返回其相应的列序号。*/
class Solution {
public:
    int titleToNumber(string s) {
      int m = s.size() - 1;    
      int sum = 0;
      for(int i = 0;i<s.size();i++)
      {
        int n = s[i] - 'A'+1;
        int multi = pow(26,m--);
        n *= multi;
        sum += n;
      }  
      return sum;
    }
};
