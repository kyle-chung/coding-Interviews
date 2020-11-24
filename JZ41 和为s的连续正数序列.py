输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

暴力法：
枚举每个正整数为起点，判断以它为起点的序列和 sum 是否等于 target 即可，由于题目要求序列长度至少大于 2，所以枚举的上界为 0.5*target
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 初始化窗口指针和输出列表
        i, j, res = 1,2, []

        # 滑动窗口的右边界不能超过target的中值
        while j <= target//2 + 1:
            # 计算当前窗口内数字之和
            cur_sum = sum(list(range(i,j+1)))
            # 若和小于目标，右指针向右移动，扩大窗口
            if cur_sum < target:
                j += 1
            # 若和大于目标，左指针向右移动，减小窗口
            elif cur_sum > target:
                i += 1
            # 相等就把指针形成的窗口添加进输出列表中
            # 别忘了，这里还要继续扩大寻找下一个可能的窗口哦
            else:
                res.append(list(range(i,j+1)))
                # 这里用j+=1，i+=1，i+=2都可以的
                j += 1
        
        return res

双指针：
暴力法是没有考虑区间与区间的信息可以复用，只是单纯的枚举起点，然后从起点开始累加。
考虑到了如果已知 [l,r] 的区间和等于 target ，那么枚举下一个起点的时候，区间 [l+1,r] 的和必然小于 arget 。
我们就不需要再从 l+1 再开始重复枚举，而是从 r+1 开始枚举，充分的利用了已知的信息来优化时间复杂度



