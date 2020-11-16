输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true

二叉搜索树定义： 左子树中所有节点的值 << 根节点的值；右子树中所有节点的值 >> 根节点的值；其左、右子树也分别为二叉搜索树。

后序遍历倒序列表为[r(n), r(n-1), ... , r(1)]，遍历此列表，设索引为i，若为⼆叉搜索树 ，则有：

当节点值r(i) > r(i+1) 时： 节点r(i)⼀定是节点r(i+1)的右⼦节点。
当节点值r(i) < r(i+1) 时： 节点r(i)⼀定是某节点 root 的左⼦节点，且 root 为节点 r(i+1) 到 r(n)中值⼤于且最接近r(i)的节点
（∵ root直接连接左⼦节点r(i)）

辅助单调栈：
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True
父节点值 root = +∞ （初始值为正无穷大，可把树的根节点看为此无穷大节点的左孩子）

