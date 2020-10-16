找出数组中重复的数字

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 


# 暴力解法：O(1)--O(n^2)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            if i in l:
                return i
            else:
                l.append(i)

方法1：利用python set的无序不重复特性：利用Python中的set集合为无序不重复集合，通过判断temp_set的长度确定是否是重复数字。

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        temp_set = set()
        repeat = -1
        for i in range(len(nums)):
            temp_set.add(nums[i])
            if len(temp_set) < i + 1:
                repeat = nums[i]
                break
        return repeat
        
方法2：利用python的sort函数排序，然后计算相邻两个数据是否相等即可。

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
                
方法3：从头到尾扫描数组,当扫描到下标为i的数字时,首先比较这个数字(用m表示)是否等于下标i,如果等于就扫描下一个数字;如果不是,则将它和第m个数字进行比较.
      如果它和第m个数相等,那么出现了重复直接返回;如果不相等,则将它和第m个数进行交换,把m放到第m个位置上
      重复这个过程,直到出现一个重复的数字 
      时间复杂度O(n)均摊,空间复杂度O(1)
  
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]] , nums[i] = nums[i] , nums[nums[i]]
        
        return None

Python 中, a,b = c,d 操作的原理是先暂存元组 (c,d) ，然后 “按左右顺序” 赋值给 a 和 b 。




