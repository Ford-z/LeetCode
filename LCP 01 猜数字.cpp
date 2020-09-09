class Solution {
public:
    int game(vector<int>& guess, vector<int>& answer) {
        int sum=0;
        for(int i=0;i<3;i++){
            if(answer[i]==guess[i]){
                sum++;
            }
        }
        return sum;
    }
};
