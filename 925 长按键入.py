#你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/long-pressed-name
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name = list(name)
        typed = list(typed)
        while name:
            aim = name.pop()
            if not typed or typed.pop() != aim:#比较typed是否第一个也为aim
                return False
            if not name or name[-1] != aim:#name如果后面的不为aim
                while typed and typed[-1]==aim:#弹出长按键
                    typed.pop()
        return not typed
