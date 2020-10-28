实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

示例 1:

输入: 2.00000, 10
输出: 1024.00000

对于任何十进制正整数n,设其二进制为 'b_m...b_3b_2b_1'

b_i为二进制某位值，i∈[1,m],则有:

二进制转十进制： n = 1b_1 + 2b_2 + 4b_3 + ... + 2^{m-1}b_m（即二进制转十进制公式） 

复杂度分析：
时间复杂度 O(log_2 n)： 二分的时间复杂度为对数级别。
空间复杂度 O(1) ： res, b 等变量占用常数大小额外空间。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res
        
算法流程：

当 x = 0 时：直接返回 0（避免后续 x = 1/x 操作报错）。

初始化 res = 1

当 n < 0时：把问题转化至 n≥0 的范围内，即执行 x = 1/x ,n = −n 

循环计算：当 n = 0 时跳出:

  当 n & 1 = 1 时：将当前 x 乘入 res （即 res∗=x ）
  执行 x = x^2
  执行 n 右移一位（即 n >>= 1）

返回 resres 。


