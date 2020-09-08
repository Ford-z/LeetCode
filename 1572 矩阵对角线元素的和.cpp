class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum=0;
        for(int i=0;i<mat.size();++i)
        {
            if(i==0||i==mat.size()-1){
                sum+=mat[i][0]+mat[i][mat.size()-1];
            }
            else{
                sum+=mat[i][i]+mat[i][mat.size()-1-i];
            }
        }
        if(mat.size()%2==1){
            sum=sum-mat[mat.size()/2][mat.size()/2];
        }
        return sum;
    }
};
