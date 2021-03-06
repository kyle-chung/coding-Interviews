写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5

记忆化递归法： O(n)
缺点： 记忆化存储需要使用 O(N) 的额外空间。

class Solution:
    def fib(self, n: int) -> int:
        l = [0,1]
        while len(l) < n:
            new = l[len(l) - 1] + l[len(l) - 2]
            l.append(new)
        return l[len(l) - 1] + l[len(l) - 2]

# recursive
常规的递归操作时间复杂度O(2^N), 循环操作时间复杂度O（N）
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

# best solution
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a 


