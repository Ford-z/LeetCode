//给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

//最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

//你可以假设除了整数 0 之外，这个整数不会以零开头。

//来源：力扣（LeetCode）
//链接：https://leetcode-cn.com/problems/plus-one
//著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution {
    public int[] plusOne(int[] digits) {
        for(int i=digits.length-1;i>=0;i--){
            if(digits[i]!=9){
                digits[i]++;
                return digits;
            }
            digits[i]=0;
        }
        int[] arr=new int[digits.length+1];
        arr[0]=1;
        return arr;
    }
}
