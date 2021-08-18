我们提供了一个类：

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
三个不同的线程 A、B、C 将会共用一个 Foo 实例。

一个将会调用 first() 方法
一个将会调用 second() 方法
还有一个将会调用 third() 方法
请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

 

示例 1:

输入: [1,2,3]
输出: "firstsecondthird"
解释: 
有三个线程会被异步启动。
输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。
正确的输出是 "firstsecondthird"。
示例 2:

输入: [1,3,2]
输出: "firstsecondthird"
解释: 
输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。
正确的输出是 "firstsecondthird"。
 

提示：

尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
你看到的输入格式主要是为了确保测试的全面性。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-in-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Foo:
    def __init__(self):
        #在这题里面功能都是类似的，就是添加阻塞，然后释放线程，只是类初始化的时候不能包含有参数，所以要写一句acquire进行阻塞，调用其他函数的时候按顺序release释放。
       self.l1 = threading.Lock()
       self.l1.acquire()
       self.l2 = threading.Lock()
       self.l2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.l1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.l2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
