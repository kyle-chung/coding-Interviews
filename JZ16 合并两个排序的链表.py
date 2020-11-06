输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        while l1:
            l.append(l1.val)
            l1 = l1.next

        while l2:
            l.append(l2.val)
            l2 = l2.next

        l.sort()

        res = ListNode(l[0])
        temp = res
        for i in range(len(l) - 1):
            temp.next = ListNode(l[i+1])
            temp = temp.next
        return res  
