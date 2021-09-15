/**
给你一个整数数组 nums ，返回数组中最大数和最小数的 最大公约数 。

两个数的 最大公约数 是能够被两个数整除的最大正整数。**/

class Solution {
    public int findGCD(int[] nums) {
        int a = nums[0], b = nums[0];
        for(int num: nums){
            a=Math.max(a,num);
            b=Math.min(b,num);
        }
        return helper(a,b);
    }
        private  int helper(int a, int b) {
            int c=Math.max(a,b),d=Math.min(a,b);
            if(c%d!=0){
                return helper(c-d,d);
            }
            return d;
        }
}
