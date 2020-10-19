/*给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。*/
class Solution {
public:
    bool isValid(string s) {
        bool flag=true;
        stack<char>s1;
        int n=s.size();
        for(int i=0;i<n;i++){
            if(s[i]=='{'||s[i]=='('||s[i]=='['){
                s1.push(s[i]);
            }
            else if(s[i]=='}'||s[i]==')'||s[i]==']'){
                if(!s1.empty()&&((s[i]=='}'&&s1.top()=='{')||(s[i]==']'&&s1.top()=='[')||(s[i]==')'&&s1.top()=='('))){
                    s1.pop();
                }
                else{
                    flag=false;
                }
            }
        }
        if(!s1.empty()){
            flag=false;
        }
        return flag;
    }
};
