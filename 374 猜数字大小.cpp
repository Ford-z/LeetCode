/*猜数字游戏的规则如下：

每轮游戏，系统都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，系统会告诉你，你猜测的数字比系统选出的数字是大了还是小了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int min = 1,max = n;
        while(true){
            int temp = min+(max-min)/2;
            int ans = guess(temp);
            if(ans == 0){
                return temp;
            }
            else if(ans == 1){
                if(min == temp){
                    min++;
                }
                else{
                    min = temp;
                }
            }
            else{
                if(max == temp){
                    max--;
                    }
                else{
                    max = temp;
                }

            }
        }
    }
};
