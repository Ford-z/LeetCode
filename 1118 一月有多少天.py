#指定年份 Y 和月份 M，请你帮忙计算出该月一共有多少天。
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if(M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12):
            return 31
        if(M==4 or M==6 or M==9 or M==11):
            return 30
        if(M==2):
            if(Y%100==0 and Y%400==0):
                return 29
            if(Y%100!=0 and Y%4==0):
                return 29
            else:
                return 28
