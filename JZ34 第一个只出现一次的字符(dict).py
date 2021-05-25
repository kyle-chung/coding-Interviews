在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "

哈希表：
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
#       for key,value in d.items()
        for k, v in dic.items():
            if v: return k
#         the same：
#         for c in s:
#             if dic[c]: return c
        return ' '

