class Solution {
public:
	bool isValid(string s) {
		bool flag = true;
		stack<char>s1;
		int n = s.size();
		for (int i = 0; i<n; i++){
			if (s[i] == '{' || s[i] == '(' || s[i] == '['){
				s1.push(s[i]);
			}
			else if (s[i] == '}' || s[i] == ')' || s[i] == ']'){
				if (!s1.empty() && ((s[i] == '}'&&s1.top() == '{') || (s[i] == ']'&&s1.top() == '[') || (s[i] == ')'&&s1.top() == '('))){
					s1.pop();
				}
				else{
					flag = false;
				}
			}
		}
		if (!s1.empty()){
			flag = false;
		}
		return flag;
	}
};