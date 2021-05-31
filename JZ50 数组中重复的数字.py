找出数组中重复的数字

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

方法1：Set 时间复杂度 O(N)

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1
HashSet 添加与查找元素皆为 O(1)
                
方法2：从头到尾扫描数组,当扫描到下标为i的数字时,首先比较这个数字(用m表示)是否等于下标i,如果等于就扫描下一个数字;如果不是,则将它和第m个数字进行比较.
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




