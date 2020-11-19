在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

自创：
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        while nums:
            temp = nums.pop(0)
            for i in nums:
                if temp > i:
                    count += 1  
        
        return count
 
归并算法：
归并排序实际上会把数组分成两个有序部分，我们不妨称其为左和右，归并排序的过程中会将左右两部分合并成一个有序的部分。
对于每一个左右部分，我们分别计算其逆序数，然后全部加起来就是我们要求的逆序数。

