/*给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。*/
#include<cmath>
#include<vector>
class Solution {
public:
    bool buddyStrings(string A, string B) {
        int n=A.size();
        int m=B.size();
        if(n!=m){
            return false;
        }
        int count=0;
        vector<int>t (n);
        bool flag=0;
        int k=0;
        for(int i=0;i<n;i++){
            int temp=A[i]-B[i];
            if(temp!=0){
                t[k]=i;//记录下标
                count++;
                k++;
            }
        }
        if(count==2){
            if(A[t[0]]==B[t[1]] && A[t[1]]==B[t[0]]){
                return true;
            }
            return false;
        }
        if(count>2 || count==1){
            return false;
        }
        if(count==0){
            int sum=0;
            for(int i=0;i<n;i++){
                string s=A.substr(i+1);
                if(s.find(A[i])<s.size()){
                    return true;
                }
            }
            return false;
        }
        return false;
    } 
};
