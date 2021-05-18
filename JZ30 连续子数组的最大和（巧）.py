输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 动态规划（Dynamic Programming） 时间复杂度 O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
    
动态规划：将一个问题拆成几个子问题，分别求解这些子问题，即可推断出大问题的解。

假设 nums 数组的长度是 n，下标从 0 到 n−1。

我们用 f(i) 代表以第 i 个数结尾的「连续子数组的最大和」，那么很显然我们要求的答案就是最大的 f(i)

因此我们只需要求出每个位置的 f(i)，然后返回 f 数组中的最大值即可。

# 分治 时间复杂度 O(nlogn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #递归终止条件
        if n == 1:
            return nums[0]
        else:
            #递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            #递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        
        #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r)

分治：对于一个规模为n的问题，将其分解为k个规模较小的子问题，这些子问题互相独立且与原问题形式相同。递归地解这些子问题，然后将各子问题的解合并得到原问题的解。


