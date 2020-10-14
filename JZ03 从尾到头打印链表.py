输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]

# O(n)
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]

方法1：递归法 利用递归将头结点移动到末端，然后回溯，依次将节点的值放入到列表中，既可以实现链表中的值倒序输出。
O(n)

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

这个例子充分说明了递归本质上就是一个栈，先进后出。
