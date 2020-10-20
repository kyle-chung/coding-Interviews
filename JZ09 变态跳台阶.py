一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<3:
            return number
        dp = [0]*number
        dp[0],dp[1]=1,2
        for i in range(2,number):
            dp[i]=sum(dp[:i])+1
        return dp[-1]
