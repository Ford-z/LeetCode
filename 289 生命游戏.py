#根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
#给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
#如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
#如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
#如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
#根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/game-of-life
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)#deepcopy将深层的元素也复制
        n=len(board)
        m=len(board[0])
        direction = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[-1,1],[1,1]]
        for i in range(n):
            for j in range(m):
                nums = 0 #记录八个方向上的活细胞或者死细胞的个数 
                for k in range(8):
                    dx = direction[k][0]+i
                    dy = direction[k][1]+j
                    if dx>=0 and dx<n and dy>=0 and dy<m and board_copy[dx][dy]==1:
                        nums+=1
                if nums<2:
                    board[i][j] = 0
                elif nums>3:
                    board[i][j] = 0
                elif nums==3:
                    board[i][j] = 1
