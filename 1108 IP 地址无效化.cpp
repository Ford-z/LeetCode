class Solution {
public:
    string defangIPaddr(string address) {
        string ans="";
        for(int i=0;i<address.size();i++){
            if(address[i]=='.'){
                string str="[.]";
                ans=ans+str;
            }
            else{
                ans=ans+address[i];
            }
        }
        return ans;
    }
};
