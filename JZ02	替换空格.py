请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

# Traversal
class Solution:
    def replaceSpace(self, s: str) -> str:
        temp = ''
        for i in s:
            if i == ' ':
                temp += '%20'
            else:
                temp += i
        return temp

# O(n) 内置函数
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = s.split(' ')
        return '%20'.join(s)
