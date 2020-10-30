输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。


一次循环，奇数偶数直接交换
单指针
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0 
        for j in range(len(nums)):
            if nums[j]%2 == 1:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        return nums

双指针：
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums



