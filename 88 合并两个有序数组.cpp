class Solution {
public:
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		if (n>0){
			int a;
			int i = 0;
			for (; i<m; i++){
				if (nums1[i] == 0){
					break;
				}
			}
			int b, temp;
			for (int j = i, k = 0; k<n; k++, j++){
				nums1[j] = nums2[k];
				b = j;
			}//把所有元素添加到nums中
			if (b>1){
				for (int i = 0; i < b - 1; i++) {
					// 从后向前依次的比较相邻两个数的大小，遍历一次后，把数组中第i小的数放在第i个位置上
					for (int j = b - 1; j > i; j--) {
						// 比较相邻的元素，如果前面的数大于后面的数，则交换
						if (nums1[j - 1] > nums1[j]) {
							temp = nums1[j - 1];
							nums1[j - 1] = nums1[j];
							nums1[j] = temp;
						}
					}
				}
			}
			else{
				for (int j = b; j >= 0; j--) {
					// 比较相邻的元素，如果前面的数大于后面的数，则交换
					if (nums1[j - 1] > nums1[j]) {
						temp = nums1[j - 1];
						nums1[j - 1] = nums1[j];
						nums1[j] = temp;
					}
				}
			}
		}
		if (n <= 0){
			int b = 0, temp;
			for (int i = 0; i<m; i++){
				if (nums1[i] == 0){
					break;
				}
				b++;
			}
			if (b>1){
				for (int i = 0; i < b - 1; i++) {
					// 从后向前依次的比较相邻两个数的大小，遍历一次后，把数组中第i小的数放在第i个位置上
					for (int j = b - 1; j > i; j--) {
						// 比较相邻的元素，如果前面的数大于后面的数，则交换
						if (nums1[j - 1] > nums1[j]) {
							temp = nums1[j - 1];
							nums1[j - 1] = nums1[j];
							nums1[j] = temp;
						}
					}
				}
			}
			else{
				for (int j = b; j >= 0; j--) {
					// 比较相邻的元素，如果前面的数大于后面的数，则交换
					if (nums1[j - 1] > nums1[j]) {
						temp = nums1[j - 1];
						nums1[j - 1] = nums1[j];
						nums1[j] = temp;
					}
				}
			}
		}
	}
};