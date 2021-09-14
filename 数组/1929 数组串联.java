//给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：

//ans[i] == nums[i]
//ans[i + n] == nums[i]
//具体而言，ans 由两个 nums 数组 串联 形成。

//返回数组 ans 。

class Solution {
    public int[] getConcatenation(int[] nums) {
        int n=nums.length;
        int ans[]= new int[n*2];
        for(int i=0;i<n;i++){
            ans[i]=nums[i];
            ans[i+n]=nums[i];
        }
        return ans;
    }
}
