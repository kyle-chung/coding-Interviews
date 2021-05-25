在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

直观来看，使用暴力统计法即可，即遍历数组的所有数字对并统计逆序对数量。此方法时间复杂度为 O(N^2)
观察题目给定的数组长度范围 0 < N < 50000 ，可知此复杂度是不能接受的。

「归并排序」与「逆序对」是息息相关的。归并排序体现了 “分而治之” 的算法思想，具体为：

分： 不断将数组从中点位置划分开（即二分法），将整个数组的排序问题转化为子数组的排序问题；
治： 划分到子数组长度为 1 时，开始向上合并，不断将 较短排序数组 合并为 较长排序数组，直至合并至原数组时完成排序；

合并阶段 本质上是 合并两个排序数组 的过程，而每当遇到 左子数组当前元素 > 右子数组当前元素 时
意味着 「左子数组当前元素 至 末尾元素」 与 「右子数组当前元素」 构成了若干 「逆序对」 。

时间复杂度 O(N log N)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(l, r):
            # 终止条件
            if l >= r: return 0
            # 递归划分
            m = (l + r) // 2
            res = merge_sort(l, m) + merge_sort(m + 1, r)
            # 合并阶段
            i, j = l, m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(l, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1 or tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1 # 统计逆序对
            return res
        
        tmp = [0] * len(nums)
        return merge_sort(0, len(nums) - 1)

