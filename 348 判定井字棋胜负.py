#请在 n × n 的棋盘上，实现一个判定井字棋（Tic-Tac-Toe）胜负的神器，判断每一次玩家落子后，是否有胜出的玩家。
#在这个井字棋游戏中，会有 2 名玩家，他们将轮流在棋盘上放置自己的棋子。
#在实现这个判定器的过程中，你可以假设以下这些规则一定成立：
#      1. 每一步棋都是在棋盘内的，并且只能被放置在一个空的格子里；
#      2. 一旦游戏中有一名玩家胜出的话，游戏将不能再继续；
#      3. 一个玩家如果在同一行、同一列或者同一斜对角线上都放置了自己的棋子，那么他便获得胜利。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/design-tic-tac-toe
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.dig1 = [0]*(2*n-1)
        self.dig2 = [0]*(2*n-1)
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.rows[row]+=1
        else:
            self.rows[row]-=1
        if self.rows[row] == self.n:
            return 1
        if self.rows[row] == -self.n:
            return 2

        if player == 1:
            self.cols[col]+=1
        else:
            self.cols[col]-=1
        if self.cols[col] == self.n:
            return 1
        if self.cols[col]== -self.n:
            return 2
        
        if player == 1:
            self.dig1[row+col]+=1
        else:
            self.dig1[row+col]-=1
        if self.dig1[row+col] == self.n:
            return 1
        if self.dig1[row+col]== -self.n:
            return 2

        if player == 1:
            self.dig2[row-col+self.n-1]+=1
        else:
            self.dig2[row-col+self.n-1]-=1
        if self.dig2[row-col+self.n-1] == self.n:
            return 1
        if self.dig2[row-col+self.n-1]== -self.n:
            return 2

        return 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
