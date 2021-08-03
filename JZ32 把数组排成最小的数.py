输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。 

示例 1:

输入: [10,2]
输出: "102"

示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

解题思路：

此题求拼接起来的 “最小数字” ，本质上是一个排序问题。

排序判断规则： 设 nums 任意两数字的字符串格式 x 和 y ，则
若拼接字符串 x + y > y + x ，则 x '>' y ；
反之，若 x + y < y + x ，则 y '>' x ；

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def fast_sort(l , r):
            if l >= r: return None
            i, j = l, r
#           这里基准数pivot为strs[l]
            while i < j:
#               找到j '<' l
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
#               找到l '<' i
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
#               即得i '>' j，更新其位置
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i - 1)
            fast_sort(i + 1, r)
        
        strs = [str(num) for num in nums]
        fast_sort(0, len(strs) - 1)
        return ''.join(strs)

