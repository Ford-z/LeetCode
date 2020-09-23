/*在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。*/

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int ans=0;
		vector<int> a(60,0);
        for(int i=0;i<time.size();i++){
            a[time[i]%60]++;
        }
		for(int j=1;j<30;j++){
            ans=ans+a[j]*a[60-j];
        }
        ans+=a[0]*(a[0]-1)/2+a[30]*(a[30]-1)/2;
        return ans;
    }
};
