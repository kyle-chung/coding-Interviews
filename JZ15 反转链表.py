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

递归：这个思路也采用头插法的方式，建立头节点副本，用于递归中目标插入节点。匹配到最后一个不为空的节点，再建立一个副本，用于作为递归中的当前节点，以此实现头插法。

注：关键点在于每次递归后，参数值是上一次，递归前的数值，因此如果保存每次递归的值需要手动return temp。

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # 递归算法
        if not head:
            return None
        if not head.next:
            return head
        temp = head
        while temp.next:
            temp = temp.next
        # 此时temp到达了最后一个不为空的节点
        result = temp
        self.move_single(head,temp)
        return result
    
双指针
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            # "=" 右边的值先全部保存再一次性赋值给 "=" 左边的变量
            cur.next, pre, cur = pre, cur, cur.next
        return pre

