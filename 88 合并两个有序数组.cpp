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
			}//������Ԫ����ӵ�nums��
			if (b>1){
				for (int i = 0; i < b - 1; i++) {
					// �Ӻ���ǰ���εıȽ������������Ĵ�С������һ�κ󣬰������е�iС�������ڵ�i��λ����
					for (int j = b - 1; j > i; j--) {
						// �Ƚ����ڵ�Ԫ�أ����ǰ��������ں���������򽻻�
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
					// �Ƚ����ڵ�Ԫ�أ����ǰ��������ں���������򽻻�
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
					// �Ӻ���ǰ���εıȽ������������Ĵ�С������һ�κ󣬰������е�iС�������ڵ�i��λ����
					for (int j = b - 1; j > i; j--) {
						// �Ƚ����ڵ�Ԫ�أ����ǰ��������ں���������򽻻�
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
					// �Ƚ����ڵ�Ԫ�أ����ǰ��������ں���������򽻻�
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