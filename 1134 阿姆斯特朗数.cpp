/*假设存在一个 k 位数 N，其每一位上的数字的 k 次幂的总和也是 N，那么这个数是阿姆斯特朗数。
给你一个正整数 N，让你来判定他是否是阿姆斯特朗数，是则返回 true，不是则返回 false。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/armstrong-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
#include<cmath>
class Solution {
public:
    bool isArmstrong(int N) {
        string s=to_string(N);
        int sum=0;
        for(int i=0;i<s.size();i++){
            sum+=pow((s[i]-'0'),s.size());
        }
        if(sum==N){
            return true;
        }
        return false;
    }
};
