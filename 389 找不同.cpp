class Solution {
public:
	char findTheDifference(string s, string t) {
		int sum1 = 0, sum2 = 0, a = 0;
		char b;
		for (int i = 0; i<s.size(); i++){
			sum1 += s[i] - 'A' + 1;
		}
		for (int i = 0; i<t.size(); i++){
			sum2 += t[i] - 'A' + 1;
		}
		a = sum2 - sum1;
		b = 'A' + a - 1;
		return b;
	}
};