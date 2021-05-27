剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在升序数组中出现的次数。 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

排序数组中的搜索问题，首先想到 二分法 解决
class Solution:
    def search(self, nums: [int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target: i = m + 1
            else: j = m - 1
        right = i
        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target: return 0
        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target: i = m + 1
            else: j = m - 1
        left = j
        return right - left - 1

