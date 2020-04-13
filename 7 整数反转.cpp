class Solution {
public:
    int reverse(int x) {
      int a=0;
      while(x!=0){
          int pop=x%10;
          x/=10;
          if(a>INT_MAX/10||(a==INT_MAX&&pop>7)||a<INT_MIN/10||(a==INT_MIN&&pop<-8)){
              return 0;
          }
          a=a*10+pop;
      }
      return a;
    }
};
