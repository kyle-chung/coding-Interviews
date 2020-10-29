输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。


一次循环，奇数偶数直接交换
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0 
        for j in range(len(nums)):
            if nums[j]%2 == 1:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
        return nums

