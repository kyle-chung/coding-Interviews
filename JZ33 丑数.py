我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明: 
1 是丑数。

自创:
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 1
        num = 2

        while num:
            temp = num
            while temp % 2 == 0:
                temp = temp/2
            while temp % 3 == 0:
                temp = temp/3
            while temp % 5 == 0:
                temp = temp/5

            if temp == 1:
                count += 1
                if count == n:
                    return num
                    break

            num += 1


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
