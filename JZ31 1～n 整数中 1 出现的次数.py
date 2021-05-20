输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：

输入：n = 12
输出：5

示例 2：

输入：n = 13
输出：6

思路：将 1 ~ n 的个位、十位、百位、...的 1 出现次数相加，即为 1 出现的总次数。
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res
    
当 cur = 0 时： 此位 1 的出现次数只由高位 high 决定，计算公式为：
high × digit

当 cur = 1 时： 此位 1 的出现次数由高位 high 和低位 low 决定，计算公式为：
high × digit + low + 1

当 cur = 2, 3,..., 9 时： 此位 1 的出现次数只由高位 high 决定，计算公式为：
(high+1) × digit   
    
灵活利用//，%！！
