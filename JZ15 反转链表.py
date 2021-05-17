定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

通过栈，创建一个新链表
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        if not head:
            return head
        # 把head中的值加入栈里
        while head:
            stack.append(head.val)
            head = head.next
        # 取最后加入的一个，即链表尾作为新的链表头
        cur = ListNode(stack.pop())
        # 记住头部索引
        res = cur
        # 依次给新链表赋值
        while stack:
            res.next = ListNode(stack.pop())
            res = res.next
        # 返回新链表头部
        return cur

双指针
class Solution:
    # 双指针，一个指针用作新生成的一个链表当前节点，另一个指针用于原链表遍历
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = head
        cur = None
        while pre:
            # 这个临时节点就相当于一个副本
            temp = ListNode(pre.val)
            temp.next = cur
            cur = temp
            pre = pre.next
        return cur



