给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1

性质：二叉搜索树的中序遍历为 递增序列 。   

深度优先搜索:中序遍历
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
        dfs(root, res)
        return res[-k]

