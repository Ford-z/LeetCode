#给定一个整数数组 asteroids，表示在同一行的行星。
#对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
#找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/asteroid-collision
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos=[]
        for i in range(len(asteroids)):
            if len(pos) == 0 or pos[-1] * asteroids[i] > 0 or pos[-1] < 0 and asteroids[i] > 0:
                pos.append(asteroids[i])
            elif asteroids[i] < 0  and  len(pos) > 0:
                if abs(asteroids[i])<abs(pos[-1]):
                    continue
                elif abs(asteroids[i])==abs(pos[-1]):
                    pos.pop()
                else:
                    while len(pos) > 0 and asteroids[i] < 0  and  pos[-1] > 0 and abs(pos[-1]) < abs(asteroids[i]):
                        pos.pop()
                    if len(pos) > 0 and abs(asteroids[i])==abs(pos[-1]) and asteroids[i] < 0  and  pos[-1] > 0:
                        pos.pop()
                        continue
                    elif len(pos) > 0 and asteroids[i]==pos[-1] or len(pos)==0 or asteroids[i] *pos[-1] > 0:
                        pos.append(asteroids[i])
        return pos
