#给定一个整数，写一个函数来判断它是否是 3 的幂次方。
class Solution {
    public boolean isPowerOfThree(int n) {
        return Integer.toString(n, 3).matches("10*$");//// 3的n次幂对应的3进制数---> 1  10 100 1000
    }
}
