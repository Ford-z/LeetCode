class Solution {
public:
	bool isPalindrome(int x) {
		stringstream ss;
		ss << x;
		string s1 = ss.str();
		int n = s1.size();
		if (n % 2 == 0){
			for (int i = 0; i <= n / 2; i++){
				if (s1[i] != s1[n - 1 - i]){
					return false;
				}
			}
			return true;
		}
		else{
			for (int i = 0; i<n / 2; i++){
				if (s1[i] != s1[n - 1 - i]){
					return false;
				}
			}
			return true;
		}
	}
};