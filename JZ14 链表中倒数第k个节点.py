输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

1.遍历链表，将节点存入列表中
2.返回第-k个节点即可
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        l = []
        while head:
            l.append(head)
            head = head.next
        return l[-k]
      
设置一个指针走 (n−k) 步
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter     
