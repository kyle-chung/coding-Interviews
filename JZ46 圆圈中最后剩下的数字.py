0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

示例 1：

输入: n = 5, m = 3
输出: 3

示例 2：

输入: n = 10, m = 17
输出: 2

这个问题是以弗拉维奥·约瑟夫命名的，他是1世纪的一名犹太历史学家。他在自己的日记中写道，他和他的40个战友被罗马军队包围在洞中。
他们讨论是自杀还是被俘，最终决定自杀，并以抽签的方式决定谁杀掉谁。约瑟夫斯和另外一个人是最后两个留下的人。约瑟夫斯说服了那个人，他们将向罗马军队投降，不再自杀。
约瑟夫斯把他的存活归因于运气或天意，他不知道是哪一个。

暴力法：
由于列表要执行pop操作 n-1次，而每次pop(i)是平均O(n)复杂度，所以总的时间复杂度是O(n^2)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        i, a = 0, list(range(n))
        while len(a) > 1:
            i = (i + m - 1) % len(a)
            a.pop(i)
        return a[0]

recur：
如果我们知道对于一个长度 n - 1 的序列，留下的是第几个元素，那么我们就可以由此计算出长度为 n 的序列的答案。
# Python 默认的递归深度不够，需要手动设置
sys.setrecursionlimit(100000)

def f(n, m):
    if n == 0:
        return 0
    x = f(n - 1, m)
    return (m + x) % n

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return f(n, m)

pop(0)真的很低效哦
