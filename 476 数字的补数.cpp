class Solution {
public:
	int findComplement(int num) {
		int n = 1;
		while ((num&n) != num){
			n = (n << 1) + 1;
		}
		return num^n;
	}
};