/**给你一个字符串 s ，如果 s 是一个 好 字符串，请你返回 true ，否则请返回 false 。

如果 s 中出现过的 所有 字符的出现次数 相同 ，那么我们称字符串 s 是 好 字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-all-characters-have-equal-number-of-occurrences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。**/
class Solution {
    public boolean areOccurrencesEqual(String s) {
        int [] ans=new int[26];
        for (int i=0;i<26;i++){
            ans[i]=0;
        }
        int temp=0;
        for (char c : s.toCharArray()){
            ans[c-'a']+=1;
            temp=ans[c-'a'];
        }
        for (int i=0;i<26;i++){
            if(ans[i]!=temp && ans[i]!=0){
                return false;
            }
        }
        return true;
    }
}
