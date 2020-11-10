数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

数组排序法： 将数组 nums 排序，数组中点的元素 一定为众数。
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
由于sort()函数使用的是Timsort方法,一种归并方法的改进
时间复杂度为O(nlogn)

使用字典进行搜索,即hashmap：
class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        write = {}
        for i in nums:
            if i not in write:
                write[i] = 1
            else:
                write[i] += 1
                if write[i] > (len(nums) / 2):
                    return i
        return None
