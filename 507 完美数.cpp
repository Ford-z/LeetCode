/*对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/

#include<cmath>
class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num < 4){
            return false;
        }
        int sum = 1;//从1开始
        for(int i = 2; i <= (int)sqrt(num); i++){
            if (num % i == 0){
                sum += i;
                sum += num / i;
            }
        }
        if(num==sum){
            return true;
        }
        else{
            return false;
        }
    }
};
