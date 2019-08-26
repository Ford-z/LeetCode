class Solution {
public:
	string removeOuterParentheses(string S) {
		string S2, S3;
		stack<char>s1;
		int n = S.size();
		int cout = 0;
		for (int i = 0; i<n; i++){
			S3 += S[i];
			cout++;
			if (S[i] == '('){
				s1.push(S[i]);
			}
			if (S[i] == ')'){
				s1.pop();
			}
			if (s1.empty() == true){
				S2.append(S3, 1, cout - 2);
				S3.clear();
				cout = 0;
			}
		}
		return S2;
	}
};